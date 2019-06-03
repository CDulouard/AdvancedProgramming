def enum():
    with open("textSource", "r") as file:
        text = file.read()
        words = text.split()
        formatedText = ""
        for i, word in enumerate(words):
            formatedText += str((i // 15) + 1) + ( " " *  (10 - len(str((i // 15) + 1))) )  if i % 15 == 0 else ""
            formatedText += word + " "
            formatedText += '\n' if (i + 1) % 15 == 0 else ""
        with open("result", "w") as result:
            result.write(formatedText)

