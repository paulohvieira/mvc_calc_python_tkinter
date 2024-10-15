'''
15-10-24
'''
from model import Model
from view import View

class Controller:
    '''
    Controller
    '''
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        print('Hello World!')
        self.view.main()

    def on_button_click(self, caption: str) -> None:
        result = self.model.calculate(caption)
        self.view.value_var.set(result)
