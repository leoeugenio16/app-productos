#nos vamos a mongo db para opbtener un cluster online, para usar las base de datos y las
#conexiones que necesitemos

from pymongo import MongoClient
#para que nos deje conectarnos importamos certifi

import certifi
MONGO_URI ="mongodb+srv://leoeugenio16:OjvarxxEFmf1iAAG@cluster0.bg8dsqb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

ca = certifi.where()

#creamos una funcion para conectarnos a la base de datos

def dbConection():
    try: #cremoas un try poara que se conecte si todo va bien
        client = MongoClient(MONGO_URI,tlsCAFile=ca) #le pasamos la url y el certifiado apra que nos permita conectarnos
        #si la base de datos no existe la creamos con ese nombre
        db = client["dbb_products_app"] #nombre de la base de datos
    except ConnectionError:
        print('Error de conexion con la base de datos')
    return db

#en la terminal instalamos py mongo con el comango pip install pymongo para poder conectarnos a mongodb

#luego instalamos certifi con el comando pip install certifi
# que proporciona una colección de certificados de confianza para ser utilizados en aplicaciones que necesitan
# verificar la autenticidad de conexiones HTTPS

#luego instalamos pymongo[srv], proporciona soporte para los URIs de conexión SRV de MongoDB, lo que facilita la configuración 
# y conexión a un clúster de MongoDB desde la aplicación Python utilizando pymongo

#CLUSTER:un "clúster de bases de datos" se refiere a un conjunto de nodos de bases de datos que trabajan juntos para almacenar
# y gestionar los datos de manera distribuida

