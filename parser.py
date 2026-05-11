#!/usr/bin/env python3

ip_counter = {}

with open('test.log', 'r') as file:
    for line in file:
        if 'Failed password' in line:
            parts = line.strip().split()

            if "from" in parts:
                index = parts.index("from") + 1
                ip = parts[index]
                ip_counter[ip] = ip_counter.get(ip, 0) + 1
threshold = 5
print("\nPotential brute-force sources:\n")
for ip, count in ip_counter.items():
    if count >= threshold:
        print(f"{ip} failed to log in {count} times")

successful_logins = {}

with open('test.log', 'r') as file:
    for line in file:
        if 'Accepted password' in line:
            parts = line.strip().split()

            if "for" in parts:
                index = parts.index("for") + 1
                username = parts[index]
                successful_logins[username] = successful_logins.get(username, 0) + 1

print("\nSuccessful logins:\n")
for user, count in successful_logins.items():
    print(f"{user}: {count} successful logins")

sudo_commands = []

with open('test.log', 'r') as file:
    for line in file:
        if 'sudo' in line and 'COMMAND=' in line:
            command = line.split('COMMAND=')[1].strip()
            sudo_commands.append(command)
print("\nSudo commands executed:\n")
for command in sudo_commands:
    print(command)
