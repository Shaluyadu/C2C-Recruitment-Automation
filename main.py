import subprocess
import sys


def run_script(script_name):
    print("\n - main.py:6" + "=" * 60)
    print(f"RUNNING: {script_name} - main.py:7")
    print("= - main.py:8" * 60)

    result = subprocess.run(
        [sys.executable, script_name]
    )

    if result.returncode != 0:
        print(f"\nERROR: {script_name} failed. - main.py:15")
        return False

    print(f"\n{script_name} completed successfully. - main.py:18")
    return True


def main():

    print("= - main.py:24" * 60)
    print("C2C RECRUITMENT AUTOMATION SYSTEM - main.py:25")
    print("= - main.py:26" * 60)

    scripts = [
        "job_search.py",
        "resume_matcher.py",
        "outreach.py",
        "duplicate_checker.py",
        "follow_up.py",
        "reply_detector.py",
        "dashboard.py"
    ]

    for script in scripts:

        if not run_script(script):
            print("\nWorkflow stopped because an error occurred. - main.py:41")
            return

    print("\n - main.py:44" + "=" * 60)
    print("COMPLETE RECRUITMENT WORKFLOW FINISHED - main.py:45")
    print("= - main.py:46" * 60)


if __name__ == "__main__":
    main()