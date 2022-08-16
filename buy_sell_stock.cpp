#include <vector>
#include <iostream>
using namespace std;

/*
Find the maximum difference between b and a (b - a)
where b occurs after a.
*/
int max_profit(vector<int> &prices) {
  int best_price = 0;
  for (auto i = 0; i < prices.size(); i++) {
    for (auto j = i; j < prices.size(); j++) {
      if (prices[j] - prices[i] > best_price)
	best_price = prices[j] - prices[i];
    }
  }
  
  return best_price;
}

int main() {
  vector<int> prices = {7, 6, 4, 3, 1};
  vector<int> prices1 = {7, 1, 5, 3, 6, 4};
  cout << max_profit(prices) << endl;
  cout << max_profit(prices1) << endl;
}
