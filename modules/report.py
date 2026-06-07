from modules.database import get_events
from datetime import datetime


def generate_report():

    events = get_events()

    report_path = "reports/security_report.txt"

    with open(report_path, "w") as report:

        report.write("=== CyberWSQK Security Report ===\n\n")

        report.write(
            f"Generated On: {datetime.now()}\n\n"
        )

        if not events:

            report.write("No Security Events Found\n")

        else:

            for event in events:

                report.write(
                    f"ID: {event[0]}\n"
                    f"Type: {event[1]}\n"
                    f"Severity: {event[2]}\n"
                    f"Message: {event[3]}\n"
                    f"Timestamp: {event[4]}\n"
                    "-------------------------\n"
                )

    return report_path