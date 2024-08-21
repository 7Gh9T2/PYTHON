
class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.estado = 'en_reposo'
        self.motor = Motor(cilindros=4)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self.motor.inyecta_gasolina(10)
        else:
            self.motor.inyecta_gasolina(3)
        self.estado = 'en_movimiento'

    def get_info_auto(self):
        return f"Modelo: {self.modelo}, Marca: {self.marca}, Color: {self.color}, Estado: {self.estado}"

class Motor:
    def __init__(self, cilindros, tipo='diesel'):
        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura = 0

    def inyecta_gasolina(self, cantidad):
        # Implementar lógica si es necesario
        pass
    
    def get_info_motor(self):
        return f"Cilindros: {self.cilindros}, Tipo: {self.tipo}, Temperatura: {self.temperatura}"

if __name__ == '__main__':
    mi_motor = Motor(6, 'nafta')
    mi_auto = Automovil('Tundra', 'Toyota', 'gris')
    mi_auto.motor = mi_motor
    mi_auto.acelerar('rapida')
    print(mi_auto.get_info_auto())
    print(mi_auto.motor.get_info_motor())
