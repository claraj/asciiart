from PIL import Image
import sys

#Open file

def main():

    if (len(sys.argv) < 2):
        sys.exit("Please specify a filename")

    filename = sys.argv[1];
    try :
        img = Image.open(filename)

    except FileNotFoundError:
        exit("Sorry, that file not found")
    except OSError:
        exit("That file doesn't seem to be an image")

    ascii(img)


def ascii(img):


    h = img.height    #Height & width of original image, in pixels
    w = img.width

    ascii = ""  #Will contain our ascii picture; a string of characters

    lines = 35

    y_boxes = lines   #Since displaying in terminal, will make picture 35 lines tall.
    y_box_pix = int(h / lines)     #How many pixels on one line?

    x_boxes = int(w / y_box_pix) * 2  #Use twice as many characters for length as height
    x_box_pix = int(y_box_pix / 2) #And half as many pixels


            #Crop this box and return as new image.
    cropbox = img.crop((0, 0, h + 10, w + 10));
    print(cropbox)
    colors = cropbox.getcolors()   #Extract colors as "an unsorted list of count, pixel values"
    print(colors)

if __name__ == '__main__':
    #Running this as a script: call the main method.
    main()
else:
    #Importing this module from somewhere else; for example, a test case
    #Without this, the main method would be run when the module is imported into the
    #test case, which is probably not the behavior you want,
    #You probably don't need the else clause for this if statment
    #but I added it so I had somewhere to write this comment.
    pass
