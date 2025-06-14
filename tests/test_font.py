import subprocess
from pathlib import Path

def test_bue_output():
    font_path = Path(__file__).resolve().parent.parent / 'bbs.flf'
    result = subprocess.run(['figlet', '-f', str(font_path), 'BUE'], capture_output=True, text=True)
    assert result.returncode == 0
    expected = Path('ascii.txt').read_text()
    assert result.stdout == expected
