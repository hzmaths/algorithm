'''
string type str
'''
a='x'
print('the string a is ',a)
print("3 * a =",3*a)
print('a + a ',a+a)
print('a+ str(3) ',a+str(3))
print('the length of string a is ',len(a))

b='hello,world'
for i in range(len(b)):
	print('the ', i,' char of sting b is ',b[i])

for i in range(len(b)):
	print('the ',i, 'th char of string b from right is ',b[-i-1])

print('the char of b from 3 to 7(-1) is ',b[3:7])
