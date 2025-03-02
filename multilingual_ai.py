from deep_translator import GoogleTranslator

def translate_to_english(text, lang="auto"):
    return GoogleTranslator(source=lang, target="en").translate(text)

translated_text = translate_to_english("你好，世界", "zh")
print(translated_text)
