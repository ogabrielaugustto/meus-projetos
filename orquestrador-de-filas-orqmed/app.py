from flask import Flask, render_template, request, json
from flask_mysqldb import MySQL
import consulta_cep, mysql.connector, datetime, datatime

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='orqmed',
)

app = Flask(__name__)

mysql = MySQL(app)

resposta = str()
primeiro_nome = str()
nome_completo = str()
cpf_pac = int()
data_nasci = str()
cel_pac = int()
cep_pac = int()
pref_pac = str()
sint_pac = str()
sint_cronic = str()
preferencial = False
senhaNormal = 0
senhaPreferencial = 0
senhaFinal = str()
logradouro = str()
num_logra = int()
ultima_consulta = str()
cidade = str()
bairro = str()
sex_pac = str()
uf = str()
ibge = int()


#Página inicial/home
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

#Pergunta 1
#Captura do nome do paciente
@app.route("/pergunta1", methods=['GET', 'POST'])
def pergunta1():
    return render_template('pergunta1.html')

@app.route('/resposta1', methods=['POST'])
def resposta1():
    global nome_completo, primeiro_nome

    resposta = request.get_json(cache=True)
    nome_completo = resposta.replace('"','').replace('.','').replace(',','')
    primeiro_nome = nome_completo.split()[0]
    print(nome_completo)
    print(primeiro_nome)
    
    return nome_completo, primeiro_nome

#Pergunta 2
#Captura do CPF do cliente
@app.route("/pergunta2", methods=['GET', 'POST'])
def pergunta2():
    global primeiro_nome
    
    return render_template('pergunta2.html', primeiro_nome=primeiro_nome)

@app.route('/resposta2', methods=['POST'])
def resposta2():
    global cpf_pac
    resposta = request.get_json(cache=True)
    cpf_pac=resposta.replace('"','').replace('.','').replace('-','')
    print(cpf_pac)
    return cpf_pac

#Pergunta 3
#Captura da data de nascimento do paciente
@app.route("/pergunta3", methods=['GET', 'POST'])
def pergunta3():
    global primeiro_nome
    
    return render_template('pergunta3.html', primeiro_nome=primeiro_nome)

@app.route('/resposta3', methods=['POST'])
def resposta3():
    global data_nasci, cpf_pac
    resposta = request.get_json(cache=True)
    data_nasci=resposta.replace('"','')
    data_nasci =datetime.datetime.strptime(data_nasci, "%d/%m/%Y").strftime("%Y-%m-%d")
 
    print(data_nasci)

    return data_nasci

#Pergunta 4
#Captura do celular do paciente
@app.route("/pergunta4", methods=['GET', 'POST'])
def pergunta4():
    global primeiro_nome
    
    
    return render_template('pergunta4.html', primeiro_nome=primeiro_nome)

@app.route('/resposta4', methods=['POST'])
def resposta4():
    global cel_pac
    resposta = request.get_json(cache=True)
    cel_pac=resposta.replace('"','').replace('-','').replace(' ','')
    print(cel_pac)
    return cel_pac

#Pergunta ##
#Captura o CEP do paciente
@app.route("/Cep", methods=['GET', 'POST'])
def capturaCep():
    global primeiro_nome
    
    
    return render_template('capturaCep.html', primeiro_nome=primeiro_nome)

@app.route('/respostaCep', methods=['POST'])
def respostaCep():
    global cep_pac
   
    resposta = request.get_json(cache=True)
    cep_pac=resposta.replace('"','').replace('-','')

    print(cep_pac)
    return cep_pac

#Pergunta ##
#Captura o número da residência e complemento
@app.route("/NumLogradouro", methods=['GET', 'POST'])
def NumLogradouro():
    global logradouro, cep_pac, uf, cidade, bairro, ibge

    consulta_cep.consultarCep(cep_pac)
    logradouro = consulta_cep.logradouro
    uf = consulta_cep.uf
    cidade = consulta_cep.cidade
    bairro = consulta_cep.bairro
    ibge = consulta_cep.ibge

    return render_template('num_logradouro.html', logradouro=logradouro)

@app.route('/respostaNumLogradouro', methods=['POST'])
def respostaNumLogradouro():
    global num_logra

    resposta = request.get_json(cache=True)
    num_logra=resposta.replace('"','').replace('-','').replace(' ','')

    print(num_logra)
    return num_logra

#Pergunta 5
#Captura o gênero do paciente
@app.route("/pergunta5", methods=['GET', 'POST'])
def pergunta5():
    global primeiro_nome, logradouro
    
    return render_template('pergunta5.html', primeiro_nome=primeiro_nome, logradouro=logradouro)

@app.route('/resposta5', methods=['POST'])
def resposta5():
    global sex_pac
    resposta = request.get_json(cache=True)
    sex_pac=resposta.replace('"','')
    print(sex_pac)
    return sex_pac

#Pergunta 6
#Verifica se o paciente é preferencial
@app.route("/pergunta6", methods=['GET', 'POST'])
def pergunta6():
    global primeiro_nome
    
    return render_template('pergunta6.html', primeiro_nome=primeiro_nome)

@app.route('/resposta6', methods=['POST'])
def resposta6():
    global pref_pac, preferencial, senhaNormal, senhaPreferencial, senhaFinal

    resposta = request.get_json(cache=True)
    pref_pac=resposta.replace('"','')

    if pref_pac == 'Idoso' or pref_pac == 'Gestante' or pref_pac == 'PcD':
        preferencial = True
        senhaPreferencial += 1
        senhaFinal = (f'P{senhaPreferencial}')
    
    elif pref_pac == 'Nao':
        preferencial = False
        senhaNormal += 1
        senhaFinal = senhaNormal
    

    print(pref_pac)
    return pref_pac, senhaFinal


