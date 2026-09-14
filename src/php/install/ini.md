---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: false
translation_revision: 9ab074d32
order: 1700
---

## Configuración en tiempo de ejecución

## El fichero de configuración

El fichero de configuración (`php.ini`) es leído por PHP al inicio. Si se ha compilado PHP como módulo, el fichero solo se lee una vez, al inicio del servidor web. Para las versiones CGI y CLI el fichero es leído en cada invocación.

El `php.ini` se busca en estos lugares (y en este orden) :

- El lugar específico del módulo SAPI (la directiva `PHPIniDir` de Apache 2, la opción de la línea de comandos `-c` en CGI y en CLI)

- La variable de entorno `PHPRC`.

- El lugar donde se encuentra el fichero `php.ini` puede ser definido para diferentes versiones de PHP. La raíz de las claves de registro depende de la arquitectura de 32 o 64 bits del SO y de PHP. Para un SO y PHP de 32 bits o un SO y PHP de 64 bits, utilizar `[HKEY_LOCAL_MACHINE\SOFTWARE\PHP]` para PHP de 32 bits en un SO de 64 bits, utilizar `[HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\PHP]` en su lugar. Para una instalación con la misma arquitectura, las siguientes claves de registro se buscan en este orden : `[HKEY_LOCAL_MACHINE\SOFTWARE\PHP\x.y.z]`, `[HKEY_LOCAL_MACHINE\SOFTWARE\PHP\x.y]` y `[HKEY_LOCAL_MACHINE\SOFTWARE\PHP\x]`, donde x, y y z significan las versiones mayores, menores y normales. Para una arquitectura de 32 bits de PHP en un SO de 64 bits, las siguientes claves de registro se buscan en este orden : `[HKEY_LOCAL_MACHINE\SOFTWARE\WOW6421Node\PHP\x.y.z]`, `[HKEY_LOCAL_MACHINE\SOFTWARE\WOW6421Node\PHP\x.y]` y `[HKEY_LOCAL_MACHINE\SOFTWARE\WOW6421Node\PHP\x]`, donde x, y y z significan las versiones mayores, menores y normales. Si hay un valor para `IniFilePath` en estas claves, el primero encontrado será utilizado como el lugar donde se encuentra el fichero `php.ini` (solo en Windows).

- `[HKEY_LOCAL_MACHINE\SOFTWARE\PHP]` o `[HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\PHP]`, valor de `IniFilePath` (solo en Windows).

- El directorio de trabajo actual (excepto para CLI)

- El directorio del servidor web (para los módulos SAPI), o el directorio que contiene PHP (de otro modo en Windows)

- El directorio Windows (`C:\windows` o `C:\winnt`) (para Windows), o la opción de compilación `--with-config-file-path` durante la compilación

Si el fichero `php-SAPI.ini` existe (donde SAPI utiliza SAPI, por lo que el nombre del fichero es e.g. `php-cli.ini` o `php-apache.ini`), se utilizará en lugar de `php.ini`. El nombre SAPI puede ser determinado utilizando la función `php_sapi_name`.

> [!NOTE]
> El servidor web Apache cambia este directorio al directorio root al inicio, lo que hace que PHP intente leer `php.ini` desde el sistema de ficheros raíz si existe.

Las variables de entorno pueden ser referenciadas en los valores de configuración de `php.ini` como se ilustra a continuación. A partir de PHP 8.3.0, un valor de repliegue puede ser especificado, que será utilizado cuando la variable referenciada no esté definida.

Variables de entorno en `php.ini`

```php
; PHP_MEMORY_LIMIT se toma desde el entorno
memory_limit = ${PHP_MEMORY_LIMIT}
; Si PHP_MAX_EXECUTION_TIME no está definido, tomará el valor de repliegue 30.
max_execution_time = ${PHP_MAX_EXECUTION_TIME:-30}

   
```

