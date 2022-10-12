#!/usr/bin/python

# Copyright: (c) 2022, Kirill Setdekov <ksetdekov@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: clickhouse

short_description: This is clickhouse users management module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: Basic detailed description

author:
    - Kirill Setdekov (@ksetdekov)
'''

EXAMPLES = r'''
# Pass in a message
- name: Connect to DBMS clickhouse and create user
    clickhouse:
        login_user: default
        login_password: default
        user: new username
        password:  new user's password


- name: Connect to DBMS clickhouse and delete user
    clickhouse:
        login_user: default
        login_password: default
        user: deleted username
        password:  absent
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
mutations:
    description: List of executed mutation querries
    returned: always
    type: list
    sample: ['CREATE USER %(new_user)s {"new_user": "john"}']
    version: '2.8'
'''

from ansible.module_utils.basic import AnsibleModule


def main():

    module_args = {
        "login_user": {"type":"str", "required":True},
        "login_password": {"type":"str", "required":True},
        "user": {"type":"str", "required":True},
        "password": {"type":"str", "required":False},
        "state": {"type":"str", "required":False, "default": "new"}
    }

    result = {
        "changed":False
    }

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    module.exit_json(**result)




if __name__ == '__main__':
    main()
