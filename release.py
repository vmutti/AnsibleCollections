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

before_sha = os.environ.get('RELEASE_BEFORE_SHA', '')
after_sha = os.environ.get('RELEASE_AFTER_SHA', 'HEAD')

changed_dirs = None
if before_sha and set(before_sha) != {'0'}:
    diff_results = subprocess.run(
        ['git', 'diff', '--name-only', before_sha, after_sha, '--', 'collections/'],
        capture_output=True
    )
    diff_output = diff_results.stdout.decode()
    changed_dirs = {
        line.split('/')[1] for line in diff_output.splitlines() if line.startswith('collections/')
    }
    header('Changed collection dirs: '+', '.join(sorted(changed_dirs)) if changed_dirs else 'Changed collection dirs: none','*')
else:
    header('No before SHA available, treating all collections as changed','*')


for collection in target_collections:
    header(collection,'#')
    collection_dir = collection.split('.')[1]
    changed = changed_dirs is None or collection_dir in changed_dirs

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
    verify_errors=verify_results.stderr.decode()
    missing_message = 'HTTP Code: 404, Message: Not found.'
    missing=verify_results.returncode==1 and missing_message in verify_errors
    modified = changed
    collection_path = './collections/'+collection_dir
    print(collection,modified,missing)
    if modified:
        galaxy_file_path = collection_path+'/galaxy.yml'
        with open(galaxy_file_path,'r+') as galaxy_file:
            galaxy_contents = yaml.safe_load(galaxy_file)
            old_version = galaxy_contents['version']
            version_parts = old_version.split('.')
            new_version = '.'.join(
               version_parts[:2]+[str(int(version_parts[2])+1)]
            )
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

