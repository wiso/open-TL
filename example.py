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


def main():
    imgs = glob.glob("/var/run/media/turra/WDRuggero/d/*.JPG")[:100]
    luminances = [luminance_image(img) for img in imgs]
    fig_luminance, ax = plt.subplots()
    ax.plot(luminances)
    plt.show()

main()
