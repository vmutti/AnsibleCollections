#!/bin/env python


  
DOCUMENTATION = '''
    name: inverted_group Inventory
    plugin_type: inventory
    author:
      - Joshua Makinen (@joshuamakinen)
    short_description: Inverts the normal Ansible inventory group relationship to list the parents of a host/group instead of listing the group's children.
    description:
        - "n/a"
    version_added: "n/a"
    inventory: inverted_group
    options:
        plugin:
            description: Token that ensures this is a source file for the plugin.
            required: True
            choices: ['inverted_group', 'vmutti.fancy_groups.inverted_group']
        host_suffix:
            description: suffix appended to each host name
            required: False
        group_prefix:
            description: prefix prepended to each group name
            required: False
        hosts:
            description:
                - List of hosts, which include a list of their parent groups.
            required: False
        groups:
            description:
                - List of groups, which include a list of their parent groups.
            required: False
    requirements:
        - python >= 2.7
'''
EXAMPLES = r'''
# example inverted_group.yml file
---
plugin: vmutti.fancy_groups.inverted_group
hosts:
  example-host:
    parents:
    - devops_tools_installed
groups:
  devops_tools_installed:
    parents:
    - dev_tools_installed
    - ops_tools_installed
'''

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.inventory import BaseFileInventoryPlugin
class InventoryModule(BaseFileInventoryPlugin):

    NAME = 'vmutti.fancy_groups.inverted_group'

    def verify_file(self, path):
      super(InventoryModule, self).verify_file(path)
      return path.endswith(('igroup.yml', 'igroup.yaml','inverted_group.yml', 'inverted_group.yaml'))

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)
        self._read_config_data(path)
        host_suffix = self.get_option('host_suffix')
        if not(host_suffix):
            host_suffix=""
        group_prefix = self.get_option('group_prefix')
        if not(group_prefix):
            group_prefix=""
        hosts_in = self.get_option('hosts')
        if hosts_in:
            for host, hostdata in hosts_in.items():
                for parent in hostdata['parents']:
                    self.inventory.add_group(group_prefix+parent)
                    self.inventory.add_host(host+host_suffix,group_prefix+parent)

        groups_in = self.get_option('groups')
        if groups_in:
            for group, groupdata in groups_in.items():
                self.inventory.add_group(group_prefix+group)
                for parent in groupdata['parents']:
                    self.inventory.add_group(group_prefix+parent)
                    self.inventory.add_child(group_prefix+parent,group_prefix+group)
