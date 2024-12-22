    
#include <vector> 
#include <list>
#include <iostream>
#include <limits>
#include<list>
#include "headers.h"


long long dial(std::vector<std::vector<Edge>>& G, int source, int target, int n){
    /* With each distance, iterator to that vertex in
    its bucket is stored so that vertex can be deleted
    in O(1) at time of updation. So
    dist[i].first = distance of ith vertex from src vertex
    dist[i].second = iterator to vertex i in bucket number */
    std::vector<std::pair<long long, std::list<int>::iterator>> dist(n + 1);
 
    // Initialize all distances as infinite (INF)
    for (int i = 0; i <= n; i++) {
        dist[i].first = INF;
    }
    int W = 0;
    for(int i = 0; i < G.size(); i++) {
        for(int j = 0; j < G[i].size(); j++){
            int cost = G[i][j].cost;
            if ( cost > W ) W = cost;
        }
    }
    //std::cout << "-4" << std::endl;

    //std::list<int> buckets[W * n + 1];
    std::list<int>* buckets = new std::list<int>[W * n + 1];
    //std::cout << "-3" << std::endl;

    buckets[0].push_back(source);
    dist[source].first = 0;
    //std::cout << "0" << std::endl;
    //
    int index = 0;
    while (1) {
        // Go sequentially through buckets till one non-empty
        // bucket is found
        //std::cout << "1" << std::endl;
        while (buckets[index].size() == 0 && index < W*n) {
            index++;
        }
 
        // If all buckets are empty, we are done.
        if ( index == W * n ){
            break;
        }

        // Take top vertex from bucket and pop it
        int node = buckets[index].front();
        if( node == target ) break; 
        buckets[index].pop_front();

        // Process all adjacents of extracted vertex 'u' and
        // update their distanced if required.
        for (const Edge& edge: G[node]) {
            int neighbour = edge.dest;
            int cost = edge.cost;
 
            long long neighbourDistance = dist[neighbour].first;

            // If there is shorted path to v through u.
            long long possibleNewDistance = dist[node].first + cost;
            if ( neighbourDistance > possibleNewDistance ) {
                // If dv is not INF then it must be in B[dv]
                // bucket, so erase its entry using iterator
                // in O(1)
                if ( neighbourDistance != INF ){
                    buckets[neighbourDistance].erase(dist[neighbour].second);
                }
                // updating the distance
                dist[neighbour].first = possibleNewDistance;
                neighbourDistance  = dist[neighbour].first;
 
                // pushing vertex v into updated distance's bucket
                buckets[neighbourDistance].push_front(neighbour);
                // storing updated iterator in dist[v].second
                dist[neighbour].second = buckets[neighbourDistance].begin();
            }
        }
    }
    
    delete[] buckets;
    return dist[target].first;
}
