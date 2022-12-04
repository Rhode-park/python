#https://www.acmicpc.net/problem/2941

word = input()

wordA = word.replace('c=', '0')
wordB = wordA.replace('c-', '1')
wordC = wordB.replace('dz=', '2')
wordD = wordC.replace('d-', '3')
wordE = wordD.replace('lj', '4')
wordF = wordE.replace('nj', '5')
wordG = wordF.replace('s=', '6')
wordH = wordG.replace('z=', '7')

print(len(wordH))