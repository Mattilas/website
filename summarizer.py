import openai
import streamlit as st

openai.api_key = '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'

def split_text_in_parts(text: str, max_chars: int):
    parts = []
    while len(text) > max_chars:
        parts.append(text[:max_chars])
        text = text[max_chars:]
    parts.append(text)
    return parts


st.title("Résumeur")
text = st.text_area("Entrez votre texte ici:")
max_chars = st.number_input("Nombre maximum de caractères par partie:", value=7500, min_value=1, step=1)
if st.button("Résumer"):
    parts = split_text_in_parts(text, max_chars)
    counter = 0
    for part in parts:
        counter += 1
        st.write(f"\n\n- {counter}")
        #st.write(part)
        summary = response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Résume le texte suivant par points en les numérotant :\n{part} \n\n",
            temperature=0.7,
            max_tokens=1300,
            top_p=1.0,
            stop=None,
            frequency_penalty=0.0,
            presence_penalty=1
        )
        summary = summary.choices[0].text
        st.write(summary)
