---
title: escapeshellarg
description: Protege una cadena de caracteres para su uso en línea de comandos
source_url: https://www.php.net/manual/es/function.escapeshellarg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exec/functions/escapeshellarg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exec
translation_status: ready
translation_reviewed: false
translation_revision: 60c391265
order: 20530
---

escapeshellarg

Protege una cadena de caracteres para su uso en línea de comandos

## Descripción

```php
escapeshellarg(string $arg): string
```php

`escapeshellarg` añade comillas simples alrededor de las cadenas de caracteres, y añade comillas y escapa las comillas simples de la cadena. Esto permite pasar directamente el argumento `arg` como argumento Shell, garantizando un máximo de seguridad. `escapeshellarg` debe ser utilizada para tratar individualmente cada uno de los argumentos a pasar al Shell. Las funciones Shell son `exec`, `system` y los operadores [comillas invertidas](#language.operators.execution).

En Windows, `escapeshellarg` reemplaza en su lugar los signos de porcentaje, los signos de exclamación (sustitución de variables diferidas) y las comillas dobles con espacios y añade comillas dobles alrededor de la cadena. Además, cada serie de barras invertidas consecutivas (`\`) es escapada por una barra invertida adicional.

## Parámetros

`arg`  
El argumento a escapar.

## Valores devueltos

La cadena escapada.

## Ejemplos

Ejemplo con `escapeshellarg`

```
<?php
system('ls '.escapeshellarg($dir));
?>

    
```php

## Véase también

`escapeshellcmd`, `exec`, `popen`, `system`, [comillas invertidas](#language.operators.execution)
