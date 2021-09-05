#문자열에서 숫자를 뽑아내서 1 더한뒤 다시 합쳐서 출력
#만약 숫자가 없다면 1을 붙여서 출력
#ex) adsfsd45 -> adsfsd46 ///// dsafads -> dsafads1


word = input()
num = ''

if word.isalpha():
    word +='1'
else:
    for char in word:
        if char.isdigit():
            num += char
            word = word.replace(char,'')
    word += str(int(num) + 1)
print(word)