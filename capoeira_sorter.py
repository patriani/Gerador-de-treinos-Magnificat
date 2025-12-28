import streamlit as st
import numpy as np

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


def graduations_list(graduation, sort_type):
    pos = graduations_scope.index(graduation)

    return {
        "1": [graduation],
        "2": list(graduations_scope[pos + 1:]),
        "3": list(graduations_scope[:pos + 1]),
        "4": list(graduations_scope[pos:]),
        "5": list(graduations_scope),
    }[sort_type]


def sort_moves(graduation, sort_type, n_t, n_d):
    grads = graduations_list(graduation, sort_type)

    t, d = [], []
    for g in grads:
        t.extend(graduations_data[g]["traumatizante"])
        d.extend(graduations_data[g]["desequilibrante"])

    return {
        "traumatizantes": np.random.choice(t, min(n_t, len(t)), replace=False),
        "desequilibrantes": np.random.choice(d, min(n_d, len(d)), replace=False),
    }


# UI
st.title("Gerador de Treino")

graduation = st.selectbox("Graduação", graduations_scope)
sort_type = st.selectbox(
    "Tipo de Sorteio",
    {
        "Atual": "1",
        "Futuras": "2",
        "Atual + Anteriores": "3",
        "Atual + Futuras": "4",
        "Todas": "5",
    }
)

n_t = st.number_input("Qtd Traumatizantes", 1, 10, 2)
n_d = st.number_input("Qtd Desequilibrantes", 1, 10, 2)

if st.button("Sortear"):
    result = sort_moves(graduation, sort_type, n_t, n_d)

    for k, v in result.items():
        st.write(f"**{k}:** {', '.join(map(str, v))}")
