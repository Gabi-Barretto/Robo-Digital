from flask import Flask, render_template, request, redirect, jsonify
from data.posicoes import Posicao

global posicoes

posicoes =[
    Posicao(x="0", y="0", z="0")
]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html", posicoes=posicoes)

@app.route("/mover", methods=["GET","POST"])
def criar_evento():
    if request.method == "POST": 
        posicao = Posicao(
            x=request.form["x"],                
            y=request.form["y"],
            z=request.form["z"]
        )
        global posicoes
        posicoes.append(posicao)
        return redirect("/")
    
    return {"x": posicoes[-1].x, "y": posicoes[-1].y, "z": posicoes[-1].z}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 3000, debug=True)