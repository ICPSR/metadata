#!/usr/bin/python3

import subprocess
import shutil
import os
import sys
import argparse

def get_cli_arguments():
    """ Parse command line arguments and return an object whose members contain the argument values. """
    parser = argparse.ArgumentParser(description="Generate markdown from JSON Schema and YAML files")
    parser.add_argument('--source-dir', dest='source_dir', type=str, help='Source directory', required=True)
    return parser.parse_args()

def main():
    try:
        args = get_cli_arguments()

        if not os.path.exists(args.source_dir):
            print(f"{args.source_dir} does not exist. Please verify path and try again")
            sys.exit(1)

        #set up variables
        site_dir = os.path.join(args.source_dir, 'site')
        resource_dir = os.path.join(args.source_dir, 'resources')
        mkdocs_yml = os.path.join(resource_dir, 'mkdocs.yml')
        # rtd_css = os.path.join(resource_dir, 'readthedocs_theme.css')
        # rtd_extra_css = os.path.join(resource_dir, 'readthedocs_theme_extra.css')
        
        if not os.path.exists(site_dir):
            os.makedirs(site_dir)

        #generate html; run mkdocs
        cmd = 'mkdocs build -f {} --clean --verbose'.format(mkdocs_yml)
        subprocess.run(cmd, shell=True)

        #add improved CSS
        # shutil.copy(rtd_css, os.path.join(site_dir, 'css', 'theme.css'))
        # shutil.copy(rtd_extra_css, os.path.join(site_dir, 'css', 'theme_extra.css'))

    except Exception as ex: # pylint: disable=broad-except
        sys.exit(1)

if __name__=='__main__':
    main()