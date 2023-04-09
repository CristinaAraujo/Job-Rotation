texto = "exemplo de string"
texto_invertido = ""

for i in range(len(texto)-1, -1, -1):  # percorre um loop reverso começando do último caractere da string 'texto' até o primeiro
    texto_invertido += texto[i]  # adiciona cada caractere invertido na variável 'texto_invertido'

print(texto_invertido)