# 🧠 FutureSkillsLab  

Autoria:
Guilherme Morais de Assis - RM: 564198
Rogerio Deligi Filho - RM: 561942
Maria Fernanda Garavelli Dantas - RM: 562686

---

### Sistema Lógico de Orientação Profissional Baseado em Competências Futuras  

---

##  Descrição do Projeto  
O **FutureSkillsLab** é um sistema lógico e interativo de orientação profissional, desenvolvido como parte do trabalho acadêmico **“O Futuro Precisa do Seu Trabalho”**, na disciplina de **Computer Science**.  

Seu objetivo é ajudar estudantes e profissionais a descobrirem **carreiras do futuro** com base em suas **competências técnicas e comportamentais**.  
A aplicação utiliza lógica simples de recomendação para cruzar o perfil do usuário com os requisitos de diferentes carreiras, indicando:  

- As carreiras mais compatíveis.  
- As competências que ainda precisam ser aprimoradas.  
- Trilhas de aprendizado personalizadas para o desenvolvimento profissional.  

---

##  Funcionalidades Principais  

- **Interface textual (CLI)** simples e amigável.  
- **Criação, seleção e atualização de perfis** de usuários.  
- **Cadastro de competências padronizadas**, divididas entre técnicas e comportamentais.  
- **Sistema de recomendação de carreiras**, baseado na correspondência entre perfil e requisitos.  
- **Sugestão de trilhas de aprendizado** com base nas lacunas de competências.  
- **Listagem e gerenciamento de múltiplos perfis** em uma mesma sessão.  

---

##  Estrutura do Projeto  

```bash
Projeto_FutureSkillsLab/
│
├── main.py # Interface principal (menu CLI)
├── models.py # Classes: Perfil, Competência, Carreira
├── recommender.py # Lógica de recomendação e trilhas
├── data.py # Base de dados de carreiras e competências
├── README.md # Documentação do projeto
└── entrega.txt # Arquivo para fins de entrega acadêmica
```


---

##  Como Executar  

### 1. Pré-requisitos  
- **Python 3.8** ou superior instalado.  
- Nenhuma biblioteca externa é necessária (usa apenas bibliotecas padrão).  

### 2. Execução  
Abra o terminal na pasta do projeto e execute:  
```bash
python main.py
```

### 3. Uso do Sistema
O menu principal exibirá opções como:

```bash
1 - Criar novo perfil
2 - Selecionar perfil existente
3 - Adicionar / Atualizar competência
4 - Recomendar carreiras
5 - Sugerir trilha de aprendizado
6 - Listar todos os perfis
7 - Sair
```

Basta digitar o número correspondente à ação desejada.

Todas as interações são feitas via terminal, com menus e listas numeradas.

### 4. Demonstração

Após dar início ao sistema, comece sempre criando um novo perfil(uma pessoa) digitando 1 no terminal, essa é a classe principal do projeto, tendo em vista que todas as outras só existem para ela. Dê a ela um nome e se quiser uma idade;

![image](https://raw.githubusercontent.com/maniroliro/FutureSkillsLab/refs/heads/main/images/step1.png)

Logo em seguida, adicione uma competência digitando 2 no terminal, e escolha a desejada junto ao seu grau. As competências são separadas em 2 grupos, técnica e comportamental, isso para facilitar a visualização de todas elas. Repita esse passo quantas vezes se julgar necessário e até ter um perfil bem estruturado;

![image](https://raw.githubusercontent.com/maniroliro/FutureSkillsLab/refs/heads/main/images/step2.png)

Com isso você já consegue visualizar quais carreiras o programa julga ser pertinente para o perfil criado, basta digitar no terminal o número 4;

![image](https://raw.githubusercontent.com/maniroliro/FutureSkillsLab/refs/heads/main/images/step3.png)

Há também outras opções como "Sugerir trilha para carreira", que mostra quais competências devem ser melhoradas para uma área específica, "Selecionar / Mudar Perfil", para mudar o perfil a ser analisado e "Mostrar perfil atual", que mostra as competências e nível delas, dê uma explorada nessas funções!

![image](https://raw.githubusercontent.com/maniroliro/FutureSkillsLab/refs/heads/main/images/step4.png)

---


## Conceitos Aplicados

Lógica de Recomendação: compara as competências do usuário com as exigidas por cada carreira.

Programação Orientada a Objetos (POO): estrutura baseada em classes (Perfil, Competência, Carreira).

IA Simbólica: tomada de decisão baseada em regras lógicas e níveis de compatibilidade.

Interação Homem-Máquina: menu textual como interface simples e funcional.

## Possíveis Extensões Futuras

Sistema de salvamento permanente de dados (JSON ou banco de dados).

Interface gráfica (GUI) com Tkinter ou web (Flask).

Uso de IA generativa para análise textual de perfis.

Integração com APIs de carreiras e plataformas educacionais.
