def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)

def computepay(h,r):
    if h > 40:
        p = 1.5 * r * (h - 40)+ 40 * r
    else:
        p = r*h
    return p

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
p = computepay(h,r)
print(p)