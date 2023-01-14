#include <stdio.h>
#include <math.h>
#define SIZE 1000001

int arr[SIZE] = { 0 };
int num_arr[10001] = { 0 };
int decimal_arr[10001] = { 0 };

int main() {
   int len, k = 0;
   long long total = 1;

   for (int i = 2; i <= sqrt(SIZE); i++) {   // 최대값의 제곱근까지 반복
      if (arr[i] == 0) {      //i가 소수이면
         for (int j = 2; i * j < SIZE; j++) {   // 자신을 제외한 i의 배수 제거
            arr[i * j] = 1;
         }
      }
   }

   scanf("%d", &len);
   for (int i = 0;i < len;i++) {
      scanf("%d", &num_arr[i]);
      if (arr[(num_arr[i])] == 0) { //입력받은 수 중 소수만 decimal_arr로 받기
         decimal_arr[k] = num_arr[i];
         k++;
      }
   }
   for (int i = 0;i < k;i++) { //중복되는 수 제거
      for (int j = i+1;j < k;j++) {
         if (decimal_arr[i] == decimal_arr[j]) {
            decimal_arr[j] = 1;
         }
      }
   }
   for (int i = 0;i < k;i++) { //소수끼리 곱해서 최소공배수 구하기
      total *= decimal_arr[i];
   }

   if (total == 1) {
      total = -1;
   }
   printf("%d", total);
   return 0;
}