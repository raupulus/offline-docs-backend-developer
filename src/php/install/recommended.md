---
title: Configuración recomendada en sistemas Windows
source_url: https://www.php.net/manual/es/install.windows.recommended.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/windows/recommended.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_revision: 6160a5908
order: 1950
---

## Configuración recomendada en sistemas Windows

## OpCache

Se recomienda encarecidamente activar OpCache. Esta extensión está incluida con PHP para Windows. Compila y optimiza los scripts PHP y los almacena en caché en memoria para que no se compilen cada vez que se carga la página.

Definir el `php.ini` a :

Configuración recomendada para OpCache

    opcache.enable=On
    opcache.enable_cli=On

Y reiniciar el servidor web. Para más información, leer : [Configuración de OpCache](#opcache.configuration)

## WinCache

Se recomienda utilizar WinCache al usar IIS, especialmente en un entorno de alojamiento web compartido o al usar almacenamiento de ficheros en red (NAS). Todas las aplicaciones PHP se benefician automáticamente de la funcionalidad de caché de ficheros de WinCache. Las operaciones del sistema de ficheros se almacenan en caché en memoria. WinCache también puede almacenar en caché en memoria objetos del usuario y compartirlos entre los procesos `php.exe` o `php-cgi.exe` (compartir objetos entre las peticiones). Muchas aplicaciones web importantes tienen un complemento o una extensión o una opción de configuración para usar el caché de objetos del usuario de WinCache. Si se requiere un alto rendimiento, utilice el caché de objetos en las aplicaciones. Ver : <https://pecl.php.net/package/WinCache> para descargar una DLL WinCache (o `WINCACHE_*.tgz`) en el directorio de extensiones PHP ([extension_dir](#ini.extension-dir) en el fichero `php.ini`). Definir el `php.ini` a :

Configuración recomendada para WinCache

    extension=php_wincache.dll
    wincache.fcenabled=1
    wincache.ocenabled=1 ; removed as of wincache 2.0.0.0

Para más información, leer : [Configuración de WinCache](#wincache.configuration)
