---
title: Lista de directivas del php.ini
source_url: https://www.php.net/manual/es/ini.list.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/ini.list.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: a52e3d27c
order: 130
---

## Lista de directivas del `php.ini`

Esta lista incluye las directivas del `php.ini` que pueden ser utilizadas para configurar PHP.

La columna "Cambiable" muestra los modos que determinan cuándo y dónde se puede definir una directiva. Ver la sección sobre los [valores del modo modificable](#configuration.changes.modes) para sus definiciones.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [allow_url_fopen](#ini.allow-url-fopen) | `"1"` | `INI_SYSTEM` |  |
| [allow_url_include](#ini.allow-url-include) | `"0"` | `INI_SYSTEM` | Obsoleto a partir de PHP 7.4.0. |
| [arg_separator.input](#ini.arg-separator.input) | `"&"` | `INI_PERDIR` |  |
| [arg_separator.output](#ini.arg-separator.output) | `"&"` | `INI_ALL` |  |
| [assert.active](#ini.assert.active) | `"1"` | `INI_ALL` |  |
| [assert.bail](#ini.assert.bail) | `"0"` | `INI_ALL` |  |
| [assert.callback](#ini.assert.callback) | `null` | `INI_ALL` |  |
| [assert.exception](#ini.assert.exception) | `"0"` | `INI_ALL` |  |
| [assert.quiet_eval](#ini.assert.quiet-eval) | `"0"` | `INI_ALL` | Eliminado a partir de PHP 8.0.0. |
| [assert.warning](#ini.assert.warning) | `"1"` | `INI_ALL` |  |
| [auto_append_file](#ini.auto-append-file) | `null` | `INI_PERDIR` |  |
| [auto_detect_line_endings](#ini.auto-detect-line-endings) | `"0"` | `INI_ALL` |  |
| [auto_globals_jit](#ini.auto-globals-jit) | `"1"` | `INI_PERDIR` |  |
| [auto_prepend_file](#ini.auto-prepend-file) | `null` | `INI_PERDIR` |  |
| [browscap](#ini.browscap) | `null` | `INI_SYSTEM` |  |
| [cgi.check_shebang_line](#ini.cgi.check-shebang-line) | `"1"` | `INI_SYSTEM` |  |
| [cgi.discard_path](#ini.cgi.discard-path) | `"0"` | `INI_SYSTEM` |  |
| [cgi.fix_pathinfo](#ini.cgi.fix-pathinfo) | `"1"` | `INI_SYSTEM` |  |
| [cgi.force_redirect](#ini.cgi.force-redirect) | `"1"` | `INI_SYSTEM` |  |
| [cgi.nph](#ini.cgi.nph) | `"0"` | `INI_ALL` |  |
| [cgi.redirect_status_env](#ini.cgi.redirect-status-env) | `null` | `INI_SYSTEM` |  |
| [cgi.rfc2616_headers](#ini.cgi.rfc2616-headers) | `"0"` | `INI_ALL` |  |
| [child_terminate](#ini.child-terminate) | `"0"` | `INI_ALL` |  |
| [default_charset](#ini.default-charset) | `"UTF-8"` | `INI_ALL` | Por defecto "UTF-8". |
| [input_encoding](#ini.input-encoding) | `""` | `INI_ALL` |  |
| [output_encoding](#ini.output-encoding) | `""` | `INI_ALL` |  |
| [internal_encoding](#ini.internal-encoding) | `""` | `INI_ALL` |  |
| [default_mimetype](#ini.default-mimetype) | `"text/html"` | `INI_ALL` |  |
| [default_socket_timeout](#ini.default-socket-timeout) | `"60"` | `INI_ALL` |  |
| [disable_classes](#ini.disable-classes) | `""` | `php.ini` solo | Eliminado a partir de PHP 8.5.0 |
| [disable_functions](#ini.disable-functions) | `""` | `php.ini` solo |  |
| [display_errors](#ini.display-errors) | `"1"` | `INI_ALL` |  |
| [display_startup_errors](#ini.display-startup-errors) | `"1"` | `INI_ALL` | Anterior a PHP 8.0.0, el valor predeterminado era `"0"`. |
| [docref_ext](#ini.docref-ext) | `""` | `INI_ALL` |  |
| [docref_root](#ini.docref-root) | `""` | `INI_ALL` |  |
| [doc_root](#ini.doc-root) | `null` | `INI_SYSTEM` |  |
| [enable_dl](#ini.enable-dl) | `"1"` | `INI_SYSTEM` | Esta funcionalidad obsoleta *será* ciertamente *eliminada* en el futuro. |
| [enable_post_data_reading](#ini.enable-post-data-reading) | `"On"` | `INI_PERDIR` |  |
| [engine](#ini.engine) | `"1"` | `INI_ALL` |  |
| [error_append_string](#ini.error-append-string) | `null` | `INI_ALL` |  |
| [error_log](#ini.error-log) | `null` | `INI_ALL` |  |
| [error_log_mode](#ini.error-log-mode) | `0o644` | `INI_ALL` | Disponible a partir de PHP 8.2.0 |
| [error_prepend_string](#ini.error-prepend-string) | `null` | `INI_ALL` |  |
| [error_reporting](#ini.error-reporting) | `null` | `INI_ALL` |  |
| [exit_on_timeout](#ini.exit-on-timeout) | `""` | `INI_ALL` |  |
| [expose_php](#ini.expose-php) | `"1"` | `php.ini` solo |  |
| [extension](#ini.extension) | `null` | `php.ini` solo |  |
| [extension_dir](#ini.extension-dir) | `"/path/to/php"` | `INI_SYSTEM` |  |
| [fastcgi.impersonate](#ini.fastcgi.impersonate) | `"0"` | `INI_SYSTEM` |  |
| [fastcgi.logging](#ini.fastcgi.logging) | `"1"` | `INI_SYSTEM` |  |
| [file_uploads](#ini.file-uploads) | `"1"` | `INI_SYSTEM` |  |
| [from](#ini.from) | `""` | `INI_ALL` |  |
| hard_timeout | `"2"` | `INI_SYSTEM` | Disponible a partir de 7.1.0. |
| [highlight.comment](#ini.syntax-highlighting) | `"#FF8000"` | `INI_ALL` |  |
| [highlight.default](#ini.syntax-highlighting) | `"#0000BB"` | `INI_ALL` |  |
| [highlight.html](#ini.syntax-highlighting) | `"#000000"` | `INI_ALL` |  |
| [highlight.keyword](#ini.syntax-highlighting) | `"#007700"` | `INI_ALL` |  |
| [highlight.string](#ini.syntax-highlighting) | `"#DD0000"` | `INI_ALL` |  |
| [html_errors](#ini.html-errors) | `"1"` | `INI_ALL` |  |
| [ignore_repeated_errors](#ini.ignore-repeated-errors) | `"0"` | `INI_ALL` |  |
| [ignore_repeated_source](#ini.ignore-repeated-source) | `"0"` | `INI_ALL` |  |
| [ignore_user_abort](#ini.ignore-user-abort) | `"0"` | `INI_ALL` |  |
| [implicit_flush](#ini.implicit-flush) | `"0"` | `INI_ALL` |  |
| [include_path](#ini.include-path) | `".:/path/to/php/pear"` | `INI_ALL` |  |
| [last_modified](#ini.last-modified) | `"0"` | `INI_ALL` |  |
| [log_errors](#ini.log-errors) | `"0"` | `INI_ALL` |  |
| [log_errors_max_len](#ini.log-errors-max-len) | `"1024"` | `INI_ALL` |  |
| [mail.add_x_header](#ini.mail.add-x-header) | `"0"` | `INI_PERDIR` |  |
| mail.force_extra_parameters | `null` | `INI_SYSTEM` |  |
| [mail.log](#ini.mail.log) | `""` | `INI_PERDIR` |  |
| [max_execution_time](#ini.max-execution-time) | `"30"` | `INI_ALL` |  |
| [max_input_nesting_level](#ini.max-input-nesting-level) | `"64"` | `INI_PERDIR` |  |
| [max_input_vars](#ini.max-input-vars) | `1000` | `INI_PERDIR` |  |
| [max_input_time](#ini.max-input-time) | `"-1"` | `INI_PERDIR` |  |
| [memory_limit](#ini.memory-limit) | `"128M"` | `INI_ALL` |  |
| [open_basedir](#ini.open-basedir) | `null` | `INI_ALL` |  |
| [output_buffering](#ini.output-buffering) | `"0"` | `INI_PERDIR` |  |
| [output_handler](#ini.output-handler) | `null` | `INI_PERDIR` |  |
| [post_max_size](#ini.post-max-size) | `"8M"` | `INI_PERDIR` |  |
| [precision](#ini.precision) | `"14"` | `INI_ALL` |  |
| [realpath_cache_size](#ini.realpath-cache-size) | `"16K"` | `INI_SYSTEM` |  |
| [realpath_cache_ttl](#ini.realpath-cache-ttl) | `"120"` | `INI_SYSTEM` |  |
| [register_argc_argv](#ini.register-argc-argv) | `"1"` | `INI_PERDIR` | Obsoleto a partir de PHP 8.5.0 |
| [report_memleaks](#ini.report-memleaks) | `"1"` | `INI_ALL` | Obsoleto a partir de PHP 8.5.0 |
| report_zend_debug | `"1"` | `INI_ALL` |  |
| [request_order](#ini.request-order) | `""` | `INI_PERDIR` |  |
| [sendmail_from](#ini.sendmail-from) | `null` | `INI_ALL` |  |
| [sendmail_path](#ini.sendmail-path) | `"/usr/sbin/sendmail -t -i"` | `INI_SYSTEM` |  |
| [serialize_precision](#ini.serialize-precision) | `"-1"` | `INI_ALL` | Anterior a PHP 7.1.0, el valor predeterminado era `17`. |
| [short_open_tag](#ini.short-open-tag) | `"1"` | `INI_PERDIR` |  |
| [SMTP](#ini.smtp) | `"localhost"` | `INI_ALL` |  |
| [smtp_port](#ini.smtp-port) | `"25"` | `INI_ALL` |  |
| [sql.safe_mode](#ini.sql.safe-mode) | `"0"` | `INI_SYSTEM` | Eliminado a partir de PHP 7.2.0 |
| [syslog.facility](#ini.syslog.facility) | `"LOG_USER"` | `INI_SYSTEM` | Disponible a partir de PHP 7.3.0. |
| [syslog.filter](#ini.syslog.filter) | `"no-ctrl"` | `INI_ALL` | Disponible a partir de PHP 7.3.0. |
| [syslog.ident](#ini.syslog.ident) | `"php"` | `INI_SYSTEM` | Disponible a partir de PHP 7.3.0. |
| sys_temp_dir | `""` | `INI_SYSTEM` |  |
| [track_errors](#ini.track-errors) | `"0"` | `INI_ALL` | Obsoleto a partir de PHP 7.2.0, eliminado a partir de PHP 8.0.0. |
| uploadprogress.file.filename_template | `"/tmp/upt_%s.txt"` | `INI_ALL` |  |
| [upload_max_filesize](#ini.upload-max-filesize) | `"2M"` | `INI_PERDIR` |  |
| [max_file_uploads](#ini.max-file-uploads) | `20` | `INI_SYSTEM` |  |
| [upload_tmp_dir](#ini.upload-tmp-dir) | `null` | `INI_SYSTEM` |  |
| [url_rewriter.hosts](#ini.url-rewriter.hosts) | `""` | `INI_ALL` | Disponible a partir de PHP 7.1.0. |
| [url_rewriter.tags](#ini.url-rewriter.tags) | `"form="` | `INI_ALL` | Anterior a PHP 7.1.0, el valor predeterminado era `"a=href,area=href,frame=src,form=,fieldset="`. |
| [user_agent](#ini.user-agent) | `null` | `INI_ALL` |  |
| [user_dir](#ini.user-dir) | `null` | `INI_SYSTEM` |  |
| [user_ini.cache_ttl](#ini.user-ini.cache-ttl) | `"300"` | `INI_SYSTEM` |  |
| [user_ini.filename](#ini.user-ini.filename) | `".user.ini"` | `INI_SYSTEM` |  |
| [variables_order](#ini.variables-order) | `"EGPCS"` | `INI_PERDIR` |  |
| [windows.show_crt_warning](#ini.windows-show-crt-warning) | `"0"` | `INI_ALL` |  |
| [xbithack](#ini.xbithack) | `"0"` | `INI_ALL` |  |
| [xmlrpc_errors](#ini.xmlrpc-errors) | `"0"` | `INI_SYSTEM` |  |
| [xmlrpc_error_number](#ini.xmlrpc-error-number) | `"0"` | `INI_ALL` |  |
| yaz.keepalive | `"120"` | `INI_ALL` |  |
| yaz.log_mask | `null` | `INI_ALL` | Disponible a partir de yaz 1.0.3. |
| [zend.assertions](#ini.zend.assertions) | `"1"` | `INI_ALL` |  |
| [zend.detect_unicode](#ini.zend.detect-unicode) | `"1"` | `INI_ALL` |  |
| [zend.enable_gc](#ini.zend.enable-gc) | `"1"` | `INI_ALL` |  |
| [zend.max_allowed_stack_size](#ini.zend.max-allowed-stack-size) | `"0"` | `INI_SYSTEM` | Disponible a partir de PHP 8.3.0 |
| [fiber.stack_size](#ini.fiber.stack-size) |  | `INI_ALL` | Disponible a partir de PHP 8.1.0 |
| [zend.multibyte](#ini.zend.multibyte) | `"0"` | `INI_PERDIR` |  |
| [zend.reserved_stack_size](#ini.zend.reserved-stack-size) | `"0"` | `INI_SYSTEM` | Disponible a partir de PHP 8.3.0 |
| [zend.script_encoding](#ini.zend.script-encoding) | `null` | `INI_ALL` |  |
| [zend.signal_check](#ini.zend.signal-check) | `"0"` | `INI_SYSTEM` |  |
| [zend_extension](#ini.zend-extension) | `null` | `php.ini` solo |  |

Opciones de configuración
