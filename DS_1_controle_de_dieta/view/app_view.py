
class AppView:
    
    def options(self):
        option = input("1 - Usuário\n" +
                       "2 - Alimentos\n")
        
        return option
    
    def popup(self, msg):
        print(msg)
        