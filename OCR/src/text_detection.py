# text_detection.py

import argparse
import cv2
import torch

from pathlib import Path

from yolov5.models.experimental import attempt_load
from yolov5.utils.datasets import letterbox
from yolov5.utils.general import non_max_suppression, scale_coords
from yolov5.utils.torch_utils import time_synchronized


def process_image(img, imgsz: int):
    img = letterbox(img, imgsz)[0]

    # Convert
    img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
    img = torch.from_numpy(img).float()
    img /= 255.0  # 0 - 255 to 0.0 - 1.0
    return img.unsqueeze(0)


def main(weights_path, image_path, imgsz=640, conf_thres=0.25, iou_thres=0.45, names=None):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = attempt_load(weights_path, map_location=device)  # YOLOv5x 모델 로드

    # 이미지 로드 및 전처리
    img0 = cv2.imread(image_path)  # BGR
    img = process_image(img0, imgsz).to(device)

    # 모델 실행
    model.eval()

    with torch.no_grad():
        t1 = time_synchronized()
        pred = model(img, augment=None)[0]

        # NMS 적용
        pred = non_max_suppression(pred, conf_thres, iou_thres, classes=None, agnostic=None)

    # 결과 출력 및 저장
    for i, det in enumerate(pred):  # 이미지 인덱스 및 감지 값
        if len(det):
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img0.shape).round()

            for *xyxy, conf, cls in reversed(det):
                label = f'{names[int(cls)]} {conf:.2f}'
                print(f'label: {label}')

                plot_one_box(xyxy, img0, label=label, color=None, line_thickness=3)

    image_output = "output.jpg"
    cv2.imwrite(image_output, img0)
    print(f"Output image saved as {image_output}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--weights", type=str, required=True, help="Path to the model weights")
    parser.add_argument("--image", type=str, required=True, help="Path to the input image")
    parser.add_argument("--imgsz", type=int, default=640, help="Input image size")
    args = parser.parse_args()

    main(args.weights, args.image, args.imgsz)
    
# python text_detection.py --weights path/to/your/yolov5x.pt --image path/to/your/image.jpg