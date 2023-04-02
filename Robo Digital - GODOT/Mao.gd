extends Spatial

#iniciando timer e a conexão para realizar o request
func _ready():
	$Timer.start()
	$HTTPRequest.connect("request_completed", self, "_on_request_completed")
	
func _on_request_completed(result, response_code, headers, body):
	#recebendo a informação e organizando para movimentar o objeto principal da cena
	var json = JSON.parse(body.get_string_from_utf8())
	self.translation = Vector3(float(json.result["x"]), float(json.result["y"]), float(json.result["z"]))

	print(json.result)
	
func _on_Timer_timeout():
	#Realiza a requisição a cada 1 segundo
	$HTTPRequest.request("http://127.0.0.1:3000/mover")
