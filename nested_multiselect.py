from panel import Column, Row
from panel.template import FastListTemplate
from panel.widgets import Button, MultiSelect, Select, StaticText


info = StaticText(
    value=f"""The options of the MultiSelect widget depend on the value of the 
    Select widget. <br> A line change in a StaticText widget like this is done 
    with <b>&lt;br&gt;</b> and escaping <b>&lt;br&gt;</b> <br> can be done with 
    <b>&amplt;br&ampgt;</b> just like in HTML."""
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
        self.select = Select(
            name='Select widget', 
            options=select_widget_options,
            value=select_widget_options[0]
        )
        self.multiselect = MultiSelect(name='MultiSelect widget')
        self.widget_values = Column(
            Row(
                StaticText(
                    name='Select value ', 
                    value=self.select.value
                )
            ), 
            Row(
                StaticText(
                    name='MultiSelect value ', 
                    value=self.multiselect.value
                )
            )
        )
        self.reset_select_btn = Button(
            name='Reset Select widget value'
        )
        self.reset_select_btn.on_click(self.reset_select)
        self.reset_multiselect_btn = Button(
            name='Reset MultiSelect widget value'
        )
        self.reset_multiselect_btn.on_click(self.reset_multiselect)
        self.select.param.watch(self.select_callback, 'value')
        self.multiselect.param.watch(self.multiselect_callback, 'value')
    
    def reset_select(self, event):
        self.select.value = select_widget_options[0]
        self.multiselect.options = []

    def reset_multiselect(self, event):
        self.multiselect.value = []
    
    def select_callback(self, event):
        self.widget_values.objects[0].objects[0].value = self.select.value
        self.multiselect.options = dictionary[self.select.value]
    
    def multiselect_callback(self, event):
        self.widget_values.objects[1].objects[0].value = self.multiselect.value


def main():
    app = App()
    template = FastListTemplate(
        title='Select widget combined with MultiSelect widget demo',
        main=(
            Row(app.select, app.multiselect, info), 
            app.widget_values, 
            Row(app.reset_select_btn, app.reset_multiselect_btn)
        )
    )
    template.show()


if __name__ == '__main__':
    main()
