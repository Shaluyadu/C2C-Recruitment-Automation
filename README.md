# 🚀 C2C Recruitment Automation System

An end-to-end recruitment automation system designed to streamline the USA Corp-to-Corp (C2C) recruitment workflow.

The system automates job searching, USA C2C filtering, resume-to-job matching using NLP, recruiter outreach generation, follow-up tracking, recruiter status management, and recruitment dashboard reporting.

---

## 📌 Project Overview

The C2C Recruitment Automation System demonstrates how Python, NLP, machine learning, and data processing can be combined to automate a recruitment outreach workflow.

### Complete Workflow

Job Search  
↓  
USA C2C Filtering  
↓  
Resume Extraction  
↓  
Resume–Job Matching  
↓  
Personalized Recruiter Outreach  
↓  
Follow-up Tracking  
↓  
Recruiter Status Management  
↓  
Recruitment Dashboard

---

## ✨ Features

### 🇺🇸 1. C2C Job Search

The job search module:

- Searches C2C job opportunities
- Filters USA-based opportunities
- Stores recruiter information
- Stores job roles and locations
- Stores required technical skills
- Exports job data to CSV

**Output:**

`c2c_jobs.csv`

---

### 📄 2. Resume–Job Matching

The resume matching module compares the candidate's resume with available job requirements using NLP techniques.

Technologies used:

- TF-IDF Vectorization
- Cosine Similarity
- Scikit-learn
- PDF text extraction
- Natural Language Processing

Example:

```text
Python Developer | New York, NY | Match: 9.73%
Data Scientist | Dallas, TX | Match: 2.10%
```

The system identifies the job with the highest similarity score as the best match.

**Output:**

`matched_jobs.csv`

---

### 📧 3. Personalized Recruiter Outreach

The outreach module generates personalized email drafts based on:

- Recruiter name
- Recruiter email
- Job role
- Job location
- Candidate skills
- Resume match score

The generated email includes a personalized subject and message.

**Output:**

`outreach.csv`

Example subject:

```text
Application for Python Developer - C2C
```

---

### 📅 4. Follow-up Tracking

The follow-up module manages recruiter communication and automatically calculates a follow-up date after 3 days.

It tracks:

- Recruiter information
- Job role
- Match score
- Sent date
- Follow-up date
- Response
- Recruiter status

**Output:**

`follow_up.csv`

Available statuses:

```text
Draft
Sent
Follow-up
Replied
```

---

### 🔄 5. Recruiter Status Management

The status management module allows recruiter outreach status to be updated.

Available options:

1. Draft
2. Sent
3. Follow-up
4. Replied

This allows the recruitment workflow to maintain the current communication stage for each recruiter.

---

### 📊 6. Recruitment Dashboard

The dashboard provides a summary of the recruitment workflow.

It displays:

- Total USA C2C jobs
- Best matching job
- Best resume match score
- Total outreach records
- Draft count
- Sent count
- Follow-up count
- Replied count
- System module status

Example:

```text
JOB SUMMARY

Total USA C2C Jobs: 2

RESUME MATCHING

Best Match: Python Developer
Best Match Score: 9.73%

OUTREACH

Total Outreach Drafts: 2
Draft: 0
Sent: 1
Follow-up: 1
Replied: 0

SYSTEM STATUS

Job Search:        OK
Resume Matching:   OK
Outreach:          OK
Follow-up:         OK
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- PyPDF2
- Natural Language Processing
- CSV Data Processing
- Git
- GitHub

---

## 📂 Project Structure

```text
C2C-Recruitment-Automation/
│
├── main.py
├── job_search.py
├── resume_matcher.py
├── outreach.py
├── follow_up.py
├── update_status.py
├── dashboard.py
│
├── c2c_jobs.csv
├── matched_jobs.csv
├── outreach.csv
├── follow_up.csv
│
├── resume/
│   └── Resume.pdf
│
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Shaluyadu/C2C-Recruitment-Automation.git
```

Navigate to the project directory:

```bash
cd C2C-Recruitment-Automation
```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Install required dependencies:

```bash
pip install pandas scikit-learn PyPDF2
```

---

## ▶️ How to Run

Run the complete recruitment workflow:

```bash
python main.py
```

The main program executes:

```text
1. Job Search
2. Resume Matching
3. Recruiter Outreach
4. Follow-up Tracking
5. Dashboard Generation
```

Individual modules can also be executed separately:

```bash
python job_search.py
```

```bash
python resume_matcher.py
```

```bash
python outreach.py
```

```bash
python follow_up.py
```

```bash
python update_status.py
```

```bash
python dashboard.py
```

---

## 📈 Resume Matching Method

The system uses NLP-based similarity matching.

The process is:

```text
Resume PDF
    ↓
PDF Text Extraction
    ↓
Resume Text
    ↓
TF-IDF Vectorization
    ↓
Job Requirements
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity
    ↓
Match Percentage
```

The resulting similarity score is used to identify the most relevant job opportunity.

---

## 📧 Sample Recruiter Outreach

Example generated email:

```text
Subject: Application for Python Developer - C2C

Hi Sarah,

I hope you are doing well.

I came across the Python Developer opportunity in New York, NY
and would like to express my interest.

My background includes Python, Machine Learning, Data Science,
Flask, MongoDB, Git, and related technologies.

Based on the current job requirements, my resume shows a
9.73% match with this opportunity.

I would be happy to share my resume and discuss the opportunity further.

Thank you for your time.

Best regards,
Shalu Yadav
AI & Data Science Enthusiast
```

---

## 🔄 Complete System Flow

```text
                C2C JOB SEARCH
                       ↓
              USA C2C FILTERING
                       ↓
                RESUME EXTRACTION
                       ↓
              NLP RESUME MATCHING
                       ↓
              MATCH SCORE GENERATED
                       ↓
              RECRUITER OUTREACH
                       ↓
              FOLLOW-UP TRACKING
                       ↓
             STATUS MANAGEMENT
                       ↓
                  DASHBOARD
```

---

## 🎯 Project Objective

The main objective of this project is to demonstrate an automated recruitment outreach workflow for USA-based Corp-to-Corp opportunities.

The project combines:

- Data processing
- Natural Language Processing
- Machine Learning
- Resume analysis
- Recruiter outreach generation
- Follow-up management
- Recruitment analytics

into a single Python-based automation system.

---

## 🚀 Future Improvements

Future versions can include:

- Real-time job API integration
- LinkedIn recruiter search automation
- Gmail API integration
- Automatic email sending
- AI-powered resume customization
- Advanced semantic resume matching
- Recruiter response detection
- Streamlit web dashboard
- Database integration
- Automated scheduled follow-ups

---

## 👩‍💻 Author

**Shalu Yadav**

AI & Data Science Enthusiast

### Skills

```text
Python
Machine Learning
Data Science
Generative AI
Flask
MongoDB
Git & GitHub
NLP
Scikit-learn
Pandas
NumPy
```

---

## 🔗 GitHub Repository

https://github.com/Shaluyadu/C2C-Recruitment-Automation

---

## 📌 Project Status

| Module | Status |
|---|---|
| Job Search | ✅ Completed |
| USA C2C Filtering | ✅ Completed |
| Resume Matching | ✅ Completed |
| Recruiter Outreach | ✅ Completed |
| Follow-up Tracking | ✅ Completed |
| Status Management | ✅ Completed |
| Recruitment Dashboard | ✅ Completed |
| GitHub Deployment | ✅ Completed |

---

## 📄 License

This project is created for educational and internship purposes.