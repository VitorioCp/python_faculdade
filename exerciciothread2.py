import time
from threading import Thread

def funcao(tempo_espera, mensagem):
    print(f'\nIniciando a tarefa {mensagem}')
    time.sleep(tempo_espera)
    print(f'Conclusao da tarefa {mensagem}')

t1 = Thread(target=funcao, args=(3, 'A'))
t2 = Thread(target=funcao, args=(2, 'B'))
t1.start()
t2.start()
t1.join()
t2.join()

print("A execucao foi concluida")
