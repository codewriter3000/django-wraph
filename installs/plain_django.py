import subprocess

def install(working_dir):
    subprocess.call(['mkdir', '-p', working_dir])
    subprocess.call(['cd', working_dir])
    if subprocess.call(['python', '-m', 'venv', './venv']) != 0:
        subprocess.call(['python3', '-m', 'venv', './venv'])
    subprocess.call(['./env/Scripts/activate'])

    with open('requirements.txt', 'w') as requirements:
        requirements.write('Django>=5.0\ndjangorestframework>=3.14\nPillow=10.0.1\nwheel>=0.42')

    subprocess.call(['pip', 'install', '-r', 'requirements.txt'])
    subprocess.call(['django-admin.py', 'startproject', 'config', '.'])
