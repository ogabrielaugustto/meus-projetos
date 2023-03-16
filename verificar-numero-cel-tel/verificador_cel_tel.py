tipo_num = "Invalido"
while tipo_num == "Invalido":
    num_cel_tel = str(input("Digite um numero de telefone ou celular válido: "))
    if len(num_cel_tel) < 14:
        tipo_num = "Invalido"
        print("Não é um número de telefone ou celular válido, tente novamente!")
    else:         
        DDD = int(num_cel_tel[1:3])           # DDD do número informado
        prt_esq = str(num_cel_tel[0])          # Parenteses da esquerda
        prt_drt = str(num_cel_tel[3])          # Parenteses da direita
        trc_crt_cel = str(num_cel_tel[10])     # Traço do centro celular
        trc_crt_tel = str(num_cel_tel[9])      # Traço do centro telefone
        seq_cel_1 = num_cel_tel[4:10]     # Possui 6 caracteres - Celular
        seq_cel_2 = num_cel_tel[11:15]    # Possui 4 caracteres - Celular
        seq_tel_1 = num_cel_tel[4:9]      # Possui 5 caracteres - Telefone
        seq_tel_2 = num_cel_tel[10:14]    # Possui 4 caracteres - Telefone
        if len(num_cel_tel) == 15:
            if prt_esq == "(" and prt_drt == ")" and DDD >= 1 and DDD <= 100 and seq_cel_1[0] == " " and seq_cel_1[1] == "9" and len(seq_cel_1) == 6 and trc_crt_cel == "-" and len(seq_cel_2) == 4:
                print("Número de CELULAR válido!")
            tipo_num = "Valido"
        elif len(num_cel_tel) == 14:
            if prt_esq == "(" and prt_drt == ")" and DDD >= 1 and DDD <= 100 and seq_tel_1[0] == " " and len(seq_tel_1) == 5 and trc_crt_tel == "-" and len(seq_tel_2) == 4:
                print("Número de TELEFONE válido!")
            tipo_num = "Valido"
        else:
            tipo_num = "Invalido"
            print("Não é um número de telefone ou celular válido, tente novamente!")