# runner_digx

## Runner Information

- **Name:** IP to Dig -x
- **Description:** Queries via Dig -x for the provided IP address.
- **Version:** 0.0.1

## Building the Runner

The build process updates the package list and installs the `dnsutils` package, which contains the `dig` command.

```bash
apt update
apt install -y dnsutils
```

## Running the Runner

This runner requires an IP address as input via a web form field named `ip_address`.

It executes the following command:

```bash
dig -x <provided_ip_address>
```