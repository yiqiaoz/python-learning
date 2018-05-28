import re


def print_cheese():
    xfile = open('/Users/zhuerika/Desktop/absentees.txt', 'r')
    for cheese in xfile:
        print (cheese)


if __name__ == '__main__':
    print_cheese()

xfile = open('/Users/zhuerika/Desktop/absentees.txt', 'r')
count = 0
for line in xfile:
    count = count + 1
print ('line count:', count)

xfile = open('/Users/zhuerika/Desktop/absentees.txt', 'r')
inp = xfile.read()
print(len(inp))
print (inp[:3])

xfile = open('/Users/zhuerika/Desktop/absentees.txt', 'r')
for line in xfile:
    if line.startswith('Jeff'):
        print (line)

xfile = open('/Users/zhuerika/Desktop/absentees.txt', 'r')
for line in xfile:
    line = line.rstrip()
    if line.startswith('b'):
        print (line)


xfile = open('/Users/zhuerika/Desktop/absentees.txt', 'r')
for line in xfile:
    line = line.rstrip()
    if not line.startswith('b'):
        continue
    print (line)

xfile = open('/Users/zhuerika/Desktop/absentees.txt', 'r')
for line in xfile:
    line = line.rstrip()
    if not 'gmail.com' in line:
        continue
    print (line)

filename = input('Enter the filename:')
fhand = open(filename)
count = 0
s = 0
pattern = '^[a-zA-Z\-]*\s([0-9\.]*)$'
for line in fhand:
    matched = re.match(pattern, line)
    if matched:
        s += float(re.match(pattern, line).group(1))
    # if line.startswith('X-DSPAM-Confidence'):
    #     count = count + 1
    #     begin = line.find(' ')
    #     number = line[begin + 1:]
    #     n = float(number)
    #     s = s + n
    else:
        continue
print (s / count)



filename = input('Enter the filename: ')
fhand = open(filename)
count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print ('there were', count, 'subject line in', filename)

filename = raw_input('Enter the filename: ')
try:
    fhand = open(filename)
except:
    print ('the file cannot be opened:', filename)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print ('there were', count, 'subject line in', filename)

fname = input('Enter file name: ')
fh = open(fname)
for line in fh:
    line = line.upper()
    line = line.strip()
    print(line)
