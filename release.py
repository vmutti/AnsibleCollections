#!/bin/env python3
import subprocess
import json
import os
import yaml
import re

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
    modified_message = 'contains modified content in the following files'
    modified = modified_message in verify_results.stdout.decode()
    if modified:
        collection_path = './collections/'+collection.split('.')[1] 
        galaxy_file_path = collection_path+'/galaxy.yml'
        with open(galaxy_file_path,'r') as file:
            galaxy_contents = yaml.safe_load(file)
        old_version = galaxy_contents['version']
        version_parts = old_version.split('.')
        new_version = '.'.join(
           version_parts[:2]+[str(int(version_parts[2])+1)]
        )
        with open(galaxy_file_path,'r+') as galaxy_file:
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
        bundle_path = bundle_results.stdout.decode().split(' ')[-1]
        bundle_results = subprocess.run(
            [
                'ansible-galaxy',
                'collection',
                'publish',
                bundle_path,
            ], 
        )
        print(collection,old_version,'=>',new_version)

