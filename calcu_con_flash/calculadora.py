from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/calcular", methods=["GET", "POST"])
def calcular():
    # Método POST
    if request.method == "POST":
        numero1 = float(request.form["num1"])
        numero2 = float(request.form["num2"])
        operacion = request.form['op']

        if operacion == "+":
            
            resultado = numero1 + numero2

        # Implementar para resta, división y multiplicación

        return render_template("index.html", result=resultado)

    elif request.method == "GET":
        return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)