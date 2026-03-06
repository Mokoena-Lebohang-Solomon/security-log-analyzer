from collections import defaultdict

print("SECURITY LOG ANALYZER\n")

failed_attempts = defaultdict(int)

with open("sample_logs.txt", "r") as file:

    for line in file:

        if "Failed login attempt" in line:

            ip = line.split("IP:")[1].strip()

            failed_attempts[ip] += 1


print("Suspicious Activity Report\n")

for ip, count in failed_attempts.items():

    print("IP:", ip, "- Failed attempts:", count)

    if count >= 3:
        print("⚠ Possible brute-force attack detected!\n")
