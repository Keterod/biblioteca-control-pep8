"""
Módulo que define una Biblioteca y libros con funcionalidad de préstamo.
"""


class Biblioteca:
    """
    Representa una biblioteca que contiene una colección de libros.
    """

    def __init__(self, name):
        """
        Inicializa la biblioteca con un nombre y una lista vacía de libros.

        :param name: Nombre de la biblioteca
        """
        self.name = name
        self.libros = []

    def addb(self, book):
        """
        Agrega un libro a la biblioteca.

        :param book: Instancia de la clase Book
        """
        self.libros.append(book)

    def show(self):
        """
        Muestra por pantalla la información de todos los libros de la biblioteca.
        """
        for libro in self.libros:
            print(libro.titulo, libro.autor, libro.indice)


class Book:
    """
    Representa un libro con título, autor, índice y estado de disponibilidad.
    """

    def __init__(self, titulo, autor, indice):
        """
        Inicializa un libro con sus datos básicos.

        :param titulo: Título del libro
        :param autor: Autor del libro
        :param indice: Índice o identificador del libro
        """
        self.titulo = titulo
        self.autor = autor
        self.indice = indice
        self.exist = True

    def lend(self):
        """
        Presta el libro si está disponible.

        :return: True si se pudo prestar, False si ya estaba prestado
        """
        if self.exist:
            self.exist = False
            return True
        return False

    def back(self):
        """
        Devuelve el libro y lo marca como disponible.
        """
        self.exist = True
