from fasthtml.common import *
from componentes import gerar_titulo, gerar_formulario, gerar_lista_de_tarefas

app,route = fast_app()
lista_de_tarefas = []

@route('/')
def homepage(): 
    formulario = gerar_formulario()
    print(lista_de_tarefas)
    elemento_lista_de_tarefa = gerar_lista_de_tarefas(lista_de_tarefas)
    return gerar_titulo('Lista de tarefas','Usando o fast html'),formulario, elemento_lista_de_tarefa

@route('/Blog')
def blog(): 
    return gerar_titulo('Blog','Boguinho Bunitinho com conteudinhos de python')

@route("/adicionar_tarefa", methods=["post"])#recebe o method post
def adicionar_tarefa(tarefa: str):#obrigatório atribuir o tipo de váriável no parâmetro
    if tarefa:
        lista_de_tarefas.append(tarefa)
    return gerar_lista_de_tarefas(lista_de_tarefas)#Usando o HTMX

    #como usamos o HTMX nas funções adicionar_tarefa e deletar_tarefa, não precisamos mais deste bloco no return
    #RedirectResponse(url="/", status_code=303)#Redicionamento para o inicio da página com status code 303

@route("/deletar{indice_do_item_a_ser_apagado}")
def deletar_tarefa(indice_do_item_a_ser_apagado:int):
    if len(lista_de_tarefas) > indice_do_item_a_ser_apagado:
        lista_de_tarefas.pop(indice_do_item_a_ser_apagado)    
    return RedirectResponse(url="/", status_code=303)#Redicionamento

if __name__=='__main__':
    serve()