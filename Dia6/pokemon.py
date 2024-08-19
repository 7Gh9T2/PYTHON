class Pokemon:
    nombre = None
    tipo = None
    vida = None
    evolucion = None

    def __init__(self, nombre, tipo, vida, evolucion):
        self.nombre = nombre
        self.tipo = tipo 
        self.vida = vida
        self.evolucion = evolucion  # 1 o 2 o 3 
        self.ataque = []

    def setAtaque(self, ataque):
        self.ataque.append(ataque)

    def atacar(self, i):
        print(f"{self.nombre} atacó con {self.ataque[i]}")
    
    def defenderse(self):
        print(f"{self.nombre} se defendió")

if __name__ == "__main__":
    picachu = Pokemon(nombre="PICACHU", tipo="ELECTRICO", vida=200 , evolucion=1)
    charizar = Pokemon(nombre="CHARIZAR", tipo="FUEGO", vida=300, evolucion=3)
    

    charizar.setAtaque("FUEGO")
    picachu.setAtaque("ELECTRICO")
    
    
    charizar.atacar(0)
    picachu.defenderse()
