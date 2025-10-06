from langchain_community.document_loaders import  PyMuPDFLoader,Docx2txtLoader
from config import FILE_PATH
import json
import os

def load_file(file_path):
    file_extension = os.path.splitext(file_path)[1]
    
    if file_extension.lower() == '.docx' or file_extension.lower() == '.doc':
        loader = Docx2txtLoader(file_path)
        
    elif file_extension.lower() == '.pdf':
        loader = PyMuPDFLoader(file_path)
        
    else:
        raise ValueError("Unsupported file format. Please provide a .pdf or .docx file.")
    
    documents = loader.load()
    all_text = "\n".join([doc.page_content for doc in documents])
    return all_text


def save_json(response, output_file):
    json.dump(response, open(output_file, 'w'), indent=4)
    print(f"Data saved to {output_file}")

    
def load_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

if __name__ == "__main__":

    all_text = load_file(FILE_PATH)
    print(all_text)