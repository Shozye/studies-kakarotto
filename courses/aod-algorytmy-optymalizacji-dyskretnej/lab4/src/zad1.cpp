#include <random>
#include <iostream>
#include <vector>
#include <queue>
#include <chrono>

std::random_device rd;
std::mt19937 gen(rd());

struct Edge {
    int target;
    int residual_capacity;
    int flow = 0;
    Edge(int to, int residual_capacity){
        this->target = to;
        this->residual_capacity = residual_capacity;
    }
};

int pow(int n, int e){
    int res = 1;
    while (e > 0){
        res *= n;
        e--;
    }
    return res;
}



int getRandom(int max_range){
    std::uniform_int_distribution<> dis(1, max_range);
    int val = dis(gen);
    return val;
}

int hamming_weight(int x){
    int amount_ones = 0;
    while (x != 0){
        amount_ones += x % 2;
        x /= 2;
    }
    return amount_ones;
}
int hamming_distance(int x, int y, int k){
    int res = 0;
    int binx[k];
    int biny[k];
    for (int i = k-1; i >= 0; i--){
        binx[i] = x%2;
        biny[i] = y%2;
        x /= 2;
        y /= 2;
    }
    for(int i = 0; i < k; i++){
        if (binx[i] != biny[i]){
            res += 1;
        }
    }
    return res;
}
int Z(int x, int k){
    return k-hamming_weight(x);
}
int max(int x, int y){
    if(x > y) return x;
    return y;
}
int min(int x, int y){
    return -max(-x, -y);
}


void makeHyperCubeGraph(std::vector<std::vector<Edge>>* edges, int k){
    int amountNodes = pow(2,k);
    for(int i = 0; i < amountNodes; i++){
        std::vector<Edge> temp;
        edges->push_back(temp);
    }
    for(int i = 0; i < amountNodes;i++){
        for(int j = 0; j < amountNodes; j++){
            if(i < j && hamming_distance(i, j, k) == 1){
                int l = max(max(hamming_weight(i), Z(i,k)), max(hamming_weight(j), Z(j,k)));
                int capacity = getRandom(pow(2,l));
                edges->at(i).push_back(Edge(j, capacity));
                edges->at(j).push_back(Edge(i, 0));
            }
        }
    }
}

std::vector<int> bfs(std::vector<std::vector<Edge>>* edges, int source, int target){
    int n = edges->size();
    std::vector<int> predecessors(n, -1);
    std::queue<int> q;
    q.push(source);

    while (!q.empty()){
        int current = q.front();
        q.pop();
        for (int i = 0; i < edges->at(current).size(); i++){
            Edge& edge = edges->at(current)[i];
            int neighbour = edge.target;
            if (predecessors[neighbour] == -1 
                    && neighbour != source 
                    && edge.residual_capacity > edge.flow ){
                q.push(neighbour);
                predecessors[neighbour] = current;
            }
        }
    }
    // If we get here, it means that we have exhausted all the reachable nodes from the source,
    // and we have not reached the target. We can assume that the target is not reachable from the source.
    return predecessors;
}

Edge* get_edge(std::vector<std::vector<Edge>>* edges, int from, int to){
    for(Edge& edge: edges->at(from)){
        if(edge.target == to) return &edge;
    }
    throw "edge not found"; 
}

int get_delta_flow(std::vector<std::vector<Edge>>* edges, std::vector<int>* pred, int s, int t){
    int max_delta_flow = INT32_MAX;
    int target;
    int current = t;
    while (current != s){
        target = current;
        current = pred->at(target);
        Edge* edge = get_edge(edges, current, target);
        max_delta_flow = min(max_delta_flow, edge->residual_capacity - edge->flow);
    }
    return max_delta_flow;
}

struct Result {
    int max_flow;
    int augmenting_paths;

    Result(int max_flow, int augmenting_paths){
        this->max_flow = max_flow;
        this->augmenting_paths = augmenting_paths;
    }
};

Result edmund_karps(std::vector<std::vector<Edge>>* edges, int s, int t){
    int max_flow = 0;
    int augmenting_paths = 0;

    while (true){
        std::vector<int> pred = bfs(edges, s, t); // bfs to get shortest s-t path

        if (pred[t] == -1) break; // no more augmenting paths
        //std::cout << "Found augmenting path!" << std::endl;
        augmenting_paths += 1;// we found an augmenting path.
        // see how much flow we can send
        int delta_flow = get_delta_flow(edges, &pred, s, t);

        int target;
        int current = t;
        while (current != s){
            target = current;
            current = pred.at(target);
            Edge* edge = get_edge(edges, current, target);
            edge->flow += delta_flow;

            Edge* rev_edge = get_edge(edges, target, current);
            rev_edge->flow -= delta_flow;
        }
        max_flow += delta_flow;
    }
    return Result(max_flow, augmenting_paths);
}


int main(int argc, char** argv) {
    auto begin = std::chrono::high_resolution_clock::now();
    if(argc < 3 || argc > 4) { std::cout << "Received " << argc << " arguments. Expected 3 or 4" << std::endl;}
    int k = std::atoi(argv[2]);
    bool printFlow = argc == 4;

    std::vector<std::vector<Edge>> edges;
    makeHyperCubeGraph(&edges, k);   


    Result res = edmund_karps(&edges, 0, edges.size() - 1);

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(end - begin);

    if(printFlow){
        for(int i = 0; i < edges.size(); i++){
            for(Edge& edge: edges[i]){
                std::cout << i << ", " << edge.target << ": " << edge.flow << "/" << edge.residual_capacity << std::endl;
            }
        }
    }
    
    std::cout << ":Time:" << elapsed.count() << ":Augments:" << res.augmenting_paths << ":MaxFlow:" << res.max_flow << ":" << std::endl;
}
