import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from googlesearch import search
import datetime
import os
import time

# Renkler
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
    print(f"\n{GREEN}[+] Bilgiler log olarak kaydedildi: {file_name}{RESET}")

def analyze_number(phone_number):
    result = f"Phone OSINT Result - {phone_number}\n{'-'*50}\n"

    try:
        parsed = phonenumbers.parse(phone_number, None)
        konum = geocoder.description_for_number(parsed, 'en')
        oper = carrier.name_for_number(parsed, 'en')
        zone = timezone.time_zones_for_number(parsed)
        gecerli = phonenumbers.is_valid_number(parsed)
        olasi = phonenumbers.is_possible_number(parsed)

        print(f"\n{CYAN}[+] Temel Numara Bilgisi:{RESET}")
        print(f"{GREEN}  Konum        :{RESET} {konum}")
        print(f"{GREEN}  Operatör     :{RESET} {oper}")
        print(f"{GREEN}  Saat Dilimi  :{RESET} {zone}")
        print(f"{GREEN}  Geçerli mi?  :{RESET} {gecerli}")
        print(f"{GREEN}  Olası mı?    :{RESET} {olasi}")

        result += f"Location: {konum}\nCarrier: {oper}\nTimezone: {zone}\nValid: {gecerli}\nPossible: {olasi}\n"

        print(f"\n{CYAN}[+] Google OSINT Araması:{RESET}")
        for url in search(phone_number, num_results=8, lang="en"):
            print(f"{YELLOW}  ->{RESET} {url}")
            result += url + "\n"
            time.sleep(1)

        print(f"\n{CYAN}[+] Belge Araması (.pdf, .doc, .xls):{RESET}")
        query = f'"{phone_number}" filetype:pdf OR filetype:doc OR filetype:xls'
        for url in search(query, num_results=4, lang="en"):
            print(f"{YELLOW}  ->{RESET} {url}")
            result += url + "\n"
            time.sleep(1)

        print(f"\n{CYAN}[+] WhatsApp Tahmini:{RESET}")
        if phone_number.startswith("+90"):
            msg = "Türkiye numarası, WhatsApp’ta olma ihtimali yüksek."
        else:
            msg = "Numara uluslararası, manuel kontrol gerekir."
        print(f"{YELLOW}  ->{RESET} {msg}")
        result += f"WhatsApp Tahmini: {msg}\n"

        save_log(phone_number, result)

    except Exception as e:
        print(f"{RED}[-] Hata oluştu: {e}{RESET}")

if __name__ == "__main__":
    banner()
    num = input(f"{CYAN}Numarayı uluslararası formatta girin (örn: +1, +90, +44): {RESET}")
    analyze_number(num)
