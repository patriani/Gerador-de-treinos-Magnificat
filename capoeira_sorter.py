import streamlit as st
import numpy as np

# =========================
# Dados
# =========================

#graduations_scope = ("cinza", "verde", "azul", "amarelo")

#graduations_data = {
#    "cinza": {
#        "desequilibrante": ["Cd1", "Cd2"],
#        "traumatizante": ["Ct1", "Ct2"],
#    },
#    "verde": {
#        "desequilibrante": ["Vd1", "Vd2"],
#        "traumatizante": ["Vt1", "Vt2"],
#    },
#    "amarelo": {
#        "desequilibrante": ["Ad1", "Ad2"],
#        "traumatizante": ["At1", "At2"],
#    },
#    "azul": {
#        "desequilibrante": ["Azd1", "Azd2"],
#        "traumatizante": ["Azt1", "Azt2"],
#    },
#}

graduations_scope = ("verde", "amarelo","azul","verde e amarelo","verde e azul","amarelo e azul")

graduations_data = {
"azul": {
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
"amarelo e azul": {
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
    "verde": {
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
    "amarelo": {
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
    "verde e amarelo": {
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
    "verde e azul": {
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
        "defesa_e_ataque_com_as_maos": [
            "Cotovelada",
            "Cutilada",
            "Gravata",
            "Telefone",
        ],
    },
}

# =========================
# Lógica
# =========================

def graduations_list(graduation: str, sort_type: str) -> list[str]:
    """
    Retorna lista de graduações válida.
    Nunca levanta KeyError (web-safe).
    """

    pos = graduations_scope.index(graduation)

    options = {
        "1": [graduation],                            # Atual
        "2": list(graduations_scope[pos + 1:]),       # Futuras
        "3": list(graduations_scope[:pos + 1]),       # Atual + anteriores
        "4": list(graduations_scope[pos:]),           # Atual + futuras
        "5": list(graduations_scope),                  # Todas
    }

    # Fallback seguro
    return options.get(sort_type, [graduation])


def sort_moves(graduation: str, sort_type: str, n_t: int, n_d: int) -> dict:
    grads = graduations_list(graduation, sort_type)

    traumatizantes = []
    desequilibrantes = []

    for g in grads:
        traumatizantes.extend(graduations_data[g]["traumatizante"])
        desequilibrantes.extend(graduations_data[g]["desequilibrante"])

    return {
        "traumatizantes": list(
            np.random.choice(
                traumatizantes,
                size=min(n_t, len(traumatizantes)),
                replace=False
            )
        ),
        "desequilibrantes": list(
            np.random.choice(
                desequilibrantes,
                size=min(n_d, len(desequilibrantes)),
                replace=False
            )
        ),
    }

# =========================
# UI (Streamlit)
# =========================

st.set_page_config(page_title="Capoeira Sorter", layout="centered")

st.title("Gerador de Treino - Sistema Magnificat")

graduation = st.selectbox(
    "Cordão:",
    graduations_scope,
)

sort_type = st.selectbox(
    "Tipo de Sorteio",
    options={
        "Movimentos da Graduação Atual": "1",
        "Movimentos de Graduações Futuras": "2",
        "Atuais + Anteriores": "3",
        "Atuais + Futuras": "4",
        "Todas (*)": "5",
    },
)

n_t = st.number_input(
    "Quantidade de Traumatizantes",
    min_value=1,
    max_value=10,
    value=2,
)

n_d = st.number_input(
    "Quantidade de Desequilibrantes",
    min_value=1,
    max_value=10,
    value=2,
)

st.divider()

if st.button("Sortear movimentos", use_container_width=True):
    try:
        result = sort_moves(graduation, sort_type, n_t, n_d)

        st.success("Movimentos sorteados com sucesso!")

        for categoria, lista in result.items():
            valores = ", ".join(str(v) for v in lista)
            st.write(f"**{categoria.capitalize()}:** {valores}")

    except Exception as e:
        st.error("Erro ao gerar o treino.")
        st.exception(e)
