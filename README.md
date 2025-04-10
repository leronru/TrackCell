# TrackCell
TrackCell performs OSINT analysis on phone numbers, providing information such as location, carrier, timezone, and WhatsApp status. It also searches Google and scans for related documents. It is intended for educational purposes and should be used responsibly for testing.


# TrackCell: OSINT Tool for Phone Numbers

**TrackCell** is an advanced OSINT (Open Source Intelligence) tool designed to gather detailed information from phone numbers. It helps users analyze phone number details, such as carrier, location, timezone, and WhatsApp status. The tool also performs Google searches and document scans to enhance the collected data, with support for multiple languages.

---

## Features:
- **Phone Number Analysis**: Retrieve detailed information about a phone number, including location, carrier, and timezone.
- **WhatsApp Status Checker**: Check the WhatsApp status for a given phone number.
- **Google OSINT Search**: Perform automated Google searches to gather additional data.
- **Document Search**: Scan documents for phone number-related information.
- **Multilingual Support**: Available in both **English** and **Turkish**.

---

## How to Use:

### 1. **English Version (trackCell_EN.py)**

Follow the steps below to use the English version of TrackCell:

#### Step 1: Clone the repository
```bash
git clone https://github.com/leronru/TrackCell.git
``` 
Step 2: Navigate to the directory
```bash 
cd TrackCell
```
Step 3: Install the required libraries
```bash 
pip install -r requirements.txt
```

```bash
pip install requests beautifulsoup4 googlesearch-python phonenumbers
Step 4: Run the tool in English
```
```bash
python trackCell.py
```
This will execute the tool in English, providing results based on phone number information.


---

2. Turkish Version (TrackCell.py)

To use the Turkish version of TrackCell, follow these steps:

Step 1: Clone the repository
```bash
git clone https://github.com/leronru/TrackCell.git
```
Step 2: Navigate to the directory
```bash 
cd TrackCell
```
Step 3: Install the required libraries
```bash
pip install -r requirements.txt
```
Step 4: Run the tool in Turkish
```bash
python TrackCell.py
```
This will execute the tool in Turkish, providing results for the phone number with a Turkish interface.


---

Requirements:

The following Python libraries are required for the tool to function properly:

requests

beautifulsoup4

googlesearch-python

phonenumbers


To install the required libraries, simply run:
```bash 
pip install -r requirements.txt
```

---

Legal Disclaimer:

This tool is developed for educational and research purposes only. It should be used responsibly and in compliance with all applicable laws and regulations. By using this tool, you accept full responsibility for any actions and consequences arising from its use.

The author of this tool, Leronru, does not support or condone any illegal activities or malicious use of this software. Ensure that you have obtained proper legal authorization before using this tool in your country or jurisdiction.


---

License:

TrackCell is licensed under the MIT License. You are free to modify, distribute, and use this software under the terms of the MIT License, provided that it is not used for any illegal or unethical purposes.

License Summary:

Author: Leronru

License: MIT License

Copyright: © 2025 Leronru



---

Contributions:

No contributions or modifications to this repository are allowed without the explicit permission of the author, Leronru. Any unauthorized modifications or contributions will be considered a violation of the repository’s terms.


---

Acknowledgments:

This tool utilizes several open-source libraries and resources, which are listed in the requirements.txt file. Special thanks to the contributors of these libraries for making this tool possible.


---

Contact:

For any inquiries or to request permission for contributions, please contact the author at: leronru33@gmail.com


---

Important Notes:

Privacy and Legal Compliance: Always ensure that you have permission before using this tool in any context. Unauthorized access to personal or private information is strictly prohibited.

Ethical Use: This tool should only be used in ethical, legal contexts such as penetration testing (with permission), research, and learning.
