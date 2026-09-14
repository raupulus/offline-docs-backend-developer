---
title: recode_file
description: Recodificación de fichero a fichero, según la solicitud
source_url: https://www.php.net/manual/es/function.recode-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/recode/functions/recode-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: recode
translation_status: ready
translation_reviewed: false
translation_revision: 72f847e07
order: 68870
---

recode_file

Recodificación de fichero a fichero, según la solicitud

## Descripción

```php
recode_file(string $request, resource $input, resource $output): bool
```php

Recodifica el fichero identificado por `input` en el fichero identificado por `output` según la solicitud de recodificación `request`.

## Parámetros

`request`  
El tipo de solicitud de recodificación deseada

`input`  
Un gestor de fichero local para el argumento `input`

`output`  
Un gestor de fichero local para el argumento `output`

## Valores devueltos

Retorna `false` en caso de fallo, y `true` en caso contrario.

## Ejemplos

Ejemplo con `recode_file`

```
<?php
$input = fopen('input.txt', 'r');
$output = fopen('output.txt', 'w');
recode_file("us..flat", $input, $output);
?>

   
```php

## Notas

Esta función aún no maneja ficheros remotos (URL). Ambos ficheros deben hacer referencia a ficheros locales.

## Véase también

fopen
