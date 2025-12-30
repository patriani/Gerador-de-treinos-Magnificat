import streamlit as st
import numpy as np

# =========================
# CONFIG
# =========================

IMAGE_URL = "https://scontent.fcgh3-1.fna.fbcdn.net/v/t39.30808-6/294455734_462059872592226_7435904330031198638_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=6ee11a&_nc_eui2=AeEsJZiK50YnF_xXKMdUpCU6oSDm-nsObtqhIOb6ew5u2jbuf8xR_Qht5rwLZAd5c8sBRmVRRKG9Q_HbN6ahHbrR&_nc_ohc=rVJHprMjhNcQ7kNvwEs3XPw&_nc_oc=AdnHlC014OMAQAIMFkOl_-v1GuCntDavFPPtZyzHOELaSzlzvL5mxDOwUBG3peaqjasAoUQHJFjxKOB1KXWyMNzQ&_nc_zt=23&_nc_ht=scontent.fcgh3-1.fna&_nc_gid=cAw0inUtxcAybq95N3ISWA&oh=00_Aflg9oRWoeeSaJ5HR0u59zCxj2NB2t-WTZABwqJIRiDG4A&oe=6958DE47"

st.set_page_config(page_title="Capoeira Sorter", layout="wide")

# =========================
# HEADER COM IMAGEM À DIREITA
# =========================

col_left, col_right = st.columns([3, 1])

with col_left:
    st.markdown(
        """
        <h1 style="margin-bottom: 0;">Gerador de Treino</h1>
        <h1 style="margin-top: 0;">C.C.M.C.</h1>
        """,
        unsafe_allow_html=True
    )

