#! /usr/bin/python

DOCUMENTATION = """
---
module: foo
short_description: create foo files
description:
  - The purpose of this module is to be an example.
options:
  path:
    description:
      - path of the foo file.
    default: null
    required: true
 state:
    description:
      - Whether to ensure the foo file is present or absent.
    required: false
    default: present
    choices: [ "present", "absent" ]
  content:
    description:
      - The content of the foo file.
    required: false
    default: null

author:
    - "James S. Martin"
"""

import os

def main():


    module = AnsibleModule(
        argument_spec = dict(
            path=dict(required=True),
            state=dict(default='present', choices=['present', 'absent']),
            content=dict(required=False)
        ),
        supports_check_mode = False,
    )

    path         = module.params['path']
    state        = module.params['state']
    content      = module.params['content']


    update       = False
    changed      = False
    old_content  = None
 
    blacklist = [ '/etc/passwd', '/etc/group', '/tmp/foo' ]

    if path in blacklist:
        rc = 1
        msg = "Blacklisted file provided."
        module.fail_json(msg=msg)

    if state == 'present':
        if os.path.isfile(path):
            old_content = open(path).read()
            if old_content != content:
                update = True
        else:
            update = True

        if update:
            f = open(path, 'w')
            f.write(content)
            f.close()
            changed = True


    if state == 'absent':
        content = None
        if os.path.isfile(path):
            os.remove(path)
            changed = True


    result = { 'changed': changed, 
               'old_content': old_content,
               'new_content': content,
               'path': path }

    module.exit_json(**result)


# import module snippets
from ansible.module_utils.basic import *

main()
