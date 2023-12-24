from panel import Column, extension
from panel.template import FastListTemplate
from plotly.graph_objects import Bar, Figure, Pie

def bar_chart() -> Figure:
    fig = Figure()    
    names = ['name_1', 'name_2']
    values = [[8.5], [1.5]]
    for i, name in enumerate(names):
        fig.add_trace(
            Bar(
                y=[''], 
                x=values[i], 
                name=name, 
                orientation='h'
            )
        )
    fig.update_layout(
        title='Minimal example go.Bar',
        xaxis_title='x_axis',
        barmode='stack'
    )
    fig.update_traces(hovertemplate='%{y:.1f}%{x}')
    return fig


def pie_chart() -> Figure:
    fig = Figure()
    names = ['name_1', 'name_2', 'name_3']
    values = [3, 2, 5]
    fig.add_trace(
        Pie(
            labels=names,
            values=values,
            title=dict(
                text='Minimal go.Pie',
                position='top left'
            ),
            hole=0.3, 
            textposition='inside',
            hovertemplate='%{label}<br>%{value:.1f}%<extra></extra>'
        )
    )     
    return fig


def main() -> None:
    extension('plotly')
    template: FastListTemplate = FastListTemplate(
        title='Minimal example',
        main=Column(bar_chart(), pie_chart())
    )
    template.show()

if __name__ == '__main__':
    main()