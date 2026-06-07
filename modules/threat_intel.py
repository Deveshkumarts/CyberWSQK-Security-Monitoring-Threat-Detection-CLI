from modules.log_analyzer import analyze_logs


MALICIOUS_IPS = {
    "185.220.101.1": "Tor Exit Node",
    "45.95.147.236": "Known Brute Force Source",
    "103.145.13.91": "Malicious Scanner",
    "91.92.109.126": "SSH Brute Force Attacker",
    "198.251.89.47": "Suspicious Recon Activity"
}


def check_threats():

    result = analyze_logs()

    if isinstance(result, str):
        return result

    suspicious_ips = result["top_ips"]

    threats_found = []

    for ip, count in suspicious_ips:

        if ip in MALICIOUS_IPS:

            threats_found.append({
                "ip": ip,
                "reason": MALICIOUS_IPS[ip],
                "count": count
            })

    return threats_found