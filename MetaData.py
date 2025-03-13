import requests 
from bs4 import BeautifulSoup 
from PyPDF2 import PdfFileReader
from PIL import Image
from PIL.ExifTags import TAGS
import time
import argparse


def main(PDFurl, PDFlocalPath, IMGurl, IMGlocalPath):
	#https://nanonets.com/blog/deep-learning-ocr/

	#Funcion que extrae metdatos de pdf de una url
	if(PDFurl != ""):
		response = requests.get(PDFurl) 
		  
		soup = BeautifulSoup(response.text, 'html.parser') 
		  
		links = soup.find_all('a') 
		  
		i = 0
		name = []
		for link in links: 
		    if ('.pdf' in link.get('href', [])): 
		        i += 1
		        print("Downloading file: ", i) 

		        response = requests.get(link.get('href')) 

		        pdf = open("pdf"+str(i)+".pdf", 'wb')
		        nombre = "pdf"+str(i)+".pdf"
		        name.append(nombre)
		        pdf.write(response.content) 
		        pdf.close()
		        print("File ", i, " downloaded")
		print("All PDF files downloaded")
		time.sleep(3)
		for pdf in name:
                        fo = open(pdf + ".txt", "w")
                        with open(pdf, 'rb') as f:
                                file = PdfFileReader(f)
                                info = file.getDocumentInfo()
                                number_of_pages = file.getNumPages()       
                        fo.write("Numero de paginas: ")
                        fo.write((str(number_of_pages)) + '\n')
                        fo.write("Autor: ")
                        fo.write((str(info.author)) + '\n')
                        fo.write("Creador: ")
                        fo.write((str(info.creator)) + '\n')
                        fo.write("Productor: ")
                        fo.write((str(info.producer)) + '\n')
                        fo.write("Sujeto: ")
                        fo.write((str(info.subject)) + '\n')
                        fo.write("Titulo: ")
                        fo.write((str(info.title)) + '\n')
                        fo.close()
                        print("Los Metadatos del archivo "+ pdf +" si es que existen se han generado en un txt.")
                
	#Funcion que extrae metadatos de un pdf en ruta local
	elif(PDFlocalPath != ""):
                fo = open(PDFlocalPath + ".txt", "w")
                with open(PDFlocalPath, 'rb') as f:
                        file = PdfFileReader(f)
                        info = file.getDocumentInfo()
                        number_of_pages = file.getNumPages()
                fo.write("Numero de paginas: ")
                fo.write((str(number_of_pages)) + '\n')
                fo.write("Autor: ")
                fo.write((str(info.author)) + '\n')
                fo.write("Creador: ")
                fo.write((str(info.creator)) + '\n')
                fo.write("Productor: ")
                fo.write((str(info.producer)) + '\n')
                fo.write("Sujeto: ")
                fo.write((str(info.subject)) + '\n')
                fo.write("Titulo: ")
                fo.write((str(info.title)) + '\n')
                fo.close()
                print("Los Metadatos del archivo "+ PDFlocalPath + " si es que existen se han generado en un txt.")
	if(IMGlocalPath != ""):

		# path to the image or video
		imagename = IMGlocalPath

		# read the image data using PIL
		image = Image.open(imagename)
		# extract EXIF data
		exifdata = image.getexif()
		fo = open(imagename + ".txt" , "w")

		# iterating over all EXIF data fields
		for tag_id in exifdata:
		    # get the tag name, instead of human unreadable tag id
		    tag = TAGS.get(tag_id, tag_id)
		    data = exifdata.get(tag_id)
		    # decode bytes 
		    if isinstance(data, bytes):  
                        data = data.decode()   
		    print(f"{tag:25}: {data}")
		    fo.write((str(f"{tag:25}: {data}"))+ '\n')
		    fo.close
		    

	elif(IMGurl != ""):
		#Preguntar la url
		url_imagen = IMGurl
		#https://raw.githubusercontent.com/x4nth055/pythoncode-tutorials/master/ethical-hacking/image-metadata-extractor/image.jpg
		#Preguntar el nombre y el tipo de imagen
		nombre_local_imagen = "img.jpg"
		imagen = requests.get(url_imagen).content
		with open(nombre_local_imagen, 'wb') as handler:
			handler.write(imagen)

		time.sleep(5)
		#corrgir nombre
		# path to the image or video
		imagename = nombre_local_imagen

		# read the image data using PIL
		image = Image.open(imagename)
		# extract EXIF data
		exifdata = image.getexif()
		fo = open(imagename + ".txt", 'w')

		#si no exite metadata que lo diga
		# iterating over all EXIF data fields
		for tag_id in exifdata:
		    # get the tag name, instead of human unreadable tag id
		    tag = TAGS.get(tag_id, tag_id)
		    data = exifdata.get(tag_id)
		    # decode bytes 
		    if isinstance(data, bytes):
		        data = data.decode()
		    print(f"{tag:25}: {data}")
		    fo.write((str(f"{tag:25}: {data}"))+ '\n')
		    fo.close

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-pdfu', type=str, help='PDF url', default= "")#"https://nanonets.com/blog/deep-learning-ocr/")
	parser.add_argument('-pdflp', help='PDF local path', default= "")
	parser.add_argument('-imglp', type=str, help='Path of file', default="")
	parser.add_argument('-imgurl', type=str, help='url', default="")
	args = parser.parse_args()
	main(args.pdfu,args.pdflp, args.imgurl, args.imglp)
