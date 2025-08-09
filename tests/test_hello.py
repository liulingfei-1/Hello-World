import subprocess
import sys

def test_python_output():
    result = subprocess.run([sys.executable, "HelloWorld.py"], capture_output=True, text=True, check=True)
    assert result.stdout.strip() == "Hello, World!"
