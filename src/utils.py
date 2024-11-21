import logging

def setup_logging():
    """
    Configura o logging para o projeto.
    """
    logging.getLogger("ultralytics").setLevel(logging.WARNING)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
