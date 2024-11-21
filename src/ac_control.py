import time

# Parâmetros globais
TIME_TO_TURN_ON = 15
TIME_TO_TURN_OFF = 30
MIN_PEOPLE_COUNT = 2


def control_ac(people_count, ac_on_flag, ac_off_flag, last_ac_on_time, last_ac_off_time):
    """
    Controla o ar condicionado baseado no número de pessoas detectadas.
    """
    # Verifica se o número de pessoas é suficiente para ligar o ar condicionado
    if people_count >= MIN_PEOPLE_COUNT and not ac_on_flag:
        ac_on_flag = True
        ac_off_flag = False
        print("O ar condicionado foi ligado.")

    # Desliga o ar condicionado imediatamente quando não houver pessoas
    elif people_count == 0 and ac_on_flag:
        ac_off_flag = True
        ac_on_flag = False
        print("O ar condicionado foi desligado.")

    return ac_on_flag, ac_off_flag, last_ac_on_time, last_ac_off_time
