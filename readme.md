# Java & Python & AI
> [!NOTE]
> 실습 및 연습용입니다. <br>
> 책에서 제시된 코드를 제외하고 프로젝트의 실행 구조를 간단화하였습니다.

## 실습 저서
> 자바 스프링 부트 프로젝트와 파이썬 AI 프로젝트 연결하기

## SDK
> [!IMPORTANT]
> 각 언어 사용된 SDK는 다음과 같습니다.<br>
> 각 SDK는 직접 따로따로 설정해줘야 합니다.<br>
> Intellij 기준 File > Project Structure 에서 설정하시면 됩니다.<br>
> 단 Python 경우 좀 복잡할 수도 있습니다.<br>
> 하단에 기술해둔 Python venv 설정을 참고하시기 바랍니다.
- JAVA : Eclipse Temurin - 21
- Python : Python3 - 3.13.5

## Project Dir
```
Java2Python/
├── java_web/         # Spring Boot 프로젝트 (Gradle 기반)
├── python_ai/        # FastAPI + AI 프로젝트
│   ├── src/          # Python 소스 코드
│   ├── weights/      # YOLO 모델 저장 폴더 (자동 생성됨)
│   ├── .venv/        # Python 가상환경 (git 제외)
│   └── run.py        # FastAPI 실행 진입점
├── run_all.py        # Java + Python 동시 실행 스크립트
└── readme.md
```

## Python venv 설정
```
# python_ai 디렉토리에서 실행
cd python_ai

# 가상환경 생성 (Python 3.13.5 기준)
python3 -m venv .venv

# 가상환경 활성화
source .venv/bin/activate

# 라이브러리 설치
pip install -r requirements.txt
```

## Python Library Lists
| 라이브러리            | 버전      | 주요 기능                         |
|------------------|---------|-------------------------------|
| fastapi          | 0.111.1 | 비동기 웹 프레임워크, 자동 OpenAPI 문서 생성 |
| uvicorn          | 0.30.1  | 고성능 비동기 서버, ASGI 표준 지원        |
| pydantic         | 2.7.1   | 데이터 검증 및 직렬화, 타입 힌팅, 설정 관리    |
| Pillow           | 10.3.0  | 이미지 열기, 저장, 변환, 다양한 이미지 처리 작업 |
| numpy            | 1.24.4  | 수치 계산, 배열 및 행렬 연산, 다양한 수학 함수  |
| requests         | 2.32.3  | 간단한 HTTP 요청 및 응답 처리           |
| ultralytics      | 8.2.58  | YOLOv8 객체 탐지 모델 제공            |
| opencv-python    | 4.10.0  | 이미지 및 비디오 처리, 컴퓨터 비전 기능       |
| python-multipart | 0.0.9   | 멀티파트 폼 데이터를 파싱하기 위해 사용        |

## 기타 설명 및 주의사항
> venv/, weights/ 폴더는 .gitignore에 포함되어 있음 <br> 
> run_all.py 실행 시 Spring Boot + FastAPI 동시에 실행됨 <br> 
> FastAPI 실행 시 yolov8n.pt 모델이 없으면 자동 다운로드되어 weights/ 폴더에 저장됨

> [!WARNING]
> 다시 언급하자면, 위의 weights/ 디렉토리에 생성된 모델은 git에서 제외함 <br>
> 실행 중 로그는 [JAVA], [PYTHON] 태그로 구분되어 한 터미널에 출력됨
