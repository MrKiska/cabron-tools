

from importlib.machinery import SourceFileLoader
import os



mainPy = SourceFileLoader(
    "main",
    os.getcwd()+"/Cabron_generador/generator.py"
    ).load_module()

mainPy.onStart()
while True:
    
    mainPy.main()