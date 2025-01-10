class Personaje:

    def __init__(self,name,strenght,intelligence,defense,hp):  #constructor 
        self.name = name
        self.strenght = strenght
        self.intelligence = intelligence
        self.defense = defense
        self.hp = hp

    def atributos(self):    ## imprimir bonito los atributos
        print(f"Nombre: {self.name}")
        print(f"Fuerza: {self.strenght}")
        print(f"Inteligencia: {self.intelligence}")
        print(f"Defensa: {self.defense}")
        print(f"HP: {self.hp}")

    def subirNivel(self,strenght,intelligence,defense): ##sumar valores al subir nivel
        self.strenght += strenght
        self.intelligence += intelligence
        self.defense += defense

    def damage(self,enemy): #calculamos el damage
        return self.strenght - enemy.defense

    def attack(self,enemy): ##llama al metodo anterior, resta el damage a la vida del otro e imprime info
        damage = self.damage(enemy)
        enemy.hp = enemy.hp - damage
        print(f"{self.name} attacked {enemy.name} and caused {damage} of damage")
        print(f"{enemy.name} life is now {enemy.hp}")
    
    def estarVivo(self):
        if self.hp>0:
            print(f"{self.name} is alive")
        else:
            print(f"{self.name} is dead")

personaje1 = Personaje("Lalo", 20, 50,15,100)
personaje2= Personaje ("Luis", 10, 30, 10, 100)
#personaje1.subirNivel(10,5,5)
#personaje1.atributos()
#personaje1.estarVivo()
personaje1.attack(personaje2)
#personaje2.atributos()
