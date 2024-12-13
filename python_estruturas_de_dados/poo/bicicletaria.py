class Bibicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Bibi...")
    
    def parar(self):
        print("Parando")
    
    def correr(self):
        print("Correndo...")  
    
    def __str__(self):
        return f"{self.__class__.__name__}: {vars(self)}"
    
b1 = Bibicleta("Vermelha", "Caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

print(b1)

     