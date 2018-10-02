import sys
if len(sys.argv) == 2:
    print (sys.argv[0])
    print (sys.argv[1])
else:
    print ("Entrada inválida")

arquivo_caminho = str(sys.argv[1])
arquivo = open(arquivo_caminho, "r")
texto = arquivo.readlines()
print ("Mostrando conteúdo de: " +sys.argv[1])
lista = []
for linha in texto :
    print(linha)
    linhasembarran = linha.replace('\n','')
    lista.append(linhasembarran)


print ("Mostrando 1 diretorio: " +lista[0])
print ("Mostrando 2 diretorio: " +lista[1])
print ("Mostrando 3 diretorio: " +lista[2])

#print ("Mostrando lista completa: ") 
#print (lista)

arquivo_caminhoa = str(lista[0])
arquivoa = open(arquivo_caminhoa, "r")
textoa = arquivoa.readlines()
print ("Mostrando conteúdo de: ")
print (lista[0])
listaa = []
for linhaa in textoa:
    linhaasembarran = linhaa.replace('\n','')
    listaa.append(linhaasembarran)
print(listaa)
#
#arquivo_caminhob = str(lista[1])
#arquivob = open(arquivo_caminho, "r")

#arquivo_caminhoc = str(lista[2])
#arquivoc = open(arquivo_caminho, "r")




arquivo.close()
