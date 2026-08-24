import os
import pandas as pd
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_resume_text():

    resume_folder = "resume"

    pdf_files = [
        file
        for file in os.listdir(resume_folder)
        if file.lower().endswith(".pdf")
    ]

    if not pdf_files:
        print("ERROR: No PDF found inside the resume folder. - resume_matcher.py:19")
        return ""

    pdf_path = os.path.join(
        resume_folder,
        pdf_files[0]
    )

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + " "

    return text


def calculate_match(resume_text, job_description, required_skills):

    job_text = (
        job_description
        + " "
        + required_skills
    )

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    documents = [
        resume_text,
        job_text
    ]

    tfidf_matrix = vectorizer.fit_transform(
        documents
    )

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    score = similarity[0][0] * 100

    return round(score, 2)


def main():

    print("RESUME JOB MATCHER - resume_matcher.py:74")
    print("= - resume_matcher.py:75" * 40)

    resume_text = extract_resume_text()

    if not resume_text:
        return

    print("Resume loaded successfully. - resume_matcher.py:82")
    print()

    jobs = pd.read_csv(
        "c2c_jobs.csv"
    )

    results = []

    for _, job in jobs.iterrows():

        score = calculate_match(
            resume_text,
            job["job_description"],
            job["required_skills"]
        )

        results.append({

            "recruiter_name":
                job["recruiter_name"],

            "recruiter_email":
                job["recruiter_email"],

            "role":
                job["role"],

            "location":
                job["location"],

            "job_type":
                job["job_type"],

            "match_score":
                score
        })

    result_df = pd.DataFrame(
        results
    )

    result_df = result_df.sort_values(
        by="match_score",
        ascending=False
    )

    result_df.to_csv(
        "matched_jobs.csv",
        index=False
    )

    print("JOB MATCHING RESULTS - resume_matcher.py:134")
    print("" * 40)

    for _, job in result_df.iterrows():

        print(
            f"{job['role']} | "
            f"{job['location']} | "
            f"Match: {job['match_score']}%"
        )

    print()

    best_job = result_df.iloc[0]

    print(
        "Best Match:",
        best_job["role"]
    )

    print(
        "Match Score:",
        best_job["match_score"],
        "%"
    )

    print()

    print(
        "Saved to: matched_jobs.csv"
    )


if __name__ == "__main__":
    main()