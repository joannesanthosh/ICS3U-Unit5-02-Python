#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Nov 2022
# This program calculates the area of a triangle using functions


def calculate_area(base: int, height: int) -> None:
    # calculate area

    # process
    area = (base * height) / 2

    # output
    print("The area is {0} cm²".format(area))


def main():
    # this function gets the base and height

    # input
    base_from_user = int(input("Enter the base value of the triangle (cm): "))
    height_from_user = int(input("Enter the height value of the triangle (cm): "))
    print("")

    try:
        base = float(base_from_user)
        height = float(height_from_user)
        calculate_area(base, height)
    except ValueError:
        print("\nInvalid Input")

    print("\nDone.")

    # call functions
    calculate_area(base_from_user, height_from_user)


if __name__ == "__main__":
    main()
