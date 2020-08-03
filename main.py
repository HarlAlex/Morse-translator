from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

morse_encode = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
    'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',

    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--',
    'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...',
    't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',

    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',

    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.',
    'Ё': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-',
    'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.',
    'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
    'Ш': '----', 'Щ': '--.-', 'Ъ': '.--.-.', 'Ы': '-.--', 'Ь': '-..-',
    'Э': '...-...', 'Ю': '..--', 'Я': '.-.-',

    'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.',
    'ё': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-',
    'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.',
    'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.',
    'ш': '----', 'щ': '--.-', 'ъ': '.--.-.', 'ы': '-.--', 'ь': '-..-',
    'э': '...-...', 'ю': '..--', 'я': '.-.-'}


def encode_to_morse(text):
    letters = list(text)

    splitted_text = text.split(' ')
    for k in splitted_text:
        if k in morse_encode.values():
            return decode_from_morse(text)

    answer = []
    for i in letters:
        answer.append(morse_encode.get(i, i))
    return ' '.join(answer)


def decode_from_morse(code):
    codes = code.split(' ')
    keys = list(morse_encode.keys())
    values = list(morse_encode.values())
    answer = []
    for i in codes:
        try:
            answer.append(keys[values.index(i)])
        except ValueError:
            answer.append(i)
    return ''.join(answer)


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.name = TextInput(multiline=True, font_size=60)  # focus
        self.add_widget(self.name)

        self.submit = Button(text='Перевести', font_size=50)
        self.submit.bind(on_press=self.morse_press)
        self.add_widget(self.submit)

    def morse_press(self, instance):
        self.name.text = encode_to_morse(self.name.text)


class MorseApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MorseApp().run()
