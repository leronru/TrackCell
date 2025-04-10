import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from googlesearch import search
import datetime
import os
import time

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print(f"""{BOLD}{CYAN}
  ____  _                        ____  ____  _   _ _____ 
 |  _ \| | __ _ _   _  ___ _ __|  _ \|  _ \| \ | | ____|
 | |_) | |/ _` | | | |/ _ \ '__| | | | |_) |  \| |  _|  
 |  __/| | (_| | |_| |  __/ |  | |_| |  __/| |\  | |___ 
 |_|   |_|\__,_|\__, |\___|_|  |____/|_|   |_| \_|_____|
                |___/      v2.0.0 Global Edition      
{RESET}""")

def save_log(number, info):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    file_name = f"PhoneOSINT_{number.replace('+','')}_{now}.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(info)
    print(f"\n{GREEN}[+] Information has been saved as a log: {file_name}{RESET}")

def analyze_number(phone_number):
    result = f"Phone OSINT Result - {phone_number}\n{'-'*50}\n"

    try:
        parsed = phonenumbers.parse(phone_number, None)
        location = geocoder.description_for_number(parsed, 'en')
        carrier_name = carrier.name_for_number(parsed, 'en')
        timezone_info = timezone.time_zones_for_number(parsed)
        valid = phonenumbers.is_valid_number(parsed)
        possible = phonenumbers.is_possible_number(parsed)

        print(f"\n{CYAN}[+] Basic Phone Information:{RESET}")
        print(f"{GREEN}  Location      :{RESET} {location}")
        print(f"{GREEN}  Carrier       :{RESET} {carrier_name}")
        print(f"{GREEN}  Timezone      :{RESET} {timezone_info}")
        print(f"{GREEN}  Valid Number? :{RESET} {valid}")
        print(f"{GREEN}  Possible?     :{RESET} {possible}")

        result += f"Location: {location}\nCarrier: {carrier_name}\nTimezone: {timezone_info}\nValid: {valid}\nPossible: {possible}\n"

        print(f"\n{CYAN}[+] Google OSINT Search Results:{RESET}")
        for url in search(phone_number, num_results=8, lang="en"):
            print(f"{YELLOW}  ->{RESET} {url}")
            result += url + "\n"
            time.sleep(1)

        print(f"\n{CYAN}[+] Document Search (.pdf, .doc, .xls):{RESET}")
        query = f'"{phone_number}" filetype:pdf OR filetype:doc OR filetype:xls'
        for url in search(query, num_results=4, lang="en"):
            print(f"{YELLOW}  ->{RESET} {url}")
            result += url + "\n"
            time.sleep(1)

        print(f"\n{CYAN}[+] WhatsApp Estimate:{RESET}")
        if phone_number.startswith("+90"):
            msg = "This is a Turkish number, highly likely to be on WhatsApp."
        else:
            msg = "This is an international number, manual verification required."
        print(f"{YELLOW}  ->{RESET} {msg}")
        result += f"WhatsApp Estimate: {msg}\n"

        save_log(phone_number, result)

    except Exception as e:
        print(f"{RED}[-] An error occurred: {e}{RESET}")

if __name__ == "__main__":
    banner()
    num = input(f"{CYAN}Enter the phone number in international format (e.g., +1, +90, +44): {RESET}")
    analyze_number(num)
