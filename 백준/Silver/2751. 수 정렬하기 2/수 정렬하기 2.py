import sys

N = int(sys.stdin.readline())

numbers = []
# N번 반복하며 수 입력받기
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

# 정렬하고 출력
numbers.sort()
for number in numbers:
    print(number)