

from importlib.machinery import SourceFileLoader
import os



mainPy = SourceFileLoader(
    "main",
    os.getcwd()+"/Cabron_generador/generator.py"
    ).load_module()

mainPy.onStart()
while True:
    try:
        mainPy.main()
    except KeyboardInterrupt:
        print("returned from cabron generador")
        break