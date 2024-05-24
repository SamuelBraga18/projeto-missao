from flask import jsonify
from flask_restful import Resource, reqparse
from app.model.missao import Missao
import datetime as dt

argumento = reqparse.RequestParser()
argumento.add_argument("nome", type=str)
argumento.add_argument("destino", type=str)
argumento.add_argument("data_lancamento", type=dt.datetime)
argumento.add_argument("estado", type=str)
argumento.add_argument("carga_util", type=str)
argumento.add_argument("duracao", type=str)
argumento.add_argument("custos", type=float)
argumento.add_argument("status", type=str)
argumento.add_argument("tripulacao", type=str)

#atualizar
argumento_atualizar = reqparse.RequestParser()
argumento_atualizar.add_argument("id", type=int)
argumento_atualizar.add_argument("nome", type=str)
argumento_atualizar.add_argument("destino", type=str)
argumento_atualizar.add_argument("data_lancamento", type=dt.datetime)
argumento_atualizar.add_argument("estado", type=str)
argumento_atualizar.add_argument("carga_util", type=str)
argumento_atualizar.add_argument("duracao", type=str)
argumento_atualizar.add_argument("custos", type=float)
argumento_atualizar.add_argument("status", type=str)
argumento_atualizar.add_argument("tripulacao", type=str)

#deletar
argumento_deletar = reqparse.RequestParser()
argumento_deletar.add_argument("id", type=int)

class Index(Resource):
    def get(self):
        return jsonify("Bem vindo")

class criarMissao(Resource):
    def post(self):
        try:
            datas = argumento.parse_args()
            Missao.salvarMissao(self, datas['nome'],
                                datas['destino'],
                                datas['data_lancamento'],
                                datas['estado'],
                                datas['carga_util'],
                                datas['duracao'],
                                datas['custos'],
                                datas['status'],
                                datas['tripulacao'])
            return {"mensagem":"missão criada com sucesso"}, 200
        except Exception as e:
            return {"status": 500, "mensagem": f'{e}'}, 500
        
class atualizar(Resource):
    def put(self):
        try:
            datas = argumento.parse_args()
            Missao.salvarMissao(self, datas['id'],
                                datas['nome'],
                                datas['destino'],
                                datas['data_lancamento'],
                                datas['estado'],
                                datas['carga_util'],
                                datas['duracao'],
                                datas['custos'],
                                datas['status'],
                                datas['tripulacao'])
            return {"mensagem":"missão atualizada com sucesso"}, 200
        except Exception as e:
            return {"status": 500, "mensagem": f'{e}'}, 500
        
class deletar(Resource):
    def delete(self):
        try:
            datas = argumento_deletar.parse_args()
            Missao.deletarMissao(self, datas['id'])
            return {"mensagem": "missão deletada com sucesso"}, 200
        except Exception as e:
            return {"status": 500, "mensagem": f"{e}"}, 500
            