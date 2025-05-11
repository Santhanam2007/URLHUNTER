# ⚔️ URLHunter - Recon Juice Extractor for Bug Bounty & Pentesters

URLHunter is a custom recon triage tool built to automatically extract high-signal URLs from recon dumps.

## 🚀 Features
- Filters URLs for XSS, SQLi, Open Redirect, LFI potential
- Detects legacy tech: .swf, .xap, etc.
- Finds broken endpoints (403, 404)
- Outputs sorted files
- Includes basic payload injection module

## 📦 Requirements
```bash
pip install requests
```

## 🧪 Usage

```bash
python3 urlhunter.py -i input/live-urls.txt
```

Output files will be saved in the `output/` directory.

## 💥 Payload Injector

```bash
python3 payload_injector.py
```

## 📄 License
MIT License
