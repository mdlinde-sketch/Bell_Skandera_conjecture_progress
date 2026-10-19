#include <boost/multiprecision/cpp_int.hpp>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <array>
#include <string>
#include <chrono>
using boost::multiprecision::cpp_int;
using boost::property_tree::ptree;
using U=unsigned long long;
U C[20][20];
void init(){for(int n=0;n<20;n++){C[n][0]=C[n][n]=1;for(int k=1;k<n;k++)C[n][k]=C[n-1][k-1]+C[n-1][k];}}
cpp_int ipow(cpp_int a,int k){cpp_int z=1;while(k){if(k&1)z*=a;a*=a;k>>=1;}return z;}
U chord(int d,int j,U prev){int a=d-j+1;cpp_int rhs=ipow(prev,a-1)*ipow(C[d][j],a);cpp_int fac=ipow(C[d][j-1],a-1);U lo=0,hi=1;while(ipow(hi,a)*fac<rhs)hi*=2;while(lo+1<hi){U m=(lo+hi)/2;if(ipow(m,a)*fac>=rhs)hi=m;else lo=m;}return hi;}
U local(int d,int j,U prev,U prevprev){return (cpp_int(C[d][j])*C[d][j-2]*prev*prev/(cpp_int(C[d][j-1])*C[d][j-1]*prevprev)).convert_to<U>();}
U tangent(int d,int j,U q1,U q2){return (cpp_int(C[d][j])*ipow(q2,j-1)*ipow(d,j-2)/(ipow(C[d][2],j-1)*ipow(q1,j-2))).convert_to<U>();}
struct Audit {U nodes[7]={},prefixes=0,residual=0,h3prune=0,h4prune=0,survivors=0,blockprune=0,blockq5=0;};
struct Prefix {
 int d; U q[7]={};U tan[7]={}; cpp_int p[7]={};cpp_int h3=0, co00=0,co11=0,co22=0,co01=0,co02=0,co12=0;
 void moments4(){p[0]=d;p[1]=q[1];p[2]=p[1]*p[1]-2*q[2];p[3]=p[1]*p[2]-q[2]*p[2]+q[3]*p[1]-4*q[4];
  auto &a=p[0],&b=p[1],&c=p[2],&e=p[3],&f=p[4];
  co00=c*f-e*e;co11=a*f-c*c;co22=a*c-b*b;
  co01=c*e-b*f;co02=b*e-c*c;co12=b*c-a*e;
  h3=a*co00+b*co01+c*co02;
 }
 cpp_int H4_at(U q5,U q6) {
  p[5]=p[1]*p[4]-q[2]*p[3]+q[3]*p[2]-q[4]*p[1]+5*q5;
  p[6]=p[1]*p[5]-q[2]*p[4]+q[3]*p[3]-q[4]*p[2]+q5*p[1]-6*q6;
  cpp_int detv = co00*p[3]*p[3]+co11*p[4]*p[4]+co22*p[5]*p[5]
    +2*co01*p[3]*p[4]+2*co02*p[3]*p[5]+2*co12*p[4]*p[5];
  return h3*p[6]-detv;
 }
};
int main(int argc,char**argv){init();int d=argc>1?atoi(argv[1]):15;std::string file="independent_cpp_degree"+std::to_string(d)+"_20261016.json";if(argc>2)file=argv[2];ptree root;read_json(file,root);Audit s;auto t0=std::chrono::steady_clock::now();
 for(const char* group:{"residual","suspect"})for(auto &item:root.get_child(group)){
  std::vector<U> row;for(auto&z:item.second)row.push_back(z.second.get_value<U>());
  int k=row[0];U m=row[1],n=row[2],um=row[4];s.residual++;
  if(k!=d-2 && k!=d-3 && k!=d-4){std::cerr<<"NOT COVERED k="<<k<<"\n";return 2;}
  int q1lo=k==d-2?n:(17719*d)/10000+1,q1hi=k==d-2?n:um;
  for(U q1=q1lo;q1<=q1hi;q1++){
   U q2lo=k==d-4?chord(d,2,q1):(k==d-2?m:n);
   U q2hi=k==d-4?local(d,2,q1,1):(k==d-2?m:n);
   if(k==d-4){
     U pairBound=(cpp_int(C[d][k+2])*n*n*C[d][k]/(cpp_int(C[d][k+1])*C[d][k+1]*m)).convert_to<U>();
     q2hi=std::min(q2hi,pairBound);
   }
   if(q2lo>q2hi)continue;
   for(U q2=q2lo;q2<=q2hi;q2++){
   Prefix a; a.d=d;a.q[0]=1;a.q[1]=q1;a.q[2]=q2;
   if((d-1)*q1*q1<2*d*a.q[2])continue;
   if(a.q[2]<chord(d,2,q1) || a.q[2]>local(d,2,q1,1))continue;
   for(int j=3;j<=6;j++)a.tan[j]=tangent(d,j,q1,a.q[2]);
   s.prefixes++;
   U q3lo=chord(d,3,a.q[2]),q3hi=std::min(a.tan[3],local(d,3,a.q[2],q1));
   if(k==d-3||k==d-4){U fixed=k==d-3?m:n;q3lo=std::max(q3lo,fixed);q3hi=std::min(q3hi,fixed);}
   if(q3lo>q3hi)continue;
   for(U q3=q3lo;q3<=q3hi;q3++){
    a.q[3]=q3;s.nodes[3]++;
    U q4lo=chord(d,4,q3),q4hi=std::min(a.tan[4],local(d,4,q3,a.q[2]));
    if(k==d-4){q4lo=std::max(q4lo,m);q4hi=std::min(q4hi,m);}
    if(q4lo>q4hi)continue;
    a.q[4]=q4lo;a.moments4();if(a.h3<0){s.h3prune++;continue;}
    for(U q4=q4lo;q4<=q4hi;q4++){
      a.q[4]=q4;a.moments4();s.nodes[4]++;
      if(a.h3<0)break; // H3 slope in q4 is -4H2
      U q5lo=chord(d,5,q4),q5hi=std::min(a.tan[5],local(d,5,q4,q3));
      if(q5lo>q5hi)continue;
      // Safe interval certificate: H4 decreases as q6 increases (H3 >=0).
      // q6 must be >= chord(d,6,q5), a monotone function of q5,
      // so H4(q5,q6) <= H4(q5,chord(d,6,q5lo)).
      // The right side is a concave quadratic in q5 (leading coefficient -25 H2 <=0).
      // Evaluate its exact maximum across ALL integers q5 in [lo,hi].
      U l6=chord(d,6,q5lo);
      cpp_int f0=a.H4_at(q5lo,l6);
      cpp_int f1=a.H4_at(q5lo+1,l6);
      cpp_int f2=a.H4_at(q5lo+2,l6);
      cpp_int A=(f2-2*f1+f0)/2;
      cpp_int B=f1-f0-A;
      if(A>0){std::cerr<<"ERROR convex H4 q5";return 3;}
      U width=q5hi-q5lo;
      auto quadratic=[&](U t)->cpp_int{return f0+B*t+A*cpp_int(t)*t;};
      cpp_int maxH=std::max(quadratic(0),quadratic(width));
      if(A<0 && B>0){
        cpp_int vertex=B/(-2*A);
        U t=vertex>width?width:vertex.convert_to<U>();
        if(quadratic(t)>maxH)maxH=quadratic(t);
        if(t<width && quadratic(t+1)>maxH)maxH=quadratic(t+1);
      }
      if(maxH<0){s.blockprune++;s.blockq5+=width+1;continue;}
      for(U q5=q5lo;q5<=q5hi;q5++){
       a.q[5]=q5;s.nodes[5]++;
       U q6lo=chord(d,6,q5),q6hi=std::min(a.tan[6],local(d,6,q5,q4));
       if(q6lo>q6hi)continue;
       cpp_int h=a.H4_at(q5,q6lo);
       if(h<0){s.h4prune++;continue;}
       for(U q6=q6lo;q6<=q6hi;q6++){
        s.nodes[6]++;
        if(h<0)break;
        s.survivors++;
        std::cerr<<"SURVIVOR d="<<d<<" k="<<k<<" m="<<m<<" n="<<n<<" q="<<q1<<","<<a.q[2]<<","<<q3<<","<<q4<<","<<q5<<","<<q6<<"\n";
        h-=6*a.h3;
       }
      }
    }
   }
  }
  }
  if(s.residual%20==0){std::cerr<<"progress cases="<<s.residual<<" of "<<root.get_child("residual").size()+root.get_child("suspect").size()<<" depth5="<<s.nodes[5]<<" elapsed="<<std::chrono::duration_cast<std::chrono::seconds>(std::chrono::steady_clock::now()-t0).count()<<"s\n";}
 }
 std::cout<<"degree="<<d<<" pairs="<<s.residual<<" prefixes="<<s.prefixes<<" d3="<<s.nodes[3]<<" d4="<<s.nodes[4]<<" d5="<<s.nodes[5]<<" d6="<<s.nodes[6]<<" h3pruned="<<s.h3prune<<" h4pruned="<<s.h4prune<<" blockprune="<<s.blockprune<<" blockq5="<<s.blockq5<<" survivors="<<s.survivors<<"\n";
 return s.survivors?1:0;
}
