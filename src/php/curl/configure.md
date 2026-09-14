---
title: Instalación
source_url: https://www.php.net/manual/es/curl.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: 184f3f7bd
order: 9590
---

## Instalación

Para utilizar cURL desde los scripts PHP, debe compilárselo con la opción `--with-curl[=DIR]` donde DIR es la ruta hasta el directorio que contiene los directorios `lib` y `include`. En el directorio `include`, debe existir un directorio llamado `curl`, que contiene entre otros los ficheros `easy.h` y `curl.h`. Debe existir también un fichero llamado `libcurl.a` en el directorio `lib`.

> [!NOTE]
> Para activar este módulo en el entorno Windows, `libeay32.dll` y `ssleay32.dll`, o, desde OpenSSL 1.1, `libcrypto-*.dll` y `libssl-*.dll`, deben estar presentes en el `PATH`. `libssh2.dll` debe estar también presente en el `PATH`.
>
> No es necesario `libcurl.dll` del sitio cURL.
