#!/usr/bin/python

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
    - "YOUR NAME HERE"
"""

def main():

    module = AnsibleModule(
        argument_spec = dict(
            # your spec here
        ),
        supports_check_mode = False,
    )

    # your module logic here 

    # (rc, out, err) = module.run_command(cmd)

    if rc:
        return module.fail_json(msg=err, rc=rc, path=path)
    else:
        return module.exit_json(changed=changed, msg=path,
          rc=rc, old_content=old_content, new_content=content)

# import module snippets (must stay here after your code)
from ansible.module_utils.basic import *

main()
