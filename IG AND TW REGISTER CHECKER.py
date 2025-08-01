import requests
import pyfiglet

logo = pyfiglet.figlet_format('MASA')
print(logo)

class ChecK():

    def __init__(self):
        self.emails = self.load_emails("masa.txt")
        self.telegram_bot_token = '8340034878:AAEgBlxLa5bsX76bUbPJWAKspqY0inhspu8'  # استبدل هذا بالتوكن الخاص بك
        self.telegram_chat_id = '7957784778'  # استبدل هذا بمعرف الدردشة الخاص بك
        self.check_emails()

    def load_emails(self, filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]

    def send_to_telegram(self, message):
        url = f"https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage"
        payload = {
            'chat_id': self.telegram_chat_id,
            'text': message,
            'parse_mode': 'Markdown'  # يمكنك استخدام Markdown لتنسيق الرسالة
        }
        requests.post(url, json=payload)

    def PrintT(self, email):
        message = f"Twitter acc: {email}"
        print(message + "\n")
        self.send_to_telegram(message)

    def PrintI(self, email):
        message = f"Instagram acc: {email}"
        print(message + "\n")
        self.send_to_telegram(message)

    def PrintF(self, email):
        print(f"{email} = Unlinked" + "\n")

    def check_emails(self):
        for email in self.emails:
            self.twitter(email)
            self.instagram(email)

    def twitter(self, email):
        print("==================")
        print("[+] Twitter [+]")
        print("")
        r = requests.Session()
        url = f"https://api.twitter.com/i/users/email_available.json?email={email}"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
        r.headers = {
            'User -Agent': user_agent,
            'Host': "api.twitter.com",
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        }
        req = r.get(url).json()
        if req.get('valid') is False:
            self.PrintT(email) 
        else:
            self.PrintF(email)

    def instagram(self, email):
        print("==================")
        print("[+] Instagram [+]")
        print("")
        r = requests.Session()
        url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        r.headers = {'user-agent': user_agent}
        r.headers.update({'X-CSRFToken': "missing"})
        data = {"email_or_username": email}
        req = r.post(url, data=data)
        if "We sent an email to" in req.text or "password" in req.text or "sent" in req.text:
            self.PrintI(email)
        else:
            self.PrintF(email)


if __name__ == "__main__":
    ChecK()
    print('')    
    print('Press enter to exit.')
    input('')
