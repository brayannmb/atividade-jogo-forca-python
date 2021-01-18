import random
import vencer
import perder

print (40 * "-")
print ("{:^40}".format("Jogo da Forca")) #centralizar o titulo
print (40 * "-")

def level (nivel):
    while nivel not in '123':
        nivel = input("Digite o nível escolhido: ")
    return nivel

def nivel2 (nivel):
    if nivel == '1':
        aux = easy.lower() #jogando todas as letras para minusculas para melhor comparação 
        #print(aux)

    if nivel == '2':
        aux = medium.lower() #jogando todas as letras para minusculas para melhor comparação
        #print(aux)

    if nivel == '3':
        aux = hard.lower() #jogando todas as letras para minusculas para melhor comparação
        #print(aux)
    return aux

def entradaf (nivel): #função de entrada que busca o nivel no arquivo fruta facil
    if nivel  == '1':
        with open ("Fruta_facil.txt", 'r') as entrada_facil:
            facil = entrada_facil.readlines() #randomizando as palavras 
            fruta = random.choice(facil)
        return fruta

def entradam (nivel):
    if nivel == '2':
        with open ("Fruta_medio.txt", 'r') as entrada_medio:
            medio = entrada_medio.readlines()
            fruta1 = random.choice(medio) #randomizando as palavras 
        return fruta1

def entradad (nivel):
    if nivel == '3':
        with open ("Fruta_dificil.txt", 'r') as entrada_dificil:
            dificil = entrada_dificil.readlines() #randomizando as palavras 
            fruta2 = random.choice(dificil)
        return fruta2

def words (aux): #função de validação de letras
    letras = '1'
    while letras not in "abcdefghijklmnopqrstuvwxyz-":
        letras = str(input("\nDigite uma letra:")).lower() #jogando validação para minuscula para fazer comparação
    return letras

def inserir (letras):
    if letras in aux:
        cont = len(aux) #contagem de caracteres
        for c in range (0,cont): #percorrendo a fruta e verificando se há igualdades entre caractéres
            if aux[c] == letras:
                lista_vazia[c] = letras #adicionando a letra encontra a uma lista 
    return lista_vazia
        

erros = 0
nivel = "x"
tentativa = 7
z = True

while z == True: 
    nivel = (level(nivel))
    easy = (entradaf(nivel))
    medium = (entradam(nivel))
    hard = (entradad(nivel))

    aux = (nivel2(nivel))
    cont = (len(aux))

    lista_vazia = []
    for letra in range(0,cont - 1 ): #aplicando uma lista de traços para identificar espaços a serem escritos
        c = lista_vazia.append('(_)')
        
    val = '1'
    utilizadas = []

        
    while val != aux:
        letras = (words(aux))
        if letras in aux:
            validacao = (inserir(letras))
            val = ''.join(validacao)
            print (f'\nAcerte a palavra: {val}\n')
            utilizadas.append(letras)
            print (f'\nAs letras já utilizadas são: {utilizadas}')

            comparar_aux = aux.split()
            comparar_val = val.split()
            win  = vencer.trofeu(comparar_aux,comparar_val)
            if win == 1:
                continuar = '1'
                while continuar not in 'SN':
                    continuar = input("Desejar continuar? [S/N] ").upper()
                    nivel = 'x'
                    if continuar == 'S':
                        erros = 0
                        aux = val
                        
                    if continuar == 'N':
                        erros = 0
                        z = False
                        aux = val
                        
                
                
        if letras not in aux:
            erros+= 1
            utilizadas.append(letras)
            print (f'As letras já utilizadas são: {utilizadas}')
            failed = perder.fail(erros, aux)
            if failed == 2:
                val = aux
                continuar = '1'
                while continuar not in 'SN':
                    continuar = input("Desejar continuar? [S/N] ").upper()
                    nivel = 'x'
                    if continuar == 'S':
                        erros = 0
                        aux = val 
                    if continuar == 'N':
                        erros = 0
                        z = False
                        aux = val 
            
       
                        

        

        
