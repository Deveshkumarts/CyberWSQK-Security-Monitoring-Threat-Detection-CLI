import os
import re


def analyze_logs():

    log_file = "/var/log/auth.log"

    if not os.path.exists(log_file):
        return "auth.log not found"

    failed = 0
    success = 0
    invalid = 0

    ip_counter = {}

    with open(log_file, "r", errors="ignore") as file:

        for line in file:

            # Failed SSH Login
            if "Failed password" in line and "sshd" in line:
                failed += 1

            # Successful SSH Login
            if (
                "Accepted password" in line
                or "Accepted publickey" in line
            ) and "sshd" in line:
                success += 1

            # Invalid User Attempt
            if "Invalid user" in line and "sshd" in line:
                invalid += 1

            # Extract IPv4 Address
            ip_match = re.search(
                r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
                line
            )

            if ip_match:

                ip = ip_match.group()

                # Ignore localhost
                if ip == "127.0.0.1":
                    continue

                if ip not in ip_counter:
                    ip_counter[ip] = 0

                ip_counter[ip] += 1

    top_ips = sorted(
        ip_counter.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    return {
        "failed": failed,
        "success": success,
        "invalid": invalid,
        "top_ips": top_ips
    }