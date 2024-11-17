# Automated Cron Jobs

## Cron Tasks

1. **Delete Files from Temporary Directory:**
   - **Schedule:** Every day at 2:00 AM
   - **Command:**
     ```bash
     0 2 * * * rm -rf /path/to/home/temp/*
     ```

2. **Backup Home Directory:**
   - **Schedule:** Every Sunday at 3:00 AM
   - **Command:**
     ```bash
     0 3 * * 0 tar -czf /path/to/backup/home_backup_$(date +\%Y\%m\%d).tar.gz /path/to/home/
     ```

3. **Daily Disk Usage Report:**
   - **Schedule:** Every day at 8:30 AM
   - **Command:**
     ```bash
     30 8 * * * df -h | mail -s "Daily Disk Usage Report" your_email@example.com
     ```

