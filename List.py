# list enclosed with []
# list has order and is mutable
# can create a list with list().append
# line.split() --> list --> dict.get(word in list,0)+1--> dict


def basic_function():
    t = [3, 4, 5, 6, 7, 8, 9, 10]
    print t[1:4]
    print t[:3]
    print t[3:]
    print t[:]

    print([1, 2, 3])

    print (['marry', 3, ['john', 25]])

    for i in [5, 4, 3, 2, 1]:
        print(i)
    print('blastoff')

    friends = ['Carrie', 'Miranda', 'Chalotte']
    for friend in friends:
        print ('Happy new year:', friend)
    print ('Done!')

    friends = ['Carrie', 'Miranda', 'Chalotte']
    print (friends[1])

    fruit = 'Banana'
    x = fruit.lower()
    print(x)


    lotte = [1, 2, 3, 4, 5]
    lotte[2] = 5
    print (lotte)

    greet = 'hello bob'
    print (len(greet))

    x = [1, 2, 'joe', 99]
    print (len(x))

    print(range(len(x)))

    print (range(10))

    friends = ['Carrie', 'Miranda', 'Chalotte']
    for i in range(len(friends)):
        friend = friends[i]
        print ('Happy new year:', friend)

    a = [1, 2, 3]
    b = [2, 5, 6]
    c = a + b
    print(c)

    t = [3, 4, 5, 6, 7, 8, 9, 10]
    print t[1:4]
    print t[:3]
    print t[3:]
    print t[:]

    x = list()
    print type(x)
    print dir(x)

    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    print(fruits.count('apple'))
    print(fruits.index('banana'))
    print(fruits.index('banana', 4))
    fruits.reverse()
    print (fruits)
    fruits.append('grape')
    print (fruits)

    fruits.sort()
    print (fruits)

    print(fruits.pop(4))
    print(fruits)

    fruits.remove('banana')
    print(fruits)

    fruits.insert(len(fruits), 'yiwei')
    print(fruits)

    stuff = list()

    stuff.append(99)
    stuff.append('book')
    stuff.append('yiwei')
    print(stuff)

    print('book' in stuff)
    print(6 not in stuff)

    nums = [1, 8, 9, 67, 0, 89, 765]
    print (len(nums))
    print (max(nums))
    print (min(nums))
    print(sum(nums) / len(nums))

    count = 0
    sum_numbers = 0
    print('before' + str(count) + str(sum_numbers))
    for thing in nums:
        count = count + 1
        sum_numbers = sum_numbers + thing
        print(str(count) + str(sum_numbers) + str(thing))
    print('after', sum_numbers, count, sum_numbers / count)

    total = 0
    count = 0
    while True:
        inp = raw_input('Enter a number:')

        if inp == 'done':
            break
        value = float(inp)
        total = total + value
        count = count + 1
    average = total / count
    print('Average:', average)

    numlist = list()
    while True:
        inp = raw_input('Enter a number:')
        if inp == 'done':
            break
        value = float(inp)
        numlist.append(value)
    average = sum(numlist) / len(numlist)
    print ('Average:', average)


def split_words():
    abc = 'with three words'
    stuff = abc.split()
    print (stuff)
    print (len(stuff))
    print (stuff[0])
    for w in stuff:
        print w



def split_string():


    line = 'first;second;third'
    thing = line.split(';')
    print thing
    print (len(thing))


    fhand = open('/Users/zhuerika/Desktop/mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From '):
            continue
        words = line.split()
        print(words[2])
        email = words[1]
        pieces = email.split('@')
        print (pieces[1])


def assignment1():
    filename = raw_input('Enter the filename:')
    with open(filename, 'r') as fhand:
        count = 0
        for line in fhand:

            line = line.rstrip()
            words = line.split()
            # Guardian in a compound statement
            if len(words) < 3 or words[0] != 'From':
                continue

            count = count+1

            email = words[1]
            print (email)
        print("There were", count, "lines in the file with From as the first word")


def assignment2():
    filename = raw_input('Enter a filename:')
    with open(filename,'r') as fhand:
        poem = list()
        for line in fhand:
            line = line.rstrip()
            words = line.split()
            print (words)
            for word in words:
                if word not in poem:
                    poem.append(word)
        poem.sort()
        print(poem)







if __name__ == '__main__':
    basic_function()
