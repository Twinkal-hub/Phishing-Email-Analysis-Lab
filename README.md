# Phishing-Email-Analysis-Lab

## Overview

This project demonstrates phishing email analysis using Python to identify Indicators of Compromise (IOCs), classify threats, and document findings. The objective is to simulate a SOC analyst investigation workflow and detect phishing characteristics within suspicious emails.


## Objective

Analyze a suspicious email to identify phishing indicators and assess the threat.


## Tools Used

- Python 3
- VS Code
- Windows PowerShell
- GitHub
- MITRE ATT&CK Framework


## Project Structure

```text
Phishing-Email-Analysis-Lab
│
├── reports
│     └── phishing-analysis-report.md
│
├── samples
│     └── phishing-email.txt
│
├── screenshots
│     └── email-analysis-output.png
│
├── email-analyzer.py
├── README.md
└── LICENSE
```


## Python Email Analyzer

The Python script performs:

- Email header extraction
- Sender analysis
- URL extraction
- URL defanging for safe investigation
- Threat classification
- MITRE ATT&CK mapping


## Indicators of Compromise (IOCs)

### Suspicious Sender

```
support@paypa1-security.com
```

### Suspicious URL

```
hxxp://paypal-account-security-login.com
```


## Threat Classification

**Threat Type:** Credential Phishing

**Severity:** HIGH


## MITRE ATT&CK Mapping

### Technique

T1566.002 – Spearphishing Link

### Tactic

Initial Access


## Incident Report

Detailed analysis and investigation:

📄 [View Report](reports/phishing-analysis-report.md)


## Project Workflow

```text
Suspicious Email
       ↓
Python Email Analyzer
       ↓
IOC Extraction
       ↓
Threat Classification
       ↓
MITRE ATT&CK Mapping
       ↓
Incident Report
```

## Skills Demonstrated

- Email Security
- Threat Analysis
- IOC Identification
- Python Automation
- Incident Investigation
- MITRE ATT&CK Mapping
- Cybersecurity Reporting
- Incident Response
- Security Monitoring
- Security Awareness


## Evidence

Python analysis output screenshot is included in the investigation report.


## Future Improvements

- Extract IP addresses from email headers
- Analyze attachments
- Export findings to CSV
- Integrate VirusTotal API
- Perform automated IOC enrichment
- Add OSINT checks


## Author

**Twinkal Rana**

**Focus Areas:** SOC Analyst | Cybersecurity Analyst | Incident Response | Blue Team
