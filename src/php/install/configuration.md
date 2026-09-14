---
title: Configuration
source_url: https://www.php.net/manual/es/install.fpm.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/fpm/configuration.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: false
translation_revision: 1f01e2a8e
order: 1670
---

## Configuration

FPM uses `php.ini` syntax for its configuration file - `php-fpm.conf`, and pool configuration files.

## List of global `php-fpm.conf` directives

`pid` `string`  
Path to PID file. Default value: none.

`error_log` `string`  
Path to error log file. Default value: `#INSTALL_PREFIX#/log/php-fpm.log`. If it's set to "syslog", log is sent to syslogd instead of being written in a local file.

`log_level` `string`  
Error log level. Possible values: alert, error, warning, notice, debug. Default value: notice.

`log_limit` `int`  
Log limit for the logged lines which allows to log messages longer than 1024 characters without wrapping. Default value: 1024. Available as of PHP 7.3.0.

`log_buffering` `bool`  
Experimental logging without extra buffering. Default value: yes. Available as of PHP 7.3.0.

`syslog.facility` `string`  
used to specify what type of program is logging the message. Default value: daemon.

`syslog.ident` `string`  
Prepended to every message. If you have multiple FPM instances running on the same server, you can change the default value which must suit common needs. Default value: php-fpm.

`emergency_restart_threshold` `int`  
If this number of child processes exit with SIGSEGV or SIGBUS within the time interval set by `emergency_restart_interval`, then FPM will restart. A value of 0 means 'Off'. Default value: 0 (Off).

`emergency_restart_interval` `mixed`  
Interval of time used by `emergency_restart_interval` to determine when a graceful restart will be initiated. This can be useful to work around accidental corruptions in an accelerator's shared memory. Available Units: s(econds), m(inutes), h(ours), or d(ays). Default Unit: seconds. Default value: 0 (Off).

`process_control_timeout` `mixed`  
Time limit for child processes to wait for a reaction on signals from master. Available units: s(econds), m(inutes), h(ours), or d(ays) Default Unit: seconds. Default value: 0.

`process.max` `int`  
The maximum number of processes FPM will fork. This has been design to control the global number of processes when using dynamic PM within a lot of pools. Use it with caution. Default value: 0.

`process.priority` `int`  
Specify the nice(2) priority to apply to the master process (only if set). The value can vary from -19 (highest priority) to 20 (lower priority). Default value: not set.

`daemonize` `bool`  
Send FPM to background. Set to 'no' to keep FPM in foreground for debugging. Default value: yes.

`rlimit_files` `int`  
Set open file descriptor rlimit for the master process. Default value: system defined value.

`rlimit_core` `int`  
Set max core size rlimit for the master process. Default value: 0.

`events.mechanism` `string`  
Specify the event mechanism FPM will use. The following is available: epoll, kqueue (\*BSD), port (Solaris), poll, select. Default value: not set (auto detection preferring epoll and kqueue).

`systemd_interval` `int`  
When FPM is build with systemd integration, specify the interval, in second, between health report notification to systemd. Set to 0 to disable. Default value: 10.

## List of pool directives

With FPM you can run several pools of processes with different setting. These are settings that can be tweaked per pool.

`listen` `string`  
The address on which to accept FastCGI requests. Valid syntaxes are: 'ip.add.re.ss:port', 'port', '/path/to/unix/socket'. This option is mandatory for each pool.

`listen.backlog` `int`  
Set listen(2) backlog. A value of `-1` means maximum on BSD systems. Default value: `-1` (FreeBSD or OpenBSD) or `511` (Linux and other platforms).

`listen.allowed_clients` `string`  
List of IPv4 or IPv6 addresses of FastCGI clients which are allowed to connect. Equivalent to the FCGI_WEB_SERVER_ADDRS environment variable in the original PHP FastCGI (5.2.2+). Makes sense only with a tcp listening socket. Each address must be separated by a comma. If this value is left blank, connections will be accepted from any ip address. Default value: not set (any ip address accepted).

