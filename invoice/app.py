from flask import Flask, render_template, jsonify, redirect
import csv

app = Flask(__name__)

def cargar_productos():
    productos = []
    with open('./invoice/productos.csv', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            productos.append({
                'nombre': fila['nombre_producto'],
                'precio': fila['precio']
            })
    return productos

@app.route('/')
def redirects():
    return redirect("/productos", code=302)

@app.route('/json')
def obtener_productos():
    productos = cargar_productos()
    return jsonify(productos)

@app.route('/productos')
def listar_productos():
    productos = cargar_productos()
    return render_template('index.html', productos=productos)

@app.route('/productos/<nombre>')
def detalle_producto(nombre):
    productos = cargar_productos()
    producto = next((p for p in productos if p['nombre'] == nombre), None)
    if producto:
        return render_template('detalle.html', producto=producto)
    return "El producto no existe o no ha sido encontrado!", 404

if __name__ == '__main__':
    app.run(debug=True)
