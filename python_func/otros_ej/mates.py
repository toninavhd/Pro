def calcular_expresion(a, b):
    
    parte_izquierda = a**2 + b**2
    
    
    parte_derecha = a * b
    
    
    raiz_cuadrada = parte_derecha ** 0.5
    
    
    result = parte_izquierda - raiz_cuadrada
    
    return result

#otro

def calcular_expresion(a, b):
    
    parte_izquierda = -a * (abs(b))**0.5
    
    
    parte_derecha = 2 * b * a * (abs(a))**0.5
    
   
    result = parte_izquierda / parte_derecha
    
    return float(round(result,7))