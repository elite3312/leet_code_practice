import subprocess
import sys


filePath = "perry.py"
process = subprocess.Popen(
    ["python", filePath, "55688"],
    stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True
)
stdout, stderr =process.communicate(input="1223\n")
# Read from stdout
print(stdout)
print(stderr)
