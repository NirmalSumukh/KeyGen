import sys
from os.path import dirname, abspath
sys.path.insert(0, abspath(dirname(__file__)))

from main import app as application  # This points to your FastAPI app