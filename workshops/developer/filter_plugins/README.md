The included filter plugin (in directory "reference") will take a list of dicts and transform it into a flat list based on one key that you specify. This may be particularly useful dealing with the results from a combined register+with_items task.

For example, this output:

```
ok: [localhost] => {
    "output": {
        "changed": true,
        "failed": true,
        "msg": "One or more items failed.",
        "results": [
            {
                "changed": true,
                "cmd": [
                    "mkdir",
                    "a"
                ],
                "delta": "0:00:00.004365",
                "end": "2014-08-28 15:52:44.798666",
                "invocation": {
                    "module_args": "mkdir a",
                    "module_name": "command"
                },
                "item": "a",
                "rc": 1,
                "start": "2014-08-28 15:52:44.794301",
                "stderr": "mkdir: a: File exists",
                "stdout": "",
                "warnings": [
                    "Consider using file module with state=directory rather than running mkdir"
                ]
            },
            {
                "changed": true,
                "cmd": [
                    "mkdir",
                    "b"
                ],
                "delta": "0:00:00.005014",
                "end": "2014-08-28 15:52:44.899251",
                "invocation": {
                    "module_args": "mkdir b",
                    "module_name": "command"
                },
                "item": "b",
                "rc": 1,
                "start": "2014-08-28 15:52:44.894237",
                "stderr": "mkdir: b: File exists",
                "stdout": "",
                "warnings": [
                    "Consider using file module with state=directory rather than running mkdir"
                ]
            }
        ]
    }
}
```

Can be transformed into:

```
ok: [localhost] => {
    "output.results|deeplist(\"stderr\")": [
        "mkdir: a: File exists",
        "mkdir: b: File exists"
    ]
}
```

To use, put custom_filters.py into your filters_path, specified in ansible.cfg.