#Pergunta 7
#Captura os sintomas do paciente
@app.route("/pergunta7", methods=['GET', 'POST'])
def pergunta7():
    global primeiro_nome
    
    return render_template('pergunta7.html', primeiro_nome=primeiro_nome)

@app.route('/resposta7', methods=['POST'])
def resposta7():
    global sint_pac
    resposta = request.get_json(cache=True)
    sint_pac=resposta.replace('"','')
    print(sint_pac)
    return sint_pac

#Pergunta 8
#Verifica se o paciente possuí doenças crônicas
@app.route("/pergunta8", methods=['GET', 'POST'])
def pergunta8():
    global primeiro_nome
    
    return render_template('pergunta8.html', primeiro_nome=primeiro_nome)

@app.route('/resposta8', methods=['POST'])
def resposta8():
    global sint_cronic
    resposta = request.get_json(cache=True)
    sint_cronic=resposta.replace('"','')
    print(sint_cronic)
    return sint_cronic

#Finalizar
#Imprime a complexidade do paciente e sua senha
@app.route("/finalizar", methods=['GET', 'POST'])
def finalizar():
    global primeiro_nome, sint_pac, senhaNormal, sint_cronic, tipo_da_fila, preferencial

    tipo_da_fila = str()
    situa = str()

    lista_sintomas_leves = ['coriza','febre','febres','tosse','tosses','fadiga','enxaqueca','enxaquecas', 'dor de garganta', 'dor de cabeça', 'vomitando', 'ansia de vomito', 'vomito']
    lista_sintomas_grave = ['dor no peito','pressão persistente no tórax','desconforto respiratório','dificuldade para respirar', 'falta de ar', 'respiração ofegante']
    lista_doenca_cronica = ['diabetes','asma','hipertensão','gestante','lactante']
    tem_leve = False
    tem_grave = False
    tem_cronic = False

    for sint_leve in lista_sintomas_leves:
        if sint_leve.lower() in sint_pac.lower():
            tem_leve = True
            
    for doc_cronic in lista_doenca_cronica:
        if doc_cronic.lower() in sint_cronic.lower():
            tem_cronic = True
            
    for sint_grave in lista_sintomas_grave:
        if sint_grave.lower() in sint_pac.lower():
            tem_grave = True

    if tem_leve == True and tem_cronic == False and tem_grave == False:
        tipo_da_fila = 'VERDE'
        situa = 'Entendemos o desconforto, devido aos sintomas apresentados, você foi encaixado na fila'
        print(situa, tipo_da_fila)
        
    if tem_leve == True and tem_cronic == True and tem_grave == False or tem_leve == True and tem_cronic == False and tem_grave == True:
        tipo_da_fila = 'AMARELA'
        situa = 'Entendemos que sua situção necessita de mais atenção, você foi encaixado na fila'
        print(situa, tipo_da_fila)

    if tem_grave == True and tem_cronic == True and tem_leve == True:
        tipo_da_fila = 'VERMELHA'
        situa = 'Entendemos a gravidade da situação pelos sintomas apresentados, você foi encaixado na fila'
        print(situa, tipo_da_fila)
            

    return render_template('finalizar.html', primeiro_nome=primeiro_nome, situa=situa, senhaFinal=senhaFinal, tipo_da_fila=tipo_da_fila)

@app.route('/respostaFinalizar', methods=['POST'])
def respostaFinalizar():
    global nome_completo, data_nasci, sex_pac, cpf_pac, cel_pac, cep_pac, cep_pac, uf, cidade, bairro, logradouro, num_logra, ibge, sint_pac, sint_cronic, ultima_consulta

    resposta = request.get_json(cache=True)
    finalizou = resposta.replace('"','')




    datatime.verifUltimaConsulta()
    ultima_consulta = datatime.ultima_consulta
    
    my_cursor = mydb.cursor()
    sql = f"INSERT INTO pacientes (nome, nascimento, sexo, cpf, celular, cep, uf, cidade, bairro, logradouro, num_logra, ibge, sintomas, doencas_cronicas, ultima_consulta) VALUES ('{nome_completo}', '{data_nasci}', '{sex_pac}', '{cpf_pac}', '{cel_pac}', '{cep_pac}', '{uf}', '{cidade}', '{bairro}', '{logradouro}', '{num_logra}', '{ibge}', '{sint_pac}', '{sint_cronic}', '{ultima_consulta}')"
    my_cursor.execute(sql)
    mydb.commit()

    print('Dados enviados com sucesso')
    return 'Dados enviados com sucesso'



# Area de fila
@app.route("/areafila", methods=['GET', 'POST'])
def areafila():
    global primeiro_nome, preferencial

    #Colocar orquestrador de fila aqui
    
    return render_template('area_fila.html', primeiro_nome=primeiro_nome)

@app.route('/respostaAreaFila', methods=['POST'])
def respostaAreaFila():
    global pref_pac, preferencial, senhaNormal, senhaPreferencial, senhaFinal

    resposta = request.get_json(cache=True)
    pref_pac=resposta.replace('"','')

    print(pref_pac, preferencial)
    return pref_pac, preferencial



# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
    