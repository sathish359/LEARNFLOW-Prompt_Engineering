class TranslationTool:
    def __init__(self):
        self.translations = {
            "drink water": {
                "es": "beba agua",
                "fr": "bois de l'eau",
            },
            "good morning": {
                "es": "buenos días",
                "fr": "bonjour",
            },
            "goodbye": {
                "es": "adiós",
                "fr": "au revoir",
            },
        }

    def translate(self, text, language):
        translation = self.translations.get(text, {}).get(language)
        if translation:
            return translation
        else:
            return f"Sorry, I cannot translate '{text}' to {language}."

def run_translation_tool():
    tool = TranslationTool()

    while True:
        text = input("Enter a phrase to translate or type 'exit' to quit: ")
        if text.lower() == "exit":
            break

        language = input("Enter the target language code (e.g., 'es' for Spanish, 'fr' for French): ")
        translation = tool.translate(text, language)
        print(translation)

if __name__ == "__main__":
    run_translation_tool()
