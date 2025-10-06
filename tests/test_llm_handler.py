import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.llm_handler import ask_llm,validate_json
from src.utils import load_file
from src.config import FILE_PATH
from src.schema import question


all_text = load_file(FILE_PATH)

response = ask_llm(all_text, question)

print("Raw Response:")
print(response) 

print("#" * 20)

validated_response = validate_json(response)


print(validated_response)

