def normalize_text(text):

    if text is None:
        return ""

    text = str(text)

    text = text.lower()

    text = text.replace("\n", " ").replace("\t", " ")

    text = " ".join(text.split())

    return text
