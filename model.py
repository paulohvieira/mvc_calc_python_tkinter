'''
15-10-24
'''

class Model:
    '''
    Model
    '''
    def __init__(self):
        '''
        Contructor
        '''
        self.previous_value: str = ''
        self.value: str = ''
        self.operator: str = ''

    def calculate(self, caption: str) -> str:
        match caption:
            case 'C':
                self.previous_value = ''
                self.value = ''
                self.operator = ''

            case '±':
                try:
                    self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
                except IndexError:
                    pass
            case '%':
                self.value /= 100
            case '/':
                self.operator = '/'
            case 'x':
                self.operator = 'x'
            case '-':
                self.operator = '-'
            case '+':
                self.operator = '+'
            case '.':
                if not '.' in self.value:
                    self.value += caption
            case '=':
                self.value = self.value
            case _:
                self.value += str(caption)

        return self.value