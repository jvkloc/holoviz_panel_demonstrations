from panel import Row
from panel.template import FastListTemplate
from panel.widgets import Button, MultiSelect, StaticText


class App():
    
    def __init__(self):
        self.tags = MultiSelect(
            name='MultiSelect widget', 
            options=['option_0', 'option_1', 'option_2']
        )
        self.printed = Row(StaticText(
                name='MultiSelect widget value ', value=self.tags.value
            )
        )
        self.reset = Button(name='Reset MultiSelect widget value')
        self.reset.on_click(self.reset_callback)
        self.tags.param.watch(self.selector_callback, 'value')

    def reset_callback(self, event):
        self.tags.value.clear()
        self.printed.__setitem__(0, StaticText(
                name='MultiSelect widget value ', value=self.tags.value
            )
        )
    
    def selector_callback(self, event):
        self.printed[0].value = self.tags.value


def main():
    app = App()
    template = FastListTemplate(
        title='MultiSelect widget demo',
        main=(app.tags, app.printed, app.reset)
    )
    template.show()


if __name__ == '__main__':
    main()
