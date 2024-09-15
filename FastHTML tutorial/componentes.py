from fasthtml.common import Div, H1, P, Form, Input, Button, Ul,Li,A
#componentes que vamos usar
def gerar_titulo(titulo, subtitulo):
    return Div(#isto vai retornar um elemento -->> Div
        H1(titulo),
        P(subtitulo),
    )
    
def gerar_formulario():
    formulario =  Form(
        Input(type='text', name='tarefa', placeholder='Insira a tarefa'),
        Button('Enviar'),
        method="post",#enviando uma informação
        action="/adicionar_tarefa",
        hx_post="/adicionar_tarefa",#Ação que será realizada
        hx_target="#lista-de-tarefas",#item que vai mudar, modificação do elemento através do id
        hx_swap='outerHTML',#o que vai alterar/editar, no caso substituir o elemento inteiro para isso usa-se:outerHTML
    )
    return formulario

def gerar_lista_de_tarefas(lista_de_itens):
    item_da_lista = [Li(tarefa, ' - ', A('Excluir',
                                        hx_get=f"/deletar{i}",
                                        hx_target="#lista-de-tarefas",
                                        hx_swap="outerHTML" )
                        ) for i,tarefa in enumerate(lista_de_itens)]
    
    return Ul(
        *item_da_lista, id='lista-de-tarefas'#passando sem colchetes uso do asterísco
    )
    
    
    
    