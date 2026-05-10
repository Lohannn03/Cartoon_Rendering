import cv2 as cv
import numpy as np


sigmaColor, sigmaSpace = 60, 120
threshold1, threshold2 = 40, 70

original = cv.imread('forest.jpg')
if original is None:
    print("Cannot read image.")
    exit()

height, width = original.shape[:2]
new_width = 500
new_height = int(height * new_width / width)
img = cv.resize(original, (new_width, new_height))


smooth = img.copy()
smooth = cv.bilateralFilter(smooth, 5, sigmaColor, sigmaSpace)
gray = cv.cvtColor(smooth, cv.COLOR_BGR2GRAY)

edges = cv.Canny(gray, threshold1, threshold2)
edges = 255 - edges
edges_bgr = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)

cartoon = cv.bitwise_and(smooth, edges_bgr)

cartoon_show = np.hstack((img, cartoon))
cv.imshow("Original | Cartoon", cartoon_show)
cv.imwrite("forest_cartoon_result.jpg", cartoon_show)
cv.waitKey(0)
cv.destroyAllWindows()