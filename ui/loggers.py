from abc import ABC, abstractmethod
from distutils.log import Log

class Logger(ABC):
    def __init__(self) -> None:
        super().__init__()
    @abstractmethod
    def log(text: str):
        pass

class QtLogger(Logger):
    def __init__(self, ui_element) -> None:
        super().__init__()
        self.ui_element = ui_element

    def log(self, text: str):
        self.ui_element.append(f'<p style="color: green;">LOGGER: {text}</p>')


