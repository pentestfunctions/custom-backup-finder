import itertools
import re

# List of common archive names (excluding date-based)
archive_names = [
    "website_backup",
    "site_backup",
    "daily_backup",
    "weekly_backup",
    "monthly_backup",
    "full_backup",
    "incremental_backup",
    "database_backup",
    "files_backup",
    "server_backup",
    "web_backup",
    "public_html_backup",
    "www_backup",
    "backup_archive",
    "website_snapshot",
    "site_copy",
    "data_backup",
    "website_data",
    "html_backup",
    "mysql_backup",
    "postgres_backup",
    "sql_backup",
    "logs_backup",
    "config_backup",
    "assets_backup",
    "images_backup",
    "documents_backup",
    "code_backup",
    "media_backup",
    "content_backup",
    "system_backup",
    "resources_backup",
    "template_backup",
    "theme_backup",
    "plugins_backup",
    "modules_backup",
    "settings_backup",
    "backup_timestamp",
    "backup_v1",
    "backup_v2",
    "backup_production",
    "backup_staging",
    "backup_test",
    "backup_dev",
    "example_2024",
    "example_2024_full",
    "example_2024_daily",
    "example_2024_weekly",
    "example_2024_monthly",
    "example_2024_yearly",
    "example_2024_db",
    "example_2024_files",
    "example_2024_media",
    "example_2024_content",
    "example_backup",
    "example_full_backup",
    "example_db_backup",
    "example_files_backup",
    "example_media_backup",
    "example_content_backup",
    "backup_2024_example",
    "backup_2024_example_full",
    "backup_2024_example_daily",
    "backup_2024_example_weekly",
    "backup_2024_example_monthly",
    "backup_2024_example_yearly",
    "backup_2024_example_db",
    "backup_2024_example_files",
    "backup_2024_example_media",
    "backup_2024_example_content",
    "example_full",
    "example_daily",
    "example_weekly",
    "example_monthly",
    "example_yearly",
    "example_db",
    "example_files",
    "example_media",
    "example_content",
    "subdomain_example_2024",
    "subdomain_example_2024_full",
    "subdomain_example_2024_daily",
    "subdomain_example_2024_weekly",
    "subdomain_example_2024_monthly",
    "subdomain_example_2024_yearly",
    "subdomain_example_2024_db",
    "subdomain_example_2024_files",
    "subdomain_example_2024_media",
    "subdomain_example_2024_content",
    "subdomain_backup_2024_example",
    "subdomain_backup_2024_example_full",
    "subdomain_backup_2024_example_daily",
    "subdomain_backup_2024_example_weekly",
    "subdomain_backup_2024_example_monthly",
    "subdomain_backup_2024_example_yearly",
    "subdomain_backup_2024_example_db",
    "subdomain_backup_2024_example_files",
    "subdomain_backup_2024_example_media",
    "subdomain_backup_2024_example_content",
    "website_backup_example",
    "website_backup_example_full",
    "website_backup_example_daily",
    "website_backup_example_weekly",
    "website_backup_example_monthly",
    "website_backup_example_yearly",
    "website_backup_example_db",
    "website_backup_example_files",
    "website_backup_example_media",
    "website_backup_example_content",
    "site_backup_example",
    "site_backup_example_full",
    "site_backup_example_daily",
    "site_backup_example_weekly",
    "site_backup_example_monthly",
    "site_backup_example_yearly",
    "site_backup_example_db",
    "site_backup_example_files",
    "site_backup_example_media",
    "site_backup_example_content",
    "full_backup_example",
    "full_backup_example_com",
    "daily_backup_example",
    "daily_backup_example_com",
    "weekly_backup_example",
    "weekly_backup_example_com",
    "monthly_backup_example",
    "monthly_backup_example_com",
    "yearly_backup_example",
    "yearly_backup_example_com",
    "compressed_backup_example",
    "compressed_backup_example_com",
    "example_com_backup_daily",
    "example_com_backup_weekly",
    "example_com_backup_monthly",
    "example_com_backup_yearly",
    "example_com_backup_compressed",
    "subdomain_example_com_backup_daily",
    "subdomain_example_com_backup_weekly",
    "subdomain_example_com_backup_monthly",
    "subdomain_example_com_backup_yearly",
    "subdomain_example_com_backup_compressed",
    "full_example_com_backup_daily",
    "full_example_com_backup_weekly",
    "daily_example_com_backup",
]

# List of common file extensions
file_extensions = [
    ".zip",
    ".tar",
    ".tar.gz",
    ".tgz",
    ".tar.bz2",
    ".tar.xz",
    ".7z",
    ".rar",
    ".sql",
    ".bak",
    ".dump",
    ".gzip",
    ".bz2",
    ".gz",
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

# Apply replacements to archive names
new_archive_names = []
for name in archive_names:
    for old, new in replacements:
        name = name.replace(old, new)
    new_archive_names.append(name)

# Generate combinations of archive names and file extensions
all_combinations = [f"{name}{ext}" for name, ext in itertools.product(new_archive_names, file_extensions)]

# Save to a wordlist called custom_backupfinder.txt
with open("custom_backupfinder.txt", "w") as file:
    file.write("\n".join(all_combinations))

print("Wordlist saved to custom_backupfinder.txt")
