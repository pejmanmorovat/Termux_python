from googletrans import Translator

def main():
    translator = Translator()
    text = input("Enter text to translate (English to Persian): ")
    translation = translator.translate(text, src="en", dest="fa")
    print(f"Translation: {translation.text}")

if __name__ == "__main__":
    main()

