---
title: Soporte para Windows
source_url: https://www.php.net/manual/es/migration82.windows-support.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration82/windows-support.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 65716f476
order: 980
---

## Soporte para Windows

## Núcleo

Los mensajes de error específicos de Windows ya no están localizados, pero siguen estando disponibles en inglés para que coincidan mejor con los mensajes de error de PHP.

Se ha añadido un soporte preliminar y altamente experimental para la compilación en ARM64.

## OCI8

Dado que la compilación con Oracle Client 10g ya no es soportada de ninguna manera, la opción de configuración `--with-oci8` ha sido eliminada. Las opciones de configuración `--with-oci8-11g`, `--with-oci8-12c` y `--with-oci8-19` siguen estando soportadas.

## Zip

La extensión Zip se ha actualizado a la versión 1.21.0, y ahora se compila como una biblioteca enlazada dinámicamente (DLL) por defecto.
