# Cartoon Rendering using OpenCV

## 1. Project Overview

This project implements a cartoon-style image rendering algorithm using OpenCV.  
The goal is to transform a real-world image into a cartoon-like or painting-like image using classical image processing techniques.

The algorithm focuses on:
- Color simplification (quantization)
- Edge smoothing and enhancement
- Lighting and tone adjustment
- Painterly (soft cartoon) effect

---

## 2. Method

The algorithm consists of the following steps:

1. **Smoothing**
   - Bilateral filter is applied multiple times to reduce noise while preserving edges.

2. **Color Quantization**
   - The number of color levels is reduced to make the image look more like a cartoon.

3. **Tone Adjustment**
   - CLAHE is applied to enhance local contrast.
   - Saturation and brightness are increased slightly.

4. **Soft Edge Extraction**
   - Laplacian operator is used to extract soft edges instead of strong black outlines.

5. **Blending**
   - Edge information is blended with the color image.

6. **Painterly Effect**
   - A slight glow effect is added to simulate digital painting.

  ## 3. How to Run

*Install*
bash
pip install opencv-python numpy

bash
python cartoon.py

## 4. Demo

### 4.1 만화 스타일이 잘 표현되는 경우

다음과 같은 이미지에서는 만화 스타일 효과가 잘 나타난다.

- 주제가 명확한 이미지
- 배경이 단순한 이미지
- 조명이 밝고 균일한 이미지
- 색상이 비교적 뚜렷한 이미지

## Good Case

### Original
![Good](https://github.com/user-attachments/assets/bee6d41c-67cf-4f51-89e6-7a9204f9589e)

### Cartoon Result
![GoodDemo](https://github.com/user-attachments/assets/b85dbfdb-8cf5-4625-a9e1-618eab750991)

### Screenshot
<img width="1919" height="1079" alt="GoodDemo(screenshot)" src="https://github.com/user-attachments/assets/3b27fdda-4718-4e5a-9958-6fc6177e8330" />
---

### 4.2 만화 스타일이 잘 표현되지 않는 경우

다음과 같은 이미지에서는 결과가 좋지 않다.

- 배경이 복잡한 이미지
- 너무 어두운 이미지
- 명암 대비가 약한 이미지
- 디테일이 너무 많은 이미지 (머리카락, 나뭇잎 등)

## Bad Case

### Original
![Bad](https://github.com/user-attachments/assets/fddf2225-2987-4552-a52c-da100cee9308)

### Cartoon Result
![BadDemo](https://github.com/user-attachments/assets/53217a16-d0a3-43a2-a4b1-1ff763b2994f)

### Screenshot
<img width="1919" height="1079" alt="BadDemo(screenshot)" src="https://github.com/user-attachments/assets/df454e34-58b6-4a25-8648-1f9dde44a875" />
---

## 5. 한계점 (Limitations)

본 알고리즘은 다음과 같은 한계를 가진다.

1. 딥러닝이 아닌 전통적인 이미지 처리 기법을 사용하기 때문에 실제 애니메이션 스타일을 완벽하게 재현하기 어렵다.

2. 이미지의 조명, 대비, 배경 복잡도에 따라 결과가 크게 달라진다.

3. 머리카락, 나뭇잎, 옷 주름과 같은 복잡한 텍스처는 깔끔하게 단순화되지 않고 노이즈처럼 보일 수 있다.

4. 객체를 인식하지 못하기 때문에 배경과 인물을 구분하지 않고 동일하게 처리한다.

5. 최적의 결과를 얻기 위해서는 이미지마다 파라미터 조정이 필요하다.

---

## 6. 결론 (Conclusion)

본 프로젝트는 OpenCV를 이용한 기본적인 컴퓨터 비전 기법만으로도 만화 스타일 이미지를 생성할 수 있음을 보여준다.  
비록 모든 이미지에서 완벽한 결과를 얻을 수는 없지만, 단순한 구조와 좋은 조명을 가진 이미지에서는 효과적인 결과를 얻을 수 있다.
