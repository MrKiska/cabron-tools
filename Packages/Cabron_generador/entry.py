

from importlib.machinery import SourceFileLoader
import os
from lib.voter import askForOptions

import Packages.Cabron_generador.generator as mainPy

root = os.getcwd()


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
    mainPy.main(langCode = language)