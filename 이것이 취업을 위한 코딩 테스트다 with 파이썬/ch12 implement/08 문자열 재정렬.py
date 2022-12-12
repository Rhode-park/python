characters = input()

result = ""
alphabets = []
count = 0

for character in characters:
    if character.isalpha() == True:
        alphabets.append(character)
    if character.isnumeric() == True:
        count += int(character)

alphabets.sort()

for alphabet in alphabets:
    result += alphabet
result += str(count)

print(result)