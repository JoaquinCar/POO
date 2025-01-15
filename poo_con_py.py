class Personaje:

    def __init__(self,name,strenght,intelligence,defense,hp):  #constructor 
        self.__name = name
        self.__strenght = strenght
        self.__intelligence = intelligence
        self.__intelligence = defense
        self.__hp = hp

    def atributos(self):    ## imprimir bonito los atributos
        print(f"Nombre: {self.__name}")
        print(f"Fuerza: {self.__strenght}")
        print(f"Inteligencia: {self.__intelligence}")
        print(f"Defensa: {self.__intelligence}")
        print(f"HP: {self.__hp}")

    def subirNivel(self,strenght,intelligence,defense): ##sumar valores al subir nivel
        self.__strenght += strenght
        self.__intelligence += intelligence
        self.__intelligence += defense

    def damage(self,enemy): #calculamos el damage
        return self.__strenght - enemy.__intelligence

    def attack(self,enemy): ##llama al metodo anterior, resta el damage a la vida del otro e imprime info
        damage = self.damage(enemy)
        if damage < 0:
            damage = 0

        enemy.__hp = enemy.__hp - damage
        if enemy.__hp < 0:
            enemy.__hp = 0
            print(f"{self.__name} attacked {enemy.__name} and caused {damage} of damage")
            print (f"{enemy.__name} has {enemy.__hp} points of life, and now is dead")
        else:
            print(f"{self.__name} attacked {enemy.__name} and caused {damage} of damage /n {enemy.__name} life is {enemy.__hp}")
    
    def estarVivo(self):
        if self.__hp>0:
            print(f"{self.__name} is alive")
        else:
            print(f"{self.__name} is dead")
    def get_strenght(self):
        return f"la fuerza es {self.__strenght}"
    
    def set_strenght(self,strenght):
        self.__strenght = strenght
        if strenght <= 0:
            self.__strenght = 0
            print("No se puede tener fuerza negativa")
        else:
            return f"la nueva fuerza es {self.__strenght}"

personaje1 = Personaje("Lalo", 10, 40,15,100)
personaje2= Personaje ("Luis", 10, 30, 50, 100)
#personaje1.subirNivel(10,5,5)
#personaje1.atributos()
#personaje1.estarVivo()
#personaje1.attack(personaje2)
personaje1.set_strenght(-25)
print(personaje1.get_strenght())

