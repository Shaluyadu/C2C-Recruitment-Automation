import pandas as pd
from datetime import datetime, timedelta
import os


def create_follow_up_file():

    print("FOLLOWUP TRACKING SYSTEM")
    print("=" * 60)

    # Read outreach data
    outreach = pd.read_csv("outreach.csv")

    # Existing follow-up file
    existing_file = "follow_up.csv"

    # Today's date
    today = datetime.now().date()

    # Follow-up after 3 days
    follow_up_date = today + timedelta(days=3)

    # ---------------------------------------------------------
    # If follow_up.csv already exists, preserve existing status
    # ---------------------------------------------------------
    if os.path.exists(existing_file):

        existing = pd.read_csv(existing_file)

        # Preserve important columns from previous tracking
        previous_columns = [
            "recruiter_email",
            "status",
            "sent_date",
            "follow_up_date",
            "response"
        ]

        available_columns = [
            col for col in previous_columns
            if col in existing.columns
        ]

        existing_status = existing[available_columns].copy()

        # Remove old tracking columns from new outreach data
        for column in [
            "sent_date",
            "follow_up_date",
            "response",
            "status"
        ]:
            if column in outreach.columns:
                outreach = outreach.drop(columns=[column])

        # Add default values for new records
        outreach["sent_date"] = ""
        outreach["follow_up_date"] = follow_up_date.strftime("%Y-%m-%d")
        outreach["response"] = "Pending"
        outreach["status"] = "Draft"

        # Merge old status information using recruiter email
        if "recruiter_email" in existing_status.columns:

            outreach = outreach.merge(
                existing_status,
                on="recruiter_email",
                how="left",
                suffixes=("", "_old")
            )

            # Preserve old values when they exist
            outreach["status"] = outreach["status_old"].fillna(
                outreach["status"]
            )

            outreach["sent_date"] = outreach["sent_date_old"].fillna(
                outreach["sent_date"]
            )

            outreach["follow_up_date"] = outreach[
                "follow_up_date_old"
            ].fillna(
                outreach["follow_up_date"]
            )

            outreach["response"] = outreach["response_old"].fillna(
                outreach["response"]
            )

            # Remove temporary columns
            old_columns = [
                "status_old",
                "sent_date_old",
                "follow_up_date_old",
                "response_old"
            ]

            for column in old_columns:
                if column in outreach.columns:
                    outreach = outreach.drop(columns=[column])

    else:

        # First-time creation
        outreach["sent_date"] = ""
        outreach["follow_up_date"] = follow_up_date.strftime("%Y-%m-%d")
        outreach["response"] = "Pending"
        outreach["status"] = "Draft"

    # Save tracking file
    outreach.to_csv(
        existing_file,
        index=False
    )

    print()
    print("Followup records created:", len(outreach))
    print("Saved to: follow_up.csv")
    print()

    # Display tracking information
    for _, record in outreach.iterrows():

        print("Recruiter:", record["recruiter_name"])
        print("Role:", record["role"])
        print("Match Score:", record["match_score"], "%")
        print("Status:", record["status"])
        print("Followup Date:", record["follow_up_date"])
        print("Response:", record["response"])
        print("-" * 50)


if __name__ == "__main__":
    create_follow_up_file()