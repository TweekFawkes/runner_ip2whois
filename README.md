# runner_ip2whois

This runner takes an IP address as input, finds the system's `whois` command, and executes it to perform a Whois lookup for that address.

## Usage

```bash
python app.py <IP_ADDRESS>
```

The script will:
1.  Check if the `whois` command is available in the system's PATH.
2.  Validate the basic format of the provided `<IP_ADDRESS>`.
3.  Execute `whois <IP_ADDRESS>` using the found `whois` executable.
4.  Print the standard output and standard error from the `whois` command.
5.  Exit with the return code of the `whois` command (or 1 if errors like command not found or timeout occur).

## Example Runner Configuration (`runner.yaml`)

- **Name:** IP to Whois (via Python script)
- **Description:** Uses a Python script to query via the system's Whois for the provided IP address.
- **Build:** Installs `python3` and the `whois` package (e.g., `apt install python3 whois`).
- **Input:** Requires an `ip_address` via a webform or environment variable.
- **Launch:** Executes `python app.py ${ip_address}`.