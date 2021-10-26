class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        print(f"Ta biblioteka znajduje się w mieście {self.city},\n"
              f"przy ulicy {self.street}, kod pocztowy: {self.zip_code}\n"
              f"godziny otwarcia - {self.open_hours}, telefon: {self.phone}.")


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        print(f"Pracownik biblioteki: {self.first_name} {self.last_name}\n"
              f"Zatrudniony: {self.hire_date}, urodzony: {self.birth_date}\n"
              f"zamieszkały w: {self.city}, przy ul. {self.street}\n"
              f"Kod pocztowy: {self.zip_code}, tel. {self.phone}.")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        print(f"Zamówienie obsługuje pracownik: {self.employee}\n"
              f"zamówienie złożone przez: {self.student}, książki: {self.books}\n"
              f"Data zamówienia: {self.order_date}.")


class Book:
    def __init__(self, title, library, publication_date, author_name, author_surname, number_of_pages):
        self.title = title
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        print(f"Książka: '{self.title}' z biblioteki {self.library}, wydana\n"
              f"{self.publication_date}\n"
              f"imię i nazwisko autora: {self.author_name} {self.author_name}\n"
              f"liczba stron: {self.number_of_pages}.")


class Student:
    def __init__(self, first_name, last_name, university, city):
        self.first_name = first_name
        self.last_name = last_name
        self.university = university
        self.city = city

    def __str__(self):
        print(f"Ja, {self.first_name} {self.last_name}\n"
              f"jestem studentem w: {self.university} w mieście {self.city}.")


biblio1 = Library("Jaworzno", "Kolorowa 1", "43-600", "8:00 - 16:00", "500 600 700")
biblio2 = Library("Katowice", "Owocowa 3", "42-600", "8:00 - 15:00", "700 600 500")
book1 = Book("Ania z Zielonego Wzgórza", "Biblioteka w Katowicach", "20.10.1995", "Ania", "Zielona", "350")
book2 = Book("Harry Potter", "Biblioteka w Jaworznie", "15.09.1999", "J.K.", "Rowling", "500")
book3 = Book("Władca Pierścieni", "Biblioteka w Jaworznie", "10.05.1995", "J.", "Tolkien", "750")
book4 = Book("Dziady", "Biblioteka w Katowicach", "05.04.1750", "Adam", "Mickiewicz", "50")
book5 = Book("Futbol na Tak", "Biblioteka w Jaworznie", "06.06.2002", "Jerzy", "Engel", "75")
pracownik1 = Employee("Zenon", "Krótki", "09.09.2020", "01.07.1995", "Jaworzno", "Maślana 3", "43-600", "501 601 701")
pracownik2 = Employee("Genowefa", "Piękna", "05.04.2005", "04.05.1965", "Katowice", "Zakochanych 4", "42-600", "565 205 449")
pracownik3 = Employee("Brajan", "Bravo", "16.08.2019", "06.11.2001", "Mysłowice", "Kopalniana 40", "42-650", "666 555 444")
student1 = Student("Michał", "Mańkowski", "Uniwersytet Ekonomiczny", "Katowice")
student2 = Student("Jadzia", "Wybredna", "Uniwersytet Śląski", "Katowice")
student3 = Student("Adam", "Spadam", "Wyższa Szkoła Bankowa", "Chorzów")
order1 = Order("Zenon", "Mańkowski Michał", "Ania z Zielonego Wzgórza", "05.05.2021")
order2 = Order("Genowefa", "Wybredna Jadzia", "Dziady", "06.06.2021")
order1.__str__()
order2.__str__()