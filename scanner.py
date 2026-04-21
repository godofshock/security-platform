import subprocess

def run_scan(target):
    print(f"[+] Scanning {target}...\n")

    result = subprocess.run(
        ["nmap", "-sV", target],
        capture_output=True,
        text=True
    )

    print(result.stdout)

if __name__ == "__main__":
    target = input("Enter target IP: ")
    run_scan(target)
