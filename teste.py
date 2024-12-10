def conta_vogais(texto):
    
    VOGAIS = "AEIOUaeiou"        
    contador = 0
    
    for char in texto:
        
        if char in VOGAIS:
          
          contador += 1
    
    return contador

texto = input()

resultado = conta_vogais(texto)
print(f"O número de vogais na string {texto} é: {resultado}")