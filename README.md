# 🧩 Flask API – Hello World

Pequeno projeto introdutório com **Flask**, criado como parte de introdução da disciplina de MLOps.  
Esta versão simples serve como ponto de partida para evoluir para uma API completa de Machine Learning.

---

## 📁 Estrutura inicial do projeto

```
flask-api/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧰 Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- **Python 3.9+**
- **pip** (gerenciador de pacotes do Python)
- (Opcional, mas recomendado) **virtualenv**

---

## ⚙️ Instruções de execução do projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/jaisonschmidt/mlops-flask-simple-api
cd mlops-flask-simple-api
```

### 2️⃣ Criar e ativar um ambiente virtual
```bash
python -m venv .venv
# Ativar o ambiente
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o servidor Flask
```bash
python app/main.py
```

### 5️⃣ Testar no navegador
Acesse [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  
Você deverá ver a seguinte resposta JSON:

```json
{
  "message": "Hello World, Flask API is running!"
}
```

---

## 🚀 Próximos passos

Nos próximos capítulos, este projeto será expandido para incluir:
- Endpoints adicionais (`/status`, `/predict`)
- Integração com modelos de Machine Learning
- Versionamento e boas práticas de MLOps

---

🧑‍💻 **Autor:** Jaison Schmidt  
