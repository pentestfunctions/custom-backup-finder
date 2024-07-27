import itertools
import re
from datetime import datetime, timedelta, timezone

# List of common log names
log_names = [
    "access",
    "error",
    "debug",
    "info",
    "warn",
    "warning",
    "fatal",
    "security",
    "auth",
    "application",
    "system",
    "webserver",
    "app",
    "server",
    "request",
    "response",
    "transaction",
    "event",
    "service",
    "audit",
]

# List of common log file extensions
file_extensions = [
    ".log",
    ".txt",
    ".sql",
]

# Get user input
url = input("Enter the URL: ")

# Extract domain and subdomain
domain_pattern = r"https?://(www\.)?(?P<subdomain>[\w-]+\.)?(?P<domain>[\w-]+\.\w+)"
match = re.match(domain_pattern, url)

if not match:
    raise ValueError("Invalid URL format")

domain = match.group("domain")
subdomain = match.group("subdomain")[:-1] if match.group("subdomain") else f"www.{domain}"

# Generate domain variants
domain_without_tld = domain.split('.')[0]
subdomain_without_tld = subdomain.split('.')[0] if subdomain else domain_without_tld

# Create a list of domain and subdomain variants
replacements = [
    (f"example_com", domain.replace(".", "_")),
    (f"example.com", domain),
    (f"example_", f"{domain_without_tld}_"),
    (f"example_", f"{domain}_"),
    (f"subdomain_example_", f"{subdomain_without_tld}_") if subdomain else (f"subdomain_example_", f"{domain_without_tld}_"),
    (f"subdomain_example", subdomain_without_tld) if subdomain else (f"subdomain_example", domain_without_tld),
    (f"subdomain_", f"{subdomain_without_tld}_") if subdomain else (f"subdomain_", f"{domain_without_tld}_")
]

# Apply replacements to log names
new_log_names = []
for name in log_names:
    for old, new in replacements:
        name = name.replace(old, new)
    new_log_names.append(name)

# Generate date-based log filenames for the last 7 days with detailed timestamps
today = datetime.now(timezone.utc)
date_formats = ["%Y-%m-%d", "%Y%m%d", "%Y%m%d%H", "%Y%m%d%H%M"]

date_log_names = []
for i in range(7):
    base_date = today - timedelta(days=i)
    for fmt in date_formats:
        # Handle various time granularities
        for hour in range(24):  # Hourly granularity
            for minute in range(0, 60, 15):  # 15-minute intervals
                date_str = base_date.strftime(fmt)
                if "%H" in fmt and "%M" in fmt:
                    date_str += f"{hour:02}{minute:02}"
                elif "%H" in fmt:
                    date_str += f"{hour:02}"
                elif "%M" in fmt:
                    date_str += f"{minute:02}"
                date_log_names.extend([
                    f"{domain}_{date_str}.log",
                    f"{subdomain}_{date_str}.log",
                    f"{date_str}_log.txt",
                ])

# Combine standard log names with date-based names
all_log_names = new_log_names + date_log_names

# Generate combinations of log names and file extensions
all_combinations = [f"{name}{ext}" for name, ext in itertools.product(all_log_names, file_extensions)]

# Save to a wordlist called custom_logfinder.txt
with open("custom_logfinder.txt", "w") as file:
    file.write("\n".join(all_combinations))

print(f"Wordlist saved to custom_logfinder.txt with {len(all_combinations)} entries")
