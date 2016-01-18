from PIL import Image
import sys

#Open file

def main():

    if (len(sys.argv) < 2):
        print("specify filename")
        exit()

    #TODO exit gracefully if file not found

    filename = sys.argv[1];
    img = Image.open(filename)

    h = img.height    #Height & width of original image, in pixels
    w = img.width

    ascii = ""  #Will contain our ascii picture

    y_boxes = 35   #Since displaying in terminal, will make picture 35 lines tall.

    y_box_pix = int(h / 35)     #How many pixels on one line?


    x_boxes = int(w / y_box_pix) * 2  #Use two characters

    x_box_pix = int(y_box_pix / 2) #And half as many pixels

    #print("horiz, vert, boxpix",  w, h, x_boxes, y_boxes, x_box_pix, y_box_pix)

    #Loop over all of the boxes....

    for ybox in range(0, y_boxes):

        for xbox in range(0, x_boxes):

            left = xbox * x_box_pix
            upper = ybox * y_box_pix
            right = left + x_box_pix
            lower = upper + y_box_pix

            #Crop this box and return as new image.
            cropbox = img.crop((left, upper, right, lower));

            colors = cropbox.getcolors()   #Extract colors as "an unsorted list of count, pixel values"

            #Identify most popular color in this box; we'll call this "average" color
            avg = avg_col(colors);

            #And transform this average color into one of our ASCII character 'pixels'
            pixel = ascii_pix(avg)

            ascii += pixel

        ascii += '\n'

    print(ascii)


def avg_col(colors):

    #Example of colors:
    # [(2, (124, 84, 33)), (5, (125, 83, 33)), (3, (126, 82, 33)), (4, (124, 82, 32)), (2, (125, 81, 32))]

    if colors is None:
        return 0;

    #Find most popular color. Turn it to greyscale. Return greyscale value - between 0-255.
    mostpopindex = 0
    occurance = colors[0][0]
    for c in range(len(colors)):
        if colors[c][0] > occurance:
            occurance = colors[c][0]
            mostpopindex = c

    pop_color = colors[mostpopindex][1]
    grey = 0.2989 * pop_color[0] + 0.5870 * pop_color[1] + 0.1140 * pop_color[2]  #http://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python

    return grey;


def ascii_pix(color):

    #color is a number between 0 and 255
    #divide by 24

    val = 255-color;

    #print(val)

    index = int(val/32)

    #val in range 0-255. We only have 8 different pixels.
    #Divide grey by 32 to reduce range to 0-7.

    #Can edit this to create alternate palette of characters.
    #Characters arranged from 'light' to 'dark'.
    ascii_pixels = [
        ' ',
        '.',
        '~',
        '/',
        '*',
        '0',
        '#',
        '@'
    ]

    return ascii_pixels[index];



main()
