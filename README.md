# VulnShield - Deliberately Vulnerable Python Application

VulnShield is a Flask-based web application designed to benchmark security scanners like **CodeShield**. It contains intentional vulnerabilities across SCA, SAST, Secret Scanning, and DAST categories.

## ⚠️ WARNING
**DO NOT deploy this application in a production environment.** It is intentionally insecure and can lead to full system compromise if exposed to the internet.

## Vulnerabilities Included

### 1. SCA (Software Composition Analysis)
- Outdated `Flask`, `requests`, and `PyYAML` versions with known CVEs.

### 2. SAST (Static Application Security Testing)
- **SQL Injection**: In `app/models/user.py`.
- **Command Injection**: In `app/services/system.py`.
- **Insecure Deserialization**: Using `pickle` in `app/services/system.py`.
- **Dangerous Eval**: In `app/services/system.py`.
- **Weak Crypto**: MD5 hashing in `app/models/user.py`.
- **Hardcoded Credentials**: In `app/models/user.py` and `config/settings.py`.

### 3. Secret Scanning
- Hardcoded AWS Keys, GitHub Tokens, and Database passwords in `.env`, `config/settings.py`, and `logs/backup.json`.

### 4. DAST (Dynamic Application Security Testing)
- **Reflected XSS**: On the home page via the `name` parameter.
- **SQLi**: On the `/search` endpoint.
- **Command Injection**: On the `/ping` endpoint.
- **Path Traversal**: On the `/download` endpoint.
- **IDOR**: On the `/profile/<id>` endpoint.

## Deployment

### Using Docker
```bash
docker build -t vulnshield .
docker run -p 5000:5000 vulnshield
```

### Manual
```bash
pip install -r requirements.txt
python run.py
```
