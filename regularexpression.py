def lecture1():

    fhand = open('/Users/zhuerika/Desktop/mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if line.find('From:')>=0:
            print (line)


def lecture2():
    import re
    fhand = open('/Users/zhuerika/Desktop/mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if re.search('From:',line):
             print (line)

def lecture3():

    fhand = open('/Users/zhuerika/Desktop/mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if line.startswith('From:'):
            print (line)


def lecture4():
    import re
    fhand = open('/Users/zhuerika/Desktop/mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if re.search('^From:',line):
             print (line)

# ^X.*:  means start with X  then follow by any character for 0 or more times:
# ^X-/S+ start with X  then follow by a dash, non-white space character for one or more times :



def lecture5():

    import re
    x = 'My 2 favourite numbers are 19 and 42'
    y = re.findall('[0-9]+',x)     # extract one or more digit
    print (y)


    import re
    x = 'My 2 favourite numbers are 19 and 42'
    y = re.findall('[AEIOU]+',x)     # extract one or more UPPERCASE

def lecture6():
    #greedy matching; tend to find the largest possible string
    import re
    x = 'From: Using the: character'
    y = re.findall('^F.+:',x)
    print (y)

    import re
    x = 'From: Using the: character'
    y = re.findall('^F.+?:', x)  # non-greedy
    print (y)

def lecture7():
    import re
    x = 'From yzz5070@gmail.com Thu Jan  11 08:08:08 2018'
    y = re.findall('\S+@\S+', x)     #   \S is non-blank character
    print (y)


def lecture8():
    # extracting less than matching by using ()
    import re
    x = 'From yzz5070@gmail.com Thu Jan  11 08:08:08 2018'
    y = re.findall('^From (\S+@\S+)', x)  # \S is non-blank character
    print (y)

def lecture9():
    # extracting host using find and string slicing
    data = 'From yzz5070@gmail.com Thu Jan  11 08:08:08 2018'
    atpos = data.find('@')
    print(atpos)
    stopus = data.find(' ',atpos)
    print (stopus)
    host = data[atpos+1: stopus]
    print (host)

    #double split
    data = 'From yzz5070@gmail.com Thu Jan  11 08:08:08 2018'
    words = data.split()
    email = words[1]
    piece = email.split('@')
    host = piece[1]
    print (host)

    #Regex
    import re
    data = 'From yzz5070@gmail.com Thu Jan  11 08:08:08 2018'
    host = re.findall('@([^ ]*)', data)   # [^ ] match non-blank character
    print (host)

    import re
    data = 'From yzz5070@gmail.com Thu Jan  11 08:08:08 2018'
    host = re.findall('^From .*@([^ ]*)', data)  # [^ ] match non-blank character
    print (host)

def exercise1():
    import re
    fhand = open('/Users/zhuerika/Desktop/mbox-short.txt')
    numlist = list()
    for line in fhand:
        line = line.rstrip()
        spam = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) #[0-9.]  a digit or period
        if len(spam) != 1:
            continue
        num = float(spam[0])
        numlist.append(num)
    print ('Maximum:', max(numlist))


def lecture10():
    # escape character: ask a regular expression character to behave normally, prefix with '\'
    import re
    x = 'we just receive $10.00 for cookie'
    y = re.findall('\$[0-9.]+', x)
    print (y)


def assignment1():

    import re
    fname = raw_input('Enter file:')

    if len(fname)<1:
        fname = '/Users/zhuerika/Desktop/regex_sum_2554.txt'
    fhand = open(fname)
    l = list()
    for line in fhand:
        line = line.rstrip()
        numbers = re.findall('[0-9]+', line)
        for n in numbers:
            number = int(n)
            l.append(number)
    print (sum(l))









if __name__=='__main__':
    assignment1()
