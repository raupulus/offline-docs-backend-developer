---
title: Instalación
source_url: https://www.php.net/manual/es/exif.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exif/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exif
translation_status: ready
translation_revision: 6a08181be
order: 20650
---

## Instalación

Para habilitar el soporte para exif configure PHP con `--enable-exif`

Los usuarios de Windows deben habilitar las DLL `php_mbstring.dll` y `php_exif.dll` en `php.ini`. La DLL `php_mbstring.dll` debe cargarse *antes* que la DLL `php_exif.dll`, así que ajuste su `php.ini` como corresponde.
