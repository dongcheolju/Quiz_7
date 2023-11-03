x = int(input("몇 층짜리 트리를 만들까요~?: "))

for i in range(x):
    for j in range(x - i - 1): # 공백 설정
        print(" ", end="")
    for k in range(2 * i + 1): # 별 삽입
        print("*", end="")
    print()

