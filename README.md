# runner_whois

This runner takes an IP address as input and performs a Whois lookup for that address.

## Configuration (`runner.yaml`)

- **Name:** IP to Whois
- **Description:** Queries via Whois for the provided IP address.
- **Build:** Installs the `whois` package using `apt`.
- **Input:** Requires an `ip_address` via a webform.
- **Launch:** Executes the `whois` command with the provided IP address.