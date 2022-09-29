from escritorios import escritorios
from ptsatencion import ptsatencion
from transacciones import transacciones

class listad:
    def __init__(self) -> None:
        self.raiz = escritorios()
        self.ultimo = escritorios()

        
