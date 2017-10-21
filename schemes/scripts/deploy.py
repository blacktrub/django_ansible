import os
import argparse

# todo: need get only existing environments
environments = ('prod', 'stage', 'dev',)

parser = argparse.ArgumentParser()

parser.add_argument(
    '--inventory', '-i',
    type=str,
    choices=list(environments),
    help='specify inventory host path',
)

if __name__ == '__main__':
    args = parser.parse_args()
    template = 'ansible-playbook -i environments/{} site.yml'
    command = template.format(args.inventory)
    os.system(command)
