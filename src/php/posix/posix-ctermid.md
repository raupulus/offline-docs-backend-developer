---
title: posix_ctermid
description: Obtener el nombre de la ruta del terminal controlador
source_url: https://www.php.net/manual/es/function.posix-ctermid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-ctermid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: f8854f6a6
order: 65110
---

posix_ctermid

Obtener el nombre de la ruta del terminal controlador

## Descripción

```php
posix_ctermid(): string
```php

Genera un `string` que es el nombre de la ruta del terminal controlador actual para el proceso. En caso de error se establecerá a errno, que puede ser comprobado usando `posix_get_last_error`

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

En caso de terminación exitosa, devuelve un `string` del nombre de ruta del terminal controlador actual. De otro modo devuelve `false` y se establece errno, que puede ser comprobado con `posix_get_last_error`.

## Ejemplos

Ejemplo de `posix_ctermid`

Este ejemplo mostrará la ruta del TTY actual.

```
<?php
echo "Esto ejecutándome desde ".posix_ctermid();
?>

    
```php

## Véase también

`posix_ttyname`, `posix_get_last_error`
