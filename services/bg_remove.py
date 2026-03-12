from rembg import remove
from PIL import Image


def remove_background_with_color(input_path, output_path, color=(255, 255, 255)):

    img = Image.open(input_path)

    # remove background
    result = remove(img).convert("RGBA")

    # create solid color background
    background = Image.new("RGBA", result.size, color)

    # paste foreground on new background
    background.paste(result, (0, 0), result)

    background = background.convert("RGB")

    background.save(output_path)

    return output_path