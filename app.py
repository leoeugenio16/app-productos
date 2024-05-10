from flask import Flask,render_template,request,Response,jsonify,redirect,url_for


#cremoas acceso a ala database
import database as dbase
from product import Product

#nos conectamos a la funcion que tenemos en el archivo database
db = dbase.dbConection()
#Rutas de la aplicacion
#esta es la intancia
app = Flask(__name__)

#creamos la primera ruta para lanzar la aplicacion
@app.route('/')
def home():
    products = db['products']
    #Obtenemos todos los datos y los guardamos en la variabel  productsReceived
    productsReceived = products.find()
    #a parte de renderizar el index, vamos a poder obtener los datos obtenidos
    return render_template('index.html', products = productsReceived)


#method POST
@app.route('/products',methods=['POST'])
def addProduct():
    #aca le añadimos a productos lo que trameos de la base de datos, en el caso de no
    #existir lo crea
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']
    
    #con el siguiente condicional vamos a chequear que tenemos todos los datos
    #y los guardmaos en el formulario creado en products
    if name and price and quantity:
        product = Product(name,price,quantity)
        products.insert_one(product.toDBCollection())
        #a travez del metodo response de flask obtendremos una respuesta de metodo
        #json
        response = jsonify({
            'name' : name,
            'price' : price,
            'quantity' : quantity
        })
        #una vez que se guarden los datos nos redirigimos a home
        return redirect(url_for('home'))
    else:
        return notFound()
#Metho DELETE, en la ruta le apsaremos el producto que queremos eleminar como string
@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name' : product_name})
    return redirect(url_for('home'))  

#Method Put
@app.route('/edit/<string:product_name>',methods=['POST'])
def edit(product_name):
    #recogemos los datos igual que en el metohodo add
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']
    if name and price and quantity:
        products.update_one({'name' : product_name},{'$set' : {'name':name,'price' : price, 'quantity' : quantity}})
        responde = jsonify({'message': 'Product' + product_name + 'actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()
@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response
        

#condicionamos

#si este main esta como archivo principal,lanzamos la aplicacion con app.run 
# en modo de desarrollo, en el puerto 4000
if __name__ == '__main__':
    app.run(debug=True, port=4000)