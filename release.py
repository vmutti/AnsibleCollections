#!/bin/env python3
import subprocess
import json
import os
import yaml
import re

def header(message,char='*'):
    message = " "+message+" "
    count_l = int(((50-len(message))/2)/len(char))
    count_r = int((50-len(message)-count_l)/len(char))
    print(char*count_l+message+(char*count_r))

collections_dir = os.getcwd()+"/.ansible"
subprocess.run(
    [
        'ansible-galaxy',
        'collection',
        'install',
        '-p', 
        collections_dir, 
        '-r', 
        "./requirements.yml", 
        '--force'
    ]
)

collections_results = subprocess.run(
    [
        'ansible-galaxy',
        'collection',
        'list',
        '-p',
        collections_dir,
        '--format',
        'json'
    ], 
    capture_output=True
)
collections = json.loads(collections_results.stdout)
target_collections = collections[collections_dir+'/ansible_collections'].keys()


for collection in target_collections:
    header(collection,'#')
    verify_results = subprocess.run(
        [
            'ansible-galaxy',
            'collection',
            'verify',
            '-p',
            collections_dir,
            collection
        ],
        capture_output=True
    )
    verify_output=verify_results.stdout.decode()
    verify_errors=verify_results.stderr.decode()
    modified_message = 'contains modified content in the following files'
    modified = modified_message in verify_output
    missing_message = 'HTTP Code: 404, Message: Not found.'
    missing=verify_results.returncode==1 and missing_message in verify_errors
    collection_path = './collections/'+collection.split('.')[1] 
    if modified:
        galaxy_file_path = collection_path+'/galaxy.yml'
        with open(galaxy_file_path,'r+') as galaxy_file:
            galaxy_contents = yaml.safe_load(galaxy_file)
            old_version = galaxy_contents['version']
            version_parts = old_version.split('.')
            new_version = '.'.join(
               version_parts[:2]+[str(int(version_parts[2])+1)]
            )
            print(verify_output)
            header('Bumping '+collection+' version '+old_version+' => '+new_version,'*')

            galaxy_file.seek(0)
            galaxy_file_contents = galaxy_file.read()
            regx = re.compile(r"^version:\W+\d+\.\d+\.\d+$", re.MULTILINE)
            
            galaxy_file.seek(0)
            new_galaxy_file=regx.sub(
                'version: '+new_version,
                galaxy_file_contents,
                1
            )
            galaxy_file.write(new_galaxy_file)
            galaxy_file.truncate()
    if modified or missing:
        header('Bundling '+collection,'*')
        bundle_results = subprocess.run(
            [
                'ansible-galaxy',
                'collection',
                'build',
                '--output-path=./builds',
                '--force',
                collection_path
            ], 
            capture_output=True
        )
        bundle_path = bundle_results.stdout.decode().split(' ')[-1].strip()
        print(bundle_results.stdout.decode().strip())
        header('Publishing '+collection,'*')
        subprocess.run(
            [
                'ansible-galaxy',
                'collection',
                'publish',
                bundle_path,
                '--token',
                os.environ['ANSIBLE_GALAXY_TOKEN']
            ], 
        )
    else:
        header('Up to date','*')

