user_input = 'random'
data = []


def show_menu():
    print('menu:')
    print('1. add an item')
    print('2. mark as done')
    print('3. view items')
    print('4. exit')

while user_input != '4':

    show_menu()
    user_input = input('enter you choices:')
    
    if user_input == '1':
        item = input('what is to be done?')
        data.append(item)
        print('added item', item)
    elif user_input == '2':
        item = input('what is to be marked as done?')
        if item in data:
            data.remove(item)
            print('removed item:')
        else:
            print('item does not exist in the list')
    elif user_input == '3':
        print('list of to-do items:')
        for item in data:
            print(item)
    
    elif user_input == '4':
        print('goodbye')
    else:
        print('please enter one 1, 2 3 or 4')



