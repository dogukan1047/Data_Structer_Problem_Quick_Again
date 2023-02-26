def solution(s):
    for i in range(int(len(s)/2)):
        if i == 0:
            s[i], s[-1] = s[-1], s[i]
        else:
            s[i], s[-i - 1] = s[-i - 1], s[i]
    return s
print(solution(["h","a","n","t","a","H"]))


def fib( n: int) -> int:
    if n == 2:
        return 1
    if n == 1:
        return 0
    return fib(n - 1) + fib(n - 2)

print(fib(5))
