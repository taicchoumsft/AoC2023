
#include "../stdc++.h"
#include "../stringutils.h"

using namespace std;

unordered_map<string, vector<string>> mp;
vector<string> start_nodes;
string path;

int path_to_z(string cur, const string& path, unordered_map<string, vector<string>>& mp) {
    int cnt = 0;
    int idx = 0;

    while (cur.back() != 'Z') {
        char dir = path[idx];
        cur = mp[cur][(dir == 'R')];
        cnt += 1;
        idx = (idx + 1) % path.size();
    }
    return cnt;
}

void solution(const vector<string>& input) {
    cout << path_to_z("AAA", path, mp) << endl;
}

uint64_t gcd(uint64_t a, uint64_t b) {
    if (a == 0) return b;
    return gcd(b, a % b);
}

uint64_t lcm(uint64_t a, uint64_t b) {
    return a * b / gcd(a, b);
}

void solution2(const vector<string>& input) {
    auto result = accumulate(start_nodes.begin(), start_nodes.end(), 1LL, [](uint64_t acc, string node) {
        return lcm(acc, path_to_z(node, path, mp));
    });

    cout << result << endl;
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

    vector<string> input;
    string line;
    while (getline(file, line)) {
        input.push_back(line);
    }
    file.close();

    path = strip(input[0], ' ');

    for (int i=2; i<input.size(); i++) {
        vector<string> tokens = split(input[i], '=');
        string key = strip(tokens[0], ' ');
        vector<string> values = split(tokens[1].substr(1, tokens[1].size() - 2), ',');

        for (auto v: values) {
            mp[key].push_back(strip(v, ' '));
        }

        if (key.back() == 'A') {
            start_nodes.push_back(key);
        }
    }

    solution(input);
    solution2(input);

    return 0;
}