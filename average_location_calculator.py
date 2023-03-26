
from time import process_time_ns
from time import sleep
from statistics import fmean
import distance_calculator
import geocoding
import input_reading

def main():
    try:
        center_address = geocoding.ForwardNominatimEncoding(input_reading.read_central_location())

        location_objects_coords = (geocoding.ForwardNominatimEncoding(address).coords() for address in input_reading.read_locations())
        
        distances = distance_calculator.calculate_distance(center_address.coords(), location_objects_coords)
        
        print(fmean(distances), 'miles')
    except Exception as e:
        print(' '.join(e.args))



if __name__ == '__main__':
    main()