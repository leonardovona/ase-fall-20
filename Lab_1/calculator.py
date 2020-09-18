#calculator.py

def sum(m, n):
    if n < 0:
        for _x in range(abs(n)):
            m -= 1
    else:
        for _x in range(n):
            m += 1
    return m

def divide(m, n):
    if n == 0:
        raise ZeroDivisionError
    result = 0
    negativeResult = m > 0 and n < 0 or m < 0 and n > 0
    n = abs(n)
    m = abs(m)
    while (m - n) >= 0:
        m -= n
        result += 1

    #result -= result if negativeResult else result
    
    if negativeResult:
        return -result
    else:
        return result