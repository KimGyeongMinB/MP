import sys
N = int(sys.stdin.readline()) # 입력값 몇개 넣을 것인지
stack = [] # 입력값
result = []
count = 1
for _ in range(N):
    num = int(sys.stdin.readline())
    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1

    if stack.pop() == num:
        result.append('-')
    else:
        print('NO')
        sys.exit()

for i in result:
    print(i)
