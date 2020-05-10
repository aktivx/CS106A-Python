from simpleimage import SimpleImage

PIXELS_TO_CROP = 30


def crop_image(filename, n):
    """
    Takes the left half of image, and copies it on top of the right half.
    """
    image = SimpleImage(filename)
    width = image.width
    new_width = width - (2 * n)
    height = image.height
    new_height = height - (2 * n)
    image_crop_width = SimpleImage.blank(new_width, height)
    for y in range(height):
        for x in range(new_width):
            pixel = image.get_pixel((x + n), y)
            image_crop_width.set_pixel(x, y, pixel)
    image_crop_width.show()

    image_crop_height = SimpleImage.blank(width, new_height)
    for y in range(new_height):
        for x in range(width):
            pixel = image.get_pixel(x, y + n)
            image_crop_height.set_pixel(x, y, pixel)
    image_crop_height.show()

    image_crop_width_height = SimpleImage.blank(new_width, new_height)
    for y in range(new_height):
        for x in range(new_width):
            pixel = image.get_pixel(x + n, y + n)
            image_crop_width_height.set_pixel(x, y, pixel)
    image_crop_width_height.show()

def main():
    crop_image('karel.png', PIXELS_TO_CROP)


if __name__ == "__main__":
    main()
