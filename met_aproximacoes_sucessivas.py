import math


def fi(x):
    # Solve the equation
    y = math.exp(x-3) # Função 𝜑(𝑥) tal que 𝑓(𝑥) = 0 ⇔ 𝑥 = 𝜑(𝑥); Escreva aqui a função
    return y
    

x0 = 0.5 # Solução inicial

erro = 0.001 # 𝜀 > 0 (precisão);

stop = False
i = 0

while stop == False:
    
    x1  = fi(x0)
    
    if abs(x1 - x0) < erro:
        stop = True
        print(f'x = {x1}, com iterations = {i+2} e erro relativo menor que 𝜀 = {erro}')
        
    else:
        x0 = x1
        i += 1