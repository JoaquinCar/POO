class Personaje:

    def __init__(self,name,strenght,intelligence,defense,hp):  #constructor 
        self.name = name
        self.strenght = strenght
        self.intelligence = intelligence
        self.intelligence = defense
        self.hp = hp

    def atributos(self):    ## imprimir bonito los atributos
        print(f"Nombre: {self.name}")
        print(f"Fuerza: {self.strenght}")
        print(f"Inteligencia: {self.intelligence}")
        print(f"Defensa: {self.intelligence}")
        print(f"HP: {self.hp}")

    def subirNivel(self,strenght,intelligence,defense): ##sumar valores al subir nivel
        self.strenght += strenght
        self.intelligence += intelligence
        self.intelligence += defense

    def damage(self,enemy): #calculamos el damage
        return self.strenght - enemy.intelligence

    def attack(self,enemy): ##llama al metodo anterior, resta el damage a la vida del otro e imprime info
        damage = self.damage(enemy)
        if damage < 0:
            damage = 0
        enemy.hp = enemy.hp - damage
        if enemy.hp < 0:
            enemy.hp = 0
            print(f"{self.name} attacked {enemy.name} and caused {damage} of damage")
            print (f"{enemy.name} is dead")
        else:
            print(f"{self.name} attacked {enemy.name} and caused {damage} of damage")
            print(f"{enemy.name} life is now {enemy.hp}")
             

    def estarVivo(self):
        if self.hp>0:
            print(f"{self.name} is alive")
        else:
            print(f"{self.name} is dead")

personaje1 = Personaje("Lalo", 10, 40,15,100)
personaje2= Personaje ("Luis", 10, 30, 50, 100)

class Guerrero(Personaje):
        def __init__(self, name, strenght, intelligence, defense, hp,sword):
             super().__init__(name, strenght, intelligence, defense, hp)
             self.sword = sword
            
personaje1 = Personaje("Lalo", 50, 40,15,100)
personaje2= Personaje ("Luis", 10, 30, 40, 100)
guerrero = Guerrero("Guts", 50,20,10,100,10)

#personaje1.subirNivel(10,5,5)
personaje1.attack(personaje2)
#personaje1.atributos()
#personaje1.estarVivo()
#personaje1.attack(personaje2)



