---
title: Instalación
source_url: https://www.php.net/manual/es/memcached.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_revision: 7916455ba
order: 46300
---

## Instalación

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/memcached>.

Si libmemcached está instalada en una ubicación no estándar, use la opción `--with-libmemcached-dir=DIR`, siendo DIR el prefijo de instalación de libmemcached. Este directorio debe contener el fichero `include/libmemcached/memcached.h`.

Se requiere Zlib para el soporte de compresión. Para especificar una instalación no estándar de Zlib, use la opción `--with-zlib-dir=DIR` siendo DIR el prefijo de instalación de Zlib.

El soporte para el controlador de sesiones está activado de manera predeterminada. Para desactivarlo, use la opción `--disable-memcached-session`.

El soporte para la autenticación SASL está deshabilitado de forma predeterminada. Para habilitarlo, use la opción `--enable-memcached-sasl`. Esto requiere que haya sido instalada libsasl2 y que libmemcached haya sido construida con el soporte para SASL habilitado.
