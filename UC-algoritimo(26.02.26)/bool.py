#resp = input("Voce vai passar de ano? s/N:")
#resultado = bool(resp)

#print("Resposta", resp )
#print("resultado", resultado)


resp = input("Voce vai passar de ano? s/N:").strip().lower() 

resultado = (resp == "s")

print("Resultado", resultado )
print(type(resultado))
