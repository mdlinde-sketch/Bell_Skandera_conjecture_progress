// Exact C++ finite PSD verifier for norm-one degree 14 residuals.
// Adapted from independent_unitnorm_d14_20261016.cpp, with necessary shifted moments.
// Reads independent_cpp_degree14_20261016.json from the 16 October audit archive.
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>
#include <iostream>
#include <map>
#include <array>
#include <algorithm>
#include <cstdint>
using boost::multiprecision::cpp_int;
using boost::property_tree::ptree;
using U=unsigned long long;
U C[20][20];
void init(){for(int n=0;n<20;n++){C[n][0]=C[n][n]=1;for(int k=1;k<n;k++)C[n][k]=C[n-1][k-1]+C[n-1][k];}}
cpp_int power(cpp_int a,int k){cpp_int p=1;while(k){if(k&1)p*=a;a*=a;k>>=1;}return p;}
U chord(int d,int j,U prev){int a=d-j+1;cpp_int rhs=power(prev,a-1)*power(C[d][j],a);cpp_int leftscale=power(C[d][j-1],a-1);U lo=0,hi=1;while(power(hi,a)*leftscale<rhs)hi*=2;while(lo+1<hi){U mid=(lo+hi)/2;if(power(mid,a)*leftscale>=rhs)hi=mid;else lo=mid;}return hi;}
U local(int d,int j,U prev,U prevprev){return (cpp_int(C[d][j])*C[d][j-2]*prev*prev/(cpp_int(C[d][j-1])*C[d][j-1]*prevprev)).convert_to<U>();}
U tangent(int d,int j,U q1,U q2){if(j==1)return q1;if(j==2)return q2;return (cpp_int(C[d][j])*power(q2,j-1)*power(d,j-2)/(power(C[d][2],j-1)*power(q1,j-2))).convert_to<U>();}
cpp_int H3(int d,const U q[]){cpp_int p1=q[1],p2=p1*p1-2*q[2],p3=p1*p2-cpp_int(q[2])*p1+3*q[3],p4=p1*p3-cpp_int(q[2])*p2+cpp_int(q[3])*p1-4*q[4];return d*(p2*p4-p3*p3)-p1*(p1*p4-p2*p3)+p2*(p1*p3-p2*p2);}
cpp_int S2(int d,const U q[]){cpp_int p1=q[1],p2=p1*p1-2*q[2],p3=p1*p2-cpp_int(q[2])*p1+3*q[3];return p1*p3-p2*p2;}
cpp_int S3(int d,const U q[]){
 cpp_int p1=q[1],p2=p1*p1-2*q[2],p3=p1*p2-cpp_int(q[2])*p1+3*q[3];
 cpp_int p4=p1*p3-cpp_int(q[2])*p2+cpp_int(q[3])*p1-4*q[4];
 cpp_int p5=p1*p4-cpp_int(q[2])*p3+cpp_int(q[3])*p2-cpp_int(q[4])*p1+5*q[5];
 return p1*(p3*p5-p4*p4)-p2*(p2*p5-p4*p3)+p3*(p2*p4-p3*p3);
}
cpp_int det4(const std::array<std::array<cpp_int,4>,4>& a){std::array<int,4> p={0,1,2,3};cpp_int res=0;do{int inv=0;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)if(p[i]>p[j])inv++;cpp_int term=1;for(int i=0;i<4;i++)term*=a[i][p[i]];res+=(inv%2)?-term:term;}while(std::next_permutation(p.begin(),p.end()));return res;}
cpp_int H4(int d,const U q[]){std::array<cpp_int,7> p;p[0]=d;for(int s=1;s<=6;s++){p[s]=0;for(int i=1;i<s;i++){cpp_int term=cpp_int(q[i])*p[s-i];if((i-1)%2)term=-term;p[s]+=term;}cpp_int term=cpp_int(s)*q[s];if((s-1)%2)term=-term;p[s]+=term;}
 std::array<std::array<cpp_int,4>,4> h;for(int i=0;i<4;i++)for(int j=0;j<4;j++)h[i][j]=p[i+j];return det4(h);}
struct Stats{U nodes[7]={},h3_pruned=0,h4_pruned=0,s2_pruned=0,s3_pruned=0,survivors=0,initial=0,initial_accepted=0;};
void dfs(int d,int j,U q[],int fixed3,U tangents[],Stats &st){
 if(j>6){st.survivors++;std::cerr<<"SURVIVOR q=";for(int i=0;i<=6;i++)std::cerr<<q[i]<<",";std::cerr<<"\n";return;}
 U lo=chord(d,j,q[j-1]);U hi=std::min(tangents[j],local(d,j,q[j-1],q[j-2]));
 if(fixed3>=0 && j==3){lo=std::max(lo,(U)fixed3);hi=std::min(hi,(U)fixed3);}
 if(lo>hi)return;
 if(j==3){q[3]=hi;if(S2(d,q)<0){st.s2_pruned++;return;}}
 if(j==4){q[4]=lo;if(H3(d,q)<0){st.h3_pruned++;return;}}
 if(j==5){q[5]=hi;if(S3(d,q)<0){st.s3_pruned++;return;}}
 if(j==6){q[6]=lo;if(H4(d,q)<0){st.h4_pruned++;return;} /* H4 decreases with q6 since H3>=0 */}
 for(U v=lo;v<=hi;v++){
  q[j]=v;st.nodes[j]++;
  if(j==3 && S2(d,q)<0)continue;
  if(j==5 && S3(d,q)<0)continue;
  if(j==4 && H3(d,q)<0)break; // H3 affine with negative slope, H2>=0
  if(j==6){if(H4(d,q)<0)break;st.survivors++;std::cerr<<"SURVIVOR q=";for(int i=0;i<=6;i++)std::cerr<<q[i]<<",";std::cerr<<"\n";}
  else dfs(d,j+1,q,fixed3,tangents,st);
 }
}
int main(int argc,char**argv){init();int d=14;std::string path=argc>1?argv[1]:"independent_cpp_degree14_20261016.json";ptree root;read_json(path,root);Stats st;for(const char* group: {"residual", "suspect"}) for(auto &item:root.get_child(group)){std::vector<U> v;for(auto &z:item.second)v.push_back(z.second.get_value<U>());int k=v[0];U m=v[1],n=v[2],um=v[4];st.initial++;int q1low=(17719*d)/10000+1;int q1high=(k==12)?n:um;
 for(int q1=(k==12?n:q1low);q1<=q1high;q1++){
  U q[15]={};q[0]=1;q[1]=q1;q[2]=(k==12?m:n);q[14]=1;
  if((d-1)*q[1]*q[1]<2*d*q[2])continue;
  if(q[2]<chord(d,2,q[1]))continue;
  if(q[2]>local(d,2,q[1],1))continue;
  U tangents[7]={};for(int j=3;j<=6;j++)tangents[j]=tangent(d,j,q[1],q[2]);
  int fixed3=k==11?(int)m:-1;
  st.initial_accepted++;dfs(d,3,q,fixed3,tangents,st);
 }
 }
 std::cout<<"d=14 residual_cases="<<st.initial<<" prefixes="<<st.initial_accepted<<"\n";
 for(int j=3;j<=6;j++)std::cout<<"depth"<<j<<"="<<st.nodes[j]<<"\n";
 std::cout<<"H3_bound_pruned="<<st.h3_pruned<<" H4_bound_pruned="<<st.h4_pruned<<" S2_pruned="<<st.s2_pruned<<" S3_pruned="<<st.s3_pruned<<" survivors="<<st.survivors<<"\n";
 return st.survivors?1:0;
}
