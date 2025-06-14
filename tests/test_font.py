from pathlib import Path
import pyfiglet

def test_bue_output():
    base_dir = Path(__file__).resolve().parent
    font_path = base_dir.parent / 'bbs'
    fig = pyfiglet.Figlet(font=str(font_path))
    output = fig.renderText('BUE')
    expected = (base_dir.parent / 'ascii.txt').read_text()
    assert output.rstrip() == expected.rstrip()
