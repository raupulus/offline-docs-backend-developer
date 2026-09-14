---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/mysql.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_reviewed: true
translation_revision: 15d88bef8
order: 52510
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [mysql.allow_local_infile](#ini.mysql.allow-local-infile) | "1" | `INI_SYSTEM` |  |
| [mysql.allow_persistent](#ini.mysql.allow-persistent) | "1" | `INI_SYSTEM` |  |
| [mysql.max_persistent](#ini.mysql.max-persistent) | "-1" | `INI_SYSTEM` |  |
| [mysql.max_links](#ini.mysql.max-links) | "-1" | `INI_SYSTEM` |  |
| [mysql.trace_mode](#ini.mysql.trace-mode) | "Off" | `INI_ALL` |  |
| [mysql.default_port](#ini.mysql.default-port) | NULL | `INI_ALL` |  |
| [mysql.default_socket](#ini.mysql.default-socket) | NULL | `INI_ALL` |  |
| [mysql.default_host](#ini.mysql.default-host) | NULL | `INI_ALL` |  |
| [mysql.default_user](#ini.mysql.default-user) | NULL | `INI_ALL` |  |
| [mysql.default_password](#ini.mysql.default-password) | NULL | `INI_ALL` |  |
| [mysql.connect_timeout](#ini.mysql.connect-timeout) | "60" | `INI_ALL` |  |

Opciones de configuración MySQL {#mysql.configuration.options}

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`mysql.allow_local_infile` `int`  
Permite el acceso, desde el punto de vista de PHP, a los ficheros locales, con las consultas LOAD DATA.

`mysql.allow_persistent` `bool`  
Activa o desactiva las [conexiones persistentes](#features.persistent-connections) a la base de datos MySQL.

`mysql.max_persistent` `int`  
El número máximo de conexiones persistentes a las bases de datos MySQL, por proceso.

`mysql.max_links` `int`  
El número máximo de conexiones a las bases de datos MySQL, incluyendo las conexiones persistentes, por proceso.

`mysql.trace_mode` `bool`  
Modo de seguimiento. Cuando `mysql.trace_mode` está activado, se mostrarán alertas para escaneos de tabla o de índice, para olvidos de liberación de recursos o errores SQL. Esta opción fue introducida en PHP 4.3.0.

`mysql.default_port` `string`  
El número de puerto TCP por defecto, utilizado para conectarse a la base de datos, cuando no se especifica ningún puerto. Si no se especifica ningún puerto por defecto, el puerto se obtendrá entonces leyendo la variable de entorno `MYSQL_TCP_PORT`, la entrada `mysql-tcp` en el fichero `/etc/services` o la constante de compilación `MYSQL_PORT`, en este orden. Windows utilizará también solo la constante `MYSQL_PORT`.

`mysql.default_socket` `string`  
El nombre por defecto del socket cuando se conecta al servidor local, si no se especifica ningún otro socket.

`mysql.default_host` `string`  
Dirección por defecto del servidor, a utilizar al conectarse a un servidor MySQL, si no se especifica ningún host. No se aplica cuando el [safe mode SQL](#ini.sql.safe-mode) está activado.

`mysql.default_user` `string`  
Usuario por defecto, a utilizar al conectarse a un servidor MySQL, si no se especifica ningún usuario. No se aplica cuando el [safe mode SQL](#ini.sql.safe-mode) está activado.

`mysql.default_password` `string`  
Contraseña por defecto, a utilizar al conectarse a un servidor MySQL, si no se especifica ninguna contraseña. No se aplica cuando el [safe mode SQL](#ini.sql.safe-mode) está activado.

`mysql.connect_timeout` `int`  
Tiempo máximo de espera de la respuesta de un servidor, en segundos. En Linux, este tiempo sirve también durante el intercambio del primero con el servidor.
