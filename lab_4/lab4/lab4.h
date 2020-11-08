#ifndef LAB4_H
#define LAB4_H
#include <iostream>
#include <random>
#include <chrono>
#include <vector>
#include <thread>
#include <cmath>
#include <queue>
#include <random>
#include <mutex>

#define OK 0
#define ERR_EMPTY 1
#define ERR_SIZE 2

using namespace std;

int vinogradOPT(const vector<vector<int>>& A, const vector<vector<int>>& B,
    const int m, const int n, const int q, vector<vector<int>>& C);

int threadedVinogradOPT(const vector<vector<int>>& A, const vector<vector<int>>& B,
    const int m, const int n, const int q, vector<vector<int>>& C,
    const int& nThreads);

#endif