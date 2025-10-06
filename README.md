# 📄 Resume Parsing with LLM

A **resume parsing system powered by Large Language Models (LLMs)**.
This project enables users to upload resumes in **PDF or DOCX format**, automatically extracts key details such as **contact information, skills, education, work experience, and projects**, and returns them in a **well-structured JSON format**.

## 🔹 Why This Project?

Traditional resume parsing solutions rely on **regex rules** or **basic NLP techniques**, which often fail due to the wide variety of resume formats and layouts. By leveraging **LLMs (Large Language Models)**, this system provides:

* ✅ **Higher Accuracy** → Handles diverse resume formats without breaking on layout differences.
* ✅ **Structured Output** → Returns information in a **consistent JSON schema**, making it easy to store, analyze, or integrate with other systems.
* ✅ **Multi-format Support** → Works with `.pdf` and `.docx` files, with potential to extend to images (OCR).
* ✅ **ATS-Friendly Data** → Prepares resumes for **Applicant Tracking Systems (ATS)** by organizing key details cleanly.
* ✅ **Scalability** → Can be used for **bulk resume processing** in recruitment pipelines.
* ✅ **Extensibility** → New fields (e.g., certifications, languages, awards) can be added easily in the JSON schema.

## 🔹 Benefits

* 📂 **Recruiters & HR** → Save time by instantly extracting and structuring candidate details for faster filtering and matching.
* 🧑‍💻 **Developers & Researchers** → Get a ready-to-use parsing pipeline that can be integrated into **job boards, HR systems, or analytics dashboards**.
* 🏢 **Organizations** → Improve efficiency in **talent acquisition** by automating manual resume screening.
* 🔎 **Data Analysis** → Structured resume data can be used for **skills analytics, hiring trends, or workforce planning**.

---

## ✨ Features

* 📂 **Multi-format support** → Upload resumes in `.pdf` or `.docx`
* 🧠 **LLM-powered extraction** → Uses LangChain + OpenAI models
* ✅ **Validated JSON output** → Ensures consistent schema
* ⚡ **FastAPI backend** → REST API endpoints for parsing & retrieval
* 🧪 **Tests included** → Testing LLM handler & parser pipeline
* 📊 **Notebook experiments** → Test prompts and parsing logic in `notebooks/`

---

## 📂 Project Structure

```
Resume_Parsing_with_LLM/
│── data/                          # Sample resumes
│   └── Mostafa-Mohamed-Mostafa-Resume-3p.pdf
│
│── notebooks/                     # Experimentation
│   └── testing_llm.ipynb
│
│── src/                           # Source code
│   ├── config.py                  # File path & configs
│   ├── llm_handler.py             # LLM calls + JSON validation
│   ├── main.py                    # FastAPI app entry
│   ├── parser.py                  # Pipeline: load → ask LLM → validate → save
│   ├── schema.py                  # Prompt templates & schema
│   └── utils.py                   # File loaders, save/load JSON
│
│── tests/                         # Tests
│   ├── test_llm_handler.py
│   └── test_parser.py
│
│── requirements.txt               # Python dependencies
│── .env.example                   # Example environment variables
└── README.md                      # Documentation
```

---

## ⚙️ Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/MoustafaMohammedd/Resume_Parsing_with_LLM.git
   cd Resume_Parsing_with_LLM
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Environment Variables

Create a `.env` file in the project root based on `.env.example`:

```ini
API_KEY="your_api_key_here"
BASE_URL="https://api.openai.com/v1"
MODEL_NAME="openai/gpt-oss-20b:free"
```

---

## ▶️ Running the API

Start the FastAPI server with Uvicorn:

```bash
uvicorn src.main:app --reload
```

* API runs at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger UI (interactive docs): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📌 API Endpoints

### 1️⃣ Root Check

`GET /`
Returns a welcome message.

### 2️⃣ Process Resume File

`POST /process_file`

**Request Body:**

```json
{
  "file_path": "data/Mostafa-Mohamed-Mostafa-Resume-3p.pdf"
}
```

**Response:**

```json
{
  "message": "File processed successfully.",
  "output_file": "parsed_resume/data/Mostafa-Mohamed-Mostafa-Resume-3p.json"
}
```

### 3️⃣ Get Parsed Data

`POST /get_parsed_data`

**Request Body:**

```json
{
  "message": "File processed successfully.",
  "output_file": "parsed_resume/data/Mostafa-Mohamed-Mostafa-Resume-3p.json"
}
```

**Response:**

```json
{
  "data": {
    "name": "Mostafa Mohamed Mostafa",
    "contact": {
      "email": "mostafaelkazaz149@gmail.com",
      "phone": "+201025823935"
    },
    "skills": ["Python", "Machine Learning", "NLP"],
    "education": [...],
    "experience": [...]
  }
}
```

---

## 🚀 Future Enhancements

* 🌐 Add **UI** for easy upload and visualization
* 📁 Support for more file formats (`.txt`, `.jpg` scanned resumes)
* 📊 Integrate with ATS (Applicant Tracking System) for job matching
* 🔎 Improve entity extraction with fine-tuned LLM

---
