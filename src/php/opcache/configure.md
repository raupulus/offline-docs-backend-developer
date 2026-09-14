---
title: Instalación
source_url: https://www.php.net/manual/es/opcache.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/opcache/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: opcache
translation_status: ready
translation_reviewed: false
translation_revision: 87d6bb1bb
order: 58560
---

## Instalación

OPcache solo puede ser compilado como una extensión compartida. Si se ha desactivado la compilación de extensiones por omisión con `--disable-all`, es necesario compilar PHP con la opción `--enable-opcache` para que OPcache esté disponible.

Una vez compilado, puede utilizarse la directiva de configuración [zend_extension](#ini.zend-extension) para cargar la extensión OPcache en PHP. Esto puede realizarse con `zend_extension=/full/path/to/opcache.so` en plataformas no-Windows, y `zend_extension=C:\path\to\php_opcache.dll` en Windows.

> [!NOTE]
> Si se desea utilizar OPcache con [Xdebug](http://xdebug.org/), debe cargarse OPcache antes que Xdebug.

## Configuración php.ini recomendada

La siguiente configuración es generalmente recomendada, ya que proporciona un buen rendimiento :

    opcache.memory_consumption=128
    opcache.interned_strings_buffer=8
    opcache.max_accelerated_files=4000
    opcache.revalidate_freq=60
    opcache.fast_shutdown=1 ; anterior a PHP 7.2.0
    opcache.enable_cli=1

Asimismo, podría ser deseable desactivar [opcache.save_comments](#ini.opcache.save-comments) y activar [opcache.enable_file_override](#ini.opcache.enable-file-override), sin embargo, tenga en cuenta que debe probarse el código antes de utilizarlo en producción, ya que podría romper frameworks y aplicaciones, especialmente en casos donde se utilicen anotaciones de comentarios de documentación.

En Windows, [opcache.file_cache_fallback](#ini.opcache.file-cache-fallback) debe estar activado, y [opcache.file_cache](#ini.opcache.file-cache) debe definirse a una carpeta existente y escribible.

Una lista completa de directivas de configuración soportadas por OPcache [está disponible](#opcache.configuration).
