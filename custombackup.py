import itertools
import re
from typing import List, Tuple, Set
from datetime import datetime, timedelta
import hashlib

class BackupFileGenerator:
    def __init__(self):
        self.current_date = datetime.now()
        
        # Common real-world backup terms
        self.backup_terms = {
            'backup', 'bak', 'old', 'new', 'temp',
            'copy', 'migration', 'migrate', 'transfer',
            'snapshot', 'clone', 'archive', 'export',
            'dump', 'save', 'stored', 'latest'
        }
        
        # Common version and status indicators
        self.version_indicators = {
            'old', 'new', '1', '2', 'orig', 'original',
            'latest', 'final', 'live', 'dev', 'development',
            'prod', 'production', 'staging', 'stage', 'test',
            'v1', 'v2', 'v3', 'ver1', 'ver2', 'pre', 'post'
        }
        
        # Real-world file extensions
        self.file_extensions = {
            # Most common archives
            '.zip', '.tar.gz', '.sql.gz', '.sql',
            # Database dumps
            '.sql', '.mysql', '.mysqldump',
            # Common compressions
            '.gz', '.tgz', '.tar',
            # Backup extensions
            '.bak', '.backup', '.old', '.save',
            # Temporary files
            '.tmp', '.temp', '.bk',
            # Common mistakes/incomplete transfers
            '.part', '.partial', '.temp_zip'
        }
        
        # Date format patterns seen in real backups
        self.date_formats = [
            '%Y%m%d',           # 20240308
            '%Y-%m-%d',         # 2024-03-08
            '%d%m%Y',           # 08032024
            '%m%d%Y',           # 03082024
            '%Y%m%d-%H%M',      # 20240308-1530 (common in automated backups)
            '%d-%m-%Y',         # 08-03-2024
            '%Y_%m_%d',         # 2024_03_08
        ]
        
        # Common CMS and platform patterns
        self.cms_patterns = {
            # WordPress specific
            'wp-content', 'wp-config', 'wordpress', 'wp', 'wpress',
            'wpbackup', 'wp-backup', 'wp-db', 'wp-files',
            'wordpress-backup', 'wordpress-db', 'wordpress-files',
            # BackupBuddy specific
            'backup-', 'backupbuddy', 'pb_backupbuddy',
            # UpdraftPlus specific
            'updraft', 'updraftplus', 'updraft_backup',
            # All-in-One WP Migration
            'ai1wm-backups', 'ai1wm', 'wpress',
            # WP Migrate DB
            'wp-migrate-db', 'migrate',
            # Duplicator patterns
            'dup-installer', 'dup-backup', 'duplicator',
            # ManageWP patterns
            'managewp', 'mwp',
            # MainWP patterns
            'mainwp', 'mainwp-backup',
            # Common CMS
            'drupal', 'joomla', 'magento', 'opencart',
            # Generic but common
            'public_html', 'www', 'html', 'site', 'web',
            'httpdocs', 'httpsdocs', 'private_html'
        }

        # Common hosting panel patterns
        self.hosting_patterns = {
            # cPanel patterns
            'cpanel', 'cpmove', 'cpbackup', 'home_dir',
            'public_ftp', 'access-logs', 'bandwidth-logs',
            # Plesk patterns
            'plesk', 'pleskbackup', 'domain_backup',
            # DirectAdmin patterns
            'directadmin', 'da_backup', 'user_backup',
            # Common hosting paths
            'vhosts', 'domains', 'subdomains', 'clients',
            'hosting', 'host', 'main', 'root'
        }

        # Database backup patterns
        self.db_patterns = {
            # MySQL patterns
            'mysql', 'mysqldump', 'sql', 'database',
            'db_backup', 'db-backup', 'db_dump', 'db-dump',
            # Common prefixes/suffixes
            'backup_db', 'backup-db', 'dump_db', 'dump-db',
            # Version indicators
            'db_v1', 'db_v2', 'db_old', 'db_new',
            # Date indicators
            'db_latest', 'db_daily', 'db_weekly',
            # Common mistakes
            'dump', 'sqldump', 'sql_dump', 'dbdump'
        }

    def parse_url(self, url: str) -> Tuple[str, str]:
        """Parse URL to extract domain and subdomain."""
        domain_pattern = r"https?://(www\.)?(?P<subdomain>[\w-]+\.)?(?P<domain>[\w-]+\.\w+)"
        match = re.match(domain_pattern, url)
        
        if not match:
            raise ValueError("Invalid URL format")
            
        domain = match.group("domain")
        subdomain = match.group("subdomain")[:-1] if match.group("subdomain") else None
        
        return domain, subdomain

    def generate_domain_variants(self, domain: str, subdomain: str = None) -> Set[str]:
        """Generate real-world domain variants."""
        variants = set()
        domain_parts = domain.split('.')
        domain_name = domain_parts[0]
        tld = domain_parts[-1]
        
        # Basic domain variants
        variants.update([
            domain_name,                    # example
            domain.replace('.', '_'),       # example_com
            domain.replace('.', '-'),       # example-com
            f"www_{domain_name}",          # www_example
            f"{domain_name}_{tld}",        # example_com
            domain,                         # example.com
        ])
        
        if subdomain and subdomain != 'www':
            subdomain_clean = subdomain.split('.')[0]
            variants.update([
                subdomain_clean,                    # sub
                f"{subdomain_clean}_{domain_name}", # sub_example
                f"{subdomain_clean}-{domain_name}", # sub-example
                f"{domain_name}_{subdomain_clean}", # example_sub
                f"{domain_name}-{subdomain_clean}"  # example-sub
            ])
        
        return variants

    def generate_cms_specific_patterns(self, domain_var: str) -> Set[str]:
        """Generate CMS-specific backup patterns."""
        patterns = set()
        
        # WordPress backup plugin patterns
        wp_patterns = [
            # UpdraftPlus patterns
            f"updraft_{domain_var}",
            f"updraft_backup_{domain_var}",
            f"{domain_var}_updraft",
            f"{domain_var}_updraftplus",
            
            # BackupBuddy patterns
            f"backup_{domain_var}_backupbuddy",
            f"pb_backupbuddy_{domain_var}",
            f"{domain_var}_backupbuddy",
            
            # All-in-One WP Migration
            f"ai1wm-{domain_var}",
            f"{domain_var}.wpress",
            f"{domain_var}-migrate",
            
            # Duplicator patterns
            f"duplicator-pro_{domain_var}",
            f"dup-installer_{domain_var}",
            f"{domain_var}_duplicator",
            f"dup-backup_{domain_var}",
            
            # ManageWP patterns
            f"managewp_{domain_var}",
            f"{domain_var}_mwp",
            
            # MainWP patterns
            f"mainwp_{domain_var}",
            f"{domain_var}_mainwp",
            
            # WP default patterns
            f"{domain_var}_wp_content",
            f"wp-content_{domain_var}",
            f"{domain_var}_wordpress",
            f"wordpress_{domain_var}"
        ]
        
        patterns.update(wp_patterns)
        return patterns

    def generate_hosting_patterns(self, domain_var: str) -> Set[str]:
        """Generate hosting-specific backup patterns."""
        patterns = set()
        
        hosting_patterns = [
            # cPanel patterns
            f"backup.{domain_var}",
            f"cpmove_{domain_var}",
            f"cpanel_{domain_var}",
            f"{domain_var}_cpanel",
            f"backup_{domain_var}_cpanel",
            
            # Plesk patterns
            f"plesk_{domain_var}",
            f"{domain_var}_plesk",
            f"domain_backup_{domain_var}",
            
            # DirectAdmin patterns
            f"directadmin_{domain_var}",
            f"{domain_var}_da_backup",
            f"user_backup_{domain_var}",
            
            # Common hosting patterns
            f"vhost_{domain_var}",
            f"domain_{domain_var}",
            f"client_{domain_var}",
            f"hosting_{domain_var}",
            f"{domain_var}_hosting",
            f"{domain_var}_backup",
            f"backup_{domain_var}",
            
            # Migration patterns
            f"{domain_var}_migration",
            f"migration_{domain_var}",
            f"{domain_var}_transfer",
            f"transfer_{domain_var}",
            
            # Temporary patterns
            f"{domain_var}_temp",
            f"temp_{domain_var}",
            f"{domain_var}_tmp",
            f"tmp_{domain_var}"
        ]
        
        patterns.update(hosting_patterns)
        return patterns

    def generate_database_patterns(self, domain_var: str) -> Set[str]:
        """Generate database-specific backup patterns."""
        patterns = set()
        
        db_patterns = [
            # MySQL dumps
            f"{domain_var}_mysqldump",
            f"mysqldump_{domain_var}",
            f"{domain_var}_mysql",
            f"mysql_{domain_var}",
            
            # Generic database backups
            f"{domain_var}_db",
            f"db_{domain_var}",
            f"{domain_var}_database",
            f"database_{domain_var}",
            f"{domain_var}_sql",
            f"sql_{domain_var}",
            
            # Common variations
            f"{domain_var}_db_backup",
            f"db_backup_{domain_var}",
            f"{domain_var}_dump",
            f"dump_{domain_var}",
            
            # Version indicators
            f"{domain_var}_db_v1",
            f"{domain_var}_db_v2",
            f"{domain_var}_db_old",
            f"{domain_var}_db_new",
            
            # Date indicators
            f"{domain_var}_db_latest",
            f"{domain_var}_db_daily",
            f"{domain_var}_db_weekly"
        ]
        
        patterns.update(db_patterns)
        return patterns

    def generate_real_world_dates(self) -> Set[str]:
        """Generate date patterns commonly found in backups."""
        dates = set()
        
        # Generate dates for today and recent past (most common in real backups)
        for days in [0, 1, 7, 14, 30]:  # Today, yesterday, week ago, 2 weeks ago, month ago
            date = self.current_date - timedelta(days=days)
            for date_format in self.date_formats:
                try:
                    dates.add(date.strftime(date_format))
                except ValueError:
                    continue
        
        # Add just the year and year-month (common in archive names)
        dates.add(self.current_date.strftime('%Y'))  # 2024
        dates.add(self.current_date.strftime('%Y%m'))  # 202403
        
        # Add some common manual date formats
        current_year = self.current_date.strftime('%Y')
        current_month = self.current_date.strftime('%m')
        dates.update([
            current_year,           # 2024
            f"{current_year}{current_month}",  # 202403
            f"{current_year}-{current_month}"  # 2024-03
        ])
        
        return dates

    def generate_patterns(self, domain_variants: Set[str]) -> Set[str]:
        """Generate comprehensive backup patterns."""
        patterns = set()
        dates = self.generate_real_world_dates()
        
        for domain_var in domain_variants:
            # Add CMS-specific patterns
            patterns.update(self.generate_cms_specific_patterns(domain_var))
            
            # Add hosting patterns
            patterns.update(self.generate_hosting_patterns(domain_var))
            
            # Add database patterns
            patterns.update(self.generate_database_patterns(domain_var))
            
            # Add date-based patterns
            for date in dates:
                patterns.update([
                    f"{domain_var}_{date}",
                    f"{date}_{domain_var}",
                    f"backup_{domain_var}_{date}",
                    f"{domain_var}_backup_{date}",
                    f"{domain_var}_{date}_backup",
                    f"db_{domain_var}_{date}",
                    f"{domain_var}_db_{date}"
                ])
            
            # Add version-based patterns
            for version in self.version_indicators:
                patterns.update([
                    f"{domain_var}_{version}",
                    f"{version}_{domain_var}",
                    f"backup_{domain_var}_{version}",
                    f"{domain_var}_backup_{version}"
                ])
            
            # Add common manual backup patterns
            for term in self.backup_terms:
                patterns.update([
                    f"{domain_var}_{term}",
                    f"{term}_{domain_var}",
                    f"{domain_var}_{term}_backup",
                    f"backup_{domain_var}_{term}"
                ])

        return patterns

    def generate_wordlist(self, url: str, output_file: str = "custom_backupfinder.txt") -> None:
        """Generate and save the optimized wordlist."""
        try:
            domain, subdomain = self.parse_url(url)
            domain_variants = self.generate_domain_variants(domain, subdomain)
            patterns = self.generate_patterns(domain_variants)
            
            # Generate final combinations with extensions
            combinations = set()
            for pattern in patterns:
                # Add pattern without extension
                combinations.add(pattern)
                # Add patterns with extensions
                for ext in self.file_extensions:
                    combinations.add(f"{pattern}{ext}")
            
            # Write unique patterns
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(sorted(combinations)))
            
            print(f"Generated {len(combinations)} optimized backup patterns")
            print(f"Wordlist saved to {output_file}")
            
        except Exception as e:
            print(f"Error generating wordlist: {str(e)}")

def main():
    generator = BackupFileGenerator()
    url = input("Enter the URL (e.g., https://example.com): ").strip()
    generator.generate_wordlist(url)

if __name__ == "__main__":
    main()
