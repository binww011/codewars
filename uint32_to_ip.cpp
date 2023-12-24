#include <bits/stdc++.h>
using namespace std;

int btoi(string b) {
  int res = 0, cnt = b.size()-1;
  for (char bin : b) {
    if (bin == '1') res += pow(2, cnt);
    --cnt;
  }
  return res;
}

string uint32_to_ip(uint32_t ip)
{
  string binrep = "", binfin = "";
  int ip_address[4] = {0, 0, 0, 0};
  uint32_t inum = ip;
  
  while (inum > 0) {
    binrep += to_string(inum%2);
    inum /= 2;
  }
  
  if (binrep.length() != 32) {
    for (int k = binrep.length(); k < 32; ++k) {
      binrep += '0';
    }
  }
  
  for (int i = binrep.length()-1; i >= 0; --i) {
    binfin += binrep[i];
  }
  
  string tmp = "";
  int octet = 0;
  for (size_t i = 0; i < binfin.size(); ++i) {
    tmp += binfin[i];
    
    if ((i+1)%8 == 0 && i > 0) {
      ip_address[octet] += btoi(tmp);
      tmp = "";
      ++octet;
    }
  }
  
  string res = "";
  for (int i = 0; i < 4; ++i) {
    res += to_string(ip_address[i]);
    if (i != 3) res += '.';
  }
  
  return res;
}
