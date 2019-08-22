#include<bits/stdc++.h>
using namespace std;
main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    /*int c; long long m, x;
    cin>>c;
    x = c;
    m = 4;
    cout<<sizeof(x)<<"\n"<<sizeof(m)<<"\n"<<sizeof(c);*/
    int m = 5;
    for (int i =-12;i<-1;i++){
        if (i%m < 0)
            cout<<(i%m)+m<<endl;
        else
            cout<<(i%m)<<endl;
        
    }
}