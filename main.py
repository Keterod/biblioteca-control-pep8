"""
Módulo principal para la gestión de la biblioteca central.
Se crean libros, se agregan a la biblioteca y se prueban los préstamos.
"""

from biblioteca import Biblioteca, Book


objetoBiblioteca = Biblioteca("central")

book1 = Book("Python","Guido",1)
book2 = Book("Java","Gosling",2)

objetoBiblioteca.addb(book1)
objetoBiblioteca.addb(book2)

objetoBiblioteca.show()

print(book1.lend())
print(book1.lend())
book1.back()
print(book1.lend())
