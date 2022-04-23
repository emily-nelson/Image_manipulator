from PIL import Image

def extractfilename(filelocation):
    name_extracted = filelocation.split('\\')[-1]
    return name_extracted.split('.')[0]

fileloc = input("Enter full path of image file: ")

image = Image.open(fileloc)

width, height = image.size

image_resized = image.resize((int(width/2), int(height/2)))

filename = extractfilename(fileloc)

image = image_resized.save(filename + '_resized.jpeg')