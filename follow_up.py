import pandas as pd
from datetime import datetime, timedelta


def create_follow_up_file():

    print("FOLLOWUP TRACKING SYSTEM - follow_up.py:7")
    print("= - follow_up.py:8" * 40)

    # Read outreach data
    outreach = pd.read_csv("outreach.csv")

    # Today's date
    today = datetime.now().date()

    # Follow-up after 3 days
    follow_up_date = today + timedelta(days=3)

    # Create tracking columns
    outreach["sent_date"] = ""
    outreach["follow_up_date"] = follow_up_date.strftime("%Y-%m-%d")
    outreach["response"] = "Pending"

    # Keep current status as Draft
    outreach["status"] = "Draft"

    # Save tracking file
    outreach.to_csv(
        "follow_up.csv",
        index=False
    )

    print()
    print("Followup records created: - follow_up.py:34", len(outreach))
    print("Saved to: follow_up.csv - follow_up.py:35")
    print()

    for _, record in outreach.iterrows():

        print("")
        print("Recruiter: - follow_up.py:41", record["recruiter_name"])
        print("Role: - follow_up.py:42", record["role"])
        print("Match Score: - follow_up.py:43", record["match_score"], "%")
        print("Status: - follow_up.py:44", record["status"])
        print("Followup Date: - follow_up.py:45", record["follow_up_date"])
        print("Response: - follow_up.py:46", record["response"])

    print("")


if __name__ == "__main__":
    create_follow_up_file()