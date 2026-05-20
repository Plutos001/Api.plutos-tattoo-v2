from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "API PLUTOS TATTOO V2 ONLINE 💎⚙️"
from flask import request, jsonify

@app.route('/orcamento', methods=['POST'])
def orcamento():
    dados = request.get_json()
    nome = dados.get('nome')
    tamanho = dados.get('tamanho')
    estilo = dados.get('estilo')
    
    preco = 250  # preço base
    if tamanho == 'grande':
        preco = 600
    
    return jsonify({
        "cliente": nome,
        "preco_estimado": preco,
        "mensagem": f"Salve {nome}! Orçamento para tattoo {estilo} tá R${preco} 💎⚙️"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)