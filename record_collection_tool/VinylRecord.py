# Author: Noah McGarry
# Date: 10/12/2024
# !/usr/bin/env python3


class VinylRecord:
    __artist: ""
    __title: ""
    __genre: ""
    __release_year: 0
    __comment: ""
    __map = {}

    def __init__(self, artist, title, genre, release_year, comment):
        self.__artist = artist
        self.__title = title
        self.__genre = genre
        self.__release_year = release_year
        self.__comment = comment
        self.__class__.__map[self.get_key()] = self


    def get_key(self):
        return f"{self.__artist}: {self.__title}".lower()

    def get_artist(self):
        return self.__artist

    def get_title(self):
        return self.__title

    def __str__(self):
        return f"<{self.__title} by {self.__artist} released in {self.__release_year}. {self.__comment}>"

    @staticmethod
    def get_records():
        from Database import Database
        return Database.get_albums()

    # def get_genre(self):
    #    return self.__genre

    # def get_release_year(self):
    #    return self.__release_year

    # def get_comment(self):
    #    return self.__comment
