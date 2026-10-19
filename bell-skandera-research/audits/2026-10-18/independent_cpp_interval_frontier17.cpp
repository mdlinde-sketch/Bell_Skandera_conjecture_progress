// Independent C++17/Boost exact interval-frontier classification for all k,
// including d17 k1..12. Does not import Python lists. All comparisons exact.
#include <boost/multiprecision/cpp_int.hpp>
#include <array>
#include <vector>
#include <tuple>
#include <map>
#include <string>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <algorithm>
using boost::multiprecision::cpp_int;
using U=unsigned long long;
using Row=std::array<U,5>;
U C[65][65];
cpp_int power(cpp_int b,int k){cpp_int r=1;while(k){if(k&1)r*=b;b*=b;k>>=1;}return r;}
void init(){for(int i=0;i<65;i++){C[i][0]=C[i][i]=1;for(int j=1;j<i;j++)C[i][j]=C[i-1][j-1]+C[i-1][j];}}
int cutoff(int d,int k){int r=d;while(power(C[r][k+1],k)*power(C[d][k],k+1)<=power(C[d][k+1],k)*power(C[r+1][k],k+1))++r;return r;}
U KK(int k,U m){U sum=0;int cap=64;for(int i=k;i>0;i--){int lo=i-1,hi=cap;while(lo+1<hi){int mid=(lo+hi)/2;if(C[mid][i]<=m)lo=mid;else hi=mid;}if(lo>=i){sum+=C[lo][i+1];m-=C[lo][i];}cap=lo;}if(m)throw std::runtime_error("KK remainder");return sum;}
U floor_root(cpp_int n,int k){if(n<0)throw std::runtime_error("negative root");U lo=0,hi=1;while(power(hi,k)<=n){if(hi>(1ULL<<60))throw std::runtime_error("root U overflow");hi*=2;}while(lo+1<hi){U mid=lo+(hi-lo)/2;if(power(mid,k)<=n)lo=mid;else hi=mid;}return lo;}
U nmax(int d,int k,U m){cpp_int num=power(C[d][k+1],k)*power(m,k+1);cpp_int den=power(C[d][k],k+1);return floor_root(num/den,k);}
U coeff_upper(int d,int k,U m,U n,int j){if(j==k)return m;if(j==k+1)return n;int a,b;cpp_int num,den;
if(j<k){a=k+1-j;b=k-j;num=cpp_int(C[d][j])*power(m,a)*power(C[d][k+1],b);den=power(C[d][k],a)*power(n,b);}
else{a=j-k;b=j-k-1;num=cpp_int(C[d][j])*power(n,a)*power(C[d][k],b);den=power(C[d][k+1],a)*power(m,b);}
return (num/den).convert_to<U>();}
struct Stats{U blocks=0,explicit_n=0,no_pair=0,trace_blocks=0,residual=0,special=0;};
std::vector<Row> res,special;
void classify(int d,int k,U m,U n,Stats &s){U u1=coeff_upper(d,k,m,n,1);if(10000*u1<=17719*(U)d)return;U ud=coeff_upper(d,k,m,n,d);if(!ud)return;U um=coeff_upper(d,k,m,n,d-1);if(ud>=3){special.push_back({(U)k,m,n,ud,um});s.special++;return;}if(10000*um>17719*(U)d){res.push_back({(U)k,m,n,ud,um});s.residual++;}if(ud>=2 && 10*um+30>=29*(U)d){special.push_back({(U)k,m,n,ud,um});s.special++;}}
void search(int d,int k,U a,U b,Stats &s){s.blocks++;U lo=KK(k,a)+1,hi=nmax(d,k,b);if(lo>hi){s.no_pair++;return;}if(10000*coeff_upper(d,k,b,lo,1)<=17719*(U)d){s.trace_blocks++;return;}if(a<b){U mid=a+(b-a)/2;search(d,k,a,mid,s);search(d,k,mid+1,b,s);return;}for(U n=lo;n<=hi;n++){s.explicit_n++;classify(d,k,a,n,s);}}
int main(int argc,char**argv){init();int d=argc>1?std::atoi(argv[1]):17;if(d<2||d>17)throw std::runtime_error("supports d<=17");Stats total;for(int k=1;k<d;k++){Stats s;U a=C[d][k],b=C[cutoff(d,k)][k]-1;search(d,k,a,b,s);total.blocks+=s.blocks;total.explicit_n+=s.explicit_n;total.no_pair+=s.no_pair;total.trace_blocks+=s.trace_blocks;total.residual+=s.residual;total.special+=s.special;std::cerr<<"k="<<k<<" blocks="<<s.blocks<<" explicit_n="<<s.explicit_n<<" residual="<<s.residual<<" special="<<s.special<<"\n";}
std::string path="cpp_interval_frontier_degree"+std::to_string(d)+"_20261018.json";std::ofstream out(path);out<<"{\"degree\":"<<d<<",\"counts\":{\"blocks\":"<<total.blocks<<",\"n_explicit\":"<<total.explicit_n<<"},\"residual\":[";
for(size_t i=0;i<res.size();i++){if(i)out<<",";out<<"[";for(int j=0;j<5;j++){if(j)out<<",";out<<res[i][j];}out<<"]";}out<<"],\"suspect\":[";
for(size_t i=0;i<special.size();i++){if(i)out<<",";out<<"[";for(int j=0;j<5;j++){if(j)out<<",";out<<special[i][j];}out<<"]";}out<<"]}\n";
std::cout<<"DONE d="<<d<<" blocks="<<total.blocks<<" explicit_n="<<total.explicit_n<<" residual="<<res.size()<<" special="<<special.size()<<" file="<<path<<"\n";
}
