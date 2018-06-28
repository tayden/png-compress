import cv2
import numpy as np


def quantize_colors(img, K):
    """Reduce the number of colors in img so only K distinct colours remain. Uses K-means."""

    Z = img.reshape((-1,3))
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    return res.reshape((img.shape))


def load_img(path):
    """Load an image from path as an opencv image."""
    return cv2.imread(path)


def save_img(img, compression, path):
    """Compress and save img to location path with compression amount of png compression."""
    opts = [cv2.IMWRITE_PNG_COMPRESSION, compression]
    cv2.imwrite(path, img, opts)