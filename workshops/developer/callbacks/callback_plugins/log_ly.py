#! /usr/bin/env python

import os
import time
import json
import logging
import logging.config
import loggly.handlers
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
logging.config.fileConfig(os.path.expanduser('~/.loggly-ansible.conf'))
logger = logging.getLogger('ansible-callback')


MSG_FORMAT="%(host)s - %(category)s - %(data)s"



def log(host, category, data):
    if type(data) == dict:
        data['host'] = host
        if 'verbose_override' in data:
            # avoid logging extraneous data from facts
            data = {}
            data['nolog'] = True
            data['host'] = host
        else:
            data = json.dumps(data)

    logger.info(data)

class CallbackModule(object):
    """
    """

    def on_any(self, *args, **kwargs):
        pass

    def runner_on_failed(self, host, res, ignore_errors=False):
        log(host, 'FAILED', res)

    def runner_on_ok(self, host, res):
        log(host, 'OK', res)

    def runner_on_skipped(self, host, item=None):
        log(host, 'SKIPPED', '...')

    def runner_on_unreachable(self, host, res):
        log(host, 'UNREACHABLE', res)

    def runner_on_no_hosts(self):
        pass

    def runner_on_async_poll(self, host, res, jid, clock):
        pass

    def runner_on_async_ok(self, host, res, jid):
        pass

    def runner_on_async_failed(self, host, res, jid):
        log(host, 'ASYNC_FAILED', res)

    def playbook_on_start(self):
        pass

    def playbook_on_notify(self, host, handler):
        pass

    def playbook_on_no_hosts_matched(self):
        pass

    def playbook_on_no_hosts_remaining(self):
        pass

    def playbook_on_task_start(self, name, is_conditional):
        pass

    def playbook_on_vars_prompt(self, varname, private=True, prompt=None, encrypt=None, confirm=False, salt_size=None, salt=None, default=None):
        pass

    def playbook_on_setup(self):
        pass

    def playbook_on_import_for_host(self, host, imported_file):
        log(host, 'IMPORTED', imported_file)

    def playbook_on_not_import_for_host(self, host, missing_file):
        log(host, 'NOTIMPORTED', missing_file)

    def playbook_on_play_start(self, name):
        pass

    def playbook_on_stats(self, stats):
        pass
