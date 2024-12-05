#!/bin/env python


  
DOCUMENTATION = '''
    name: Vagrant Inventory
    plugin_type: inventory
    author:
      - Joshua Makinen (@joshuamakinen)
    short_description: Dynamic inventory plugin for Vagrant machines.
    description:
        - Calls into vagrant to fetch information on where to find different guests
    version_added: "n/a"
    inventory: vagrant
    options:
        plugin:
            description: Token that ensures this is a source file for the plugin.
            required: True
            choices: ['vagrant','makinj.vagrant.vagrant']
        project_path:
            description:
                - The path directory where Vagrant commands will be run
            required: True
    requirements:
        - python >= 2.7
    extends_documentation_fragment:
      - inventory_cache
'''
EXAMPLES = r'''
# example vagrant.yml file
---
plugin: makinj.vagrant.vagrant
project_path: ~/vagrant/
'''

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.inventory import BaseFileInventoryPlugin, Cacheable

import os
import sys
import subprocess
import yaml
import json



def get_machines():
    command=["vagrant","status", "--machine-readable"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print(error)
    machines=[]
    for line in output.decode().split('\n'):
        parts=line.split(",")
        if len(parts)>=3 and parts[2]=="state":
            machines.append(parts[1])
    print('got machines:',machines)
    return machines

def get_ssh_port(machine):
    command=["vagrant","port", machine, "--machine-readable"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print(error)
    for line in output.decode().split('\n'):
        parts=line.split(",")
        if len(parts)>=5 and parts[2]=="forwarded_port" and parts[3]=="22":
            return int(parts[4])
    return None

inventory={}


class InventoryModule(BaseFileInventoryPlugin, Cacheable):

    NAME = 'makinj.vagrant.vagrant'

    def verify_file(self, path):
      super(InventoryModule, self).verify_file(path)
      return path.endswith(('vagrant.yml', 'vagrant.yaml'))

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)
        self._read_config_data(path)


        cache_key = self.get_cache_key(path)


        # cache may be True or False at this point to indicate if the inventory is being refreshed
        # get the user's cache option too to see if we should save the cache if it is changing
        user_cache_setting = self.get_option('cache')

        # read if the user has caching enabled and the cache isn't being refreshed
        attempt_to_read_cache = user_cache_setting and cache
        # update if the user has caching enabled and the cache is being refreshed; update this value to True if the cache has expired below
        cache_needs_update = user_cache_setting and not cache
        results = {}
        # attempt to read the cache if inventory isn't being refreshed and the user has caching enabled

        if attempt_to_read_cache:
            try:
                results = self._cache[cache_key]
            except KeyError:
                print('failed to find in cache')
                # This occurs if the cache_key is not in the cache or if the cache_key expired, so the cache needs to be updated
                cache_needs_update = True

        if not attempt_to_read_cache or cache_needs_update:
            results = self.fetch()

        if cache_needs_update:
            self._cache[cache_key] = results


        self.populate(results)


    def fetch(self):
        results={}

        project_path_in = self.get_option('project_path')
        if os.path.isabs(project_path_in):
            project_path = project_path_in
        else:
            project_path = os.path.join(os.path.dirname(path), project_path_in)
        starting_path=os.getcwd()
        os.chdir(project_path)

        machines = get_machines()
        for machine in machines:
            results[machine]={}
            ssh_port = get_ssh_port(machine)
            if ssh_port:
                results[machine]['ssh_port']=ssh_port
        os.chdir(starting_path)
        print('got results',results)

        return results

    def populate(self, results):
        vagrant_group_name='vagrant_guest'
        print('populating',results)

        self.inventory.add_group(vagrant_group_name)
        self.inventory.set_variable(vagrant_group_name,'ansible_host', '127.0.0.1')

        not_running_group_name='not_running'
        self.inventory.add_group(not_running_group_name)
        running_group_name='running'
        self.inventory.add_group(running_group_name)
        for machine_name, machine in results.items():
            host_name = self.inventory.add_host(machine_name,vagrant_group_name)

            if 'ssh_port' in machine:
                self.inventory.add_host(machine_name,running_group_name)
                self.inventory.set_variable(machine_name,'ansible_port', machine['ssh_port'])
            else:
                host_name = self.inventory.add_host(machine_name,not_running_group_name)
