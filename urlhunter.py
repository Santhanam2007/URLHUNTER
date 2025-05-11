import os
import re
import argparse

# Define extensions
DYNAMIC_EXTENSIONS = ['.php', '.asp', '.aspx', '.jsp', '.cgi', '.cfm', '.shtml']
LEGACY_FILES = ['.swf', '.xap', '.flv', '.webm', '.mp4', '.mp3']

# Prepare folder
os.makedirs("output", exist_ok=True)

# Parse arguments
parser = argparse.ArgumentParser(description="URLHunter - Advanced URL Sorter for Recon & Bug Bounty")
parser.add_argument("-i", "--input", required=True, help="Path to input file (e.g. live-urls.txt)")
args = parser.parse_args()

# Read input
with open(args.input, "r") as f:
    lines = f.readlines()

# Init buckets
param_urls, dynamic_urls, legacy_urls, error_urls = [], [], [], []

for line in lines:
    line = line.strip()
    if not line or not line.startswith("http"):
        continue

    url_only = line.split()[0]
    status = None

    # Extract status code
    match = re.search(r"\[(\d{3})\]", line)
    if match:
        status = int(match.group(1))

    # Bucket 1: Param URLs
    if "?" in url_only:
        param_urls.append(url_only)

    # Bucket 2: Dynamic Ext URLs
    if any(ext in url_only.lower() for ext in DYNAMIC_EXTENSIONS):
        dynamic_urls.append(url_only)

    # Bucket 3: Legacy Tech URLs
    if any(ext in url_only.lower() for ext in LEGACY_FILES):
        legacy_urls.append(url_only)

    # Bucket 4: Error Codes
    if status in [403, 404]:
        error_urls.append(url_only)

# Write outputs
def save_to_file(name, data):
    path = f"output/{name}.txt"
    with open(path, "w") as f:
        for url in sorted(set(data)):
            f.write(url + "\n")
    print(f"[+] Saved: {path} ({len(data)} URLs)")

save_to_file("params", param_urls)
save_to_file("dynamic", dynamic_urls)
save_to_file("legacy", legacy_urls)
save_to_file("errors", error_urls)

print("\n✅ Done. All URLs categorized into the 'output/' folder.\n")