`listen.owner` `string`  
Set permissions for unix socket, if one is used. In Linux, read/write permissions must be set in order to allow connections from a web server. Many BSD-derived systems allow connections regardless of permissions. Default values: user and group are set as the running user, mode is set to 0660.

`listen.group` `string`  
See `listen.owner`.

`listen.mode` `string`  
See `listen.owner`.

`listen.acl_users` `string`  
When POSIX Access Control Lists are supported you can set them using this option. When set, `listen.owner` and `listen.group` are ignored. Value is a comma separated list of user names.

`listen.acl_groups` `string`  
See `listen.acl_users`. Value is a comma separated list of group names.

`listen.setfib` `int`  
Set the associated the route table (FIB). FreeBSD only. Default Value: `-1`. Since PHP 8.2.0.

`user` `string`  
Unix user of FPM processes. This option is mandatory.

`group` `string`  
Unix group of FPM processes. If not set, the default user's group is used.

`pm` `string`  
Choose how the process manager will control the number of child processes. Possible values: `static`, `ondemand`, `dynamic`. This option is mandatory.

`static` - the number of child processes is fixed (`pm.max_children`).

`ondemand` - los procesos se generan bajo demanda (cuando se solicita, a diferencia de dinámico, donde `pm.start_servers` se inician cuando se inicia el servicio).

`dynamic` - el número de procesos hijos se establece dinámicamente en función de las siguientes directivas: `pm.max_children`, `pm.start_servers`, `pm.min_spare_servers`, `pm.max_spare_servers`.

`pm.max_children` `int`  
El número de procesos hijos que se crearán cuando `pm` se establece en `static` y el número máximo de procesos hijos que se crearán cuando `pm` se establece en `dynamic` o `ondemand`. Esta opción es obligatoria.

Esta opción establece el límite en el número de solicitudes simultáneas que se atenderán. Equivalente a la directiva ApacheMaxClients con mpm_prefork y a la variable de entorno `PHP_FCGI_CHILDREN` en el PHP FastCGI original.

`pm.start_servers` `int`  
The number of child processes created on startup. Used only when `pm` is set to `dynamic`. Default Value: (min_spare_servers + max_spare_servers) / 2.

`pm.min_spare_servers` `int`  
The desired minimum number of idle server processes. Used only when `pm` is set to `dynamic`. Also mandatory in this case.

`pm.max_spare_servers` `int`  
The desired maximum number of idle server processes. Used only when `pm` is set to `dynamic`. Also mandatory in this case.

`pm.max_spawn_rate` `int`  
The number of rate to spawn child processes at once. Used only when `pm` is set to `dynamic`. Default value: 32

`pm.process_idle_timeout` `mixed`  
The number of seconds after which an idle process will be killed. Used only when `pm` is set to `ondemand`. Available units: s(econds)(default), m(inutes), h(ours), or d(ays). Default value: 10s.

`pm.max_requests` `int`  
The number of requests each child process should execute before respawning. This can be useful to work around memory leaks in 3rd party libraries. For endless request processing specify '0'. Equivalent to `PHP_FCGI_MAX_REQUESTS`. Default value: 0.

