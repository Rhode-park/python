# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    n = len(s)

    result = []

    if n == 1:
        return 1
    else:
        for i in range(1, n + 1):
            compression = ''
            count = 1
            previous = s[:i]
            for j in range(i, n + i, i):  # range(i, n+1, i)이라고 하면 안 됨
                if previous == s[j:j + i]:
                    count += 1
                elif previous != s[j:j + i]:
                    if count != 1:
                        compression += str(count) + previous
                    if count == 1:
                        compression += previous
                    previous = s[j:j + i]
                    count = 1
            result.append(len(compression))
        return min(result)