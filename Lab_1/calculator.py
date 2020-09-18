#calculator.py

def sum(m, n):
    if n < 0:
        for x in range(abs(n)):
            m -= 1
    else:
        for x in range(n):
            m += 1
    return m

def divide(m, n):
    result = 0
    negativeResult = m > 0 and n < 0 or m < 0 and n > 0
    n = abs(n)
    m = abs(m)
    while (m - n) >= 0:
        m -= n
        result += 1
    
    if negativeResult:
        return -result
    else:
        return result

#print(divide(0,0))
#print(divide(1,0))
print(divide(0,1))
#print(divide(1,1))
#print(divide(3,1))
#print(divide(1,3))
#print(divide(-1,0))
#print(divide(0,-1))
#print(divide(-1,-1))
#print(divide(1,-1))
#print(divide(5,-1))
#print(divide(-1,1))
#print(divide(-5,1))