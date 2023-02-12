import streamlit as st

def split_text_in_parts(text: str, max_chars: int):
    parts = []
    while len(text) > max_chars:
        split_index = text.rfind(".", 0, max_chars)
        if split_index == -1:
            split_index = max_chars
        parts.append(text[:split_index+1])
        text = text[split_index+1:]
    parts.append(text)
    return parts

st.title("Text Splitter in Equal Parts")
st.markdown(
    '''
    <div style="overflow-x: hidden;">
    Prompt : Summarize the following text into as many points as necessary (numbering them from 1 to n) :
    </div>
    ''',
    unsafe_allow_html=True,
)
text = st.text_area("Enter your text here:")
max_chars = st.number_input("Maximum number of characters per part:", value=14500, min_value=1, step=1)
if st.button("Split"):
    parts = split_text_in_parts(text, max_chars)
    counter = 0
    st.write(f"Le texte sera découpé en {len(parts)} parties : ")
    for part in parts:
        counter += 1
        st.write(f"\n\n- Part {counter}")
        st.write(part)