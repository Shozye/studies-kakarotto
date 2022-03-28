#pragma once
#include<iostream>
#include<fstream>
#include<string>
#include<cmath>

void print_list_with_indexes(int* nums, int n);
double entropy(std::ifstream* file);
double entropy(std::string filename);