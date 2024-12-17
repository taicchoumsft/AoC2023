
#include "../stdc++.h"
#include "../stringutils.h"

using namespace std;

vector<vector<int>> parse(vector<string>& input) {
    vector<vector<int>> result;
    for (auto& line : input) {
        result.push_back(splitT<int>(line));
    }
    return result;
}

vector<vector<int>> process(vector<int>& arr) {
    vector<vector<int>> result;
    result.push_back(arr);

    while (!all_of(result.back().begin(), result.back().end(), [](int i) { return i == 0; })) {
        vector<int> row;
        for (int j=0; j<result.back().size() - 1; ++j) {
            row.push_back(result.back()[j+1] - result.back()[j]);
        }
        result.push_back(row);
    }
    return result;
}

pair<int, int> calculate(vector<vector<int>>& arr) {
    int front = 0;
    int back = 0;
    for (int i=arr.size() - 2; i >= 0; --i) {
        front = arr[i].front() - front;
        back += arr[i].back();
    }
    return {front, back};
}

void solution(vector<string>& input) {
    vector<vector<int>> nums = parse(input);

    int total_back = 0;
    int total_front = 0;
    for (auto& arr : nums) {
        vector<vector<int>> result = process(arr);
        auto [front, back] = calculate(result);
        total_back += back;
        total_front += front;
    }
    cout << "Solution 1: " << total_back << endl;
    cout << "Solution 2: " << total_front << endl;
}

int main(int argc, char** argv) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    ifstream file(argv[1]);

    if (!file.is_open()) {
        cout << "File not found" << endl;
        return 0;
    }

    vector<string> lines;
    string line;
    while (getline(file, line)) {
        lines.push_back(line);
    }

    solution(lines);
    file.close();
    return 0;
}