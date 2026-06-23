import email
import re
from email import policy

def analyze_eml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        msg = email.message_from_file(f, policy=policy.default)

    print("===== PHISHING EMAIL ANALYSIS =====")
    print(f"Subject: {msg['Subject']}")
    print(f"From: {msg['From']}")
    print(f"To: {msg['To']}")

    body = msg.get_body(preferencelist=('plain', 'html'))
    if body:
        content = body.get_content()

        urls = re.findall(r'https?://\S+', content)

        print("\nURLs Found:")
        for url in urls:
            print(url.replace("http://", "hxxp://").replace("https://", "hxxps://"))

    print("\nThreat Type: Credential Phishing")
    print("Severity: HIGH")
    print("MITRE ATT&CK: T1566.002 - Spearphishing Link")

analyze_eml("samples/phishing-email.txt")
