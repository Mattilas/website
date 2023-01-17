import streamlit as st

def split_text_in_parts(text: str, max_chars: int):
    parts = []
    while len(text) > max_chars:
        parts.append(text[:max_chars])
        text = text [max_chars:]
    parts.append(text)
    return parts

st.title("Séparateur de texte en parties égales")
st.markdown(
    '''
    <div style="overflow-x: hidden;">
    Prompt : Résume le texte suivant en autant de points que nécessaires (en les numérotant de 1 à n) :
    </div>
    ''',
    unsafe_allow_html=True,
)
text = st.text_area("Entrez votre texte ici:")
max_chars = st.number_input("Nombre maximum de caractères par partie:", value=15500, min_value=1, step=1)
if st.button("Séparer"):
    parts = split_text_in_parts(text, max_chars)
    counter =0
    for part in parts:
        counter+=1
        st.write(f"\n\n- {counter}")
        st.write(part)