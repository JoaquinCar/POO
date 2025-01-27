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
    
    def personaje_con_mas_vida(self): 
        personajes = [guts, mago_de_hielo, persona]
        personaje_con_mas_vida = max(personajes, key=lambda personaje: personaje.hp)
        return(f"El personaje con mas vida es {personaje_con_mas_vida.name} con {personaje_con_mas_vida.hp} de vida")

    def suma_inteligencias(self):
        personajes = [guts, mago_de_hielo, persona]
        suma_inteligencias = sum(personaje.intelligence for personaje in personajes)
        return (f"La suma de las inteligencias de los personajes es {suma_inteligencias}")

    
    def personajes_vida_mayor_a_80(self):
        personajes = [guts, mago_de_hielo, persona]
        personajes_vida_mayor_a_80 = [personaje for personaje in personajes if personaje.hp >= 80]
        personajes_info = ', '.join(f"{personaje.name} Tiene (HP: {personaje.hp})" for personaje in personajes_vida_mayor_a_80)
        return f"Los personajes con vida mayor a 80 son: {personajes_info}"


    def subirNivel(self,strenght,intelligence,defense): ##sumar valores al subir nivel
        self.strenght += strenght
        self.intelligence += intelligence
        self.defense += defense

    def damage(self,enemy): #calculamos el damage
        return self.strenght - enemy.defense

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


class Guerrero(Personaje):
        def __init__(self, name, strenght, intelligence, defense, hp,sword,shield):
             super().__init__(name, strenght, intelligence, defense, hp)
             self.sword = sword
             self.shield = shield * defense
             self.vida_escudo = hp + self.shield
             

        def atributos(self):   ## sobre escribimos el metodo para que imprima el nuevo atributo, con el super es lo mismo, solo se agrega
            super().atributos()
            print(f"Fuerza de espada: {self.sword} \nEscudo: {self.shield}\n >>>>>>>>>>>>>\n")
    
        
        def elegir_arma(self):
            while True:
                try:
                    choice = int(input("Eres un guerrero,elige un arma \n (1)Lanza de obsidiana, Damage:10 \n (2)Lanza de madera, Damage:5 \n Ingresa tu eleccion: "))
                    if choice == 1:
                        print(f"Ha elegido la lanza de obsidiana con damage de 10, \n")
                        self.sword += 10
                        print(f"Tu fuerza ahora es {self.sword}\n >>>>>>>>>>>>>\n")
                        break
                    elif choice == 2:
                        print(f"Ha elegido la lanza de obsidiana con damage de 5 \n")
                        self.sword += 5
                        print(f"Tu fuerza ahora es {self.sword}\n >>>>>>>>>>>>>\n")
                        break
                    else:
                        print("Valor no valido")
                except ValueError:
                    print("Entrada no válida. Debes ingresar un número.")
            ##sobre escribir el metodo damage para sumar el daño de la espada
        def damage(self,enemy):
            return self.strenght + self.sword - enemy.defense
        

class Mago(Personaje):
        def __init__(self, name, strenght, intelligence, defense, hp, magic):
             super().__init__(name, strenght, intelligence, defense, hp)
             self.magic = magic

        def atributos(self):   ## sobre escribimos el metodo para que imprima el nuevo atributo, con el super es lo mismo, solo se agrega
            super().atributos()
            print(f"Magia: {self.magic} \n >>>>>>>>>>>>>\n ")
        
        def elegir_arma(self):
            while True:
                try:
                    choice = int(input("Eres un mago,elige un arma \n (1)Guia C++, Damage:10 \n (2)Manual de Ensamblador, Damage:5 \n Ingresa tu eleccion: "))
                    if choice == 1:
                        print(f"Ha elegido la guia de C++ con damage de 10 \n")
                        self.magic += 10
                        print(f"Tu magia ahora es {self.magic}\n >>>>>>>>>>>>>\n")
                        break
                    elif choice == 2:
                        print(f"Ha elegido el manual de Ensamblador con damage de 5 \n")
                        self.magic += 5
                        print(f"Tu magia ahora es {self.magic}\n >>>>>>>>>>>>>\n")
                        break
                    else:
                        print("Valor no valido")
                except ValueError:
                    print("Entrada no válida. Debes ingresar un número.")

        def damage(self,enemy):
            return self.magic + self.intelligence - enemy.defense        
            

persona = Personaje("Lalo", 50, 40,15,100)
guts = Guerrero("Guts", 100,20,10,75,10,5)
mago_de_hielo = Mago("Mago de Hielo", 10,50,10,100,10)
guts.atributos()

personaje_con_mas_vida = persona.personaje_con_mas_vida()
print(personaje_con_mas_vida)
inteligencias = persona.suma_inteligencias()
print(inteligencias)
personajes_vida_mayor_a_80 = persona.personajes_vida_mayor_a_80()
print(personajes_vida_mayor_a_80)
