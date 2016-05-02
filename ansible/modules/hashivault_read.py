#!/usr/bin/env python
DOCUMENTATION = '''
---
module: hashivault_read
version_added: "0.1"
short_description: Hashicorp Vault read module
description:
    - Module to read to Hashicorp Vault.
options:
    url:
        description:
            - url for vault
        default: False
    username:
        description:
            - username to login to vault.
        default: False
    password:
        description:
            - password to login to vault.
        default: False
    secret:
        description:
            - secret to operate on.
        default: False
    field:
        description:
            - secret field to operate on.
        default: False
'''
EXAMPLES = '''
- action: hashivault_read secret=foo field=bar
'''


def main():
    module = hashivault_init()
    result = hashivault_read(module.params)
    if result.get('failed'):
        module.fail_json(**result)
    else:
        module.exit_json(**result)


from ansible.module_utils.basic import *
from ansible.module_utils.hashivault import *

if __name__ == '__main__':
    main()