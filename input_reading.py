from collections import Iterable

def read_central_location() -> str:
    """ reads the starting location
        which will be used to calculate the distance
        to the other locations"""
    return input("Enter the central location address: \n")



def read_locations() -> Iterable[str] | int:
    """ reads the locations from the user
        and yields them as a list"""
    
    while True:
        address = input("Enter an address, or press 'enter' to end: \n")
        if address == "":
            return 0
        yield address


