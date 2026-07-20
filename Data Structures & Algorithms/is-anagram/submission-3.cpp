class Solution {
public:
    bool isAnagram(string s, string t) {
        
        // step-1: check if sizes are mismatched
        int n = s.size();
        int m = t.size();
        if (n!=m){
            return false;
        }
        // step-2: create frequency maps
        unordered_map<char,int> x;
        unordered_map<char,int> y;


        // step-3: increment the counts of the characters in the hashmaps
        for (char c:s){
            x[c]++;
            }
        for (char d:t){
            y[d]++;
        }        
    // check if they are the same
    return x==y;
    }
};
