import math


def volume_of_sphere(radius):
    return (math.pi * radius * radius * radius * 4) / 3


def volume_of_pyramid(area, height):
    return (area * height) / 3


def volume_of_cuboid(length, breadth, height):
    return length * breadth * height


def volume_of_cone(radius, height):
    return (math.pi * radius * radius * height)/3
