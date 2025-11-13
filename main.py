# main.py - CLI com suporte a múltiplos perfis e seleção de usuário
from models import Competencia, Perfil
from recommender import recomendar_carreiras, sugerir_trilha
from data import carreiras_exemplo

# --- Listas padronizadas ---
COMPETENCIAS_TECNICAS = [
    "Lógica", "Programação", "Estatística", "Testes",
    "Prototipagem", "Análise de Dados", "Inteligência Artificial", "Cibersegurança"
]

COMPETENCIAS_COMPORTAMENTAIS = [
    "Criatividade", "Colaboração", "Empatia", "Pensamento Crítico",
    "Comunicação", "Resiliência", "Negociação", "Liderança", "Ética", "Adaptabilidade"
]

# --- Funções auxiliares ---
def exibir_menu():
    print("\n=== FUTURE SKILLS LAB ===")
    print("1 - Criar novo perfil")
    print("2 - Adicionar / Atualizar competência")
    print("3 - Mostrar perfil atual")
    print("4 - Recomendar carreiras (top 5)")
    print("5 - Sugerir trilha para carreira")
    print("6 - Selecionar / Mudar Perfil")
    print("0 - Sair")
    return input("Escolha uma opção: ").strip()


def escolher_tipo_competencia():
    print("\nTipo de competência:")
    print("1 - Técnica")
    print("2 - Comportamental")
    op = input("Escolha (1/2): ").strip()
    if op == "1":
        return "tecnica"
    if op == "2":
        return "comportamental"
    print("Opção inválida. Tente novamente.")
    return escolher_tipo_competencia()


def escolher_competencia_da_lista(tipo):
    if tipo == "tecnica":
        lista = COMPETENCIAS_TECNICAS
    else:
        lista = COMPETENCIAS_COMPORTAMENTAIS

    print("\nSelecione a competência:")
    for i, nome in enumerate(lista, start=1):
        print(f"{i} - {nome}")
    escolha = input("Número da competência: ").strip()
    try:
        idx = int(escolha) - 1
        if 0 <= idx < len(lista):
            return lista[idx]
    except ValueError:
        pass
    print("Seleção inválida. Tente novamente.")
    return escolher_competencia_da_lista(tipo)


def pedir_nivel(min_v=0, max_v=5):
    val = input(f"Digite o nível ({min_v}-{max_v}): ").strip()
    try:
        n = int(val)
        if min_v <= n <= max_v:
            return n
    except ValueError:
        pass
    print("Valor inválido. Digite um número inteiro dentro do intervalo.")
    return pedir_nivel(min_v, max_v)


# --- Ações principais ---
def criar_ou_atualizar_perfil(perfis):
    nome = input("\nNome: ").strip()
    idade = input("Idade (opcional): ").strip()
    idade_val = int(idade) if idade.isdigit() else None
    perfil = Perfil(nome, idade_val)
    perfis.append(perfil)
    print(f"✅ Perfil criado: {perfil.nome}")
    return perfil


def adicionar_ou_atualizar_competencia(perfil: Perfil):
    tipo = escolher_tipo_competencia()
    nome_comp = escolher_competencia_da_lista(tipo)
    print(f"Competência selecionada: {nome_comp} ({'técnica' if tipo=='tecnica' else 'comportamental'})")
    nivel = pedir_nivel(0, 5)
    comp = Competencia(nome_comp, tipo, nivel)
    perfil.adicionar_competencia(comp)
    print(f"✅ '{nome_comp}' = {comp.nivel} salvo no perfil.")


def mostrar_perfil(perfil: Perfil):
    if not perfil:
        print("\nNenhum perfil selecionado.")
        return
    d = perfil.to_dict()
    print("\n=== Perfil Atual ===")
    print(f"Nome: {d.get('nome')}")
    print(f"Idade: {d.get('idade')}")
    comps = d.get("competencias", {})
    if not comps:
        print("Nenhuma competência cadastrada.")
        return
    print("Competências:")
    for k, v in comps.items():
        print(f"- {v['nome']}: {v['nivel']} ({v['tipo']})")


def recomendar(perfil: Perfil):
    if not perfil:
        print("\nCrie ou selecione um perfil primeiro.")
        return
    carreiras = carreiras_exemplo()
    top = recomendar_carreiras(perfil, carreiras, top_n=5)
    print("\n=== Recomendações (score 0..100) ===")
    for score, c in top:
        print(f"- {c.titulo}: {score}% — {c.descricao}")


def sugerir_trilha_menu(perfil: Perfil):
    if not perfil:
        print("\nCrie ou selecione um perfil primeiro.")
        return
    carreiras = carreiras_exemplo()
    print("\nCarreiras disponíveis:")
    for i, c in enumerate(carreiras):
        print(f"{i} - {c.titulo}")
    sel = input("Escolha o número da carreira: ").strip()
    if not sel.isdigit():
        print("Seleção inválida.")
        return
    idx = int(sel)
    if idx < 0 or idx >= len(carreiras):
        print("Seleção inválida.")
        return
    c = carreiras[idx]
    passos = sugerir_trilha(perfil, c)
    print(f"\nTrilha sugerida para {c.titulo}:")
    for p in passos:
        print("*", p)


def selecionar_perfil(perfis):
    if not perfis:
        print("\n⚠️ Nenhum perfil criado ainda.")
        return None
    print("\n=== Perfis Cadastrados ===")
    for i, p in enumerate(perfis, 1):
        print(f"{i} - {p.nome}")
    escolha = input("Escolha o número do perfil: ").strip()
    try:
        idx = int(escolha) - 1
        if 0 <= idx < len(perfis):
            print(f"✅ Perfil selecionado: {perfis[idx].nome}")
            return perfis[idx]
    except ValueError:
        pass
    print("Seleção inválida.")
    return None


# --- Loop principal ---
def main():
    perfis = []        # lista com todos os perfis criados
    perfil_atual = None

    while True:
        opc = exibir_menu()

        if opc == "1":
            perfil_atual = criar_ou_atualizar_perfil(perfis)
        elif opc == "2":
            if perfil_atual:
                adicionar_ou_atualizar_competencia(perfil_atual)
            else:
                print("\n⚠️ Crie ou selecione um perfil primeiro.")
        elif opc == "3":
            mostrar_perfil(perfil_atual)
        elif opc == "4":
            recomendar(perfil_atual)
        elif opc == "5":
            sugerir_trilha_menu(perfil_atual)
        elif opc == "6":
            novo = selecionar_perfil(perfis)
            if novo:
                perfil_atual = novo
        elif opc == "0":
            print("\n👋 Saindo... até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
