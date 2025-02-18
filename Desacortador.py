import requests

def obtener_url_redirigida(enlace):
    try:
        # Realizar la solicitud sin seguir redirecciones automáticamente
        respuesta = requests.get(enlace, allow_redirects=False)
        
        # Obtener la URL de redirección
        if 'Location' in respuesta.headers:
            url_redirigida = respuesta.headers['Location']
            print(f"URL de destino: {url_redirigida}")
        else:
            print("No se encontró una redirección en la URL proporcionada.")
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

if __name__ == "__main__":
    enlace_acortador = input("Ingresa la URL: ")
    obtener_url_redirigida(enlace_acortador)
