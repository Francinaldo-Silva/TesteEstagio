def vogais(palavra):
    v = "aeiou"
    total = 0
    for i in palavra:
        if i in v:
            total += 1
    return total
palavra = "paralelepipedo"
print(vogais(palavra))
    
