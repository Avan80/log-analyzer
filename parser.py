#!/usr/bin/env python3

ip_counter = {}

with open('test.log', 'r') as file:
    for line in file:
        if 'Failed password' in line:
            print(line.strip().split())
            parts = line.strip().split()

            if "from" in parts:
                index = parts.index("from") + 1
                ip = parts[index]
                if  ip not in ip_counter:
                    ip_counter[ip] = 1
                else:
                    ip_counter[ip] += 1
threshold = 5
print("\nPotential brute-force sources \n")
for ip, count in ip_counter.items():
    if count >= threshold:
        print(f"{ip} failed to log in {count} times")
