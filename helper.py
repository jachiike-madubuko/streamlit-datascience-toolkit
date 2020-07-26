def write(lit,text):
    if "<" in text:
        lit.write(text, unsafe_allow_html=True)
    else:
        lit.write(text)
