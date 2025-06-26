# run_all.py
import subprocess
import os

# 경로 설정
spring_dir = os.path.join(os.getcwd(), "java_web")
python_dir = os.path.join(os.getcwd(), "python_ai")

# 1. Spring Boot - WEB 표시
spring = subprocess.Popen(["./gradlew", "bootRun"], cwd=spring_dir)

# 2. FastAPI - AI
fastapi = subprocess.Popen(["python", "run.py"], cwd=python_dir)

# 3. 기다리기 (Ctrl+C 때까지)
try:
    spring.wait()
    fastapi.wait()
except KeyboardInterrupt:
    spring.terminate()
    fastapi.terminate()