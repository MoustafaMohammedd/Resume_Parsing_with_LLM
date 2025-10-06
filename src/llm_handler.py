import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from langchain_openai import ChatOpenAI
from langchain_core.prompts import SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser,StrOutputParser
from schema import extract_prompt,system_prompt,json_prompt

from dotenv import load_dotenv
load_dotenv(".env")



api_key=os.getenv("API_KEY")
base_url=os.getenv("BASE_URL")
model_name=os.getenv("MODEL_NAME")

llm=ChatOpenAI(api_key=api_key,model=model_name,base_url=base_url)

system_template = SystemMessagePromptTemplate.from_template(system_prompt)
human_template = HumanMessagePromptTemplate.from_template(extract_prompt)
json_template = HumanMessagePromptTemplate.from_template(json_prompt)

def ask_llm(context, question):
    
    messages = [system_template, human_template]
    template = ChatPromptTemplate(messages)

    qna_chain = template | llm | StrOutputParser()
    return qna_chain.invoke({'context': context, 'question': question})


def validate_json(data):
 
    json_messages = [system_template, json_template]
    
    json_templa = ChatPromptTemplate(json_messages)

    json_chain = json_templa | llm | JsonOutputParser()
    
    return json_chain.invoke({'data': data})


