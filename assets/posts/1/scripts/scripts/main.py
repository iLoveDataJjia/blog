import os
from importlib.resources import files

import cv2
import numpy as np
from cv2.dnn_superres import DnnSuperResImpl
from PIL.Image import Image, fromarray, open
from PIL_DAT.dat_light import DATLight

from scripts import resources
from scripts.resources import images

OUT_FOLDER = "./out"


def get_edsr() -> DnnSuperResImpl:
    model = DnnSuperResImpl.create()
    model.setModel("edsr", 2)
    pb_path = str(files(resources) / f"EDSR_x2.pb")
    model.readModel(pb_path)
    return model


def get_dat() -> DATLight:
    return DATLight(2)


def upscale_with_edsr(model: DnnSuperResImpl, image: Image) -> Image:
    image_array = np.array(image.convert("RGB"))
    image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    image_array = model.upsample(image_array)
    return fromarray(cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB))


def upscale_with_dat(model: DATLight, image: Image) -> Image:
    return model.upscale(image)


if __name__ == "__main__":
    images_base_path = files(images)
    image_filenames = os.listdir(str(images_base_path))
    image_filenames = [x for x in image_filenames if x.endswith(".png")]
    print("Discovered images:", image_filenames)

    edsr = get_edsr()
    dat = get_dat()
    print("Models loaded!")

    for image_filename in image_filenames:
        image_input = open(str(images_base_path / image_filename))
        name, ext = image_filename.split(".")
        upscale_with_dat(dat, image_input).save(f"./{OUT_FOLDER}/{name}_dat.{ext}")
        upscale_with_edsr(edsr, image_input).save(f"./{OUT_FOLDER}/{name}_edsr.{ext}")
        print("Processing success:", image_filename)
