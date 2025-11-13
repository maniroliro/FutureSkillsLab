"""
recommender.py
Funções para gerar recomendações a partir de um Perfil.
"""
from typing import List, Tuple
from models import Carreira, Perfil

def recomendar_carreiras(perfil: Perfil, carreiras: List[Carreira], top_n: int = 5):
    scored = []
    for c in carreiras:
        score = c.atende(perfil)
        scored.append((score, c))
    scored.sort(reverse=True, key=lambda x: x[0])
    return scored[:top_n]

def sugerir_trilha(perfil: Perfil, carreira: Carreira):
    falta = []
    for req, nivel in carreira.requisitos.items():
        nivel_perfil = perfil.competencias.get(req, None)
        atual = nivel_perfil.nivel if nivel_perfil else 0
        if atual < nivel:
            falta.append((req, atual, nivel))
    # ordenar por maior gap
    falta.sort(key=lambda x: x[2]-x[1], reverse=True)
    # retorno simples: lista de passos (competencia, de, para)
    passos = [f"Aprimore {req} de {atual} → {meta}" for req, atual, meta in falta]
    if not passos:
        passos = ["Perfil já atende aos requisitos principais dessa carreira."]
    return passos
