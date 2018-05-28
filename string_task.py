fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

fruit = 'banana'
for letter in fruit:
    print(letter)

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print (count)

word = 'Yiqiao Zhu'
print(word[0:4])
print (word[7:9])
print (word[8:20])
print (word[:2])
print (word[3:])

a = 'hello'
x = a + 'Yiqiao'
print (x)

a = 'hello'
x = a + '' + 'Yiqiao'
print (x)

fruit = 'banana'
if 'n' in fruit:
    print ('found it!')

f = 'Apple'
if f == 'banana':
    print ('all right, bananas.')
if f < 'banana':
    print('your world,' + f + ',comes before banana.')
elif f > 'banana':
    print('your world' + f + ',comes after banana.')
else:
    print('all right,bananas.')

greet = 'Hello Yiwei'
zap = greet.lower()
print(zap)

print('Hello Yiqiao'.lower())

stuff = 'Love you'
type(stuff)
dir(stuff)

phrase = 'Love you'
pos = phrase.find('ove')
print(pos)

greet = 'Hello Yiqiao'
love = greet.replace('Yiqiao', 'Yiwei')
print (love)

greet = '  hello yiqiao  '
love = greet.lstrip()
print (love)

greet = '  hello yiqiao  '
love = greet.rstrip()
print (love)

greet = '  hello yiqiao  '
love = greet.strip()
print (love)

line = 'Please have a nice day'
line.startswith('Please')

line = 'Please have a nice day'
line.startswith('p')

data = 'From yzz5070@gmail.com Sat Jan 25 09:18:34 2012'
atpos = data.find('@')
print(atpos)
tops = data.find(' ', atpos)
print(tops)
host = data[atpos + 1:tops]
print (host)

x = 'From marquard@uct.ac.za'
a = x.find('@')
print(a)
b = x.find('.', a)
print(b)
host = x[a + 1:b]
print(host)

text = 'X-DSPAM-Confidence:    0.8475'
begin = text.find('0')
print(begin)
end = text.find('5',begin)
print (end)
number = text[begin:end+1]
print(float(number))

