# 🛡️ SegurIA Monitor

Plataforma inteligente de **Monitoramento de Segurança com IA**, que identifica comportamentos anômalos em tempo real. Desenvolvido com **Python**, esta solução combina **Machine Learning**, **banco de dados vetorial**, **dashboards interativos** e **alertas automatizados**, para fornecer segurança proativa e visibilidade operacional.

---

## 🌍 Idiomas | Languages | Idiomas

- 🇧🇷 [Português](#português)
- 🇺🇸 [English](#english)
- 🇪🇸 [Español](#español)

---

## 🇧🇷 Português

### 🔍 Funcionalidades

- 🧠 Detecção de anomalias em tempo real com *Machine Learning* (Isolation Forest)
- 📊 Dashboard interativo com Streamlit
- 🔐 API REST com autenticação JWT (FastAPI)
- 💬 Alertas automáticos por e-mail e WhatsApp (via Twilio)
- 🧠 Banco de dados vetorial com FAISS
- 🗃️ Armazenamento em PostgreSQL
- 🛡️ Arquitetura segura e pronta para produção

### 🚀 Como executar

```bash
# Clone o repositório
git clone https://github.com/seuusuario/seguria-monitor.git
cd seguria-monitor

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure variáveis de ambiente
cp .env.example .env

# Execute a API
uvicorn api.main:app --reload

# Execute o dashboard
streamlit run dashboard/dashboard.py
```

---

## 🇺🇸 English

### 🔍 Features

- 🧠 Real-time anomaly detection using *Machine Learning* (Isolation Forest)
- 📊 Interactive dashboard with Streamlit
- 🔐 Secure REST API with JWT (FastAPI)
- 💬 Email and WhatsApp alerts via Twilio
- 🧠 Vector database with FAISS
- 🗃️ PostgreSQL storage
- 🛡️ Production-ready secure architecture

### 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/youruser/seguria-monitor.git
cd seguria-monitor

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env

# Run the API
uvicorn api.main:app --reload

# Run the dashboard
streamlit run dashboard/dashboard.py
```

---

## 🇪🇸 Español

### 🔍 Funcionalidades

- 🧠 Detección de anomalías en tiempo real con *Machine Learning* (Isolation Forest)
- 📊 Panel interactivo con Streamlit
- 🔐 API REST segura con JWT (FastAPI)
- 💬 Alertas por correo electrónico y WhatsApp (Twilio)
- 🧠 Base de datos vectorial con FAISS
- 🗃️ Almacenamiento con PostgreSQL
- 🛡️ Arquitectura segura lista para producción

### 🚀 Cómo ejecutar

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/seguria-monitor.git
cd seguria-monitor

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env

# Ejecutar la API
uvicorn api.main:app --reload

# Ejecutar el panel
streamlit run dashboard/dashboard.py
```

---

## 🖼️ Screenshots

> *(Adicione capturas de tela aqui mostrando o dashboard e exemplos de alertas)*

---

## 📂 Estrutura do Projeto

```
seguria_monitor/
├── api/                # Backend (FastAPI + IA + FAISS)
├── dashboard/          # Dashboard Streamlit
├── db/                 # Integração com banco de dados (PostgreSQL)
├── tests/              # Testes com PyTest
├── .env.example        # Exemplo de configuração
├── requirements.txt    # Dependências do projeto
├── README.md           # Este arquivo
└── .gitignore
```

---

## 📜 Licença

Este projeto está licenciado sob os termos da **MIT License**. Veja o arquivo `LICENSE` para mais detalhes.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um *pull request* ou *issue*.

---

## 📬 Contato

Desenvolvido por [Seu Nome ou Empresa] – contato via [seu-email@dominio.com]