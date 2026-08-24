import pandas as pd


def search_c2c_jobs():

    data = [
        {
            "recruiter_name": "John Smith",
            "recruiter_email": "john@example.com",
            "role": "Data Scientist",
            "location": "Dallas, TX",
            "job_type": "C2C",
            "job_description": (
                "Looking for a Data Scientist with experience in "
                "Python, Machine Learning, Pandas, NumPy, SQL, "
                "Scikit-learn and Data Analysis."
            ),
            "required_skills": (
                "Python, Machine Learning, Pandas, NumPy, "
                "SQL, Scikit-learn, Data Analysis"
            )
        },
        {
            "recruiter_name": "Sarah Johnson",
            "recruiter_email": "sarah@example.com",
            "role": "Python Developer",
            "location": "New York, NY",
            "job_type": "C2C",
            "job_description": (
                "Looking for a Python Developer with experience in "
                "Python, Flask, REST APIs, SQL, Git, MongoDB and "
                "backend development."
            ),
            "required_skills": (
                "Python, Flask, REST APIs, SQL, Git, MongoDB, "
                "Backend Development"
            )
        },
        {
            "recruiter_name": "Mike Brown",
            "recruiter_email": "mike@example.com",
            "role": "QA Engineer",
            "location": "Toronto, Canada",
            "job_type": "C2C",
            "job_description": (
                "Looking for a QA Engineer with experience in "
                "manual testing, automation testing, Selenium, "
                "Python and test case development."
            ),
            "required_skills": (
                "Manual Testing, Automation Testing, Selenium, "
                "Python, Test Cases"
            )
        }
    ]

    df = pd.DataFrame(data)

    usa_states = [
        "TX", "NY", "CA", "FL", "WA",
        "IL", "NJ", "VA", "MA", "GA",
        "NC", "AZ"
    ]

    result = df[
        df["location"].apply(
            lambda x: any(
                state in x
                for state in usa_states
            )
        )
    ]

    return result


def main():

    print("C2C JOB SEARCH SYSTEM - job_search.py:79")
    print("= - job_search.py:80" * 40)

    jobs = search_c2c_jobs()

    jobs.to_csv(
        "c2c_jobs.csv",
        index=False
    )

    print()

    for _, job in jobs.iterrows():

        print("Recruiter: - job_search.py:93", job["recruiter_name"])
        print("Email: - job_search.py:94", job["recruiter_email"])
        print("Role: - job_search.py:95", job["role"])
        print("Location: - job_search.py:96", job["location"])
        print("Job Type: - job_search.py:97", job["job_type"])
        print("Required Skills: - job_search.py:98", job["required_skills"])
        print()

    print(
        "Total USA C2C Jobs:",
        len(jobs)
    )

    print(
        "Saved to: c2c_jobs.csv"
    )


if __name__ == "__main__":
    main()