---
title: Opciones SAPI
source_url: https://www.php.net/manual/es/configure.options.servers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/configure/servers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 6a5b42e0d
order: 70
---

### Opciones SAPI

La siguiente lista contiene las SAPI disponibles (`Server Application Programming Interface`) para PHP.

`--with-apxs[=FILE]`  
Compila un módulo compartido de Apache. FILE es la ruta de acceso opcional a la herramienta apxs de Apache; el valor predeterminado es apxs. Se debe asegurar de especificar la versión de apxs instalada en el sistema y no la que se encuentra en el archivo comprimido del código fuente de Apache.

`--with-apache[=DIR]`  
Compila un módulo estático de Apache. DIR es el directorio de compilación de nivel superior de Apache; el valor predeterminado es `/usr/local/apache`.

`--with-mod_charset`  
Habilita la transferencia de tablas para mod_charset (Apache en ruso).

`--with-apxs2[=FILE]`  
Compila un módulo compartido de Apache 2.0. FILE es la ruta de acceso opcional a la herramienta apxs; el valor predeterminado es apxs.

`--disable-cli`  
Deshabilita la versión CLI de PHP (esto fuerza [--without-pear](#configure.without-pear)). Para obtener más información, véase la sección sobre [Uso de PHP desde la línea de comandos](#features.commandline).

`--enable-phpdbg`  
Habilita el soporte para el módulo SAPI de depuración interactiva phpdbg.

`--enable-embed[=TYPE]`  
Habilita la creación de la biblioteca SAPI. TYPE es `shared` o `static`, el valor por defecto es `shared`.

`--with-servlet[=DIR]`  
Incluye soporte para servlet. DIR es el directorio base de instalación del JSDK. Esta SAPI requiere que la extensión Java se compile como una biblioteca dinámica compartida (dl).

`--disable-cgi`  
Deshabilita la compilación de la versión CGI de PHP.

Este argumento también habilita FastCGI.
