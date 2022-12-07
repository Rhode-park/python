# https://www.acmicpc.net/problem/1316

n = int(input())

words = []
for i in range(n):
    words.append(input())

count = n

for word in words:
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    alphaCount = [0 for _ in range(26)]
    previousAlphabet = word[0]
    for k in range(len(alphabets)):
        if alphabets[k] == previousAlphabet:
            alphaCount[k] += 1
    for i in range(len(word)):
        if word[i] == previousAlphabet:
            continue
        else:
            for j in range(len(alphabets)):
                if alphabets[j] == word[i]:
                    alphaCount[j] += 1
            previousAlphabet = word[i]
    count0 = alphaCount.count(0)
    count1 = alphaCount.count(1)
    if count0+count1 < 26:
        count -= 1

print(count)

#뭔가 코드가 깔끔한 것 같진 않아서 찾아본 다른 사람의 풀이

# N = int(input())
# cnt = N
#
# for i in range(N):
#     word = input()
#     for j in range(0, len(word)-1):
#         if word[j] == word[j+1]:
#             pass
#         elif word[j] in word[j+1:]:
#             cnt -= 1
#             break
#
# print(cnt)