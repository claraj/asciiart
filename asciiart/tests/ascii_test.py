import unittest

import asciiart
from asciiart import asciify as asc


class AsciifyTest(unittest.TestCase):


    def test_avg_color(self):


        #list of colors are in the format: (frequency, RGBcolor)
        # [(2, (124, 84, 33)), (5, (125, 83, 33)), (3, (126, 82, 33)), (4, (124, 82, 32)), (2, (125, 81, 32))]
        #
        #Some examples. This function should return the tuple associaed with the highest frequency
        #In case of a tie, current behavior is to return the first of the joint highest.

        expected = asc.avg_col([(2, (124, 84, 33)), (5, (125, 83, 33)), (3, (126, 82, 33)), (4, (124, 82, 32)), (2, (125, 81, 32))])
        self.assertEqual(expected, (125,83,33))

        expected2 = asc.avg_col([(2, (124, 84, 33)), (3, (126, 82, 33)), (4, (124, 82, 32)), (2, (125, 81, 32))])
        self.assertEqual(expected2, (124, 82, 32))

        expected3 = asc.avg_col([(16, (34, 76, 23)) ] )
        self.assertEqual(expected3, (34, 76, 23))

        expected2 = asc.avg_col([(5, (124, 84, 33)), (3, (126, 82, 33)), (3, (124, 82, 32)), (5, (125, 81, 32))])
        self.assertEqual(expected2, (124, 84, 33))


    def test_color_to_gray(self):

        # grayval = 0.3 * color[0] + 0.6 * color[1] + 0.1 * color[2]
        # grayval = 0.3 * red + 0.6 * blue + 0.1 * green

        #Example colors and expected return values
        colorvals = { (0, 0, 0) : 0,
            (-10, -10, -10) : 0 ,      #out of range, return lowest regular value
            (100, 100, 100) : 100,     #This color is gray... returns same number
            (45, 120, 170) : 102,      # A typical color
            (600, 600, 600) : 255     #Out of range - should return max val
        }

        for val in colorvals:

            g = asc.color_to_gray(val)
            self.assertEqual(g, colorvals[val])     #Assert we get expected value...
            self.assertTrue(g >=0 and g <= 255)     #And that it is within the correct range.



    def test_ascii_pix(self):

        #Testing the appropriate character is being returned...
        self.assertEqual(asc.ascii_pixels[0], asc.ascii_pix(255) , '1')
        self.assertEqual(asc.ascii_pixels[2], asc.ascii_pix(190) , '2')
        self.assertEqual(asc.ascii_pixels[4], asc.ascii_pix(110) , '3')
        self.assertEqual(asc.ascii_pixels[7], asc.ascii_pix(2) , '4')



if __name__ == '__main__':
    unittest.main()
