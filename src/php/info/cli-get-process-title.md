---
title: cli_get_process_title
description: Devuelve el título del proceso actual
source_url: https://www.php.net/manual/es/function.cli-get-process-title.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/cli-get-process-title.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: false
translation_revision: b08b472de
order: 38740
---

cli_get_process_title

Devuelve el título del proceso actual

## Descripción

```php
cli_get_process_title(): string
```php

Devuelve el título del proceso actual, tal como se definió mediante la función `cli_set_process_title`. Tenga en cuenta que este título puede ser ligeramente diferente al que se muestra mediante los comandos `ps` y `top`, según el sistema subyacente.

Esta función solo está disponible en modo [CLI](#features.commandline).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el título del proceso actual, en forma de una cadena de caracteres, o `null` si ocurre un error.

## Errores/Excepciones

Se generará una advertencia de nivel `E_WARNING` si el sistema subyacente no es compatible.

## Ejemplos

Ejemplo con `cli_get_process_title`

```
<?php
echo "Título del proceso: " . cli_get_process_title() . "\n";
?>

    
```php

## Véase también

`cli_set_process_title`
