import requests

def get_location(ip):   # función para consultar información de una ip 
    url = f"https://freeipapi.com/api/json/{ip}"    #devuelve json con información de ip
    response = requests.get(url)    
    response.raise_for_status() # si falla requests a url devuelve la excepción
    data = response.json()  # si no falla obtenemos el json
    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city" : data["cityName"],
        "code" : data["countryCode"]
    }

if __name__ == "__main__":
    print(get_location("8.8.8.8"))  