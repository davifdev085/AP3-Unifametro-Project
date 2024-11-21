import time
import cv2
from src.detector import initialize_model, count_people
from src.ac_control import control_ac
from src.video_capture import start_video_capture
from src.utils import setup_logging


def display_people_count(frame, people_count):
    """
    Exibe o número de pessoas detectadas no frame.

    Args:
        frame (ndarray): O frame do vídeo.
        people_count (int): O número de pessoas detectadas.

    Returns:
        ndarray: O frame com a contagem de pessoas exibida.
    """
    cv2.putText(frame, f"Pessoas na sala: {people_count}", (5, 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 5, 54), 2)
    return frame


def display_ac_status(frame, ac_on_flag, ac_off_flag):
    """
    Exibe o status do ar condicionado no frame.

    Args:
        frame (ndarray): O frame do vídeo.
        ac_on_flag (bool): Flag que indica se o ar condicionado está ligado.
        ac_off_flag (bool): Flag que indica se o ar condicionado está desligado.

    Returns:
        ndarray: O frame com o status do ar condicionado exibido.
    """
    status_text = "Ar Condicionado: Ligado" if ac_on_flag else "Ar Condicionado: Desligado"
    color = (0, 255, 0) if ac_on_flag else (0, 0, 255)
    cv2.putText(frame, status_text, (5, frame.shape[0] - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
    return frame


def main():
    """
    Função principal que gerencia a captura de vídeo, detecção de pessoas e controle do ar condicionado.
    """
    setup_logging()  # Configura o logging

    # Inicializa o modelo YOLO para detecção de objetos
    model = initialize_model('yolov8n.pt')

    # Inicializa a captura de vídeo
    cap = start_video_capture()

    # Flags para controle do estado do ar condicionado
    ac_on_flag = False
    ac_off_flag = False

    # Tempos de controle para ligar/desligar o ar condicionado
    last_ac_on_time = time.time()
    last_ac_off_time = time.time()

    # Loop principal para captura e processamento de frames
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Falha ao capturar frame.")
            break

        # Contar o número de pessoas no frame atual
        people_count, frame = count_people(frame, model)

        # Exibir a contagem de pessoas no vídeo
        frame = display_people_count(frame, people_count)

        # Controlar o estado do ar condicionado com base no número de pessoas
        ac_on_flag, ac_off_flag, last_ac_on_time, last_ac_off_time = control_ac(
            people_count, ac_on_flag, ac_off_flag, last_ac_on_time, last_ac_off_time
        )

        # Exibir o status do ar condicionado no vídeo
        frame = display_ac_status(frame, ac_on_flag, ac_off_flag)

        # Exibe o frame com as informações atualizadas
        cv2.imshow('Detecção de Pessoas e Controle de Ar Condicionado', frame)

        # Condição para sair do loop (pressione 'q' para sair)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera os recursos da captura de vídeo e fecha as janelas do OpenCV
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
