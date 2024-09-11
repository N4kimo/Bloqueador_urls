import time
from datetime import datetime as dt

# Caminho para o arquivo hosts
hosts_path = "/etc/hosts"  # Para Windows, use "C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"

# Coloque a url que deseja bloquear
website_list = []
url = input("Digite a URL desejada: ")
website_list.append(url)

# Horário que vai começar e terminar (exemplo: das 8h às 18h)
start_hour = int(input("Digite a hora de início: "))
end_hour = int(input("Digite a hora de término: "))

while True:
    # Verifica se está dentro do horário de trabalho
    if dt.now().hour >= start_hour and dt.now().hour < end_hour:
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
