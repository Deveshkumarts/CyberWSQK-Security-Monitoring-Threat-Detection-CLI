from modules.monitor import get_system_stats
from modules.ports import get_open_ports
from modules.log_analyzer import analyze_logs
from modules.database import get_events


def show_dashboard():

    stats = get_system_stats()
    ports = get_open_ports()
    logs = analyze_logs()
    events = get_events()

    dashboard = (
        "\n"
        "=================================\n"
        "        CyberWSQK Dashboard\n"
        "=================================\n\n"

        "System Status\n"
        "-------------\n"
        f"CPU Usage       : {stats['cpu']}%\n"
        f"RAM Usage       : {stats['ram']}%\n"
        f"Disk Usage      : {stats['disk']}%\n"
        f"Processes       : {stats['processes']}\n\n"

        "Network\n"
        "-------\n"
        f"Open Ports      : {len(ports)}\n\n"

        "Security\n"
        "--------\n"
        f"Failed SSH      : {logs['failed']}\n"
        f"Invalid Users   : {logs['invalid']}\n\n"

        "Database\n"
        "--------\n"
        f"Stored Events   : {len(events)}\n\n"

        "================================="
    )

    return dashboard