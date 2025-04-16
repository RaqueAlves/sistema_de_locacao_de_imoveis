class UserView:

    def creat_user(self):
        print("--- Sistema de controle de dieta ---\n" +
              "Preencha as informações abaixo:\n")
        name = input("Nome: ")
        age = int(input("Idade: "))
        gender = input("Gênero(Feminino/Masculino): ")
        weight = float(input("Peso(kg): "))
        height = float(input("Altura(m): "))
        activity_level = input("Escreva seu nível de atividade física:\n"
            "sedentário\n"
            "atividade leve\n"
            "atividade moderada\n"
            "atividade intensa\n"
            "atividade muito intensa\n")
        goals = input("Objetivo:\n"
                      "perda de peso\n"
                      "manutenção\n"
                      "ganho de massa\n")

        return name, age, gender, weight, height, activity_level, goals
    
    def show_user(self, users):
        for user in users:
            print(user)
    
    def options(self):
        choose_option = input("--- Sistema de controle de dieta ---\n" +
              "1 - Verificar informações de cadastro\n" +
              "2 - Registro de consumo diário\n" +
              "3 - Verificar Metabolismo Basal e Gasto Energético Total\n")
        return choose_option

