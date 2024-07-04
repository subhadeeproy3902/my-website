import os
from datetime import datetime, timedelta

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 2, 24)

delta = end_date - start_date

for i in range(delta.days + 1):
    commit_date = start_date + timedelta(days=i)
    formatted_date = commit_date.strftime("%a %b %d %H:%M:%S %Y -0600")
    
    filename = f"commit_{commit_date.strftime('%Y%m%d')}.txt"
    with open(filename, 'w') as file:
        file.write(f"Commit for {commit_date.strftime('%Y-%m-%d')}\n")
    
    os.system(f'git add {filename}')
    os.system(f'git commit --date="{formatted_date}" -m "Commit for {commit_date.strftime("%Y-%m-%d")}"')
    os.system(f'git commit --amend --no-edit --date="{formatted_date}"')

print("Backdated commits created successfully.")
