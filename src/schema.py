
system_prompt = """You are helpful AI assistant who answer user question based on the provided context."""


extract_prompt ="""
            **Task:** Extract key information from the following resume text.

            **Resume Text:**
            {context}

            **Instructions:**
            Please extract the following information and format it in a clear structure:

            1. **Contact Information:**
            - Name:
            - Email:
            - Phone Number:
            - Website/Portfolio:

            2. **Education:**
            - Institution Name:
            - Degree:
            - Field of Study:
            - Graduation Dates:

            3. **Experience:**
            - Job Title:
            - Company Name:
            - Location:
            - Dates of Employment:
            - Responsibilities/Projects:

            4. **Projects:**
            - Project Title:
            - Description/Technologies Used:
            - Outcomes/Results:

            5. **Skills:**
            - Programming Languages:
            - Technologies/Tools:

            6. **Additional Information:** (if applicable)
            - Certifications:
            - Awards or Honors:
            - Professional Affiliations:
            - Languages:

            **Question:**
            {question}

            **Extracted Information:**
        """


json_prompt = """
        Please validate and correct the following JSON data:

        **Extracted Information:**
        {data}

        Provide only the corrected JSON, with no preamble or explanation.

        **Corrected JSON:**"""
        
        
        
question = """You are tasked with parsing a job resume. Your goal is to extract relevant information in a valid structured 'JSON' format. 
                Do not write preambles or explanations."""