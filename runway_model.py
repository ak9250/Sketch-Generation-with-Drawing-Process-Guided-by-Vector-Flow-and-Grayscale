import runway
import numpy as np
import argparse
import torch
from torchvision import transforms
from process_order import draw

@runway.command('translate', inputs={'source_imgs': runway.image(description='input image to be translated'),}, outputs={'image': runway.image(description='output image containing the translated result')})
def translate(learn, inputs):
    os.makedirs('images', exist_ok=True)
    inputs['source_imgs'].save('images/temp.jpg')

    paths = os.path.join('images','temp.jpg')
    draw(paths)
    pathout = "./output/temp/process/result.jpg"
    img = Image.open(open(pathout, 'rb'))
    return img


if __name__ == '__main__':
    runway.run(port=8889)
