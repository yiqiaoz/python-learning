# dict is collection of pairs. it's like a mini database
# dict is mutable, but does not have order
# dict.items() --> list

def lecture1():

    purse = dict()
    purse['Money'] = 12
    purse['candy'] = 3
    purse['tissue'] = 6
    print (purse)

    print (purse['Money'])

    purse['tissue'] = purse['tissue']+1
    print(purse['tissue'])

    jjj = {'name': 'chuck','age': 42, 'family':3}
    print(jjj)

    ooo = {}
    print (ooo)

def lecture2():

    counts = dict()
    names = ['erika','kane','rachel','joey','erika','erika','kane']
    for name in names:
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] = counts[name]+1
    print (counts)

def lecture3():

    counts = dict()
    names = ['erika', 'kane', 'rachel', 'joey', 'erika', 'erika', 'kane']
    for name in names:
        counts[name] = counts.get(name,0)+1
    print (counts)

def lecture4():

    counts = {'rachel': 1, 'kane': 2, 'joey': 1, 'erika': 3}
    for key in counts:
        print(key, counts[key])

    print(list(counts))
    print (counts.keys())
    print (counts.values())
    print (counts.items())

    # 2 iteration variables
    for aaa,bbb in counts.items():
        print (aaa,bbb)

def lecture5():

    fname = raw_input('Enter file:')
    fhand = open(fname)

    counts = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0)+1

    bigword = None
    bigcount = None
    for word,count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count

    print (bigword, bigcount)

def assignment1():

    fname = raw_input('Enter file:')
    if len(fname)<1:
        fname = '/Users/zhuerika/Desktop/mbox-short.txt'
    fhand = open(fname)


    counts  = dict()

    for line in fhand:
        if not line.startswith('From '):
            continue
        words = line.split()
        print(words)
        name = words[1]

        counts[name] = counts.get(name,0)+1

    print (counts)

    bigname = None
    bigcount = None
    for name,count in counts.items():
        if bigcount is None or count > bigcount:
            bigcount = count
            bigname =name

    print (bigname,bigcount)







if __name__=='__main__':
    lecture4()

