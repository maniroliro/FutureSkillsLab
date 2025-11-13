"""
models.py
Classes: Competencia, Perfil, Carreira
"""
from typing import List, Dict

class Competencia:
    def __init__(self, nome: str, tipo: str, nivel: int = 0):
        """
        nome: nome da competência (ex: Lógica, Criatividade)
        tipo: 'tecnica' ou 'comportamental'
        nivel: 0..5 (inteiro)
        """
        self.nome = nome
        self.tipo = tipo
        self.nivel = max(0, min(5, int(nivel)))

    def to_dict(self):
        return {"nome": self.nome, "tipo": self.tipo, "nivel": self.nivel}

    def __repr__(self):
        return f"<Competencia {self.nome} ({self.tipo}) = {self.nivel}>"
        
class Perfil:
    def __init__(self, nome: str, idade: int = None):
        self.nome = nome
        self.idade = idade
        # usar dicionário: chave = nome da competência, valor = Competencia
        self.competencias: Dict[str, Competencia] = {}

    def adicionar_competencia(self, comp: Competencia):
        self.competencias[comp.nome.lower()] = comp

    def atualizar_nivel(self, nome_comp: str, nivel: int):
        key = nome_comp.lower()
        if key in self.competencias:
            self.competencias[key].nivel = max(0, min(5, int(nivel)))
        else:
            raise KeyError(f"Competência '{nome_comp}' não encontrada.")

    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "competencias": {k: v.to_dict() for k,v in self.competencias.items()}
        }

    def __repr__(self):
        return f"<Perfil {self.nome} comps={len(self.competencias)}>"

class Carreira:
    def __init__(self, titulo: str, requisitos: Dict[str, int], descricao: str = ""):
        """
        requisitos: dicionário {nome_comp: nivel_minimo}
        """
        self.titulo = titulo
        self.requisitos = {k.lower(): int(v) for k,v in requisitos.items()}
        self.descricao = descricao

    def atende(self, perfil: Perfil) -> float:
        """
        Retorna um score de 0..100 indicando quanto o perfil atende a carreira.
        Score baseado em média ponderada: para cada requisito, se nivel_perfil >= nivel_req,
        contribui proporcionalmente; caso contrário, contribui menos.
        """
        if not self.requisitos:
            return 0.0
        soma = 0.0
        for nome, req_nivel in self.requisitos.items():
            nivel = perfil.competencias.get(nome, Competencia(nome, 'tecnica', 0)).nivel
            # se nivel >= req -> 100% do requisito; se menor -> proporção (nivel/req)
            if req_nivel <= 0:
                contrib = 1.0 if nivel>0 else 0.0
            else:
                contrib = min(1.0, nivel / req_nivel)
            soma += contrib
        media = soma / len(self.requisitos)
        return round(media * 100, 1)

    def to_dict(self):
        return {"titulo": self.titulo, "requisitos": self.requisitos, "descricao": self.descricao}

    def __repr__(self):
        return f"<Carreira {self.titulo}>"
