from app import db
import json

class Missao(db.Model):
    __tablename__ = "missao"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    destino = db.Column(db.String)
    data_lancamento =db.Column(db.DateTime) 
    estado = db.Column(db.String)
    carga_util = db.Column(db.String)
    duracao = db.Column(db.String)
    custo = db.Column(db.Float)
    status = db.Column(db.String)
    tripulacao = db.Column(db.String)
    
    def set_tripulacao(self, tripulacao_list):
            self.tripulacao = json.dumps(tripulacao_list)

    def get_tripulacao(self):
        if self.tripulacao:
            return json.loads(self.tripulacao)
        return []
    
    def __init__(self, nome, destino, data_lancamento, estado, carga_util, duracao, custo, status, tripulacao):
        self.nome = nome
        self.destino = destino
        self.data_lancamento = data_lancamento
        self.estado = estado
        self.carga_util = carga_util
        self.duracao = duracao
        self.custo = custo
        self.status = status
        if tripulacao is not None:
            self.set_tripulacao(tripulacao)
            
    def salvarMissao(self, nome, destino, data_lancamento, estado, carga_util, duracao, custo, status, tripulacao):
        try:
            add_banco = Missao(nome, destino, data_lancamento, estado, carga_util, duracao, custo, status, tripulacao)
            print(add_banco)
            db.session.add(add_banco)
            db.session.commit()
        except Exception as e:
            print(e)


    def atualizarMissao(self, id, nome, destino, data_lancamento, estado, carga_util, duracao, custo, status, tripulacao):
        try:
            db.session.query(Missao).filter(Missao.id==id).update({"nome": nome,
                                                                    "destino": destino,
                                                                    "data lancamento": data_lancamento,
                                                                    "estado": estado,
                                                                    "carga util": carga_util,
                                                                    "duracao": duracao,
                                                                    "custo": custo,
                                                                    "status": status,
                                                                    "tripulacao": tripulacao})
            db.session.commit()
        except Exception as e:
            print(e)
        
    
    def deletarMissao(self, id):
        try:
            db.session.query(Missao).filter(Missao.id==id).delete()
            db.session.commit()
        except Exception as e:
            print(e)