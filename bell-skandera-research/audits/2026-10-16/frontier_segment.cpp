// Standalone C++17/Boost exact independent Bell-Skandera finite-frontier generator.
// No input from earlier Python case lists. Does NOT check Hankel DFS.
#include <boost/multiprecision/cpp_int.hpp>
#include <cmath>
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <tuple>
#include <stdexcept>
#include <cstdlib>
using boost::multiprecision::cpp_int;
using U=unsigned long long;
using U128=unsigned __int128;
U128 pow128(U128 a,int k){U128 p=1;while(k--){p*=a;}return p;}
U C[65][65];
void init(){for(int n=0;n<65;n++){C[n][0]=C[n][n]=1;for(int k=1;k<n;k++) C[n][k]=C[n-1][k-1]+C[n-1][k];}}
cpp_int powi(cpp_int a,int k){cpp_int p=1;while(k){if(k&1)p*=a;a*=a;k>>=1;}return p;}
int cutoff(int d,int k){int r=d;while(powi(C[r][k+1],k)*powi(C[d][k],k+1)<=powi(C[d][k+1],k)*powi(C[r+1][k],k+1))r++;return r;}
U kk(int k,U m){U rem=m,ans=0;int cap=64;for(int i=k;i>=1;i--){int lo=i-1,hi=cap;while(lo+1<hi){int mid=(lo+hi)/2;if(C[mid][i]<=rem)lo=mid;else hi=mid;}if(lo>=i){rem-=C[lo][i];ans+=C[lo][i+1];}cap=lo;}if(rem)throw std::runtime_error("KK remainder");return ans;}
U upper(int d,int k,U m,U n,int j){if(j==0)return 1;if(j==k)return m;if(j==k+1)return n;cpp_int num,den;int a,b;if(j<k){a=k+1-j;b=k-j;num=cpp_int(C[d][j])*powi(m,a)*powi(C[d][k+1],b);den=powi(C[d][k],a)*powi(n,b);}else{a=j-k;b=j-k-1;num=cpp_int(C[d][j])*powi(n,a)*powi(C[d][k],b);den=powi(C[d][k+1],a)*powi(m,b);}return (num/den).convert_to<U>();}
int main(int argc,char**argv){init();int d=argc>1?std::atoi(argv[1]):13;std::map<std::string,U> count;std::map<int,U> per_k;std::vector<std::tuple<int,U,U,U,U>> resid,suspect;int start=argc>2?std::atoi(argv[2]):1;int end=argc>3?std::atoi(argv[3]):d;for(int k=start;k<end;k++){int r=cutoff(d,k);U low=C[d][k],high=C[r][k];U count_k=0;cpp_int CkPow=powi(C[d][k],k+1),DkPow=powi(C[d][k+1],k);
 const cpp_int scalePow=powi(cpp_int(256),k);U rootUpper=256;
 for(U m=low;m<high;m++){
 U min_n=kk(k,m)+1;
 if(k<=12){U128 s128=pow128(256,k);while(U128(C[d][k])*pow128(rootUpper,k)<U128(m)*s128)rootUpper++;}
 else{while(cpp_int(C[d][k])*powi(cpp_int(rootUpper),k)<cpp_int(m)*scalePow)rootUpper++;}
 U rigorousUpper=(cpp_int(C[d][k+1])*m*rootUpper/(cpp_int(C[d][k])*256)).convert_to<U>();
 if(min_n>rigorousUpper)continue; // mathematically certified integer-only upper bound
 cpp_int rhs=DkPow*powi(m,k+1);
 if(powi(min_n,k)*CkPow>rhs)continue; // exact Maclaurin test
 U max_n=rigorousUpper;
 while(powi(max_n+1,k)*CkPow<=rhs)max_n++;
 while(max_n>0 && powi(max_n,k)*CkPow>rhs)max_n--;
 if(max_n<min_n)continue;
 // u1 upper bound is nonincreasing in n; eliminate the entire exact interval
 // when its n=min_n endpoint is already under Smyth's threshold.
 U u1_most=upper(d,k,m,min_n,1);
 if(10000*u1_most<=17719*(U)d){
     U amount=max_n-min_n+1;count["raw"]+=amount;count["smyth_original"]+=amount;count_k+=amount;continue;
 }
 for(U n=min_n;n<=max_n;n++){
 count["raw"]++;count_k++;
 U u1=upper(d,k,m,n,1);
 if(10000*u1<=17719*(U)d){count["smyth_original"]++;continue;}
 U ud=upper(d,k,m,n,d);
 if(ud<1){count["impossible_ud"]++;continue;}
 U um=upper(d,k,m,n,d-1);
 if(ud>=3){count["ud_ge_3"]++;suspect.emplace_back(k,m,n,ud,um);continue;}
 if(10000*um<=17719*(U)d){count["smyth_reverse_norm1"]++;}
 else{count["norm1_residual"]++;resid.emplace_back(k,m,n,ud,um);}
 if(ud>=2){if(10*um+30<29*(U)d)count["norm2_inverse_elim"]++;else{count["norm2_unresolved"]++;suspect.emplace_back(k,m,n,ud,um);}}
 }
 }
 per_k[k]=count_k;std::cerr<<"k="<<k<<" pairs="<<count_k<<"\n";
 }
 std::string path="independent_cpp_degree"+std::to_string(d)+"_k"+std::to_string(start)+"-"+std::to_string(end-1)+"_20261016.json";std::ofstream f(path);
 f<<"{\"degree\":"<<d<<",\"counts\":{";bool first=true;for(auto &x:count){if(!first)f<<",";first=false;f<<"\""<<x.first<<"\":"<<x.second;}f<<"},\"by_k\":{";first=true;for(auto &x:per_k){if(!first)f<<",";first=false;f<<"\""<<x.first<<"\":"<<x.second;}f<<"},\"residual\":[";first=true;for(auto &x:resid){if(!first)f<<",";first=false;auto[k,m,n,ud,um]=x;f<<"["<<k<<","<<m<<","<<n<<","<<ud<<","<<um<<"]";}f<<"],\"suspect\":[";first=true;for(auto &x:suspect){if(!first)f<<",";first=false;auto[k,m,n,ud,um]=x;f<<"["<<k<<","<<m<<","<<n<<","<<ud<<","<<um<<"]";}f<<"]}\n";
 std::cout<<"d="<<d<<"\n";for(auto &x:count)std::cout<<x.first<<"="<<x.second<<"\n";std::cout<<"residual="<<resid.size()<<" suspect="<<suspect.size()<<" file="<<path<<"\n";
}
