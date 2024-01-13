#include <algorithm>
#include <string>

using namespace std;

class Solution
{
public:


  int minSteps(string s, string t)
  {
    int chars[26] = {};
    for (int i = 0; i < s.size(); i++)
    {
      chars[t[i] - 'a']++;
      chars[s[i] - 'a']--;
    }
    int res = 0;
    for (int i = 0; i < 26; i++)
    {
      res += std::max(0, chars[i]);
    }
    return res;
  }
};

// first, we count the number of each character in s and t
// then, we count the number of characters that are in t but not in s
// this is how many characters we need to change