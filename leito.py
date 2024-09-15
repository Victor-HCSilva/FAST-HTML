# Leito:
from datetime import datetime

DATA = str(datetime.now().date())

leito1 = {#diponivel manha, tarde e noite 
    'leito':[1],
    'dia': [DATA],
    'manha':[True, None,],
    'tarde':[True, None],
    'noite':[True, None], 
    'agenda': {'2025-10-2':['manha','tarde','noite'], '2024-10-20':[None,'tarde','noite']}
}

leito2 = {#diponivel manha e tarde
    'leito':[2],
    'dia': [DATA],
    'manha':[True, None,],
    'tarde':[True, None,],
    'noite':[False, 'nome da pessoa que esta ocupando'],
    'agenda': {'2024-10-2':['manha','tarde','noite'], '2024-12-2':[None,'tarde',None]}
}

leitos = [leito1,leito2]#lista de quartos

#Vizualização geral
'''for dicionario in leitos:
    if dicionario['manha'][0] == True:
        print(f'\nLeito diponível: {dicionario['leito']}, data: {DATA}, horário: Manhã')
    if dicionario['tarde'][0] == True:
        print(f'\nLeito diponível: {dicionario['leito']}, data: {DATA}, horário: Tarde')
    if dicionario['noite'][0] == True:
        print(f'\nLeito diponível: {dicionario['leito']}, data: {DATA}, horário: Noite')
'''
#Exibindo datas agendadas
for dicionario in leitos:
    for agenda in dicionario.values():#
            if type(agenda) == dict:
                for data in agenda.items():
                    print(f'Data: {data} ')
        