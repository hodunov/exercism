def answer(question):
    operator_mapping = {
        "plus": "+",
        "minus": "-",
        "divided by": "/",
        "multiplied by": "*",
    }

    if not question.startswith("What is"):
        raise ValueError("unknown operation")

    question = question.removeprefix("What is").removesuffix("?")

    if not question:
        raise ValueError("syntax error")

    for old, new in operator_mapping.items():
        question = question.replace(old, new)

    question = question.split()
    question.insert(0, "(")
    question.insert(4, ")")

    if any(word.isalpha() for word in question):
        raise ValueError("unknown operation")

    try:
        result = eval(" ".join(question))
        return result
    except SyntaxError:
        raise ValueError("syntax error")
