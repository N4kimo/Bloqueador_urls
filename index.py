import time
from datetime import datetime as dt

# Caminho para o arquivo hosts
hosts_path = "/etc/hosts"  # Para Windows, use "C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"

# Coloque a url que deseja bloquear
website_list = ["Instagram.com", "https://www.instagram.com/"]

# Horário de trabalho (exemplo: das 8h às 18h)
start_hour = 9
end_hour = 10

while True:
    # Verifica se está dentro do horário de trabalho
    if dt(dt.now().year, dt.now().month, dt.now().day, start_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_hour):
        print("Horário de trabalho... Bloqueando sites")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Fora do horário de trabalho... Desbloqueando sites")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
