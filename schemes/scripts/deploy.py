import os
import argparse

PATH = os.path.abspath(os.curdir)
ENVIRONMENTS_DIR = os.path.join(PATH, 'environments')

environments = [
    name for name in os.listdir(ENVIRONMENTS_DIR)
    if os.path.isdir(os.path.join(ENVIRONMENTS_DIR, name))
]

parser = argparse.ArgumentParser()

parser.add_argument(
    '--inventory', '-i',
    type=str,
    choices=environments,
    help='specify inventory host path',
)

if __name__ == '__main__':
    args = parser.parse_args()
    template = 'ansible-playbook -i environments/{} site.yml'
    command = template.format(args.inventory)
    os.system(command)
