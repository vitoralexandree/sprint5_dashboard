# 📊 Dashboard de Anúncios de Carros (Streamlit)

Aplicação web simples feita no **Streamlit** para explorar um dataset de anúncios de veículos.  
Inclui **histograma** e **gráfico de dispersão** (controlados por **botões/checkbox**).

---

## ▶️ Como rodar localmente
```bash
# 1. Criar e ativar o ambiente virtual
python -m venv .venv
.\.venv\Scripts\activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Rodar o app Streamlit
streamlit run app.py

🔗 Links

## 🔗 Links
- App no Render: https://sprint5-dashboard-ek7h.onrender.com/
- Repositório: https://github.com/vitoralexandree/sprint5_dashboard


🧰 Tecnologias

Python, Pandas

Plotly Express (gráficos interativos)

Streamlit (aplicação web)

Jupyter Notebook (EDA)

📦 Estrutura do projeto
sprint5_dashboard/
├─ app.py
├─ vehicles_us.csv
├─ requirements.txt
├─ .streamlit/
│  └─ config.toml
├─ notebooks/
│  └─ EDA.ipynb
└─ README.md