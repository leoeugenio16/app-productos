#contendra una clase producto para poder tener la estructura de 
#doceumento que guardarmeos en la clase de datos :nombre, precio,cantidad

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity 
    def toDBCollection(self):
        return{
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }
