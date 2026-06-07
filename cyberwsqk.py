import typer
from modules.monitor import get_system_stats
from modules.ports import get_open_ports
from modules.ssh_monitor import check_ssh
from modules.database import get_events
from modules.report import generate_report
from modules.log_analyzer import analyze_logs
from modules.dashboard import show_dashboard
from modules.threat_intel import check_threats
from modules.web_scanner import scan_website

app = typer.Typer()


@app.command()
def monitor():
    """System Monitoring"""

    stats = get_system_stats()

    print("\n=== CyberWSQK System Monitor ===\n")

    print(f"CPU Usage      : {stats['cpu']}%")
    print(f"RAM Usage      : {stats['ram']}%")
    print(f"Disk Usage     : {stats['disk']}%")
    print(f"Processes      : {stats['processes']}")
    print(f"Boot Time      : {stats['boot_time']}")


@app.command()
def ports():

    open_ports = get_open_ports()

    print("\n=== CyberWSQK Port Monitor ===\n")

    print("Port      Status")
    print("----------------")

    for port in open_ports:
        print(f"{port:<10} LISTEN")

    print(f"\nTotal Open Ports: {len(open_ports)}")


@app.command()
def ssh():
    """SSH Security Monitoring"""

    result = check_ssh()

    print("\n=== CyberWSQK SSH Monitor ===\n")

    print(result)


@app.command()
def events():

    print("\n=== Stored Security Events ===\n")

    events_list = get_events()

    if not events_list:
        print("No Events Found")
        return

    for event in events_list:
        print(event)


@app.command()
def report():

    path = generate_report()

    print(f"\nReport Generated: {path}")


@app.command()
def logs():

    result = analyze_logs()

    if isinstance(result, str):
        print(result)
        return

    print("\n=== CyberWSQK Log Analysis ===\n")

    print(f"Failed Logins      : {result['failed']}")
    print(f"Successful Logins  : {result['success']}")
    print(f"Invalid Users      : {result['invalid']}")

    print("\nTop Suspicious IPs\n")

    if not result["top_ips"]:
        print("No suspicious IPs found")

    else:
        for ip, count in result["top_ips"]:
            print(f"{ip} -> {count} events")


@app.command()
def dashboard():

    print(show_dashboard())    


@app.command()
def intel():

    threats = check_threats()

    print("\n=== CyberWSQK Threat Intelligence ===\n")

    if isinstance(threats, str):
        print(threats)
        return

    if not threats:
        print("No Known Malicious IPs Found")
        return

    print(f"{'IP Address':<20}{'Threat'}")
    print("-" * 50)

    for threat in threats:

        print(
            f"{threat['ip']:<20}"
            f"{threat['reason']}"
        )    


@app.command()
def webscan(url: str):

    result = scan_website(url)

    if "error" in result:

        print(result["error"])
        return

    print("\n=== CyberWSQK Web Scanner ===\n")

    print("Security Headers")
    print("----------------")

    for header, status in result["headers"].items():

        print(f"{header}: {status}")

    print("\nTechnology Stack")
    print("----------------")

    if result["technologies"]:

        for tech in result["technologies"]:

            print(tech)

    else:

        print("Not Detected")

    print("\nSSL/TLS Information")
    print("-------------------")

    ssl_info = result["ssl"]

    if "error" not in ssl_info:

        print(
            f"TLS Version : {ssl_info['version']}"
        )

        print(
            f"Expiry Date : {ssl_info['expires']}"
        )

    else:

        print(ssl_info["error"])

    print("\nHTTP Methods")
    print("------------")

    if result["methods"]:

        for method in result["methods"]:

            print(method)

    else:

        print("Could not detect")

    print("\nSecurity Score")
    print("--------------")

    print(f"{result['score']}/100")           
if __name__ == "__main__":
    app()
