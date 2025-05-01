import argparse
# import socket # Removed unused import
import sys
import shutil # Add shutil import
import subprocess # Add subprocess import

### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ###

# get_cymru_whois_info function removed

### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ###

def main():
    parser = argparse.ArgumentParser(description="Lookup IP Address ASN and BGP info using the system 'whois' command.") # Updated description
    # Use a positional argument for the IP address
    parser.add_argument('ip_address', help='IP Address to Get Information For')
    args = parser.parse_args()

    ip_address = args.ip_address

    # Basic IP format validation (optional but recommended)
    # Add more robust validation if needed (e.g., using ipaddress module)
    if '.' not in ip_address and ':' not in ip_address:
         print(f"[!] Error: '{ip_address}' does not look like a valid IPv4 or IPv6 address.", file=sys.stderr)
         return 1

    # Check if the 'whois' command is available
    whois_path = shutil.which("whois")
    if whois_path:
        print(f"[*] Found 'whois' executable at: {whois_path}")
        # Optionally call the system 'whois' command here
        print(f"[*] Running system 'whois' command for {ip_address}...")
        try:
            process = subprocess.run(
                [whois_path, ip_address],
                capture_output=True,
                text=True,
                check=False, # Don't raise exception on non-zero exit code
                timeout=30 # Add a timeout (e.g., 30 seconds)
            )
            print("--- System WHOIS Output ---")
            if process.stdout:
                print("[Stdout]")
                print(process.stdout.strip())
            if process.stderr:
                print("[Stderr]")
                print(process.stderr.strip())
            if process.returncode != 0:
                print(f"[!] System 'whois' command exited with code: {process.returncode}")
            print("---------------------------")
            # Return the exit code of the whois command itself, or 0 if successful
            return process.returncode

        except subprocess.TimeoutExpired:
             print(f"[!] Error: System 'whois' command timed out for {ip_address}", file=sys.stderr)
             return 1 # Indicate failure
        except Exception as e:
             print(f"[!] Error running system 'whois' command: {e}", file=sys.stderr)
             return 1 # Indicate failure

    else:
        # If whois command is not found, print error and exit
        print("[!] Error: 'whois' command not found in system PATH.", file=sys.stderr)
        return 1 # Indicate failure

### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ###

if __name__ == "__main__":
    # Use sys.exit() to ensure the exit code is propagated correctly
    sys.exit(main())