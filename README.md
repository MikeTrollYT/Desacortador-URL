# Desacortador-URL

## Descripción

Este proyecto es un script en Python para desacortar URLs acortadas y revelar su destino original. Incluye dos versiones:

- **Desacortador simple**: Introduces la URL acortada y se muestra la URL real.
- **Desacortador con portapapeles**: Además de mostrar la URL real, la copia automáticamente al portapapeles para mayor comodidad.

## Características

- Expande URLs acortadas de diferentes servicios.
- No sigue redirecciones automáticamente para evitar accesos no deseados.
- Versión que copia la URL desacortada al portapapeles.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalados los siguientes componentes:

- Python 3.6 o superior
- Paquetes Python:
  - `requests`
  - `pyperclip` (solo para la versión con portapapeles)

## Instalación

1. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta el script simple:
   ```bash
   python Desacortador.py
   ```
   - Introduce la URL acortada y obtendrás la URL de destino.

2. Ejecuta el script con copia al portapapeles:
   ```bash
   python Desacortador_Portapapeles.py
   ```
   - Introduce la URL acortada y la URL real se copiará automáticamente al portapapeles.

## Notas

- Si la URL proporcionada no tiene redirección, el script lo indicará.
- Algunas URLs pueden usar técnicas avanzadas de redirección que este script no detecta.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.
