import itertools

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

# Function to split domain into base and TLD
def split_domain(domain):
    parts = domain.rsplit('.', 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    return domain, ''  # No TLD found

# Get the domain input from the user
domain_input = input("Enter the domain name (e.g., example.com): ")
domain, tld = split_domain(domain_input)

# Custom domain variations
domain_variations = [
    f"{domain}_{tld}",  # domain_tld
    f"{domain}{tld}",   # domaintld
]

# Customized permutations for the given domain
custom_permutations = []
for variation in domain_variations:
    for ext in file_extensions:
        # Add domain variations with and without common archive names
        custom_permutations.append(f"{variation}{ext}")
        for name in archive_names:
            custom_permutations.append(f"{variation}_{name}{ext}")

# Generate permutations of common archive names and file extensions
common_permutations = itertools.product(archive_names, file_extensions)

# Generate permutations with real dates
date_permutations = [
    f"backup_{year:04d}{month:02d}{day:02d}{ext}"
    for year in range(2022, 2023)
    for month in range(1, 13)
    for day in range(1, 31)
    for ext in file_extensions
]

# Output the generated permutations to a file
with open("custom_backup_list.txt", "w") as file:
    for name, extension in common_permutations:
        file.write(f"{name}{extension}\n")

    for date in date_permutations:
        file.write(f"{date}\n")

    for custom_name in custom_permutations:
        file.write(f"{custom_name}\n")

print("Permutations have been written to custom_backup_list.txt.")
