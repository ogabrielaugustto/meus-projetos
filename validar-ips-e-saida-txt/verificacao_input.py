with open("entrada_ips.txt") as arquivo:
    total_linhas = sum(1 for linha_ip in arquivo)
arquivo = open('entrada_ips.txt', 'r')

ips_validos = []
ips_invalidos = []

for ips in range (total_linhas):
    linha_ip = arquivo.readline()
    el_ip = linha_ip.split(".")
    el0 = int(el_ip[0])
    el1 = int(el_ip[1])
    el2 = int(el_ip[2])
    el3 = int(el_ip[3])
    if  el0 <= 255 and el1 <= 255 and el2 <= 255 and el3 <= 255:
        ips_validos.append(f"{linha_ip}")
    else:
        ips_invalidos.append(f"{linha_ip}")

arquivo_final = open("relatorio_final_ips.txt" ,"w")
arquivo_final.write("[IPs Válidos:]\n")
arquivo_final.writelines(ips_validos)
arquivo_final.write("\n[IPs Inválidos:]\n")
arquivo_final.writelines(ips_invalidos)
arquivo.close()