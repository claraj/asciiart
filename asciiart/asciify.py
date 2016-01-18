from PIL import Image
import sys

#Open file

def main():

    if (len(sys.argv) < 2):
        print("specify filename")
        exit()

    filename = sys.argv[1];
    img = Image.open(filename)

    colors = img.getcolors(200)   #an unsorted list of count, pixel values

    #print(colors)

    palette = img.getpalette();

    #print(palette)


    h = img.height
    w = img.width


    ascii = ""

    y_boxes = 35

    y_box_pix = int(h / 35)     #ascii image 35 lines tall. so if img is 1000 pix high, and are using 100 boxes, will be 1000/0 = 10 px high


    x_boxes = int(w / y_box_pix) * 2  #which determines the # of y boxes. But, they don't have to be boxes?

    x_box_pix = int(y_box_pix / 2)

    print("horiz, vert, boxpix",  w, h, x_boxes, y_boxes, x_box_pix, y_box_pix)

    #for  vbox in range(0, vert_boxes, box_pix):
    for ybox in range(0, y_boxes):

        for xbox in range(0, x_boxes):

            left = xbox * x_box_pix
            upper = ybox * y_box_pix
            right = left + x_box_pix
            lower = upper + y_box_pix
            #print(left, upper, right, lower)
            cropbox = img.crop((left, upper, right, lower));

            colors = cropbox.getcolors()   #an unsorted list of count, pixel values

            #print()

            #print(colors)

            #Transform color into one of the ascii_pixels

            avg = avg_col(colors);

            pixel = ascii_pix(avg)

            ascii += pixel

        ascii += '\n'


    print(ascii)



def avg_col(colors):

    #Example of colors:
    # [(2, (124, 84, 33)), (5, (125, 83, 33)), (3, (126, 82, 33)), (4, (124, 82, 32)), (2, (125, 81, 32))]

    if colors is None:
        return 0;

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

    #print(color)
    #color is a number between 0 and 255
    #divide by 24

    val = 255-color;

    #print(val)

    index = int(val/32)

    #print(index)

    ascii_pixels = [
        ' ',
        '.',
        '/',
        '^',
        '*',
        '&',
        '#',
        '@'
    ]

    return ascii_pixels[index];



main()
