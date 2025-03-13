# 📝 Extractor de Metadatos de PDF e Imágenes

## Descripción
Este script en Python permite extraer metadatos de archivos PDF e imágenes, ya sea desde una URL o desde una ruta local. Los metadatos extraídos se guardan en archivos de texto.

## Requisitos
- Python 3.x
- Librerías: `requests`, `beautifulsoup4`, `PyPDF2`, `Pillow`

## Instalación
1. Instala las librerías necesarias:
   ```bash
   pip install requests beautifulsoup4 PyPDF2 Pillow


## Uso
**Parámetros**
-pdfu: URL de un PDF.
-pdflp: Ruta local de un PDF.
-imglp: Ruta local de una imagen.
-imgurl: URL de una imagen.

## Ejemplos de Uso
## Extraer metadatos de un PDF desde una URL:
python script.py -pdfu "https://example.com/document.pdf"
## Extraer metadatos de un PDF desde una ruta local:
python script.py -pdflp "/ruta/al/documento.pdf"
