---
title: gztell
description: Indica la posición de lectura/escritura del apuntador al archivo gz
source_url: https://www.php.net/manual/es/function.gztell.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gztell.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: 02ba67b51
order: 108900
---

gztell

Indica la posición de lectura/escritura del apuntador al archivo gz

## Descripción

```php
gztell(resource $stream): int
```php

Obtiene la posición del apuntador al archivo dado; por ejemplo, su desplazamiento en el flujo del archivo sin comprimir.

## Parámetros

`stream`  
El apuntador al archivo gz. Debe ser válido y debe apuntar a un archivo abierto exitosamente por `gzopen`.

## Valores devueltos

La posición del apuntador al archivo o `false` si ocurre un error.

## Véase también

`gzopen`, `gzseek`, `gzrewind`
