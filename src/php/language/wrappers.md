---
title: Protocolos y Envolturas soportados
source_url: https://www.php.net/manual/es/wrappers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/wrappers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 8e2783c96
order: 4720
---

PHP incorpora de serie envolturas para distintos protocolos tipo URL para trabajar junto con funciones del sistema de ficheros, como `fopen`, `copy`, `file_exists` y `filesize`. Además de estas envolturas, se pueden definir por el usuario utilizando la función `stream_wrapper_register`.

> [!NOTE]
> La sintaxis de URL que se utiliza para describir una envoltura solo puede ser `scheme://...`. Las sintaxis `scheme:/` y `scheme:` no están soportadas.
