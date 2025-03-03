#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: may 24 2025
# This program ask the user the radius of a circle in mm
# Then it calculates and displays the circumference using Tau.
import constant

def calculate_circumference(radius):
    return constant.TAU * radius

def main():
    radius = float(input("Enter the radius of the circle (mm): "))
    circumference = calculate_circumference(radius)
    print("\nCircumference = {} mm".format(circumference))

if __name__ == "__main__":
    main()