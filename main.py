
import argparse
import json
import logging
import os
import sys

from phm import run_translator, list_handlers

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("system.log"), logging.StreamHandler(sys.stdout)],
)

parser = argparse.ArgumentParser(description="Processing images labeled by GIMP")
parser.add_argument('--dir_in', '--dir', '-d', type=str, help="Directory containing the images.")
parser.add_argument('--file_out', '--dir_out', '--out', '-o', type=str, required=False, help="Output Directory")
parser.add_argument('--handler', '--type', required=False, default='mask', choices=list_handlers(), help="Handler Type")
parser.add_argument('--binarize', '-b', action='store_true', help="Whether binarize the masks.")
parser.add_argument('--num_worker', '-w', type=int, required=False, default=1, help="Number of workers.")
parser.add_argument('--config', type=str, required=False, help='Configuration file')
parser.add_argument('--name', '-n', type=str, required=False, default='', help='Dataset name')
parser.add_argument('--info', type=str, required=False, default='', help='Description')
parser.add_argument('--url', type=str, required=False, default='', help='URL')
parser.add_argument('--version', type=str, required=False, default='', help='Version')
parser.add_argument('--year', type=int, required=False, default=2022, help='Year')
parser.add_argument('--contrib', type=str, required=False, default='Parham Nooralishahi', help='Contributor')
parser.add_argument('--category', '-c', action='append', help='Class Categories')

def main():

    args = parser.parse_args()
    parser.print_help()

    config = {}
    if args.config is not None:
        if not os.path.isfile(args.config) or not args.config.endswith('.json'):
            logging.error(f'{args.config} is not valid!')
            return
        
        with open(args.config, 'r') as fin:
            config = json.load(fin)
    else:
        config = vars(args)

    run_translator(
        config['dir_in'], 
        config['handler'], **config)

if __name__ == "__main__":
    main()