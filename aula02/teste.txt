#!/usr/bin/python3

nome_arq = input ("Digite o nome arquivo: ")
shebang = "#!/usr/bin/python3\n"

try:
    with open(nome_arq+'.py','x') as arq:
            arq.write(shebang)
except FileExistsError:
    with open(nome_arq+'.py','r') as arq:
        conteudo = arq.readlines()
        if conteudo[0] != shebang:            
            conteudo.insert(0,shebang)
            with open(nome_arq+'.py', 'w') as arq:
                arq.writelines (conteudo)
    try:
        with open(nome_arq+'.py','w') as arq:
            arq.writelines(conteudo)
    
    except NameError:
        print ("arquivo ja possui a shebang")