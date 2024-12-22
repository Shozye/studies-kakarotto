#pragma once

#include <limits>
#include <vector>
#include <queue>

const long long INF = std::numeric_limits<long long>::max();

struct Edge {
    int dest;
    int cost;
};

long long dijkstra(const std::vector<std::vector<Edge>>& G, int source, int target, int n);
long long dial(std::vector<std::vector<Edge>>& G, int source, int target, int n);
