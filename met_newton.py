import math


def f(x):
    # Solve the equation
    y = x**3 + math.cos(x) # f(x), função
    yprime = 3*x**2 - math.sin(x) # f'(x), derivada da função
    return  y / yprime


x0 = -0.5 # Solução inicial

erro = 0.01 # 𝜀 > 0 (precisão);

stop = False
i = 0

while stop == False:
    
    x1 = x0 - f(x0)
    
    if abs(x1 - x0) < erro:
        stop = True
        print(f'x = {x1}, com iterations = {i+2} e erro relativo menor que 𝜀 = {erro}')
        
    else:
        x0 = x1
        i += 1
