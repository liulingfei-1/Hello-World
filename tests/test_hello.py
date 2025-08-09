import subprocess
import sys
from pathlib import Path

def test_python_hello_output():
    script = Path(__file__).resolve().parents[1] / 'HelloWorld.py'
    result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True, check=True)
    assert result.stdout.strip() == 'Hello, World!'
