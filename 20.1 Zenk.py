def translate(text):
    text = ''.join(s for s in text if s not in 'аеёиоуыэюя.,!?:-')
    return text

txt = input("Введите текст:\n")
translatedText = translate(txt)

print(f"TranlatedText == {translatedText}")