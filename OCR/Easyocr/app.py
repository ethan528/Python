import easyocr
from PIL import Image

# 이미지 파일 경로를 지정하세요
image_path = '../1687408498175.jpg'

# 이미지 열기
image = Image.open(image_path)

# 이미지 크기 조정 (원하는 크기로 변경)
new_size = (500, 500)
resized_image = image.resize(new_size, resample=Image.BILINEAR)

# 크기 조정된 이미지 저장
resized_image.save('크기 조정된 이미지.jpg')

# EasyOCR을 사용하여 이미지에서 텍스트 추출
reader = easyocr.Reader(['en', 'ko'])
result = reader.readtext(resized_image)

# 추출된 텍스트 출력
for detection in result:
    text = detection[1]
    print(text)