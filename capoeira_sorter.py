import streamlit as st
import numpy as np

# =========================
# Dados
# =========================

graduations_scope = ("cinza", "verde", "azul", "amarelo")

graduations_data = {
    "cinza": {
        "desequilibrante": ["Cd1", "Cd2"],
        "traumatizante": ["Ct1", "Ct2"],
    },
    "verde": {
        "desequilibrante": ["Vd1", "Vd2"],
        "traumatizante": ["Vt1", "Vt2"],
    },
    "amarelo": {
        "desequilibrante": ["Ad1", "Ad2"],
        "traumatizante": ["At1", "At2"],
    },
    "azul": {
        "desequilibrante": ["Azd1", "Azd2"],
        "traumatizante": ["Azt1", "Azt2"],
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
