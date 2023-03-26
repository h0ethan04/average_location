
from time import process_time_ns
from time import sleep
from statistics import fmean
import distance_calculator
import geocoding
import input_reading

def main():
    try:
        center_address = geocoding.ForwardNominatimEncoding(input_reading.read_central_location())
        print()
        location_objects_coords = (geocoding.ForwardNominatimEncoding(address).coords() for address in input_reading.read_locations())
        
        distances = distance_calculator.calculate_distance(center_address.coords(), location_objects_coords)
        
        print('radius:', mean:=fmean(distances), 'miles from center')
        print('.....')
        print(f'North edge: {geocoding.ReverseEncoding(distance_calculator.calculate_coordinates(center_address.coords(), 0, mean)).address()}')
        print()
        print(f'South edge: {geocoding.ReverseEncoding(distance_calculator.calculate_coordinates(center_address.coords(), 180, mean)).address()}')
        print()
        print(f'East edge: {geocoding.ReverseEncoding(distance_calculator.calculate_coordinates(center_address.coords(), 90, mean)).address()}')
        print()
        print(f'West edge: {geocoding.ReverseEncoding(distance_calculator.calculate_coordinates(center_address.coords(), 270, mean)).address()}')


    except Exception as e:
        print(' '.join(e.args))



if __name__ == '__main__':
    main()