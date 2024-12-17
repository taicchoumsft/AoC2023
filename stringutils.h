// implement the basic parsing utils that are commonly used in python
// split, join, strip, etc

#ifndef _STRINGUTILS_H_
#define _STRINGUTILS_H_

#include<vector>
#include<string>

using namespace std;

string strip(string s, char delim = ' ') {
    int start = 0;
    int end = s.size() - 1;
    while (start < s.size() && s[start] == delim) {
        start++;
    }
    while (end >= 0 && s[end] == delim) {
        end--;
    }
    return s.substr(start, end - start + 1);
}

vector<string> split(const string& s, char delim) {
    vector<string> tokens;
    stringstream ss(s);
    string token;
    while (getline(ss, token, delim)) {
        tokens.push_back(strip(token, ' '));
    }
    return tokens;
}

string join(vector<string>& tokens, char delim) {
    string s;
    for (int i = 0; i < tokens.size(); i++) {
        s += tokens[i];
        if (i != tokens.size() - 1) {
            s += delim;
        }
    }
    return s;
}

template <typename T>
vector<T> splitT(string& s) {
    vector<T> tokens;
    stringstream ss(s);
    cin.rdbuf(ss.rdbuf());

    T token;
    while (cin >> token) {
        tokens.push_back(token);
    }

    return tokens;
}

#endif // _STRINGUTILS_H_