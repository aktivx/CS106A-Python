from simpleimage import SimpleImage


SQUEEZE_FACTOR = 3


def squeeze_width(filename, n):
    image = SimpleImage(filename)
    width = image.width
    height = image.height
    image_squeeze = SimpleImage.blank(width // SQUEEZE_FACTOR, height)
    for y in range(height):
        for x in range(width // n):
            pixel = image.get_pixel(x * n, y)
            image_squeeze.set_pixel(x, y, pixel)
    image_squeeze.show()


def main():
    squeeze_width('karel.png', SQUEEZE_FACTOR)


if __name__ == "__main__":
    main()
