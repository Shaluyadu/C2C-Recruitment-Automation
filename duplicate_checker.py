import pandas as pd


def check_duplicates():

    print("=" * 60)
    print("DUPLICATE RECRUITER CHECK SYSTEM")
    print("=" * 60)

    file = "outreach.csv"

    df = pd.read_csv(file)

    if "recruiter_email" not in df.columns:
        print("Error: recruiter_email column not found.")
        return

    before = len(df)

    df["duplicate"] = df.duplicated(
        subset=["recruiter_email"],
        keep="first"
    )

    duplicates = df[df["duplicate"] == True]

    print()
    print("Total Outreach Records:", before)
    print("Duplicate Records Found:", len(duplicates))

    if len(duplicates) > 0:
        print()
        print("Duplicate Recruiters:")

        for _, row in duplicates.iterrows():
            print(
                row["recruiter_name"],
                "|",
                row["recruiter_email"]
            )
    else:
        print("No duplicate recruiter records found.")

    df.to_csv("outreach.csv", index=False)

    print()
    print("Duplicate check completed successfully.")


if __name__ == "__main__":
    check_duplicates()