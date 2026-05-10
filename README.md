# Cartoon Rendering using OpenCV

## 1. Project Overview

This project implements a simple cartoon-style image rendering program using OpenCV.

The goal of this project is to transform an input image into a cartoon-like image using classical image processing techniques. The algorithm does not use deep learning. Instead, it uses image smoothing, edge detection, and image masking to create a cartoon-style effect.

The project demonstrates both:

- a good result where the cartoon effect is clearly visible
- a bad result where the cartoon effect is not well expressed
- limitations of the current algorithm

---

## 2. Algorithm

The cartoon rendering algorithm is based on the following OpenCV image processing steps.

### Step 1. Read the input image

The input image is loaded using `cv.imread()`.

```python
original = cv.imread("dragonball.jpg")
```
or:
```
original = cv.imread("forest.jpg")
```

### Step 2. Resize the image while keeping aspect ratio

The image is resized to a fixed width while preserving the original aspect ratio.
```
height, width = original.shape[:2]
new_width = 500
new_height = int(height * new_width / width)
img = cv.resize(original, (new_width, new_height))
```
This prevents the image from being stretched or distorted.

### Step 3. Smooth the image

A bilateral filter is applied to smooth the image while preserving strong edges.
```
smooth = cv.bilateralFilter(img, 5, sigmaColor, sigmaSpace)
```
The bilateral filter is useful for cartoon rendering because it reduces small texture details but keeps object boundaries relatively clear.

### Step 4. Convert to grayscale

The smoothed image is converted to grayscale for edge detection.
```
gray = cv.cvtColor(smooth, cv.COLOR_BGR2GRAY)
```

### Step 5. Detect edges using Canny

Canny edge detection is used to extract outlines from the image.
```
edges = cv.Canny(gray, threshold1, threshold2)
```
Then the edge image is inverted so that the outlines become black and the background becomes white.
```
edges = 255 - edges
```

### Step 6. Combine the smoothed image and edge mask

The edge mask is converted to a BGR image and combined with the smoothed color image.
```
edges_bgr = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
cartoon = cv.bitwise_and(smooth, edges_bgr)
```
This produces the final cartoon-style image.

### Step 7. Save the result

The original image and cartoon result are placed side by side and saved.
```
cartoon_show = np.hstack((img, cartoon))
cv.imwrite("dragonball_cartoon_result.jpg", cartoon_show)
```
or:
```
cv.imwrite("forest_cartoon_result.jpg", cartoon_show)
```
---

## 3. Main Parameters

The following parameters were used in the current implementation.
```
sigmaColor, sigmaSpace = 60, 120
threshold1, threshold2 = 40, 70
```
Parameter	Description
sigmaColor	Controls how strongly different colors are smoothed by the bilateral filter.
sigmaSpace	Controls how far neighboring pixels affect each other in the bilateral filter.
threshold1	Lower threshold for Canny edge detection.
threshold2	Upper threshold for Canny edge detection.

These parameters affect the final cartoon quality. Different input images may require different parameter values.

---

## 4. How to Run
Install requirements
pip install opencv-python numpy
Run the program
python cartoon_rendering.py

Before running the program, place the input image in the same folder as the Python file.

Example input files:

dragonball.jpg
forest.jpg

Example output files:

dragonball_cartoon_result.jpg
forest_cartoon_result.jpg

---

## 5. Demo Results
### 5.1 Good Result
Input Image

The good case uses the following original image:

dragonball.jpg

This image works well because it has:

- a clear main subject
- a simple orange background
- strong color contrast
- clear object boundaries
- less natural texture noise

Cartoon Result

The output image is saved as:

dragonball_cartoon_result.jpg

Discussion

This result can be considered a good cartoon rendering result.

The character has clear black outlines around the hair, face, clothes, arms, and legs. The orange background remains mostly clean because it does not contain many small textures. The bilateral filter smooths the color regions, while Canny edge detection creates visible outlines around the main subject.

As a result, the final image looks closer to a manga or cartoon-style illustration compared with the original image.

## 5.2 Bad Result
Input Image

The bad case uses the following original image:

forest.jpg

This image is more difficult because it contains:

- many leaves
- many tree branches
- grass and rocks
- shadows
- small animals
- complex natural textures

Cartoon Result

The output image is saved as:

forest_cartoon_result.jpg

Discussion

This result is a bad case because the cartoon effect is not clearly expressed.

The forest scene contains too many small details. Canny edge detection detects many tiny edges from leaves, branches, grass, rocks, and shadows. Because of this, the output contains a large number of noisy black outlines.

Instead of looking like a clean cartoon image, the result looks cluttered and noisy. The main subjects are also not very clear because the algorithm processes the whole image equally and does not separate foreground objects from the background.

---

## 6. Limitations

The current algorithm has several limitations.

### 1. It is sensitive to image complexity

The algorithm works better on images with a clear main subject and simple background. If the image contains many small textures, such as leaves, grass, hair, or rocks, the edge detector may create too many unnecessary outlines.

This can be seen in the forest example, where the result becomes noisy and visually cluttered.

### 2. It does not understand objects

The algorithm is based only on low-level image processing. It does not know which region is the main subject and which region is the background.

Because of this, the foreground and background are processed in the same way. This can make complex backgrounds too strong and distracting.

### 3. Canny edge detection can produce too many edges

Canny edge detection is useful for extracting outlines, but it can also detect small texture details as edges. In natural scenes, this may create many unnecessary black lines.

For example, leaves and tree branches can produce too many edge lines.

### 4. The result depends heavily on parameters

The quality of the cartoon effect depends on parameters such as:

- sigmaColor
- sigmaSpace
- threshold1
- threshold2

A parameter setting that works well for one image may not work well for another image. For this reason, the algorithm may need manual tuning for different input images.

### 5. It cannot fully reproduce real animation style

This project uses classical image processing techniques, not deep learning or style transfer. Therefore, it cannot fully reproduce professional anime or hand-drawn cartoon styles.

The output can look cartoon-like, but it may still preserve some photo-like textures.

## 7. Conclusion

This project shows that a cartoon-style image can be created using basic OpenCV image processing techniques.

The algorithm works well when the input image has a clear subject, strong boundaries, and a simple background. The Dragon Ball image is a good example because the character is clearly separated from the background and the final result has visible cartoon-like outlines.

However, the algorithm does not work well for complex natural scenes. The forest image is a bad example because the many small textures cause too many noisy edges.

Overall, the project demonstrates both the usefulness and the limitations of traditional image processing methods for cartoon rendering.