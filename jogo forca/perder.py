def fail (erros, aux):
    a = 0
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        
        print (f'\nRestam 6 tentativas')

    if(erros == 2):

        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
       
        print (f'\nRestam 5 tentativas')
                    
    if(erros == 3):
                    
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
        
        print (f'\nRestam 4 tentativas')
                    
    if(erros == 4):
                    
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
        
        print (f'\nRestam 3 tentativas')
                    
    if(erros == 5):
                    
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
        
        print (f'\nRestam 2 tentativas')
                    
    if(erros == 6):
                    
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
        
        print (f'\nRestam 1 tentativas')
                    
    if (erros == 7):
                    
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        
        print (f'\nRestam 0 tentativas\n')
                    
        print("Puxa, você foi enforcado!")
        print(f"A palavra era {aux}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           \n")
        a = 2
    return a

