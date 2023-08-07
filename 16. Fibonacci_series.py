# my approach
# n = int(input("enter range: "))
# t1 = 0
# t2 = 1
# temp = 0
# print(f"Fibonacci Series:",t1,t2,sep=" ",end = " ")
# for _ in range(n-2):
#     temp = t1
#     t1 = t2
#     t2 = temp + t1
#     print(t2, sep=" ", end=" ")

#my approach
def main():
    n = int(input("enter range of fibonacci series: "))
    fibonacci_series(n)


def fibonacci_series(rng):
    temp = 0
    t1 = 0
    t2 = 1
    print("fibonacci series: ", t1, sep=" ", end=" ")
    for _ in range(rng):
        print(t2, sep=" ", end=" ")
        temp = t1
        t1 = t2
        t2 = t1 + temp


main()