from pygame import mixer
from datetime import datetime
from time import sleep


class Alarme:
    def __init__(self, time: str, vol: float = 1.0) -> None:
        """Definição do alarme

        Args:
            time (str): Hora do dia em que o alarme irá soar
            vol (float, optional): Volume da faixa de som 
            (0.0 to 1.0). Defaults to 1.0.
        """
        self.song = 'songs\\alarm_clock.mp3'
        self.time = time
        self.vol = vol

    def tocar(self) -> None:
        """Executa a faixa e alarme
        """
        mixer.init()
        mixer.music.load(self.song)
        mixer.music.set_volume(self.vol)
        mixer.music.play()
        input('Aperte enter para finalizar a música. ')
        mixer.pause()

    def agendar(self) -> None:
        """Função responsável pelo gerenciamento
        do tempo e chamada da execução da faixa 
        sonara
        """
        
        print(f"\nNão fechar o terminal, o alarme soará\
em: {self.time}.")
        
        while True:
            """Tratamento para poder comparar a hora digtada
            com a hora verificada com sistema.
            """
            hora_A = datetime.now().time().hour
            min_A = datetime.now().time().minute
            hora_E = int(self.time[0:2])
            min_E = int(self.time[3:])
            
            time_A = f'{hora_A}:{min_A}'
            time_E = f'{hora_E}:{min_E}' 
             
            
            if time_A == time_E:
                """Executa a chamada para a função de play
                caso o horário da agendado chegue
                """
                self.tocar()
                break
        print('\nFinalizado.')
            
            
if __name__ == '__main__':
    """Executa todo os código
    """
    
    while True:
        try:
            """Vai receber o input e verificar se 
            está dentro do padrão esperado
            """
            
            time = input('Informe a hora para tocar\
o alarme [HH:MM]: ').strip()
            erro = False
            if len(time) != 5:
                print('Erro! Formato inválido.\nTente novamente')
                erro = True
            elif int(time[0:2]) > 23 or int(time[0:2]) < 0:
                print('Erro! Hora inválida.\nTente novamente.')
                erro = True
            elif int(time[3:]) > 59 or int(time[3:]) < 0:
                print('Erro! Minutos inválidos.\nTente novamente.')
                erro = True               
            elif not time.__contains__(':'):
                print('Erro! Formato inválido.\nTente novamente')
                erro = True
        except Exception as e:
            print(f'\nErro! {e}.\nTente Novamente')
        else:
            if erro:
                pass
            else:
                break
    
    while True:
        """Vai receber o input e verificar se 
        está dentro do padrão esperado
        """
        try:
            volume = float(input('Informe o volume\
do alarme [0.0 mais baixo, 1.0 mais alto]: '))
        except Exception as e:
            print(f'Erro! {e}.\nTente novamente')
        else:
            break
            
    Alarme(
        time=time,
        vol=volume
    ).agendar()
