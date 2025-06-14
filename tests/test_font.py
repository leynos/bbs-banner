from pathlib import Path
import pyfiglet
import pytest

def normalize_output(output: str) -> str:
    lines = [
        line.rstrip()
        for line in output.splitlines()
        if line.rstrip()
    ]
    return '\n'.join(lines)

@pytest.mark.parametrize('text', ['BUE', 'EBU'])
def test_bue_output(text):
    base_dir = Path(__file__).resolve().parent
    font_path = base_dir.parent / 'bbs'
    fig = pyfiglet.Figlet(font=str(font_path))
    output = fig.renderText(text)
    expected = (base_dir.parent / f'ascii_{text.lower()}.txt').read_text()
    assert normalize_output(output) == normalize_output(expected)
