import cv2
from ultralytics import YOLO

def initialize_model(model_path: str):
    """
    Inicializa o modelo YOLO com o caminho do modelo especificado.
    """
    try:
        model = YOLO(model_path)
        return model
    except Exception as e:
        print(f"Erro ao carregar o modelo YOLO: {e}")
        exit()

def count_people(frame, model):
    """
    Processa o frame e conta o número de pessoas detectadas.
    """
    results = model(frame)
    people_count = 0

    for result in results[0].boxes.data:
        x1, y1, x2, y2, conf, cls = result.tolist()
        class_name = results[0].names[int(cls)]

        if class_name == 'person':
            people_count += 1
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f'{class_name} {conf:.2f}', (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return people_count, frame

