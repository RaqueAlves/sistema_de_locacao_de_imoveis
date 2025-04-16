from controller.app_controller import AppController
from model.food import Food
from model.menu import Menu

if __name__ == "__main__":
    # run = AppController().options_menu()

    '''cadastro de um alimento'''
    # menu = Menu()
    # food = Food(name="Arroz", quantity_grams=100, calories_per_serving=130, protein=2.7, carbohydrates=28, fat=0.3)
    # menu.add_food_to_menu(food)
    # print("Alimento cadastrado com sucesso!")

    '''lisar elementos cadastrados'''
    # menu = Menu()
    # for food in menu.list_menu():
    #     print(food)

    '''remover um alimento cadastrado'''
    menu = Menu()
    menu.remove_food_from_menu("Arroz")
    print("Alimento removido com sucesso!")


