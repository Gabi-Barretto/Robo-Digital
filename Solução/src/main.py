from flask import Flask, render_template, request, redirect
from data.posicoes import Posicao
from joystick import coordenadas, move

posicoes =[
    Posicao(x="0", y="0", z="0")
]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html", posicoes=posicoes)

@app.route("/mover", methods=["POST"])
def criar_evento():
    posicao = Posicao(
        x=request.form["x"],
        y=request.form["y"],
        z=request.form["z"]
    )
    #global posicoes
   # posicoes.append(posicao)
    move(posicao.x, posicao.y, posicao.z)
    return redirect("/")

@app.route("/pegar_coordenadas", methods=["POST"])

def gerar_coordenada():
    x, y, z = coordenadas()
    posicao = Posicao(
        x=x,                
        y=y,
        z=z
    )
    global posicoes
    posicoes.append(posicao)
    return redirect("/")


app.run(host='0.0.0.0', port= 3000, debug=True)