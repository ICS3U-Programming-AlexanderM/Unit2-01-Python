# Created by Alexander Matheson
# Created on November 25 2021
# This program calculates the area and perimeter of a circle

import math


def main():
    # this program calculates area and perimeter
    print("This circle has a radius of 3cm")
    print("Area=πr^2")
    print("Area={}cm squared".format(math.pi*3**2))
    print("")
    print("Circumference=2πr")
    print("Circumference is {} cm".format(2*math.pi*3))


if __name__ == "__main__":
    main()
