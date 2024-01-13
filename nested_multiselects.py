from panel import Column, Row
from panel.template import FastListTemplate
from panel.widgets import Button, MultiSelect, StaticText


info = StaticText(
    value=f"""The options of the dependent MultiSelect widget depend on the 
    values of the independent MultiSelect widget. <br> A line change in a 
    StaticText widget like this is done with <b>&lt;br&gt;</b> and escaping 
    <b>&lt;br&gt;</b> can be done with <b>&amplt;br&ampgt;</b> <br> just like 
    in HTML."""
)

dictionary = {
    'None' : [],
    'key_1' : ['A', 'B', 'C'], 
    'key_2' : ['D', 'E', 'F'],
    'key_3': ['G', 'H', 'I']
}
select_widget_options = list(dictionary.keys())

class App():
    
    def __init__(self):
        self.select = MultiSelect(
            name='Independent MultiSelect widget', 
            options=select_widget_options,
            value=[select_widget_options[0]]
        )
        self.multiselect = MultiSelect(name='Dependent MultiSelect widget')
        self.widget_values = Column(
            Row(
                StaticText(
                    name='Independent MultiSelect value ', 
                    value=self.select.value
                )
            ), 
            Row(
                StaticText(
                    name='Dependent MultiSelect value ', 
                    value=self.multiselect.value
                )
            )
        )
        self.reset_select_btn = Button(
            name='Reset independent MultiSelect widget value'
        )
        self.reset_select_btn.on_click(self.reset_select)
        self.reset_multiselect_btn = Button(
            name='Reset dependent MultiSelect widget value'
        )
        self.reset_multiselect_btn.on_click(self.reset_multiselect)
        self.select.param.watch(self.select_callback, 'value')
        self.multiselect.param.watch(self.multiselect_callback, 'value')
    

    def reset_select(self, event):
        self.select.value = [select_widget_options[0]]
        self.multiselect.options = []


    def reset_multiselect(self, event):
        self.multiselect.value = []
    

    def select_callback(self, event):
        self.widget_values.objects[0].objects[0].value = self.select.value
        options = []
        for value in self.select.value:
            options += dictionary[value]
        self.multiselect.options = options
    

    def multiselect_callback(self, event):
        self.widget_values.objects[1].objects[0].value = self.multiselect.value


def main():
    app = App()
    template = FastListTemplate(
        title='Nested MultiSelect widgets demo',
        main=(
            Row(app.select, app.multiselect, info), 
            app.widget_values, 
            Row(app.reset_select_btn, app.reset_multiselect_btn)
        )
    )
    template.show()


if __name__ == '__main__':
    main()