# python_ai/src/config.py

import os

# Root Directory
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# YOLO 모델 파일 경로
MODEL_DIR = os.path.join(ROOT_DIR, "weights")
MODEL_NAME = "yolov8n.pt"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)

# 서버 설정
HOST = "0.0.0.0"
PORT = 8000