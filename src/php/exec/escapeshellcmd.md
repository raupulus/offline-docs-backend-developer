---
title: escapeshellcmd
description: Protege los caracteres especiales del Shell
source_url: https://www.php.net/manual/es/function.escapeshellcmd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exec/functions/escapeshellcmd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exec
translation_status: ready
translation_reviewed: false
translation_revision: 62126c55f
order: 20540
---

escapeshellcmd

Protege los caracteres especiales del Shell

## Descripción

```php
escapeshellcmd(string $command): string
```php

`escapeshellcmd` escapa todos los caracteres de la cadena `command` que podrían tener un significado especial en una orden Shell. Esta función permite asegurarse de que la orden será correctamente pasada al ejecutor de órdenes Shell `exec` y `system`, o incluso a [comillas invertidas](#language.operators.execution).

Los siguientes caracteres serán escapados: `` &#;`|*?~<>^()[]{}$\ ``, `\x0A` y `\xFF`. `'` y `"` son escapados solo si no están en pares. En Windows, todos estos caracteres así como `%` y `!` son precedidos por un circunflejo (`^`).

## Parámetros

`command`  
La orden a escapar.

## Valores devueltos

La cadena escapada.

## Ejemplos

Ejemplo con `escapeshellcmd`

```
<?php
// Se permiten intencionalmente un número arbitrario de argumentos aquí.
$command = './configure '.$_POST['configure_options'];

$escaped_command = escapeshellcmd($command);

system($escaped_command);
?>

    
```php

## Notas

> [!WARNING]
> La función `escapeshellcmd` debe ser utilizada sobre toda la cadena de orden, y permite a personas malintencionadas pasar un número arbitrario de argumentos. Para escapar un solo argumento, la función `escapeshellarg` debería ser utilizada en su lugar.

> [!WARNING]
> Los espacios no son escapados por `escapeshellcmd` lo cual puede ser problemático en Windows con rutas como: `C:\Program Files\ProgramName\program.exe`. Esto puede ser mitigado utilizando el siguiente fragmento de código:
>
> ```
> <?php
> $cmd = preg_replace('`(?<!^) `', '^ ', escapeshellcmd($cmd));
>
>     
> ```

## Véase también

`escapeshellarg`, `exec`, `popen`, `system`, [las comillas invertidas](#language.operators.execution)
