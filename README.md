# Log Analyzer

Python script that parses Linux authentication logs to detect security events and suspicious activity.

## What it does

- Detects failed login attempts (potential brute-force attacks)
- Flags IPs with 5+ failed login attempts as brute-force sources
- Tracks successful logins by user
- Lists sudo commands executed

## Usage

```bash
sudo ./parser.py
```

## Sample Output

```
================================
Initiating log analysis report
================================
Failed login attempts:

Potential brute-force sources:

192.168.1.100: 12 failed attempts
10.0.0.45: 8 failed attempts

Successful logins:

admin: 3 successful logins
root: 1 successful logins

Sudo commands executed:

/usr/bin/apt update
/bin/systemctl restart nginx
/usr/sbin/useradd admin
```

## Requirements

- Python 3.12.3
- Linux system with /var/log/auth.log
```

