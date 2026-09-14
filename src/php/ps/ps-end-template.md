---
title: ps_end_template
description: Finalizar una plantilla
source_url: https://www.php.net/manual/es/function.ps-end-template.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-end-template.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65760
---

ps_end_template

Finalizar una plantilla

## Descripción

```php
ps_end_template(resource $psdoc): bool
```php

Finaliza una plantilla que fue creada con la función `ps_begin_template`. Una vez que la plantilla ha sido finalizada se puede usar como una imagen.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_begin_template`
