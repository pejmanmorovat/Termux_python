from googletrans import Translator

def main():
    translator = Translator()
    text = input("Enter text to translate from Persian to English: ")
    translation = translator.translate(text, src="fa", dest="en")
    print(f"Translation (Persian to English): {translation.text}")

if __name__ == "__main__":
    main()

