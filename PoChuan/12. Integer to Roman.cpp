// Since Roman number has a fixed pattern
// simply stored all kind of the pattern and
// iterate it.


class Solution {
public:

    vector<pair<int, string>> symbol{{1000, "M"},
                                      {900, "CM"},
                                      {500, "D"},
                                      {400, "CD"},
                                      {100, "C"},
                                      {90, "XC"},
                                      {50, "L"},
                                      {40, "XL"},
                                      {10, "X"},
                                      {9, "IX"},
                                      {5, "V"},
                                      {4, "IV"},
                                      {1, "I"}};

    string intToRoman(int num) {
        
        string ret = "";
        for(auto it = symbol.begin(); it != symbol.end(); it++){
            
            while(num >= it->first) {

                num -= it->first;
                ret += it->second;
            }
        }

        return ret;
    }
};