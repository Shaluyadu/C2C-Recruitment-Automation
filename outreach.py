import pandas as pd


def create_email(recruiter_name, role, location, match_score):

    first_name = recruiter_name.split()[0]

    subject = f"Application for {role} - C2C"

    sentence = (
        "I came across the "
        + str(role)
        + " opportunity in "
        + str(location)
        + " and would like to express my interest."
    )

    body = (
        f"Hi {first_name},\n\n"
        f"I hope you are doing well.\n\n"
        f"{sentence}\n\n"
        f"My background includes Python, Machine Learning, "
        f"Data Science, Flask, MongoDB, Git, and related technologies.\n\n"
        f"Based on the current job requirements, my resume shows "
        f"a {match_score}% match with this opportunity.\n\n"
        f"I would be happy to share my resume and discuss the "
        f"opportunity further.\n\n"
        f"Thank you for your time.\n\n"
        f"Best regards,\n"
        f"Shalu Yadav\n"
        f"AI & Data Science Enthusiast"
    )

    return subject, body


def main():

    print("RECRUITER OUTREACH SYSTEM - outreach.py:39")
    print("= - outreach.py:40" * 40)

    jobs = pd.read_csv("matched_jobs.csv")

    outreach_data = []

    for _, job in jobs.iterrows():

        subject, body = create_email(
            job["recruiter_name"],
            job["role"],
            job["location"],
            job["match_score"]
        )

        outreach_data.append({
            "recruiter_name": job["recruiter_name"],
            "recruiter_email": job["recruiter_email"],
            "role": job["role"],
            "location": job["location"],
            "match_score": job["match_score"],
            "email_subject": subject,
            "email_body": body,
            "status": "Draft"
        })

    outreach_df = pd.DataFrame(outreach_data)

    outreach_df.to_csv(
        "outreach.csv",
        index=False
    )

    print()
    print("Outreach drafts created: - outreach.py:74", len(outreach_df))
    print("Saved to: outreach.csv - outreach.py:75")
    print()

    for _, email in outreach_df.iterrows():

        print("")
        print("To: - outreach.py:81", email["recruiter_email"])
        print("Subject: - outreach.py:82", email["email_subject"])
        print("")


if __name__ == "__main__":
    main()