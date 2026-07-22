BRUTE_FORCE_THRESHOLD = 3
PORT_SCAN_THRESHOLD = 2


def detect_incident(event_counts):
    incidents = []

    for (event_type, target), count in event_counts.items():

        if event_type == "FAILED_LOGIN" and count >= BRUTE_FORCE_THRESHOLD:
            incidents.append({
                "type": "Brute Force Attack",
                "target": target,
                "severity": "HIGH",
                "action": "Block IP + Escalate SOC Tier 2",
                "evidence": f"{count} failed login attempts detected"
            })

        elif event_type == "PORT_SCAN" and count >= PORT_SCAN_THRESHOLD:
            incidents.append({
                "type": "Port Scanning Activity",
                "target": target,
                "severity": "MEDIUM",
                "action": "Monitor + Firewall Rule Update",
                "evidence": f"{count} port scan events detected"
            })

        elif event_type == "MALWARE_DETECTED":
            incidents.append({
                "type": "Malware Detection",
                "target": target,
                "severity": "CRITICAL",
                "action": "Isolate Machine Immediately",
                "evidence": f"{count} malware detection events recorded"
            })

    return incidents