import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from llm_handler import ask_llm,validate_json
from utils import load_file,save_json
from config import FILE_PATH
from schema import question




def all_process(file_path):
    
    file_extension = os.path.splitext(file_path)[1]

    output_file = file_path.replace(file_extension, ".json")

    output_file = os.path.join("parsed_resume", output_file)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    all_text = load_file(file_path)

    response = ask_llm(all_text, question)

    validated_response = validate_json(response)

    save_json(validated_response, output_file)
    
    print("Process completed successfully.")
    
    return output_file


if __name__ == "__main__":

    all_process(FILE_PATH)