`pm.status_listen` `string`  
The address on which to accept FastCGI status request. This creates a new invisible pool that can handle requests independently. This is useful if the main pool is busy with long running requests because it is still possible to get the [FPM status page](#fpm.status) before finishing the long running requests. The syntax is the same as for [listen](#listen) directive. Default value: none.

`pm.status_path` `string`  
The URI to view the [FPM status page](#fpm.status). This value must start with a leading slash (/). If this value is not set, no URI will be recognized as a status page. Default value: none.

`ping.path` `string`  
The ping URI to call the monitoring page of FPM. If this value is not set, no URI will be recognized as a ping page. This could be used to test from outside that FPM is alive and responding. Please note that the value must start with a leading slash (/).

`ping.response` `string`  
This directive may be used to customize the response to a ping request. The response is formatted as text/plain with a 200 response code. Default value: pong.

`process.priority` `int`  
Specify the nice(2) priority to apply to the worker process (only if set). The value can vary from -19 (highest priority) to 20 (lower priority). Default value: not set.

`process.dumpable` `bool`  
Set the process dumpable flag (PR_SET_DUMPABLE prctl) even if the process user or group is different than the master process user. It allows to create process core dump and ptrace the process for the pool user. Default Value: no. Since PHP 7.0.29, 7.1.17 and 7.2.5.

`prefix` `string`  
Specify prefix for path evaluation

`request_terminate_timeout` `mixed`  
The timeout for serving a single request after which the worker process will be killed. This option should be used when the 'max_execution_time' ini option does not stop script execution for some reason. A value of '0' means 'Off'. Available units: s(econds)(default), m(inutes), h(ours), or d(ays). Default value: 0.

`request_terminate_timeout_track_finished` `bool`  
The timeout set by [request_terminate_timeout](#request-terminate-timeout) is not engaged after a [fastcgi_finish_request](#function.fastcgi-finish-request) or when application has finished and internal shutdown functions are being called. This directive will enable timeout limit to be applied unconditionally even in such cases. Default value: no. Since PHP 7.3.0.

`request_slowlog_timeout` `mixed`  
The timeout for serving a single request after which a PHP backtrace will be dumped to the 'slowlog' file. A value of '0' means 'Off'. Available units: s(econds)(default), m(inutes), h(ours), or d(ays). Default value: 0.

`request_slowlog_trace_depth` `int`  
The depth of slowlog log stack trace. Default value: 20. Since PHP 7.2.0.

`slowlog` `string`  
The log file for slow requests. Default value: `#INSTALL_PREFIX#/log/php-fpm.log.slow`.

`rlimit_files` `int`  
Set open file descriptor rlimit for child processes in this pool. Default value: system defined value.

`rlimit_core` `int`  
Set max core size rlimit for child processes in this pool. Possible Values: 'unlimited' or an integer greater or equal to 0. Default value: system defined value.

`chroot` `string`  
Chroot to this directory at the start. This value must be defined as an absolute path. When this value is not set, chroot is not used.

`chdir` `string`  
Chdir to this directory at the start. This value must be an absolute path. Default value: current directory or / when chroot.

`catch_workers_output` `bool`  
Redirect worker stdout and stderr into main error log. If not set, stdout and stderr will be redirected to /dev/null according to FastCGI specs. Default value: no.

`decorate_workers_output` `bool`  
Enable the output decoration for workers output when [catch_workers_output](#catch-workers-output) is enabled. Default value: yes. Available as of PHP 7.3.0.

`clear_env` `bool`  
Clear environment in FPM workers. Prevents arbitrary environment variables from reaching FPM worker processes by clearing the environment in workers before env vars specified in this pool configuration are added. Default value: Yes.

`security.limit_extensions` `string`  
Limits the extensions of the main script FPM will allow to parse. This can prevent configuration mistakes on the web server side. You should only limit FPM to .php extensions to prevent malicious users to use other extensions to execute php code. Default value: .php .phar

`apparmor_hat` `string`  
If AppArmor is enabled, it allows to change a hat. Default value: not set

`access.log` `string`  
The access log file. Default value: not set

`access.format` `string`  
The access log format. Default value: `"%R - %u %t \"%m %r\" %s"`:

| Placeholder | Description |
|----|----|
| `%%` | The `%` character |
| `%C` | %CPU used by the request. It can accept the following format: `%{user}C` for user CPU only, `%{system}C` for system CPU only, `%{total}C` for user + system CPU (default) |
| `%d` | Time taken to serve the request. It can accept the following formats for precision: `%{seconds}d` (default), `%{milliseconds}d`, `%{microseconds}d` |
| `%{name}e` | An environment variable (same as `$_ENV` or `$_SERVER`). A variable name must be specified within curly brackets to specify the name of the env variable. For example, server specifics like `%{REQUEST_METHOD}e` or `%{SERVER_PROTOCOL}e`, HTTP headers like `%{HTTP_HOST}e` or `%{HTTP_USER_AGENT}e` |
| `%f` | Script filename |
| `%l` | `Content-Length` of the request (for HTTP POST request only) |
| `%m` | Request HTTP method |
| `%M` | Peak of memory allocated by PHP. It can accept the following format: `%{bytes}M` (default), `%{kilobytes}M` `%{kilo}M`, `%{megabytes}M`, `%{mega}M` |
| `%n` | Pool name |
| `%{name}o` | Output header. The header name must be specified within curly brackets. For example: `%{Content-Type}o`, `%{X-Powered-By}o`, `%{Transfer-Encoding}o` |
| `%p` | PID of the child that serviced the request |
| `%P` | PID of the parent of the child that serviced the request |
| `%q` | Query string |
| `%Q` | The `'?'` character, or glue between `%q` and `%r`, if query string exists |
| `%r` | Request URI without the query string, see `%q` and `%Q` |
| `%R` | Remote IP address |
| `%s` | Status (response code) |
| `%t` | Server time the request was received. It can accept a `strftime(3)` format: `%d/%b/%Y:%H:%M:%S %z` (default) The `strftime(3)` format must be encapsulated in a `%{<strftime_format>}t` tag, e.g. for a ISO8601 formatted timestring, use: `%{%Y-%m-%dT%H:%M:%S%z}t` |
| `%T` | Time the log was written (when the request finished). It can accept a `strftime(3)` format: `%d/%b/%Y:%H:%M:%S %z` (default). The `strftime(3)` format must be encapsulated in a `%{<strftime_format>}T` tag, e.g. for a ISO8601 formatted timestring, use: `%{%Y-%m-%dT%H:%M:%S%z}T` |
| `%u` | Basic access authentication user, if specified in `Authorization` header |

Valid options {#fpm.configuration.access.format}

`access.suppress_path` `array`  
A list of request_uri values which should be filtered from the access log. Default value: not set. Since PHP 8.2.0.

It's possible to pass additional environment variables and update PHP settings of a certain pool. To do this, you need to add the following options to the pool configuration file.

Passing environment variables and PHP settings to a pool

```php
env[HOSTNAME] = $HOSTNAME
env[PATH] = /usr/local/bin:/usr/bin:/bin
env[TMP] = /tmp
env[TMPDIR] = /tmp
env[TEMP] = /tmp

php_admin_value[sendmail_path] = /usr/sbin/sendmail -t -i -f www@my.domain.com
php_flag[display_errors] = off
php_admin_value[error_log] = /var/log/fpm-php.www.log
php_admin_flag[log_errors] = on
php_admin_value[memory_limit] = 32M

      
```

PHP settings passed with `php_value` or `php_flag` will overwrite their previous value. Please note that defining [disable_functions](#ini.disable-functions) will not overwrite previously defined `php.ini` values, but will append the new value instead.

Settings defined with `php_admin_value` and `php_admin_flag` cannot be overridden with `ini_set`.

PHP settings can be set in the webserver configuration.

set PHP settings in nginx.conf

```php
set $php_value "pcre.backtrack_limit=424242";
set $php_value "$php_value \n pcre.recursion_limit=99999";
fastcgi_param  PHP_VALUE $php_value;

fastcgi_param  PHP_ADMIN_VALUE "open_basedir=/var/www/htdocs";

      
```

> [!CAUTION]
> Because these settings are passed to php-fpm as fastcgi headers, php-fpm should not be bound to a worldwide accessible address. Otherwise, anyone could alter the PHP configuration options. See also [listen.allowed_clients](#listen-allowed-clients).

> [!NOTE]
> Pools are not a security mechanism, because they do not provide full separation; e.g. all pools would use a single OPcache instance.
