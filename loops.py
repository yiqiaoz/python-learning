n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff')
print(n)

friends = ['Jo', 'yiwei', 'sally']
for friend in friends:
    print('Happy new year:' + friend)
print ('Done!')

largest_so_far = -1
print('before' + str(largest_so_far))
for the_number in [-1, 41, 12, 3, 74, 15]:
    if the_number > largest_so_far:
        largest_so_far = the_number
    print(largest_so_far)
print ('after' + str(largest_so_far))

zork = 0
print('before' + str(zork))
for thing in [9, 41, 31, 390, 44]:
    zork = zork + 1
    print (str(zork) + str(thing))
print('after' + str(zork))

zork = 0
print('before' + str(zork))
for thing in [9, 41, 2, 9, 120]:
    zork = zork + thing
    print(str(zork), str(thing))
print('after' + str(zork))

count = 0
sum = 0
print('before' + str(count) + str(sum))
for thing in [10, 39, 340, 344, 87, 987]:
    count = count + 1
    sum = sum + thing
    print(str(count) + str(sum) + str(thing))
print('after', sum, count, sum / count)

print('before')
for value in [10, 34, 45, 32, 677]:
    if value > 20:
        print('Large number', value)
print('after')

found = False
print('before', found)
for value in [7, 3, 45, 678, 34]:
    if value == 3:
        found = True
        break
print('after', found)

smallest = None
print('before')
for value in [12, 4, 5, 6, 234]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('after', smallest)

smallest = None
largest = None
while True:
    num = raw_input('Enter a number:')
    try:
        n = float(num)
        if smallest is None:
            smallest = n
        elif n < smallest:
            smallest = n
        if largest is None:
            largest = n
        elif n > largest:
            largest = n
    except:
        if num == 'done':
            break
        else:
            print ('Invalid input')
            continue
print('Maximum', largest)
print ('Minimum', smallest)
