import cv2

def start_video_capture():
    """
    Inicia a captura de vídeo da câmera.
    """
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro ao acessar a câmera.")
        exit()

    return cap
