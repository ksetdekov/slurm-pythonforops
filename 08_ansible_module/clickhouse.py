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

from contextlib import suppress
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native

CHClient = None

with suppress(ImportError):
    from clickhouse_driver import Client as CHClient

def is_user_exist(ch_client, user):
    return ch_client.execute("SELECT count() FROM system.users WHERE name = %(user)s", {"user": user})[0][0] > 0


def create_new_user(ch_client, user, password):
    queries = []
    if is_user_exist(ch_client, user):
        return {"changed": False, "queries": queries}
    query = "CREATE USER %(user)s IDENTIFIED BY %(password)s"
    query_params = {"user": user, "password": password}
    ch_client.execute(query, query_params)
    queries.append(f"{query} {query_params}")
    return {"changed": True, "queries": queries}

def delete_user(ch_client, user):
    queries = []
    if not is_user_exist(ch_client, user):
        return {"changed": False, "queries": queries}
    query = "DROP USER %(user)s"
    query_params = {"user": user}
    ch_client.execute(query, query_params)
    queries.append(f"{query} {query_params}")
    return {"changed": True, "queries": queries}

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

    if CHClient is None:
        return module.fail_json("The clickhouse-driver module is required on host")
    

    if module.check_mode:
        module.exit_json(**result)

    login_user = module.params["login_user"]
    login_password = module.params["login_password"]

    try:
        ch_client = CHClient(host="localhost", user=login_user, password=login_password)
    except Exception as e:
        return module.fail_json(to_native(e))

    state = module.params["state"]

    user = module.params["user"]

    if state == "new":
        result = create_new_user(ch_client, user, module.params["password"])
    elif state == "absent":
        result = delete_user(ch_client, user)
    else:
        return module.fail_json(f"state {state} not supported by this module")

    module.exit_json(**result)




if __name__ == '__main__':
    main()
