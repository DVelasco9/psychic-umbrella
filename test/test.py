from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase
import sys

# Crear la aplicación PRIMERO
app = QApplication(sys.argv)

# Ahora usar QFontDatabase
db = QFontDatabase()
fuentes = db.families()

print("Fuentes disponibles en tu sistema:")
for fuente in sorted(fuentes):
    print(f"  - {fuente}")