#include <vector>
#include <queue>
#include "headers.h"

struct myComp {
    constexpr bool operator()(
        Edge const& a,
        Edge const& b)
        const noexcept
    {
        return a.cost > b.cost;
    }
};

long long dijkstra(const std::vector<std::vector<Edge>>& G, int source, int target, int n){
    std::vector<long long> dist(n + 1, INF);
    std::vector<bool> visited(n + 1, false);
    std::priority_queue<Edge, std::vector<Edge>, myComp> min_heap;

    dist[source] = 0;
    min_heap.push( {source, 0} );

    while ( !min_heap.empty() ) {
        const Edge& currentEdge = min_heap.top();
        min_heap.pop();

        int node = currentEdge.dest;
        if( node == target ) break; 
        if( visited[node] ) continue;
        
        visited[node] = true;

        for ( auto& edge : G[node] ){
            int neighbour = edge.dest;
       
            int distance = currentEdge.cost + edge.cost;
            if ( distance < dist[neighbour] ){
                dist[neighbour] = distance;
                min_heap.push( { neighbour, distance });
            }
        }
    }
    return dist[target];
}