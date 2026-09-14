---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/mysqli.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 90787fda1
order: 54880
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [mysqli.allow_local_infile](#ini.mysqli.allow-local-infile) | "0" | `INI_SYSTEM` | Anterior a PHP 7.2.16 y 7.3.3 el valor por omisión era "1". |
| [mysqli.local_infile_directory](#ini.mysqli.local-infile-directory) |  | `INI_SYSTEM` | Disponible a partir de PHP 8.1.0. |
| [mysqli.allow_persistent](#ini.mysqli.allow-persistent) | "1" | `INI_SYSTEM` |  |
| [mysqli.max_persistent](#ini.mysqli.max-persistent) | "-1" | `INI_SYSTEM` |  |
| [mysqli.max_links](#ini.mysqli.max-links) | "-1" | `INI_SYSTEM` |  |
| [mysqli.default_port](#ini.mysqli.default-port) | "3306" | `INI_ALL` |  |
| [mysqli.default_socket](#ini.mysqli.default-socket) | NULL | `INI_ALL` |  |
| [mysqli.default_host](#ini.mysqli.default-host) | NULL | `INI_ALL` |  |
| [mysqli.default_user](#ini.mysqli.default-user) | NULL | `INI_ALL` |  |
| [mysqli.default_pw](#ini.mysqli.default-pw) | NULL | `INI_ALL` |  |
| [mysqli.reconnect](#ini.mysqli.reconnect) | "0" | `INI_SYSTEM` | Eliminada a partir de PHP 8.2.0 |
| [mysqli.rollback_on_cached_plink](#ini.mysqli.rollback-on-cached-plink) | "0" | `INI_SYSTEM` |  |

Opciones de configuración MySQLi {#mysqli.configuration.options}

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Para más detalles y definiciones sobre las constantes INI\_\* anteriores, consulte el capítulo sobre [ modificaciones de configuración](#configuration.changes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`mysqli.allow_local_infile` `int`  
Permite el acceso, desde PHP, a los ficheros locales cargados con LOAD DATA.

`mysqli.local_infile_directory` `string`  
Permite una carga restringida LOCAL DATA hacia ficheros que se encuentren en el directorio designado.

`mysqli.allow_persistent` `int`  
Activa la posibilidad de crear conexiones persistentes utilizando la función `mysqli_connect`.

`mysqli.max_persistent` `int`  
Número máximo de conexiones persistentes que pueden realizarse. Establecer a 0 para "ilimitado".

`mysqli.max_links` `int`  
El número máximo de conexiones MySQL por proceso, incluyendo las conexiones persistentes.

`mysqli.default_port` `int`  
El número de puerto TCP por omisión a utilizar al conectarse al servidor si no se proporciona otro puerto. Si no está definido, el puerto se obtendrá de la variable de entorno `MYSQL_TCP_PORT`, la entrada `mysql-tcp` en `/etc/services` o la constante de compilación `MYSQL_PORT`, en este orden. Win32 solo utilizará la constante `MYSQL_PORT`.

`mysqli.default_socket` `string`  
El nombre por omisión del socket a utilizar durante las conexiones locales al servidor si no se proporciona otro nombre.

`mysqli.default_host` `string`  
El servidor por omisión a utilizar al conectarse a un servidor si no se proporciona otro host.

`mysqli.default_user` `string`  
El nombre de usuario por omisión a utilizar al conectarse a un servidor si no se proporciona otro nombre.

`mysqli.default_pw` `string`  
La contraseña por omisión a utilizar al conectarse a un servidor si no se proporciona otra contraseña.

`mysqli.reconnect` `int`  
Reconexión automática si la conexión se interrumpe.

> [!NOTE]
> Esta directiva `php.ini` había sido ignorada por el controlador mysqlnd y fue eliminada a partir de PHP 8.2.0.

`mysqli.rollback_on_cached_plink` `bool`  
Si esta opción está activada, el cierre de una conexión permanente anula todas las transacciones pendientes de esta conexión antes de ser reemplazada en el grupo de conexiones persistentes. De lo contrario, las transacciones pendientes serán restauradas únicamente cuando la conexión es reutilizada o cuando se cierra realmente.

Los usuarios no pueden cambiar `MYSQL_OPT_READ_TIMEOUT` mediante una llamada a la API o en tiempo de ejecución. Tenga en cuenta que incluso si es posible, habrá diferencias en la manera en que `libmysqlclient` y los flujos van a interpretar el valor de `MYSQL_OPT_READ_TIMEOUT`.
