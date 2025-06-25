from flask import Flask, render_template, request

app = Flask  (__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/resultado' , methods=['POST'])
def resultado():
    if request.method == 'POST':
        A=int(request.form['A'])
        B=int(request.form['B'])
        C=int(request.form['C'])
        
        if A > B and A > C:
            return render_template('ejercicio1.html', resultado= 'El mayor es A', A=A, B=B, C=C)
        elif B > A and B > C:
            return render_template('ejercicio1.html', resultado= 'El mayor es B', A=A, B=B, C=C)
        elif C > A and C > B:
            return render_template('ejercicio1.html', resultado= 'El mayor es C', A=A, B=B, C=C)
        else:
            return render_template('ejercicio1.html', resultado= 'Los valores son iguales', A=A, B=B, C=C)
        
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/Notas' , methods=['POST'])
def Notas():
    if request.method == 'POST':
        X=int(request.form['X'])
        if X >= 1 and X <= 9:
            mensaje = 'Su nota es E'
        elif X >= 10 and X <= 12:
            mensaje = 'Su nota es D'
        elif X >= 13 and X <= 15:
            mensaje = 'Su nota es C'
        elif X >= 16 and X <= 18:
            mensaje = 'Su nota es B'
        elif X >= 19 and X <= 20:
            mensaje = 'Su nota es A'
        return render_template('ejercicio2.html', resultado= 'Tu nota es', X=X, mensaje=mensaje)
    
@app.route('/ejercicio3')
def ejercicio3():
        return render_template('ejercicio3.html')
    
@app.route('/solucion' , methods=['POST'])
def solucion():
    if request.method == 'POST':
        Cambio = 4086
        g=int(request.form['g'])
        h=int(request.form['h'])
        i=int(request.form['i'])
        j=int(request.form['j'])
        k=int(request.form['k'])
        Operacion = g + h + i + j + k
        solucion = Operacion * Cambio
        return render_template('ejercicio3.html', solucion=solucion)
    
@app.route('/ejercicio4')
def ejercicio4():
        return render_template('ejercicio4.html')
    
@app.route('/peo' , methods=['POST'])
def peo():
    if request.method == 'POST':
        k=int(request.form['k'])
        popo = k * 2
        triple = k * 3
        return render_template('ejercicio4.html', k=k, po = popo, pi = triple) 
    
@app.route('/ejercicio5', methods=['GET', 'POST'])
def ejercicio5():
    figura = None
    area_calculada = None
    if request.method == 'POST':
        figura = request.form['figura']
        try:
            if figura == 'circulo':
                radio = float(request.form['radio'])
                area_calculada = 3.14159 * (radio ** 2)
            elif figura == 'cuadrado':
                lado = float(request.form['lado'])
                area_calculada = lado ** 2
            elif figura == 'rectangulo':
                largo = float(request.form['largo'])
                ancho = float(request.form['ancho'])
                area_calculada = largo * ancho
            elif figura == 'triangulo':
                base = float(request.form['base'])
                altura = float(request.form['altura'])
                area_calculada = 0.5 * base * altura
            else:
                return render_template('ejercicio5.html', error="Figura no válida.")
        except ValueError:
            return render_template('ejercicio5.html', error="Por favor, ingrese valores válidos.")

    return render_template('ejercicio5.html', figura=figura, area=area_calculada)
        
            
    
    
