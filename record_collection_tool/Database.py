# Author: Noah McGarry
# Date: 10/12/2024
# !/usr/bin/env python3

from VinylRecord import VinylRecord


class Database:
    @staticmethod
    def get_albums():
        ramones_r = VinylRecord("Ramones", "Ramones", genre = "Punk Rock", release_year= 1976,
                                      comment="The first Ramones album.")
        ramones_lh = VinylRecord("Ramones", "Leave Home", "Punk Rock", 1977,
                                        "The second Ramones album.")
        ramones_rtr = VinylRecord("Ramones", "Rocket to Russia", "Punk Rock", 1977,
                                     "The third Ramones album.")
        cocteautwins_holv = VinylRecord("Cocteau Twins", "Heaven or Las Vegas", "Shoegaze",
                                        1990, "The sixth album by the Cocteau Twins.")
        beatles_rs = VinylRecord("The Beatles", "Rubber Soul", "Rock", 1965,
                                         "The sixth album by the Beatles.")
        ymo_sss = VinylRecord("Yellow Magic Orchestra", "Solid State Survivor", "Electronic",
                              1979, "The second album by Japan's Yellow Magic Orchestra")
        return [ramones_r, ramones_lh, ramones_rtr, cocteautwins_holv, beatles_rs, ymo_sss]


# it works here so I dont know why it wont print at the menu
#
# if __name__ == "__main__":
#     vinyls = Database.get_albums()
#     for vinyl in vinyls:
#         print(vinyl)