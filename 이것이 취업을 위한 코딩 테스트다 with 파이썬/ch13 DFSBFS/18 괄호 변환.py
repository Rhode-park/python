# https://programmers.co.kr/learn/courses/30/lessons/60058

# 정답보고 풀었음

p = input()

def checkCorrect(x):  # stack의 개념
    count = 0
    for i in range(len(x)-1):
        if x[i] == '(':
            count += 1
            print(i, count)
        elif x[i] == ')':
            if count == 0:
                return False
            count -= 1
            print(i, count)
    return True


def devide(x):
    for i in range(2, len(x), 2):
        u = p[0:i]
        v = p[i:len(p)]
        if checkCorrect(u) == True:
            devide(v)



if checkCorrect(p) == True:
    print('True')

devide(p)

print(p.count('('))