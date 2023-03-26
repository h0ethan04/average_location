import urllib.request
import urllib.parse
import json
import time


_BASE_URL = 'https://nominatim.openstreetmap.org/search?'

class ForwardHTTPError(Exception):
    """ Exception raised for HTTP errors """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ForwardURLError(Exception):
    """ Exception raised for network errors"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ForwardJSONError(Exception):
    """ Exception raised for json errors"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class BadInputError(Exception):
    """ Exception raised when given bad input"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ForwardNominatimEncoding:
    """ Forward geocoding using Nominatim """

    def __init__(self, address: str) -> None:
        """ creates an object that converts
        an address to latitude and longitude """
        self._address = address
        self._coords = None
        self._to_coords()

    def coords(self) -> tuple[float, float]:
        return self._coords

    def _to_coords(self) -> None:
        """ converts the address into coordinates"""

        response = None
        time.sleep(1)
        try:
            encoded_params = urllib.parse.urlencode([('q', self._address), 
                                                        ('format', 'json')])
            full_url = f'{_BASE_URL}{encoded_params}'
            request = urllib.request.Request(full_url,
                                                headers={'Referer':'https://github.com/h0ethan04/h0ethan04'},
                                                method='GET')        
            response = urllib.request.urlopen(request)
            encoded_data = response.read()
            decoded_data = json.loads(encoded_data)
            self._coords = (float(decoded_data[0]['lat']), float(decoded_data[0]['lon']))

        except urllib.error.HTTPError as e:
            raise ForwardHTTPError(f'HTTP {e.code}')
        
        except urllib.error.URLError:
            raise ForwardURLError('network error')
        
        except json.JSONDecodeError:
            raise ForwardJSONError('incompatible json encoding detected')
        
        except (KeyError, ValueError, IndexError, BadInputError):
            raise BadInputError('location could not be found')
        
        finally:
            if response is not None:
                response.close()
        


