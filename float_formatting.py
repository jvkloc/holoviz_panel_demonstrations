from bokeh.models.widgets.tables import NumberFormatter
from pandas import DataFrame as df
from panel import Column
from panel.template import FastListTemplate
from panel.widgets import IntInput, StaticText, Tabulator

class GUI():
    
    def __init__(self):
        self.data = df({
            'a': [2.718281, 3.141592, 1.618033],
            'b': [0.007874, 0.915965, 1.732050],
        })
        self.precision = self.precision()
        self.tabulator = self.tabulator()

    def tabulator(self): 
        rows = self.data.transpose().index.tolist()
        tab_format = {
            row: NumberFormatter(format='0.0')
            for row in rows
        }
        return Tabulator(self.data, formatters=tab_format)

    def callback(self, event):
        value = f"0.{event.new * '0'}"
        rows = self.data.transpose().index.tolist()
        tab_format = {
            row: NumberFormatter(format=value) 
            for row in rows
        }
        self.tabulator.formatters = tab_format

    def precision(self): 
        decimals = IntInput(
            name='Select the number of decimals (0-6)', 
            value=1, 
            step=1, 
            start=0, 
            end=6
        )
        decimals.param.watch(self.callback, 'value')
        return decimals
    

def main():
    gui = GUI()
    wikipedia = StaticText(
        value='https://en.wikipedia.org/wiki/List_of_mathematical_constants'
    )
    template = FastListTemplate(
        title='Float formatting',
        main=Column(gui.precision, gui.tabulator, wikipedia)
    )
    template.show()

if __name__ == '__main__':
    main()