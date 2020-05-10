from simpleimage import SimpleImage


def double_left(filename):
    """
    Takes the left half of image, and copies it on top of the right half.
    """
    image = SimpleImage(filename)
    width = image.width
    height = image.height
    for y in range(height):
        for x in range(width // 2):
            pixel = image.get_pixel(x, y)
            image.set_pixel((x + (width // 2)), y, pixel)
    image.show()


def main():
    double_left('karel.png')


if __name__ == "__main__":
    main()
