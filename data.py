from models import Carreira
def carreiras_exemplo():
    return [
        Carreira("Engenheiro de Dados", {
            "lógica": 4, "programação": 4, "estatística": 3, "colaboração": 3
        }, descricao="Trabalha com pipelines, modelagem e análise de dados."),
        Carreira("Designer de Experiência (UX)", {
            "criatividade": 4, "empatia": 4, "prototipagem": 3, "colaboração": 3
        }, descricao="Foca na experiência do usuário, pesquisa e design de interfaces."),
        Carreira("Especialista em IA Ética", {
            "ética": 4, "estatística": 3, "pensamento_critico": 4, "comunicação": 3
        }, descricao="Audita modelos, define práticas responsáveis e governa IA."),
        Carreira("Engenheiro de Software", {
            "programação": 4, "lógica": 4, "testes": 3, "colaboração": 3
        }, descricao="Desenvolve sistemas, aplica testes e boas práticas."),
        Carreira("Empreendedor Tech", {
            "criatividade": 4, "resiliência": 4, "negociação": 3, "liderança": 3
        }, descricao="Cria produtos e negócios tecnológicos."),
    ]
