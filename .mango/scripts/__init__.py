from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
MANGO_DIR = SCRIPT_DIR.parent
if str(MANGO_DIR) not in sys.path:
	sys.path.insert(0, str(MANGO_DIR))
