from PIL import Image

def extractfilename(filelocation):
    name_extracted = filelocation.split('\\')[-1]
    return name_extracted.split('.')[0]

fileloc = input("Enter full path of image file: ")

filename = extractfilename(fileloc)

image = Image.open(fileloc)

width, height = image.size

multiplier = float(input("INPUT A MULTIPLER. For a bigger image, multiplier should be > 1 e.g. 1.75. For a smaller image, multiplier should be below 1 e.g. 0.75 "))

image_resized = image.resize((int(width*multiplier), int(height*multiplier)))

image = image_resized.save(filename + '_resized.jpeg')