with col_right:
    st.markdown(
        f"""
        <div style="display: flex; justify-content: flex-end;">
            <img src="{IMAGE_URL}"
                 style="
                    max-width: 100%;
                    opacity: 0.35;
                    border-radius: 12px;
                 ">
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# =========================
# Dados
# =========================

graduations_scope = (
    "Verde",
    "Amarelo",
    "Azul",
    "Verde & Amarelo",
    "Verde & Azul",
    "Amarelo & Azul",
)

graduations_data = {
    "Azul": {
        "traumatizante": [
            "Chapa Lateral",
            "Chapa giratória",
            "Chapa de chão",
            "Gancho",
            "Chapéu de couro",
        ],
        "esquivas": [
            "Queda de quatro",
            "Recuo com cadeira lateral",
            "Esquiva lateral com apoio e rolê",
        ],
        "desequilibrante": [
            "Arrastão",
            "Rasteira cruzada",
            "Tesoura de frente",
        ],
        "floreios": [
            "Aú batido",
            "Aú dobrado",
            "Cama de gato",
            "S dobrado",
            "Mergulho",
            "Corta capim",
        ],
    },
    "Amarelo & Azul": {
        "traumatizante": [
            "Voo do morcego",
            "Draps",
            "Cobertura (variação)",
            "Escorpião",
            "Chibata",
            "Quebra de Perna",
            "Cabeçadas",
            "Facão",
        ],
        "esquivas": [
            "Deslocamento de sentido",
            "Giros ofensivos",
            "Giros defensivos",
            "Sequência de giros, balanços e deslocamentos (mín. 5 movimentos)",
        ],
        "desequilibrante": [
            "Cruz",
            "Crucifixo",
            "Banda Trançada",
            "Rasteira quebrada",
            "Deslocamento de eixo",
        ],
        "floreios": [
            "Aú dobrado sem as mãos",
            "Aú com queda de rim",
            "Roda baiana",
            "Raiz",
            "Raiz sem as mãos",
            "Gato dobrado",
            "Salto do peixe",
            "Salto mortal",
        ],
    },
    "Verde": {
        "traumatizante": [
            "Benção",
            "Meia-lua de frente",
            "Meia-lua de compasso",
            "Martelo",
            "Queixada",
            "Armada",
        ],
        "esquivas": [
            "Cadeira",
            "Cocorinha",
            "Queda de três",
            "Esquiva lateral com apoio",
        ],
        "desequilibrante": [
            "Rasteira de frente",
            "Rasteira de frente baixa",
        ],
        "floreios": [
            "Queda de rim",
            "Aú aberto",
            "Aú fechado",
            "Aú agulha",
        ],
    },
    "Amarelo": {
        "traumatizante": [
            "Queixada Lateral",
            "Martelo de Base",
            "Ponteira",
            "Chapa de Frente",
            "Armada Pulada",
        ],
        "esquivas": [
            "Entrada de Negativa",
            "Negativa de Avanço",
            "Negativa de Fundo",
        ],
        "desequilibrante": [
            "Rasteira de Costas",
            "Rasteira de Espelho",
            "Vingativa",
            "Boca de Calça",
        ],
        "floreios": [
            "Aú com uma mão",
            "Aú Rolê",
            "Bananeira",
            "Parada de Cabeça",
            "Macaco",
            "Peão de Mão",
            "Ponte",
        ],
    },
    "Verde & Amarelo": {
        "traumatizante": [
            "Armada Solta",
            "Chapa de costas",
            "Coice de Mula",
            "Martelo Giratório",
            "Meia-Lua Solta",
            "Martelo com apoio Básico",
        ],
        "esquivas": [
            "Descida Básica",
            "Esquiva Balão",
            "Resistência",
            "Entrada de Encruzilhada",
        ],
        "desequilibrante": [
            "Banda por Dentro",
            "Cabeçadas",
            "Tesoura de Costas",
        ],
        "floreios": [
            "Aú Chibata",
            "Aú de Costas",
            "Aú sem as Mãos",
            "Beija-Flor",
            "Camaleão",
            "Volta por Cima",
            "Gato",
            "Espera de Frente",
        ],
    },
    "Verde & Azul": {
        "traumatizante": [
            "Armada Dupla",
            "Calcanheira",
            "Encruzilhada",
            "Escorão",
            "Parafuso",
            "Gancho com apoio",
            "Rabo de arraia",
        ],
        "esquivas": [
            "Esquiva Básica",
            "Deslocamento Lateral",
        ],
        "desequilibrante": [
            "Arrastão Lateral",
            "Banda de Costas",
            "Rasteira de Mão",
            "Rasteira na base do Aú",
            "Negativa de Alavanca",
        ],
        "floreios": [
            "Aú Camaleão",
            "Aú invertido",
            "Aú com inversão de base",
            "Peão de Cabeça",
            "Escovão",
            "Macaco Dobrado",
        ],
    },
}

# =========================
# Funções
# =========================

def graduations_list(graduation: str, sort_type: str) -> list[str]:
    pos = graduations_scope.index(graduation)

    options = {
        "1": [graduation],
        "2": list(graduations_scope[pos + 1:]),
        "3": list(graduations_scope[:pos + 1]),
        "4": list(graduations_scope[pos:]),
        "5": list(graduations_scope),
    }

    return options.get(sort_type, [graduation])


def sort_moves(graduation, sort_type, n_t, n_d, n_e, n_f):
    grads = graduations_list(graduation, sort_type)

    traumatizantes, desequilibrantes, esquivas, floreios = [], [], [], []

    for g in grads:
        data = graduations_data[g]
        traumatizantes.extend(data.get("traumatizante", []))
        desequilibrantes.extend(data.get("desequilibrante", []))
        esquivas.extend(data.get("esquivas", []))
        floreios.extend(data.get("floreios", []))

    return {
        "traumatizantes": list(np.random.choice(traumatizantes, min(n_t, len(traumatizantes)), False)),
        "desequilibrantes": list(np.random.choice(desequilibrantes, min(n_d, len(desequilibrantes)), False)),
        "esquivas": list(np.random.choice(esquivas, min(n_e, len(esquivas)), False)),
        "floreios": list(np.random.choice(floreios, min(n_f, len(floreios)), False)),
    }

# =========================
# UI
# =========================

graduation = st.selectbox("Cordão:", graduations_scope)

sort_type_labels = {
    "Movimentos da Graduação Atual": "1",
    "Movimentos de Graduações Futuras": "2",
    "Atuais + Anteriores": "3",
    "Atuais + Futuras": "4",
    "Todas": "5",
}

sort_type_label = st.selectbox("Tipo de Sorteio", list(sort_type_labels.keys()))
sort_type = sort_type_labels[sort_type_label]

n_t = st.slider("Quantidade de Traumatizantes", 0, 10, 0)
n_d = st.slider("Quantidade de Desequilibrantes", 0, 10, 0)
n_e = st.slider("Quantidade de Esquivas", 0, 10, 0)
n_f = st.slider("Quantidade de Floreios", 0, 10, 0)

st.divider()

if st.button("Sortear movimentos", use_container_width=True):
    result = sort_moves(graduation, sort_type, n_t, n_d, n_e, n_f)

    st.success("Movimentos sorteados com sucesso!")

    for categoria, lista in result.items():
        if lista:
            st.write(f"**{categoria.capitalize()}:** {', '.join(lista)}")