Las directivas `php.ini` están directamente documentadas, por extensiones, en las páginas respectivas del manual de estas extensiones. La [lista de directivas internas](#ini) está disponible en el anexo. Es probable que no todas las directivas PHP estén documentadas en el manual. Para una lista completa de las directivas disponibles en su versión de PHP, lea los comentarios de su propio fichero `php.ini`. También se puede encontrar la [última versión del `php.ini`](https://github.com/php/php-src/blob/master/php.ini-production) en Git.

Extracto del `php.ini`

```php
; todo texto en una línea, situado después de un punto y coma ";" es ignorado
[php] ; los marcadores de sección (texto entre corchetes) también son ignorados
; Los valores booleanos pueden ser especificados así :
;    true, on, yes
; o false, off, no, none
register_globals = off
track_errors = yes

; se pueden colocar las cadenas de caracteres entre comillas
include_path = ".:/usr/local/lib/php"

; Las barras invertidas se tratan como cualquier carácter
include_path = ".;c:\php\lib"

    
```

Es posible referirse a variables .ini desde ficheros .ini. Por ejemplo : `open_basedir = ${open_basedir} ":/new/dir"`.

### Leer un directorio

Es posible configurar PHP para leer los ficheros .ini presentes en un directorio. después de la lectura de `php.ini`. Esto se ajusta durante la compilación con el argumento `--with-config-file-scan-dir`. El directorio a leer puede ser modificado durante la ejecución por la definición de la variable de entorno `PHP_INI_SCAN_DIR`.

Es posible leer varios directorios separándolos con un separador de ruta específico de la plataforma (`;` para Windows, NetWare y RISC OS; `:` para todas las otras plataformas; el valor utilizado por PHP es disponible en la constante `PATH_SEPARATOR`). Si se proporciona un directorio vacío en `PHP_INI_SCAN_DIR`, PHP también leerá el directorio proporcionado durante la compilación a través de `--with-config-file-scan-dir`.

En cada directorio, PHP leerá todos los ficheros que terminen por `.ini` en orden alfabético. Una lista de los ficheros que han sido cargados y en qué orden está disponible llamando a la función `php_ini_scanned_files`, o ejecutando PHP con la opción `--ini`.

    Suponiendo que PHP está configurado con --with-config-file-scan-dir=/etc/php.d,
    y que el separador de ruta es :...

    $ php
      PHP cargará todos los ficheros presentes en /etc/php.d/*.ini como fichero
      de configuración.

    $ PHP_INI_SCAN_DIR=/usr/local/etc/php.d php
      PHP cargará todos los ficheros presentes en /usr/local/etc/php.d/*.ini
      como fichero de configuración.

    $ PHP_INI_SCAN_DIR=:/usr/local/etc/php.d php
      PHP cargará todos los ficheros presentes en /etc/php.d/*.ini, luego
      /usr/local/etc/php.d/*.ini como fichero de configuración.

    $ PHP_INI_SCAN_DIR=/usr/local/etc/php.d: php
      PHP cargará todos los ficheros presentes en /usr/local/etc/php.d/*.ini, luego en
      /etc/php.d/*.ini como fichero de configuración.

## Ficheros .user.ini

PHP incluye el soporte para ficheros INI de configuración por directorio. Estos ficheros son analizados *solo* por el SAPI CGI/FastCGI. Esta funcionalidad hace obsoleta la extensión PECL `htscanner`. Si se ejecuta PHP como módulo Apache, el uso de los ficheros `.htaccess` produce el mismo efecto.

Además del fichero `php.ini` principal, PHP analiza los ficheros INI contenidos en cada directorio, comenzando por el directorio desde el cual el fichero PHP actual es llamado, y recorre los directorios hasta el directorio raíz actual (tal como se define por la variable `$_SERVER['DOCUMENT_ROOT']`). En el caso de que el fichero PHP esté fuera de la raíz web, solo su directorio será escaneado.

Solo las configuraciones INI con los modos `INI_PERDIR` y `INI_USER` serán reconocidas en los ficheros INI .user.ini-style.

Dos nuevas directivas INI, [user_ini.filename](#ini.user-ini.filename) y [user_ini.cache_ttl](#ini.user-ini.cache-ttl) controlan el uso de los ficheros INI definidos por el usuario.

[user_ini.filename](#ini.user-ini.filename) define el nombre del fichero buscado por PHP en cada directorio ; si esta directiva está definida a una cadena vacía, PHP no analizará nada en absoluto. Por defecto, vale `.user.ini`.

[user_ini.cache_ttl](#ini.user-ini.cache-ttl) controla la duración entre 2 relecturas de los ficheros INI definidos por el usuario. Por defecto, vale 300 segundos (5 minutos).

## Dónde una directiva de configuración puede ser modificada

Estos modos determinan cuándo y dónde una directiva PHP puede o no puede ser modificada, y cada directiva del manual está dirigida por uno de estos modos. Por ejemplo, algunas directivas pueden ser modificadas en un script PHP con la función `ini_set`, mientras que otras necesitan ser modificadas en los ficheros `php.ini` o `httpd.conf`.

Por ejemplo, la directiva [output_buffering](#ini.output-buffering) tiene el modo `INI_PERDIR` por lo que no puede ser modificada con la función `ini_set`. Por otro lado, la directiva [display_errors](#ini.display-errors) tiene el modo `INI_ALL`, y puede ser modificada en cualquier lugar, incluyendo con la función `ini_set`.

`INI_USER` (`int`)  
La entrada puede ser definida en scripts de usuario (como con `ini_set`) o en el [registro Windows](#configuration.changes.windows). La entrada puede ser definida en `.user.ini`

`INI_PERDIR` (`int`)  
La entrada puede ser definida en `php.ini`, `.htaccess`, `httpd.conf` o `.user.ini`

`INI_SYSTEM` (`int`)  
La entrada puede ser definida en `php.ini` o `httpd.conf`

`INI_ALL` (`int`)  
La entrada puede ser definida en cualquier lugar

## Cómo modificar la configuración

### Ejecutar PHP como módulo Apache

Cuando se utiliza el módulo Apache, también se pueden cambiar los parámetros de configuración utilizando las directivas en los ficheros de configuración de Apache (`httpd.conf`) y en los ficheros `.htaccess`. Se necesitarán los privilegios "AllowOverride Options" o "AllowOverride All".

Hay muchas directivas Apache que permiten modificar la configuración de PHP desde los ficheros de configuración de Apache. Para una lista de las directivas que son `INI_ALL`, `INI_PERDIR` o `INI_SYSTEM` consulte el anexo [Lista de directivas del php.ini](#ini.list).

`php_value` `nombre` `valor`  
Modifica el valor de la directiva especificada. Esta instrucción solo es utilizable con las directivas PHP de tipo `INI_ALL` y `INI_PERDIR`. Para anular un valor que hubiera sido modificado previamente, utilice el valor `none`.

> [!NOTE]
> No utilice `php_value` para configurar valores booleanos. `php_flag` (ver más abajo) debe ser utilizada.

`php_flag` `nombre` `on|off`  
Esta instrucción se utiliza para activar o desactivar una opción. Esta instrucción solo es utilizable con las directivas PHP de tipo `INI_ALL` y `INI_PERDIR`.

`php_admin_value` `nombre` `valor`  
Esta instrucción asigna un valor a la variable especificada. Esta instrucción *NO puede ser utilizada* en un fichero `.htaccess`. Cualquier directiva de PHP configurada con el tipo `php_admin_value` no puede ser modificada utilizando el fichero `.htaccess` o la función `ini_set`. Para anular un valor que hubiera sido modificado previamente, utilice la valor `none`.

`php_admin_flag` `name` `on|off`  
Esta directiva se utiliza para activar o desactivar una opción. Esta instrucción *NO puede ser utilizada* en un fichero `.htaccess`. Cualquier directiva de PHP configurada con el tipo `php_admin_flag` no puede ser modificada utilizando el fichero `.htaccess` o por la función `ini_set`.

Ejemplo de configuración Apache

```php
<IfModule mod_php5.c>
  php_value include_path ".:/usr/local/lib/php"
  php_admin_flag engine on
</IfModule>
<IfModule mod_php4.c>
  php_value include_path ".:/usr/local/lib/php"
  php_admin_flag engine on
</IfModule>

     
```

> [!CAUTION]
> Las constantes PHP no existen fuera de PHP. Por ejemplo, en el fichero `httpd.conf`, no se pueden utilizar constantes PHP como `E_ALL` o `E_NOTICE` para especificar el nivel de [informe de errores](#ini.error-reporting), ya que estas constantes no tienen significado para Apache, y serán reemplazadas por *0*. Utilice los valores numéricos en su lugar. Las constantes pueden ser utilizadas en el `php.ini`

### Modificar la configuración de PHP a través del registro de Windows

Cuando se utiliza PHP en Windows, la configuración puede ser modificada directorio por directorio utilizando el registro de Windows. Los valores de configuración se almacenan con la clave de registro `HKLM\SOFTWARE\PHP\Per Directory Values`, en las subclaves correspondientes a los nombres de directorio. Por ejemplo, el valor de una opción en el directorio `c:\inetpub\wwwroot` se almacenará en la clave `HKLM\SOFTWARE\PHP\Per Directory Values\c\inetpub\wwwroot`. El valor de esta opción será utilizado para todos los scripts que funcionen en este directorio o sus subdirectorios. Los valores bajo la clave deben tener el nombre de una dirección de configuración PHP, y el valor correspondiente. Las constantes PHP no son utilizables : hay que poner el valor entero. Sin embargo, solo los valores de las configuraciones en `INI_USER` pueden ser fijados de esta manera, los de `INI_PERDIR` no pueden serlo, ya que estos valores de configuración son releídos en cada solicitud.

### Otras interfaces de configuración de PHP

Según la forma en que se ejecute PHP, se pueden cambiar algunos valores durante la ejecución de los scripts utilizando `ini_set`. Consulte la documentación de la función `ini_set` para más información.

Si está interesado en una lista completa de las opciones configuradas en su sistema con sus valores actuales, puede ejecutar la función `phpinfo` y consultar la página resultante. También se puede acceder individualmente a las directivas de configuración durante la ejecución de los scripts utilizando la función `ini_get` o la función `get_cfg_var`.
