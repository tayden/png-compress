#!/usr/bin/env python

import cv2
import numpy as np
import argparse

def quantize_colors(img, K):
    """Reduce the number of colors in img so only K distinct colours remain. Uses K-means."""

    Z = img.reshape((-1,3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    return res.reshape((img.shape))


def parse_arguments():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="Path to the input PNG image", type=str)
    ap.add_argument("output", help="Path/filename of output image", type=str)
    ap.add_argument("-k", "--colors", default=8, help="Number of quantized colors", type=int)
    ap.add_argument("-c", "--compression", default=9, help="Amount of PNG compression (0=none, 9=full)", type=int, choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    return vars(ap.parse_args())


def main(*args, **kwargs):
    # Read the image
    img = cv2.imread(kwargs['input'])

    # Quantize the colors
    img = quantize_colors(img, kwargs['colors'])

    # Write the compressed png to output
    opts = [cv2.IMWRITE_PNG_COMPRESSION, kwargs['compression']]
    cv2.imwrite(kwargs['output'], img, opts)


if __name__ == "__main__":
    kwargs = parse_arguments()
    main(**kwargs)