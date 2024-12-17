
#include "../stdc++.h"
#include "../stringutils.h"

using namespace std;

void solution(vector<string>& input) {
    auto time = splitT<int>(split(input[0], ':')[1]);
    auto distance = splitT<int>(split(input[1], ':')[1]);

    for (auto t: time) {
        cout << t << endl;
    }

    int total = 1;

    // total *= len([i * (t - i) for i in range(1, t) if i * (t - i) > d])
    for (int i=1; i<time.size(); ++i) {
        int t = time[i];
        int d = i * (t - i);
        if (d > distance[i]) {
            total *= d;
        }
    }
    cout << total << endl;


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