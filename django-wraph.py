import util.colors as colors

import installs.plain_django as plain_django

if '__main__' == __name__:
    print('Welcome to Django Wraph. Follow this setup in order to generate a boilerplate for your project.')

    project_name = ''
    while True:
        project_name = input(f'Project name/working directory: \n{colors.cyan_text('? ')}')

        if project_name == '':
            print(colors.red_text('Please enter a valid project name.\n'))
        else:
            break

    print(f'{colors.green_text('Project name is:')} {project_name}')

    install_types = ['Plain django app', 'User model', 'User model + API', 'User model + API + Template']
    selected_install_type = ''
    while True:
        print('Select an install type:\n')
        print(f'1) {colors.yellow_text(install_types[0])}')
        print(f'2) {colors.green_text(install_types[1])}')
        print(f'3) {colors.cyan_text(install_types[2])}')
        print(f'4) {colors.blue_text(install_types[3])}')

        selected_install_type = input(colors.cyan_text('? '))

        if selected_install_type not in ['1', '2', '3', '4']:
            print(colors.red_text('Please enter either 1, 2, 3, or 4.'))
        else:
            break

    if selected_install_type == '1':
        print(colors.green_text('Creating Django project'))
        plain_django.install(project_name)
