# Leito:
from datetime import datetime

def ver_vagas(lista_de_leitos):
    agendas = lista_de_leitos
    
    for agenda in agendas:#percorrendo cada dicionario na lista de leitos
        for chave, valor in agenda.items():#percorrendo cada chave  e valor nos dicionários
            '''if chave == '2025-2-20' and type(valor) == dict:
                for s,d in agenda[chave].items():
                    if True in d:#se esitver disponível na data requerida
                        print(f'horario livre para data {chave}: {s}, leito: {agenda['leito']}')'''
                        
            if type(valor) == dict:#se o tipo for dicionário
                for chave1,valor2 in agenda[chave].items():#percorrendo novamente chave  e valor
                    if True in valor2:#se esitver disponível na data requerida (True in valor2)
                        print(f'horario livre para data {chave} {chave1}, leito: {agenda['leito']}')




#pensar como fazer uma inserção realizar o famoso CRUDE depoi já dá pra ir fazendo interface.
def agendar(data:str, agenda:dict, leito:list):
    try:
        if datetime(data):
            quantos_horarios = int(input('quantos horario, int: '))
            
            for s in range(quantos_horarios):
                print('manha','tarde','noite')
                escolha= input('Escolha o horário: ')
                nome = input('Nome: ')
                #agenda[data]
                
            return agenda
            
    except Exception    as erro:
        print('formato inválido',erro)
    

DATA = str(datetime.now().date())

agenda1 = {
    'leito':[1],#identificação leito 1
    '2025-02-25':{
    'manha':[True,None],
    'tarde':[False,'Nome da pessoa'],
    'noite':[False,'Nome da pessoa'],
    },
    '2025-04-28':{
    'manha':[True,None],
    'tarde':[False,'Nome da pessoa'],
    'noite':[False,'Nome da pessoa'],
    }
}

leito1 = {#diponivel manha, tarde e noite 
    'leito':[1],#indetificador ligando o leitto à agenda
    'dia': [DATA],
    'manha':[True, None,],
    'tarde':[True, None],
    'noite':[True, None], 
}


agenda2 = {#Agendamentos para o leito 2
    'leito':[2],#idetificador ligando o leitto à agenda
    '2025-02-20':{
    'manha':[True,None],
    'tarde':[False,'Nome da pessoa'],
    'noite':[True,'Nome da pessoa'],
    }
}

leito2 = {#diponivel manha e tarde
    'leito':[2],
    'dia': [DATA],
    'manha':[True, None,],
    'tarde':[True, None,],
    'noite':[False, 'nome da pessoa que esta ocupando'],
}
agendas = [agenda1,agenda2] 


#verificando se há vagas
while True:
    ver = input('sair -->> "s"')
    ver_vagas(agendas)
    if ver =='s':
        break