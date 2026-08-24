import pandas as pd


def detect_replies():

    print("=" * 60)
    print("RECRUITER REPLY TRACKING SYSTEM")
    print("=" * 60)

    file = "follow_up.csv"

    df = pd.read_csv(file)

    if "response" not in df.columns:
        df["response"] = "Pending"

    replied = df[
        df["response"].astype(str).str.lower() == "replied"
    ]

    pending = df[
        df["response"].astype(str).str.lower() == "pending"
    ]

    print()
    print("Total Recruiters:", len(df))
    print("Replies Detected:", len(replied))
    print("Pending Responses:", len(pending))

    if len(replied) > 0:

        print("\nReplied Recruiters:")

        for _, row in replied.iterrows():
            print(
                row["recruiter_name"],
                "|",
                row["recruiter_email"],
                "|",
                row["role"]
            )

    else:
        print("\nNo recruiter replies detected yet.")

    df.to_csv(
        file,
        index=False
    )

    print("\nReply tracking completed successfully.")


if __name__ == "__main__":
    detect_replies()