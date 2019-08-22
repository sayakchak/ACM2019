//#include<bits/stdc++.h>
#include<stdio.h>
#include<algorithm>
#include<cstdlib>
main(){
    int T;
    scanf("%d",&T);
    if (T<1 ||T>1000)
        exit(0);
    long x, c, c2, i, N, *A,*B, *D, M_D,m,m_D;
    for (int t= 0; t<T;t++){
        scanf("%ld",&N);
        if(N<1 ||N>(500000))
            exit(0);
        A = new long[N];
        B = new long[N];
        D = new long[N];
        M_D = -1;
        m_D = 1000000001;
        m = 1000000001;
        for (i = 0;i<N;i++){
            scanf("%ld",&A[i]);
            if(A[i]<0||A[i]>1000000000)
                exit(0);
        }
        for (i = 0;i<N;i++){
            scanf("%ld",&B[i]);
            if(B[i]<1||B[i]>1000000000)
                exit(0);
            if (B[i]<m)
                m =  B[i];
            D[i] = A[i]%B[i];
            if (D[i]>M_D)
                M_D =  D[i];
            if (D[i]<m_D)
                m_D =  D[i];
        }
        //std::cout<<m_D<<M_D;
        x = 0;
        c = 0;
        c2 = 0;
        for (i=0;i<N;i++){
            x = A[i];
            while(x%B[i] != m_D){
                x += 1; c += 1;
            }
        }
        //std::cout<<M_D<<std::endl;        
        if (m>M_D){
            for (i=0;i<N;i++){
            x = A[i];
            while(x%B[i] != M_D){
                x += 1; c2 += 1;
            }
            }
        c = std::min(c,c2);
        }
        printf("%ld\n",c);
    }
}