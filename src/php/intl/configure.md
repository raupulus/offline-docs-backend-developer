---
title: Instalación
source_url: https://www.php.net/manual/es/intl.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 6681b88ea
order: 39520
---

## Instalación

`--enable-intl` activará la extensión de manera integrada durante la compilación.

Si la biblioteca ICU está instalada en un directorio no estándar, puede ser necesario especificar su ubicación mediante la variable de entorno `LD_LIBRARY_PATH`, para que el compilador dinámico pueda encontrarla:

    $ export LD_LIBRARY_PATH=/opt/icu/lib

De lo contrario, si PHP e ICU están instalados en sus directorios por defecto, entonces no se requieren opciones particulares para `configure`.
