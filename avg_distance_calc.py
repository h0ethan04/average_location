from calculator import *
from statistics import fmean


def main():
    try:
        path = read_path()
        print()
        locations = (ForwardNominatimEncoding(address).coords() for address in parse_for_locations(path))
        center_coords = locations.__next__()
        distances = calculate_distance(center_coords, locations)
        print('radius:', mean:=fmean(distances), 'miles from center')
        print('.....')
        print(f'North edge: {ReverseEncoding(calculate_coordinates(center_coords, 0, mean)).address()}')
        print()
        print(f'South edge: {ReverseEncoding(distance_calculator.calculate_coordinates(center_coords, 180, mean)).address()}')
        print()
        print(f'East edge: {ReverseEncoding(distance_calculator.calculate_coordinates(center_coords, 90, mean)).address()}')
        print()
        print(f'West edge: {ReverseEncoding(distance_calculator.calculate_coordinates(center_coords, 270, mean)).address()}')
        print('.....')
    except Exception as e:
        print(' '.join(e.args))

    finally:
        input("Press 'enter' to exit the program")

if __name__ == "__main__":
    main()