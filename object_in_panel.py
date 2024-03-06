"A demo of an object wrapped into a Panel component."
from panel import Column

def an_object_in_panel():
    keys = [f'key_{i}' for i in range(1, 4)]
    values = [f'value_{i}' for i in range(1, 6)]
    dictionary = {key: values for key in keys}
    dictionary_in_a_column = Column(dictionary)
    
    print('Python dictionary type:', type(dictionary)
    print('The example dictionary:', dictionary)
    
    print(
        'Type of the same dictionary in a Panel Column:', 
        type(dictionary_in_a_column.objects[0])
        )
    print(
        'The same dictionary printed from the Panel Column;',
        dictionary_in_a_column.objects[0]
        )
     print(
         'It is possbile to use the dictionary from the Panel Column',
         'via Column.objects.object:' 
     )
    print(
        'type(dictionary_in_a_column.objects[0].object =',
        type(dictionary_in_a_column.objects[0].object)
    )
    print(
        'dictionary_in_a_column.objects[0].object =',
        dictionary_in_a_column.objects[0].object
    )


def main():
    an_object_in_panel()


if __name__=='__main__':
    main()