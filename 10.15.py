ALGORITHM HOMEWORK
입력예시
5 3
1 2 5 4 3
5 5 6 6 5
출력예시
26
두개의 배열 A와 B를 가지고 있다. 두 배열은 N개의 원소로 구성되어 있으며
배열의 원소는 모두 자연수이다. 최대 K번 바꿔치기 연산을 수행할 수 있는데
바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서
두 원소를 서로 바꾸는 것을 말한다.
최종목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.
• 첫 번째 줄에서 N, K가 공백으로 구분되어 입력된다.
• 두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다.
• 세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다.
최대 K번 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든

# import numpy as np
# m,n,k = map(int,input().split())
# a = []
# All = []
# max = 0
# max_index = 0
# for i in range(m):
#     a[i] = list(map(int,input().split()))
#     if len(a[i]) > n:
#         break
#     if sum(a[i])>=max:
#         max = sum(a[i])
#         max_index = i
# for i in range(m):
#     if i != max_index:
#         All += a[i]    
# All.sort()
# All.reverse()
# a[max_index].sort()
# for j in range(k):
#     a[max_index][j] 


# [1,2,3]+[1,2,3]
# a = [1,2,3,4,5]
# a.sort()
# a.reverse()
# a

# import java.util.*;
# public class Main {
# public static void main(String[] args) {
# Scanner sc = new Scanner(System.in);
# // N과 K를 입력받기
# int n = sc.nextInt();
# int k = sc.nextInt();
# // 배열 A의 모든 원소를 입력받기
# Integer[] a = new Integer[n];
# for (int i = 0; i < n; i++) {
# a[i] = sc.nextInt();
# }
# // 배열 B의 모든 원소를 입력받기
# Integer[] b = new Integer[n];
# for (int i = 0; i < n; i++) {
# b[i] = sc.nextInt();
# }
# Arrays.sort(a); // 배열 A는 오름차순 정렬 수행
# // 배열 B는 내림차순 정렬 수행
# Arrays.sort(b, Collections.reverseOrder());
# // 첫 번째 인덱스부터 배열의 원소를 최대 K번 비교
# for (int i = 0; i < k; i++) {
# if (a[i] < b[i]) {// A가 B의 원소보다 작은 경우
# int temp = a[i]; // 두 원소를 교체
# a[i] = b[i];
# b[i] = temp;
# }
# else break;
# } // A가 B의 원소보다 크거나 같을 때, 반복문을 탈출
# long result = 0; // 배열 A의 모든 원소의 합을 출력
# for (int i = 0; i < n; i++) {
# result += a[i];
# }
# System.out.println(result)
# 모

m,n,k = map(int,input().split())
#배열수 원소수 교환횟수
arr = [[0]*n for _ in range(m)]
for i in range(n):
    arr[i] = [int(j) for j in input().strip().split(" ")]

max_index = 0
max = 0
for i in 


전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가
있다. 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일
날 견적서를 요청했다.
손님이 문의한 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 이
때 가게 안에 부품이 모두 있는지를 확인하는 프로그램을 작성해 보자.
• 첫째 줄에 정수 N 이 주어진다
• 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다
• 셋째 줄에 정수 M이 주어진다
• 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다
공백으로 구분하여 각 부품이 존재하면 yes를 없으면 no를 출력한다

#10/15 HW
n_list = list(map(int,input().split()))
m_list = list(map(int,input().split()))
for i in range(len(m_list)):
    if m_list[i] in n_list:
        print("yes", end = ' ')
    else:
        print("no",end = ' ')


