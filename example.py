import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob

def luminance_image(image_name):
    print "."
    image = Image.open(image_name).convert("L")
    flatten = np.asarray(image).flatten()
    arr = flatten[np.arange(0,len(flatten),1000)]
    return arr.mean() / 256.


def main(images):
    imgs = glob.glob(images)[:100]
    luminances = [luminance_image(img) for img in imgs]
    fig_luminance, ax = plt.subplots()
    ax.plot(luminances)
    plt.show()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('images', type=str, help='images (use wildcards)')
    args = parser.parse_args()
    main(args.images)
