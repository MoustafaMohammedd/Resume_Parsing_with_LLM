import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parser import all_process

from src.config import FILE_PATH

output_file=all_process(FILE_PATH)
