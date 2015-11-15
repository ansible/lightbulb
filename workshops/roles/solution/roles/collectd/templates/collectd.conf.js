Hostname    "{{ collectd_hostname }}"
FQDNLookup  {{ collectd_fqdn_lookup | bool }}
BaseDir     "{{ collectd_basedir }}"
PIDFile     "{{ collectd_pidfile }}"
PluginDir   "{{ collectd_plugindir }}"
TypesDB     "{{ collectd_types_db }}"
Interval     {{ collectd_interval | int }} 
Timeout      {{ collectd_timeout | int }}
ReadThreads  {{ collectd_read_threads | int }}

LoadPlugin syslog
<Plugin syslog>
        LogLevel info
</Plugin>
LoadPlugin cpu
LoadPlugin interface
LoadPlugin load
LoadPlugin memory
Include "/etc/collectd.d"

