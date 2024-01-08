import math
import numpy as np
import os
import sys

class Book:
    def __init__(self,name: str, author: str, date: str, publisher: str, number_of_pages: int):
        self.name = name
        self.author = author
        self.date = date
        self.publisher = publisher
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"The book is {self.name},\nThe author is {self.author}"

    def getBookInfo(self):
        print("Information about the book:")
        print(f"Book name: {self.name}")
        print(f"Book author: {self.author}")
        print(f"Book release date: {self.date}")
        print(f"Book publisher: {self.publisher}")
        print(f"Book number of pages: {self.number_of_pages}")

    def dummyFunction(self):
        for i in range(100000):
            print(i**4)

if __name__ == "__main__":

    dataset = {
                "book1":{"name":"Apples", "author":"Sam","date": "2022","publisher":"ps1", "number_of_pages":100},
                "book2":{"name":"Fruits", "author":"Amy","date": "2021","publisher":"ps2", "number_of_pages":600},
                "book3":{"name":"Cars", "author":"Carl","date": "2020","publisher":"ps2", "number_of_pages":500},
                "book4":{"name":"Cities", "author":"Peter","date": "1922","publisher":"ps2", "number_of_pages":200}
            }

    books = []

    for book in dataset.values():
        e = Book(book["name"], book["author"], book["date"], book["publisher"], book["number_of_pages"])
        books.append(e)


    books[0].getBookInfo()
    books[0].dummyFunction()


