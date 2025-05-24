import socket

# Lista das 150 portas mais comuns
common_ports = [
     20, 21, 22, 23, 25, 53, 69, 80, 110, 123, 135, 137, 138, 139, 143, 161, 162, 179, 389, 443, 
     445, 465, 514, 515, 587, 631, 993, 995, 1080, 1433, 1521, 1701, 1720, 1723, 3306, 3389, 5432, 
     5900, 8080, 8443, 5000, 5060, 69, 123, 138, 161, 389, 636, 1521, 3306, 5432, 6379, 8080, 9200,
     11211, 27017, 27018, 5900, 5901, 6000, 7000, 8000, 8008, 8010, 8081, 8181, 10000, 11211, 
     27017, 3389, 5000, 5357, 8888, 25565, 49152, 49153, 49154, 49155, 49156, 49157, 49158, 49159,
     49160, 49161, 49162, 49163, 49164, 49165, 49166, 49167, 49168, 49169, 49170, 49171, 49172, 
     49173, 49174, 49175, 49176, 49177, 49178, 49179, 49180, 49181, 49182, 49183, 49184, 49185, 
     49186, 49187, 49188, 49189, 49190, 49191, 49192, 49193, 49194, 49195, 49196, 49197, 49198, 
     49199, 49200, 49201, 49202, 49203, 49204, 49205, 49206, 49207, 49208, 49209, 49210, 49211, 
     49212, 49213, 49214, 49215, 49216, 49217, 49218, 49219, 49220, 49221, 49222, 49223, 49224
]

def check_port(ip, port):
    """
    Testa se uma porta está aberta em um IP.
    Retorna True se a porta está aberta, caso contrário False.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout de 1 segundo
            if s.connect_ex((ip, port)) == 0:
                return True
    except Exception as e:
        print(f"Erro ao testar a porta {port}: {e}")
    return False

def test_ip(ip):
    """
    Testa todas as portas no IP fornecido e retorna as abertas.
    """
    print(f"\nTestando comunicação com o IP: {ip}")
    open_ports = []
    
    for port in common_ports:
        print(f"Testando porta {port}...", end="")
        if check_port(ip, port):
            print(" ABERTA")
            open_ports.append(port)
        else:
            print(" FECHADA")
    
    if open_ports:
        print(f"\nPortas abertas encontradas no IP {ip}:")
        for port in open_ports:
            print(f"- Porta {port} (ABERTA)")
    else:
        print(f"\nNenhuma porta aberta foi encontrada no IP {ip}.")
    return open_ports

def main():
    ips = input("Digite os IPs separados por vírgula: ").split(",")
    ips = [ip.strip() for ip in ips]  # Remove espaços em branco
    
    for ip in ips:
        test_ip(ip)

if __name__ == "__main__":
    main()
