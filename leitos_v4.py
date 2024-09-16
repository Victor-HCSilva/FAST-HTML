from datetime import date

# Nome, data de nascimento, CPF, contato, endereço,

class Leito():
    def __init__(self,identificador:str,data:date,manha:list,tarde:list,noite:list):
        self.identificador = identificador
        self.manha  = manha
        self.tarde = tarde
        self.noite = noite
        self.data = data
        self.DATA = date.today()
        
    def _agendar_por_horario_(self,horario:int):
        try:
            if 4 >= horario or horario <= 0:
                return 'Inválido, O horario deve ser 1, 2 ou 3'
            
            if horario == 1:
                h = 'manha'
            elif horario == 2:
                h = 'tarde'
            elif horario == 3:
                h = 'noite'
                
            self.paciente = {
                'data':input('Data de inicio: '),
                'nome':input('Nome: '),
                'data_de_nascimento':input('Data de nascimento: '),
                'cpf':input('CPF: '),
                'contato':input('Contato: '),#SMS?
                'endereco':input('Endereço: '),
                'horario':h,
            }
            
            self._salvar_consulta(horario=horario) 
            
        except Exception as erro:
            print(f'Erro: {erro}')
    
    def _salvar_consulta(self,horario=int):            
        #horario da manha
        if horario == 1:
            if len(self.manha) > 0:
                agenda_diponivel = False
                
                for pacientes_agendados in self.manha:
                    if self.paciente['data'] != pacientes_agendados['data'] :#Varrendo a lista e comparando as datas
                        #Se a data está diponivel entao:
                        agenda_diponivel = True
                
                #Aí podemos adicionar
                if agenda_diponivel:
                    self.manha.append(self.paciente)
                    print('\nAgendado!')
                    return
                else:
                    print('\nJá existe uma paciente para esta dia, tente agendar para outro')
                    
            #Se não tiver pacientes na lista de pacientes da manhã
            else:
                self.manha.append(self.paciente)
                
        #horario da tarde        
        if horario == 2:
            if len(self.tarde) > 0:
                
                for pacientes_agendados in self.tarde:
                    if self.paciente['data'] == pacientes_agendados['data'] :#Varrendo a lista e comparando as datas
                        #Se a data está diponivel entao:
                        return 'Já existe uma paciente para esta dia, tente agendar em outra data'
                
                
                self.tarde.append(self.paciente)    
            #Se não tiver pacientes na lista de pacientes da manhã
            else:
                self.tarde.append(self.paciente)
                
        #horario da noite
        if horario == 3:
            if len(self.noite) > 0:
                agenda_diponivel = False
                
                for pacientes_agendados in self.noite:
                    if self.paciente['data'] != pacientes_agendados['data'] :#Varrendo a lista e comparando as datas
                        #Se a data está diponivel entao:
                        agenda_diponivel = True
                
                #Aí podemos adicionar
                if agenda_diponivel:
                    self.noite.append(self.paciente)
                else:
                    print('\nJá existe uma paciente para esta dia, tente agendar para outro')
                    
            #Se não tiver pacientes na lista de pacientes da manhã
            else:
                self.noite.append(self.paciente)
    
if __name__=='__main__':
    lista_de_leitos = []
    
    for s in range(1,20):
        leito = Leito(identificador=f"{s}", data=date.today,manha=[],tarde=[],noite=[])
        lista_de_leitos.append(leito)

    while True:
        sair = input('Sair = q: ')
        escolha = input('numero Leito: ')     
        
        for leito in lista_de_leitos:
            if escolha == leito.identificador:
                h = input('Insira o horário: ')
                leito._agendar_por_horario_(int(h))
            
        if sair == 'q':
            break
        
    for s in lista_de_leitos:
        
        if s.manha:
            for t in s.manha:
                print('Manha:',t)
        elif s.tarde:
            for t in s.tarde:
                print('Manha:',t)
        elif s.noite:
            for t in s.noite:
                print('Manha:',t)