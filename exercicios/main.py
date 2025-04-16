def verifyNumber():
    while True:
        number = input("Digite uma nota entre 0 e 10.")
        if int(number) <= 10 and int(number) >= 0:
            print("Sua nota é: " + number)
            break
        else:
            print("A nota escolhida é inválida!")

def login():
    while True:
        user = input("Digite seu nome do usuário: ")
        password = input("Digite sua senha: ")

        if user != password:
            print("Usuário registrado com sucesso!")
            break
        else:
            print("Escolha uma senha diferente do nome de usuário.")

def obtemDados():
    while True:
        nome = input("Digite um nome com mais de 3 caracteres: ").strip()
        idade = int(input("Digite uma idade entre 0 e 150 anos: "))
        salario = int(input("Digite um salário maior que 0: "))
        sexo = input("Digite 'f' para sexo feminino ou 'm' para masculino: ").strip()
        estado_civil = input("Digite seu estado civil: " +
                             "'s' para solteiro(a), " +
                             "'c' para casado(a), " +
                             "'v' para viúvo(a), " +
                             "ou 'd' para divorciado(a).").strip()
        
        verificacao = leDados(nome, idade, salario, sexo, estado_civil)

        if verificacao:
            print("\n⚠️ Erros encontrados nas entradas fornecidas: ")
            for erro in verificacao:
                print(f"- {erro}")
            print("\nPor favor, corrija os erros e tente novamente.\n")
        else:
            print("\n✅ Dados cadastrados com sucesso!")
            break

def leDados(nome, idade, salario, sexo, estado_civil):
    errors = []

    if len(nome) <= 3:
        errors.append("Número de caracteres insuficientes para nome.")
    if idade < 0 and idade > 150:
        errors.append("Idade fora do intevalo aceito.")
    if salario <= 0:
        errors.append("Salário deve ser maior que 0.")
    if sexo not in ['f', 'm']:
        errors.append("Escolha um sexo que existe.")
    if estado_civil not in ['s', 'c', 'v', 'd']:
        errors.append("Escolha entre as opções de estado civil.")

def calculaAnos(populacaoA, populacaoB, taxaA, taxaB):
    anos = 0

    if taxaA < taxaB:
        print("A população de A nunca ultrapassará a população de B com essa taxa de crescimento.")
    
    elif taxaA > taxaB:
        while populacaoA < populacaoB:
            populacaoA += populacaoA * taxaA
            populacaoB += populacaoB * taxaB
            anos += 1            

    print(f"Levará {anos} anos para as duas populações se igualarem.")

def mostraNumeros(num):
    for i in range(1, num + 1):
        print(i)
    
    for i in range(1, num + 1):
        print(i, end=" ")

