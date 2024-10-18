# Author: Noah McGarry
# Date: 10/12/2024
# !/usr/bin/env python3


from VinylRecord import VinylRecord


class VinylCollection(VinylRecord):
    __location: ""
    __year_acquired: 0

    def __init__(self, artist, title, genre, release_year, comment, location, year_acquired):
        super().__init__(artist, title, genre, release_year, comment)
        self.__location = location
        self.__year_acquired = year_acquired

    def get_key(self):
        f"{self.get_artist()}: {self.get_title()} in {self.__location} acquired {self.__year_acquired}".lower()