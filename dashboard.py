import os
import pandas as pd


def dashboard():

    print("C2C RECRUITMENT AUTOMATION DASHBOARD - dashboard.py:7")
    print("= - dashboard.py:8" * 50)

    # --------------------------------
    # JOB DATA
    # --------------------------------

    if os.path.exists("c2c_jobs.csv"):

        jobs = pd.read_csv("c2c_jobs.csv")

        total_jobs = len(jobs)

    else:

        total_jobs = 0

    # --------------------------------
    # MATCHING DATA
    # --------------------------------

    if os.path.exists("matched_jobs.csv"):

        matched = pd.read_csv("matched_jobs.csv")

    else:

        matched = pd.DataFrame()

    # --------------------------------
    # OUTREACH DATA
    # --------------------------------

    if os.path.exists("outreach.csv"):

        outreach = pd.read_csv("outreach.csv")

    else:

        outreach = pd.DataFrame()

    # --------------------------------
    # FOLLOW-UP DATA
    # --------------------------------

    if os.path.exists("follow_up.csv"):

        follow_up = pd.read_csv("follow_up.csv")

    else:

        follow_up = pd.DataFrame()

    # --------------------------------
    # CALCULATIONS
    # --------------------------------

    outreach_total = len(outreach)

    sent_count = 0
    followup_count = 0
    replied_count = 0
    draft_count = 0

    if not follow_up.empty:

        sent_count = (
            follow_up["status"] == "Sent"
        ).sum()

        followup_count = (
            follow_up["status"] == "Follow-up"
        ).sum()

        replied_count = (
            follow_up["status"] == "Replied"
        ).sum()

        draft_count = (
            follow_up["status"] == "Draft"
        ).sum()

    # --------------------------------
    # BEST MATCH
    # --------------------------------

    best_role = "N/A"
    best_score = 0

    if not matched.empty:

        best_job = matched.loc[
            matched["match_score"].idxmax()
        ]

        best_role = best_job["role"]
        best_score = best_job["match_score"]

    # --------------------------------
    # DISPLAY DASHBOARD
    # --------------------------------

    print()

    print("JOB SUMMARY - dashboard.py:111")
    print("" * 50)

    print(
        "Total USA C2C Jobs:",
        total_jobs
    )

    print()

    print("RESUME MATCHING - dashboard.py:121")
    print("" * 50)

    print(
        "Best Match:",
        best_role
    )

    print(
        "Best Match Score:",
        best_score,
        "%"
    )

    print()

    print("OUTREACH - dashboard.py:137")
    print("" * 50)

    print(
        "Total Outreach Drafts:",
        outreach_total
    )

    print(
        "Draft:",
        draft_count
    )

    print(
        "Sent:",
        sent_count
    )

    print(
        "Follow-up:",
        followup_count
    )

    print(
        "Replied:",
        replied_count
    )

    print()

    print("SYSTEM STATUS - dashboard.py:167")
    print("" * 50)

    print(
        "Job Search:       ",
        "OK" if os.path.exists("c2c_jobs.csv")
        else "Missing"
    )

    print(
        "Resume Matching:  ",
        "OK" if os.path.exists("matched_jobs.csv")
        else "Missing"
    )

    print(
        "Outreach:         ",
        "OK" if os.path.exists("outreach.csv")
        else "Missing"
    )

    print(
        "Follow-up:        ",
        "OK" if os.path.exists("follow_up.csv")
        else "Missing"
    )

    print()

    print("= - dashboard.py:196" * 50)
    print("Dashboard generated successfully! - dashboard.py:197")


if __name__ == "__main__":
    dashboard()