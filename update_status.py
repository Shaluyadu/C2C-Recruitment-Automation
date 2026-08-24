import pandas as pd


def update_status():

    print("RECRUITER STATUS UPDATE SYSTEM - update_status.py:6")
    print("= - update_status.py:7" * 40)

    file_name = "follow_up.csv"

    df = pd.read_csv(file_name)

    print()
    print("Available Recruiters: - update_status.py:14")
    print()

    for index, row in df.iterrows():
        print(
            f"{index + 1}. "
            f"{row['recruiter_name']} | "
            f"{row['role']} | "
            f"Status: {row['status']}"
        )

    print()

    try:
        choice = int(
            input("Enter recruiter number: ")
        )

        index = choice - 1

        if index < 0 or index >= len(df):
            print("Invalid recruiter number. - update_status.py:35")
            return

    except ValueError:
        print("Please enter a valid number. - update_status.py:39")
        return

    print()
    print("Available Status: - update_status.py:43")
    print("1. Draft - update_status.py:44")
    print("2. Sent - update_status.py:45")
    print("3. Followup - update_status.py:46")
    print("4. Replied - update_status.py:47")

    print()

    status_choice = input(
        "Enter status number: "
    )

    status_map = {
        "1": "Draft",
        "2": "Sent",
        "3": "Follow-up",
        "4": "Replied"
    }

    if status_choice not in status_map:
        print("Invalid status. - update_status.py:63")
        return

    new_status = status_map[status_choice]

    df.loc[index, "status"] = new_status

    if new_status == "Replied":
        response = input(
            "Enter response (e.g. Interested, Not Interested): "
        )

        df.loc[index, "response"] = response

    elif new_status == "Sent":
        df.loc[index, "response"] = "Pending"

    elif new_status == "Follow-up":
        df.loc[index, "response"] = "Pending"

    else:
        df.loc[index, "response"] = "Pending"

    df.to_csv(
        file_name,
        index=False
    )

    print()
    print("Status updated successfully! - update_status.py:92")
    print(
        "Recruiter:",
        df.loc[index, "recruiter_name"]
    )
    print(
        "New Status:",
        df.loc[index, "status"]
    )


if __name__ == "__main__":
    update_status()