#include <iostream>
#include <fstream>
#include <sstream>
#include <string.h>
#include <vector>
#include <string>
#include <queue>
#include <utility>
#include <algorithm>
#include <chrono>
#include <list>
#include "headers.h"

using namespace std::chrono;

std::vector<std::vector<Edge>> vertices;

std::pair<int, int> readData(std::string filename){
    std::cout << "Reading file " << filename << std::endl;
    int n,m;
    std::ifstream myfile; 
        myfile.open(filename);
        std::string fileLine;

        int lineNum = 0;
        if ( myfile.is_open() ) {
            while (std::getline (myfile, fileLine)) {
                lineNum += 1;
                if ( fileLine[0] == 'c' ) continue;
                if (lineNum % 500000 == 0){std::cout << "Reading... " <<  lineNum << std::endl;}
                std::istringstream ss(fileLine);
                std::string del;
                std::vector<std::string> characters;
                while(getline(ss, del, ' ')) {
                    characters.push_back(del);
                }

                if ( characters[0] == "p" ){
                    n = std::stoi(characters[2]);
                    m = std::stoi(characters[3]);
                    for(int i = 0; i <= n; i++){
                        std::vector<Edge> newEmptyVector;
                        vertices.push_back(newEmptyVector);
                    }
                } else if ( characters[0] == "a" ){
                    int v1 = std::stoi(characters[1]);
                    int v2 = std::stoi(characters[2]);
                    int weight = std::stoi(characters[3]);
                    vertices[v1].push_back( { v2, weight } );
                }
                
                characters.clear();
            }
        }
    myfile.close(); 

    return {n, m};
}

std::vector<int> readSources(std::string filename){
    std::cout << "Reading ss file " << filename << std::endl;
    std::vector<int> sources;
    std::ifstream myfile; 
    myfile.open(filename);

    std::string fileLine;

    int lineNum = 0;
    if ( myfile.is_open() ) {
        while (std::getline (myfile, fileLine)) {
            lineNum ++;
            if (lineNum % 5000 == 0){std::cout << "Reading ss... " <<  lineNum << std::endl;}
            std::istringstream ss(fileLine);
            std::string del;
            std::vector<std::string> characters;
            while(getline(ss, del, ' ')) { characters.push_back(del);}
            if ( characters[0] == "c" ) continue;
            if ( characters[0] == "s" ){
                int source = std::stoi(characters[1]);
                sources.push_back(source);
            }
        }
    }

    myfile.close(); 
    return sources;
}

unsigned long run_ss(const std::vector<int>& sources, std::string algorithm, int N){
    auto start = high_resolution_clock::now();

    for (int i = 0; i < sources.size(); i++) {
        
        if (i%(sources.size()/10) == 0){std::cout << "Running... " << algorithm <<" "<< i << std::endl;}

        if( algorithm == "dijkstra" ) {
            dijkstra(vertices, sources[i], 0, N);
        } else if ( algorithm == "dial" ) {
            dial(vertices, sources[i], 0, N);
        }
    }

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    auto average_time = duration.count() / sources.size();
    return average_time;
}

std::vector<std::pair<int, int>> readP2P(std::string filename){
    std::cout << "Reading p2p file " << filename << std::endl;
    std::vector<std::pair<int, int>> pairs;
    std::ifstream myfile; 
    std::string fileLine;
    std::string del;

    myfile.open(filename);
    int lineNum = 0;
    if ( myfile.is_open() ) {
        while (std::getline (myfile, fileLine)) {
            lineNum += 1;
            if (lineNum % 2000 == 0){std::cout << "Reading p2p... " <<  lineNum << std::endl;}
            std::istringstream ss(fileLine);
            std::vector<std::string> words;
            while(getline(ss, del, ' ')) {
                words.push_back(del);
            }

            if ( words[0] == "c" ) continue;
            if ( words[0] == "q" ){
                int source = std::stoi(words[1]);
                int destination = std::stoi(words[2]);
                pairs.push_back( {source, destination });
            }
        }
    }
    myfile.close();
    return pairs;
}


std::vector<std::tuple<int, int, unsigned long long>> runP2P(std::vector<std::pair<int,int>> p2p_pairs, std::string algorithm, int N){
    std::vector<std::tuple<int, int, unsigned long long>> pairsAndCost;

    int pairNum = 0;
    for(const auto& [source, destination]: p2p_pairs){
        pairNum ++;
        if (pairNum % (p2p_pairs.size()/10) == 0){std::cout << "Running... " << algorithm <<" "<<  pairNum << std::endl;}

        long long distance;
        if( algorithm == "dijkstra" ) {
            distance = dijkstra(vertices, source, destination, N);
        } else if ( algorithm == "dial" ) {
            distance = dial    (vertices, source, destination, N);
        }
        pairsAndCost.push_back(std::make_tuple(source, destination, distance));
    }
    return pairsAndCost;
}


int main(int argc, char** argv){
    if(argc != 8){
        std::cout << "Wrong number of arguments. Got " << argc <<std::endl;
        std::cout << argv[0] << std::endl;
        std::cout << argv[1] << std::endl;
        std::cout << argv[2] << std::endl;
        std::cout << argv[3] << std::endl;
        std::cout << argv[4] << std::endl;
        std::cout << argv[5] << std::endl;
        std::cout << argv[6] << std::endl;
        std::cout << argv[7] << std::endl;
        return 0;
    }
    std::string algorithm = argv[1];
    std::string first_flag = argv[2];
    std::string nameOfFileWithData = argv[3];
    std::string second_flag = argv[4];
    std::string fileWithSources = argv[5];
    std::string resultsFile = argv[7];

    if( algorithm != "dijkstra" && algorithm != "dial" ) {
        std::cout << "Wrong algorithm passed as an argument" << std::endl;
        return 0;
    }

    if (first_flag != "-d") {
        std::cout << "Wrong first flag" << std::endl;
        return 0;
    }

    if (second_flag != "-ss" && second_flag != "-p2p"){
        std::cout << "Wrong second flag" << std::endl;
        return 0;
    }
    
    auto [n, m] = readData(nameOfFileWithData);

    if ( second_flag == "-ss" ) {
        std::vector<int> sources = readSources(fileWithSources);
        
        auto average_time = run_ss(sources, algorithm, n);
        std::ofstream myfile(resultsFile);
        myfile << "f " << nameOfFileWithData << " " << fileWithSources << "\n";
        myfile << "t " << average_time << "\n";

    } else if ( second_flag == "-p2p" ) {
        std::vector<std::pair<int,int>> p2p_pairs = readP2P(fileWithSources);
        std::vector<std::tuple<int, int, unsigned long long>> pairsAndCost = runP2P(p2p_pairs, algorithm, n);

        std::ofstream myfile(resultsFile);
        myfile << "f " << nameOfFileWithData << " " << fileWithSources << "\n";
        for (const auto& [source, destination, distance]: pairsAndCost){
            std::cout << "(" << source << ", " << destination << ") " << distance << std::endl;
            myfile << "d " << source << " " << destination << " " << distance << "\n";
        }
        
    }
} 


