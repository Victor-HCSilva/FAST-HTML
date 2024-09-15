### FastHTML explicações e observações (2024-09-14)
- instalação da biblioteca
```
pip install fast-html
```
- app e route:
    - app e route recebem o fast_app() e usamos funções para cada @route('/endereco').


- Escrevendo algo:
```
from fasthtml.common import *

app,route = fast_app()

@route('/')
def homepage(): 
    return '<h1>olá mundo</h1>'

if __name__=='__main__':
    serve()
```
- Como usar atributos do HTML, exemplo:
    - Criando uma função em outro arquivo .py, que nos permite criar um titulo e subtitulo 
        podemos usar quantas vezes quisermos.

            from fasthtml.common import Div, H1, P

            def gerar_titulo(titulo, subtitulo):
                return Div(#isto vai retornar um elemento -->> Div
                    H1(titulo),
                    P(subtitulo),
                    P('USando o Fast-HTML')
                )

### O diferencial, o HTMLX:
- Toda a ação feita na página faz com que ela tenha que recarregar, mas com o HTMLX
podemos driblar isso, atualizando apenas o elemnto que queremos para isso precisamos incluir 3 parâmetros nas funções desejados:
    - 1) hx_get:  (hx_get,hx_post,hx_put,hx_delete):
        - Ação que vai ser realizada
    - 2) hx_target: 
        - Endereço do item que vai ser mudado, o id (#lista-de-tarefas)
    - 3) hx_swap:
        - o elemento que vai ser alterado;editado, no caso é preciso mudar todo o elemento por isso usamos o "outerHTML"
        

- Exemplo:
```
def gerar_lista_de_tarefas(lista_de_itens):
    item_da_lista = [Li(tarefa, ' - ', A('Excluir',
                                        hx_get=f"/deletar{i}",
                                        hx_target="#lista-de-tarefas",
                                        hx_swap="outerHTML" )
                        ) for i,tarefa in enumerate(lista_de_itens)]
    
    return Ul(
        *item_da_lista, id='lista-de-tarefas'#passando sem colchetes uso do asterísco
    )
```

- Extra:
    - Retorna o usuário para a página inicial
```
RedirectResponse(url="/", status_code=303)
```

    - Uso do asterisco em uma lista:

```
lista = [1,2,3,4,5]

print(lista) #Output[1,2,3,4,5]

print(*lista) #Output 1 2 3 4 5
```

