# run_all.py
import os
import subprocess
import threading


def output_log(process, label):
    for line in iter(process.stdout.readline, b''):
        print(f"[{label}] {line.decode().rstrip()}")
    process.stdout.close()


def start_process(cmd, cwd, label):
    proc = subprocess.Popen(
        cmd,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=1
    )
    thread = threading.Thread(target=output_log, args=(proc, label), daemon=True)
    thread.start()
    return proc


# 경로 설정
spring_dir = os.path.join(os.getcwd(), "java_web")
python_dir = os.path.join(os.getcwd(), "python_ai")

spring_proc = start_process(["./gradlew", "bootRun"], cwd=spring_dir, label="JAVA")
python_proc = start_process(["python", "run.py"], cwd=python_dir, label="PYTHON")

try:
    spring_proc.wait()
    python_proc.wait()
except KeyboardInterrupt:
    print("🛑 종료 중...")
    spring_proc.terminate()
    python_proc.terminate()
