import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Charge une image JPG ou JPEG et retourne ses pixels en RGB."""
    try:
        image = Image.open(path)
    except Exception:
        print("Error: impossible d'ouvrir le fichier", path)
        return None

    if image.format != "JPEG" and image.format != "JPG":
        print("Error: le fichier doit etre en JPG ou JPEG")
        return None

    image = image.convert("RGB")
    tab = np.array(image)
    print("The shape of image is:", tab.shape)
    return tab


def main():
    ft_load("/Users/khelifi/42/python/day01/ex02/psg.png")


if __name__ == "__main__":
    main()