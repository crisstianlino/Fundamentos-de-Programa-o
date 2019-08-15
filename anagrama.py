# coding=utf-8
# Python v3.5
x = input("Palavra 1: ")
y = input("Palavra 2: ")
list1 = list(x)
list2 = list(y)
list1.sort()
list2.sort()
pos = 0
l = True
while pos < len(x) and l:
	if list1[pos] == list2[pos]:
		pos += 1
	else:
		l = False
if l:
	print ("Tais palavras são anagramas")
else:
	print ("Tais palavras NÃO são anagramas")
