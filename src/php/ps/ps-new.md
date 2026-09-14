---
title: ps_new
description: Crea un nuevo objeto de documento PostScript
source_url: https://www.php.net/manual/es/function.ps-new.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-new.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 9486a954a
order: 65880
---

ps_new

Crea un nuevo objeto de documento PostScript

## Descripción

```php
ps_new(): resource
```php

Crea una nueva instancia de documento. No crea el fichero en el disco ni en la memoria. Simplemente prepara todo. `ps_new` es normalmente seguida por una llamada a `ps_open_file` para crear el documento PostScript.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Recurso de un documento PostScript o `false` si ocurre un error. El valor de retorno es pasado a todas las demás funciones como primer argumento.

## Véase también

`ps_delete`
