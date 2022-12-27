

from importlib.machinery import SourceFileLoader
import os
from lib.voter import askForOptions

root = os.getcwd()

mainPy = SourceFileLoader(
    "",
    root+"/Cabron_generador/generator.py"
    ).load_module()

langs = [
    "ru_ru",
    "en_us"
]

opts = [
    [
        "language",
        [
            "ru_ru",
            "en_us"
        ]
    ]
]
answer = askForOptions(opts)

language = langs[int(answer[0])]
print(language)
mainPy.onStart(langCode = language)
while True:
    try:
        mainPy.main(langCode = language)
    except KeyboardInterrupt:
        print("returned from cabron generador")
        break