'''
15-10-24
'''
import  tkinter     as tk
from    tkinter     import ttk


class View(tk.Tk):
    '''
    View
    '''

    PAD: int = 10
    MAX_BUTTONS_PER_ROW: int = 4
    button_caption: list[str] = [
        'C', '±', '%', '/',
        '7', '8', '9', 'x',
        '4', '5', '6', '-',
        '1', '2', '3', '+',
        '0', '.', '='
    ]

    def __init__(self, controller):
        '''
        Contructor
        '''
        super().__init__()
        self.title('Python Calculator')
        self.controller = controller

        self.value_var: tk.StringVar = tk.StringVar()

        self._make_main_frame()
        self._make_entry()
        self._make_buttons()
    
    def main(self):
        self.mainloop()
    
    def _make_main_frame(self) -> None:
        self.main_frm: ttk.Frame = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)
    
    def _make_entry(self):
        ent: ttk.Entry = ttk.Entry(
            self.main_frm, justify='right', textvariable=self.value_var, state='disable'
            )
        ent.pack(fill='x')
    
    def _make_buttons(self):
        outer_frm: ttk.Frame = ttk.Frame(self.main_frm)
        outer_frm.pack()

        frm: ttk.Frame = ttk.Frame(outer_frm)
        frm.pack()

        butttons_in_row: int = 0

        for caption in self.button_caption:
            if butttons_in_row == self.MAX_BUTTONS_PER_ROW:
                frm: ttk.Frame = ttk.Frame(outer_frm)
                frm.pack()
                butttons_in_row = 0
            btn: ttk.Button = ttk.Button(frm,
                                         text=caption,
                                         command=(lambda button=caption: self.controller.on_button_click(button))
                                        )
            btn.pack(side='left')

            butttons_in_row += 1
