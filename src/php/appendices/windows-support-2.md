---
title: Soporte para Windows
source_url: https://www.php.net/manual/es/migration73.windows-support.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration73/windows-support.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 204f2c1c8
order: 660
---

## Soporte para Windows

## Núcleo PHP

### Más eliminación de archivos conforme con POSIX

Los descriptores de archivos son abiertos en modo compartido lectura/escritura/borrado por defecto. Esto mapea efectivamente la semántica de POSIX y permite eliminar los archivos con manejador en uso. No es 100% igual, algunas diferencias de plataforma todavía persisten. Después de la eliminación, la entrada del nombre del archivo es bloqueada, hasta que todos los manejadores abiertos estén cerrados.
