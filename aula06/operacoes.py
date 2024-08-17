def soma(*params):
    res = 0
    for i in params:
        res += i
    return res

def subtracao(*params):
    res = params[0]
    for i in params[1:]:
        res -= i
    return res

def multiplicacao(*params):
    res = 1
    for i in params:
        res *= i
    return res

def divisao(*params):
    res = params[0]
    for i in params[1:]:
        if i == 0:
            continue
        res /= i
    return res

def padrao(a, b, operac):
    return {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b 
    }[operac]