import os
from modules.database import save_event


def check_ssh():

    log_file = "/var/log/auth.log"

    if not os.path.exists(log_file):
        return "SSH Log File Not Found"

    failed_logins = 0
    successful_logins = 0
    invalid_users = 0

    with open(log_file, "r", errors="ignore") as file:

        for line in file:

            if "Failed password" in line and "sshd" in line:
                failed_logins += 1

            if (
                "Accepted password" in line
                or "Accepted publickey" in line
            ) and "sshd" in line:
                successful_logins += 1

            if "Invalid user" in line and "sshd" in line:
                invalid_users += 1

    alert = ""

    if failed_logins >= 10:

        alert = "\n[ALERT] Possible SSH Brute Force Attack Detected"

        save_event(
            "SSH",
            "HIGH",
            "Possible SSH Brute Force Attack"
        )

    elif invalid_users >= 5:

        alert = "\n[ALERT] Multiple Invalid User Attempts Detected"

        save_event(
            "SSH",
            "MEDIUM",
            "Multiple Invalid User Attempts"
        )

    else:

        alert = "\n[INFO] No Suspicious SSH Activity Detected"

    return (
        f"Failed Logins     : {failed_logins}\n"
        f"Successful Logins : {successful_logins}\n"
        f"Invalid Users     : {invalid_users}\n"
        f"{alert}"
    )