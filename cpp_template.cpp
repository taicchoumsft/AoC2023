
#include "../stdc++.h"
#include "../stringutils.h"

using namespace std;

void solution(vector<string>& input) {

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