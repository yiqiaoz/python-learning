# Tuple is immutable
# Tuples can be compared, so dict-->list with tuples could be sorted.
# for k,v in dict(): (k,v) is list

def lecture1():


    l = list()
    print (dir(l))


    b = tuple()
    print (dir(b))

    (x,y) = (4, 'erika')
    print (y)

    (a,b)=(98,99)
    print (b)

    d = dict()
    d['abc'] = 4
    d['efg'] = 5
    for (x,y) in d.items():
        print (x,y)

    tups = d.items()
    print (tups)

    v = d.values()
    print (v)

    # in dictionary, cannot put the same key more than once, the value can be more than once
    d = {'a':10,'b':1,'c':22}
    print(d.items())
    print (sorted(d.items()))

    for x,y in sorted(d.items()):
        print (x,y)



    print (('a','b','c')<('a','c','d'))

def lecture2():

    # tuples could be compared, which could be used to sort list, dictionary

    c ={'kane':10, 'erika':20, 'chowchow':30,'dowdow':40}
    l = list()
    for k,v in c.items():
        l.append((v,k))
    print (l)

    l = sorted(l,reverse=True)
    print (l)

def lecture3():
    fname = raw_input('Enter file: ')
    fhand = open(fname)

    counts = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0)+1

    tmp = list()
    for key, value in counts.items():
        tpl = (value,key)
        tmp.append(tpl)

    tmp = sorted(tmp, reverse=True)
    for value,key in tmp[:10]:
        print (key,value)


def Listcomprehension():
    fname = raw_input('Enter file: ')
    fhand = open(fname)

    counts = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    # expression in the bracket is a list
    print (sorted([(v,k)for k,v in counts.items()],reverse=True))

def assignment1():
    fname = raw_input('Enter file: ')
    if len(fname)<1:
        fname = '/Users/zhuerika/Desktop/mbox-short.txt'
    fhand = open(fname)
    times =list()
    for line in fhand:
        words = line.split()
        if len(words)<3 or words[0]!= 'From':
            continue

        times.append(words[5])

    counts = dict()
    for time in times:
        hour = time.split(':')
        h = hour[0]
        counts[h] = counts.get(h,0)+1
    print(sorted([(h,c) for h,c in counts.items()]))







if __name__=='__main__':
    lecture1()


