# Robo-Digital - Gabriela Barretto
 - Organização de arquivos:

 -- Robo Digital - GODOT - Contém os arquivos da aplicação godot que deve ser executada na ferramenta.

 -- Solução - Contém o ambiente virtual e sripts para execução da aplicacao python-flask e sqlAlchemy. 

 - Proposta da solução:

    Simulação de Braço Robótico com interface web para interação com usuário. A solução conta com um script em python que utilizando do framework flask e suas funções, recebe informações de um frontend, atualiza as coordenadas robô simulado via API, as salva em um banco de dados e mantém o usuário atualizado da posição atual da extremidade do Braço Robótico. 

 - Back-end
      Pontos principais: 
         
         #Instanciando flask:
         app = Flask(__name__)

         #Principal Rota da Solução com GET para receber do front e POST para manter a infomação nela e receber no Godot
         @app.route("/mover", methods=["GET","POST"])

         #Iniciando servidor na devida porta e host
         if __name__ == "__main__":
            app.run(host='0.0.0.0', port= 3000, debug=True)

         #Criando banco de dados
         engine = create_engine('sqlite:///posicao.db')
         Base.metadata.create_all(engine)

 - Simulação 
      Pontos principais: 
         
         #Requisição sendo feita no Script Godot na rota em questão
         $HTTPRequest.request("http://127.0.0.1:3000/mover")

         #Trabalhando a informação e movendo o objeto em questão à sua devida coordenada
         var json = JSON.parse(body.get_string_from_utf8())
	      self.translation = Vector3(float(json.result["x"]), float(json.result["y"]), float(json.result["z"]))