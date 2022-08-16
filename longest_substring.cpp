#include <string>
#include <iostream>
using namespace std;

int longest_substring(string s) {
  string last_character = "";
  int count = 0;
  for (auto ch: s) {
    count++;

    if (string(1, ch) == last_character) {
      return count;
    }
    last_character = ch;
  }
  return count;
}

int main() {
  string s = "pwwkew";
  cout << longest_substring(s) << endl;
}
