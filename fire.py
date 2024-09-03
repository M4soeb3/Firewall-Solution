import subprocess

def run_command(command):
    """Executes a shell command and returns the output."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

def enable_ufw():
    """Enable ufw firewall."""
    return run_command("sudo ufw enable")

def allow_service(service):
    """Allow a specific service through the firewall."""
    return run_command(f"sudo ufw allow {service}")

def deny_service(service):
    """Deny a specific service through the firewall."""
    return run_command(f"sudo ufw deny {service}")

def list_rules():
    """List all current ufw rules."""
    return run_command("sudo ufw status verbose")

def main():
    print("1. Enable ufw firewall")
    print("2. Allow a service")
    print("3. Deny a service")
    print("4. List current rules")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(enable_ufw())
    elif choice == '2':
        service = input("Enter the service to allow (e.g., ssh, http, 80/tcp): ")
        print(allow_service(service))
    elif choice == '3':
        service = input("Enter the service to deny (e.g., ftp, 21/tcp): ")
        print(deny_service(service))
    elif choice == '4':
        print(list_rules())
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

