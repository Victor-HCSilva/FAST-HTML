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
    
    def _leito(self):
        return self.identificador
    
    def ver_ocupacao(self):
        return self.identificador,self.manha,self.tarde,self.noite,self.data
    
#_____Consultas para um horário e dia________    
    def _agendar_manha_(self):    
        data = self.DATA#input('DATA: ')
        paciente = {
            'data_inicial':data,
            'data_final':data,
            'data_de_nacimento':input('Data de nascimento: '),
            'cpf':input('CPF: '),
            'contato':input('Contato: '),#SMS?
            'endereco':input('Endereço: '),
            'horario':'manha',
        }
        #Se já tiver paciente na lista depacientes do horário da manhã
        
        if len(self.manha) > 0:
            
            agenda_diponivel = False
            
            for pacientes_agendados in self.manha:
                if paciente['data'] != pacientes_agendados['data'] :#Varrendo a lista e comparando as datas
                    #Se a data está diponivel entao:
                    agenda_diponivel = True
            
            #Aí podemos adicionar
            if agenda_diponivel:
                self.manha.append(paciente)
            else:
                print('\nJá existe uma paciente para esta dia, tente agendar para outro')
                
        #Se não tiver pacientes na lista de pacientes da manhã
        else:
            self.manha.append(paciente)

    def _agendar_tarde_(self):
        data = self.DATA#input('DATA: ')
        paciente = {
            'data_inicial':data,
            'data_final':data,
            'nome':input('Nome: '),
            'data_de_nacimento':input('Data de nascimento: '),
            'cpf':input('CPF: '),
            'contato':input('Contato: '),#SMS?
            'endereco':input('Endereço: '),
            'horario':'manha',
        }
        #Se já tiver paciente na lista depacientes do horário da manhã
        
        if len(self.tarde) > 0:
            
            agenda_diponivel = False
            
            for pacientes_agendados in self.tarde:
                if paciente['data'] != pacientes_agendados['data'] :#Varrendo a lista e comparando as datas
                    #Se a data está diponivel entao:
                    agenda_diponivel = True
            
            #Aí podemos adicionar
            if agenda_diponivel:
                self.tarde.append(paciente)
            else:
                print('\nJá existe uma paciente para esta dia, tente agendar para outro')
                
        #Se não tiver pacientes na lista de pacientes da manhã
        else:
            self.tarde.append(paciente)

    def _agendar_noite_(self):
        data = self.DATA#input('DATA: ')
        
        self.paciente = {
            'data_inicial':data,
            'data_final':data,
            'nome':input('Nome: '),
            'data_de_nacimento':input('Data de nascimento: '),
            'cpf':input('CPF: '),
            'contato':input('Contato: '),#SMS?
            'endereco':input('Endereço: '),
            'horario':'manha',
        }
        
        #Se já tiver paciente na lista depacientes do horário da manhã
    
    def salvar_manha(self ):            
        if len(self.manha) > 0:
            
            agenda_diponivel = False
            
            for pacientes_agendados in self.manha:
                if self.paciente['data'] != pacientes_agendados['data'] :#Varrendo a lista e comparando as datas
                    #Se a data está diponivel entao:
                    agenda_diponivel = True
            
            #Aí podemos adicionar
            if agenda_diponivel:
                self.manha.append(self.paciente)
            else:
                print('\nJá existe uma paciente para esta dia, tente agendar para outro')
                
        #Se não tiver pacientes na lista de pacientes da manhã
        else:
            self.noite.append(self.paciente)

    #Salvar nas listas 
    def salvar_tarde(self ):            
        if len(self.noite) > 0:
            
            agenda_diponivel = False
            
            for pacientes_agendados in self.tarde:
                if self.paciente['data'] != pacientes_agendados['data'] :#Varrendo a lista e comparando as datas
                    #Se a data está diponivel entao:
                    agenda_diponivel = True
            
            #Aí podemos adicionar
            if agenda_diponivel:
                self.tarde.append(self.paciente)
            else:
                print('\nJá existe uma paciente para esta dia, tente agendar para outro')
                
        #Se não tiver pacientes na lista de pacientes da manhã
        else:
            self.noite.append(self.paciente)

    def salvar_noite(self ):            
        if len(self.noite) > 0:
            
            agenda_diponivel = False
            
            for pacientes_agendados in self.noite:
                if self.paciente['data'] != pacientes_agendados['data'] :#Varrendo a lista e comparando as datas
                    #Se a data está diponivel entao:
                    agenda_diponivel = True
            
            #Aí podemos adicionar
            if agenda_diponivel:
                self.tarde.append(self.paciente)
            else:
                print('\nJá existe uma paciente para esta dia, tente agendar para outro')
                
        #Se não tiver pacientes na lista de pacientes da manhã
        else:
            self.noite.append(self.paciente)

    def ver_leitos_disponiveis(self):
        if self.manha:
            for leito_horario_manha in self.manha:
                if leito_horario_manha:
                    print('Nome:',leito_horario_manha['nome'],'data:',leito_horario_manha['data'])
                    
        else:
           print('Não existem agendamentos para esse horário') 
           
        if self.tarde:
            for leito_horario_tarde in self.tarde:
                if leito_horario_tarde:
                    print('Nome:',leito_horario_tarde['nome'],'data:',leito_horario_tarde['data'])
        else:
           print('Não existem agendamentos para esse horário') 
        
        if self.noite:
            for leito_horario_noite in self.noite:
                if leito_horario_noite:
                    print('Nome:',leito_horario_noite['nome'],'data:',leito_horario_noite['data'])
            
        else:
           print('Não existem agendamentos para esse horário')    
    
#______________Agendar por longo tempo_________

    def _agendar_(self, data_inicial:date,data_final,nome:str,data_de_nascimento:date,cpf:str,contato:str,endereco:str, dias:int):
        
        try:
            for cadastro in range(dias):
                paciente = {
                    'data_inicial':data_inicial,
                    'data_final':data_final,
                    'nome':nome,
                    'data_de_nacimento':data_de_nascimento,
                    'cpf':cpf,
                    'contato':contato,#SMS?
                    'endereco':endereco,
                    'horario':'manha',
                }
                
                paciente = {
                    'data_inicial':data_inicial,
                    'data_final':data_final,
                    'nome':nome,
                    'data_de_nacimento':data_de_nascimento,
                    'cpf':cpf,
                    'contato':contato,#SMS?
                    'endereco':endereco,
                    'horario':'tarde',
                }
                paciente = {
                    'data_inicial':data_inicial,
                    'data_final':data_final,
                    'nome':nome,
                    'data_de_nacimento':data_de_nascimento,
                    'cpf':cpf,
                    'contato':contato,#SMS?
                    'endereco':endereco,
                    'horario':'noite',
                }
                
            print(f'Paciente {nome.title()} está agendado')
        except Exception as erro:
            print(f'erro: {erro}')
        
        #Se já tiver paciente na lista depacientes do horário da manhã
        
        if len(self.noite) > 0:
            
            agenda_diponivel = False
            
            for pacientes_agendados in self.noite:
                if paciente['data'] != pacientes_agendados['data'] :#Varrendo a lista e comparando as datas
                    #Se a data está diponivel entao:
                    agenda_diponivel = True
            
            #Aí podemos adicionar
            if agenda_diponivel:
                self.tarde.append(paciente)
            else:
                print('\nJá existe uma paciente para esta dia, tente agendar para outro')
                
        #Se não tiver pacientes na lista de pacientes da manhã
        else:
            self.noite.append(paciente)

lista_de_leitos = []

if __name__=='__main__':
        #criando 199 leitos:
    pass