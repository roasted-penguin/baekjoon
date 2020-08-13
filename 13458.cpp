/*
1. Time complexity O(n^2) over -> time out
2. If answer's data type is int, it brings out wrong answer(negative value) because the answer can be 10^12 for maxinum. -> answer's data type has to be long long(printf format : %lld).
*/

#include <stdio.h>
#include <iostream>
 
using namespace std;
 
int main()
{
   int N,super,assist;
   int A[1000000];
   
   
   scanf("%d",&N);
   for(int i=0;i<N;i++){
       scanf("%d",&A[i]);
   }
   scanf("%d%d",&super,&assist);
//   for(int k=0;k<N;k++) printf("%d ",A[k]);
//   printf("\n");
   
   long long ans = 0;//N의최대가 10^6이고, ans값이 최대 10^12나올수 있으므로 long long 사용
   for(int num=0;num<N;num++){
       long long int stack = 1;
       int student = A[num];
       
       if(student > super){//총감독관
           student = student-super;
           stack++;
           
        //   while(student > assist){//부감독관
        //         student = student-assist;
        //         stack++;
        //         // printf("\nhere");
        //   }
        //반복문 -> O(n^2)
        
            if(student%assist == 0)  stack = stack + student/assist - 1;
            else stack = stack + student/assist;
            //Timecomplexity해결
        
       }
       //else는 총감독관 하나로 커버가능하므로 stack = 1
       ans = ans + stack;
    //   printf("\n%lld ",ans);
   }
   printf("%lld",ans);
}
