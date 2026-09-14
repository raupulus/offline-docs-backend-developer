---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/apache.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apache/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apache
translation_status: ready
translation_revision: d4d5216e7
order: 4840
---

## Configuración en tiempo de ejecución

El comportamiento del módulo de PHP de Apache está regido por los valores definidos en `php.ini`. Estos valores de configuración definidos en `php.ini` pueden ser sobreescritos por la configuración del [php_flag](#configuration.changes.apache) definidos en el fichero de configuración del servidor o por los ficheros `.htaccess` locales.

Desactivar el intérprete de PHP en un directorio utilizando `.htaccess`

    php_flag engine off

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [engine](#ini.engine) | "1" | `INI_ALL` |  |
| [child_terminate](#ini.child-terminate) | "0" | `INI_ALL` |  |
| [last_modified](#ini.last-modified) | "0" | `INI_ALL` |  |
| [xbithack](#ini.xbithack) | "0" | `INI_ALL` |  |

Opciones de configuración de Apache

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`engine` `bool`  
Activa o desactiva la ejecución de PHP. Esta directiva se puede utilizar sólo en la versión de PHP como módulo de Apache. Se usa en los sitios que deseen controlar la activación o desactivación del PHP en cada directorio o servidor virtual. Al establecer `engine off` en los lugares apropiados en el archivo `httpd.conf`, PHP puede ser activado o desactivado.

`child_terminate` `bool`  
Especifica si los scripts PHP pueden solicitar la finalización de los procesos hijos al finalizar la petición, véase también `apache_child_terminate`.

`last_modified` `bool`  
Envía la fecha de modificación de los scripts PHP con la cabecera 'Last-Modified:' para estas peticiones.

`xbithack` `bool`  
Analiza los ficheros con bit de ejecución establecido para PHP, con independencia de la extensión del fichero
