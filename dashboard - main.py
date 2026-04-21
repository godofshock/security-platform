print("=== Security Platform ===")
print("1. Run Scanner")
print("2. Monitor Network")
print("3. Simulate Attack")

choice = input("Select option: ")

if choice == "1":
    import os
    os.system("python ../scanner/scanner.py")

elif choice == "2":
    import os
    os.system("python ../monitor/monitor.py")

elif choice == "3":
    import os
    os.system("python ../attacker/simulate_attack.py")
