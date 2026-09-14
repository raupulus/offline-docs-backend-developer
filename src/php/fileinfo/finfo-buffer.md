---
title: finfo_buffer
description: Devuelve información acerca de un string de buffer
source_url: https://www.php.net/manual/es/function.finfo-buffer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fileinfo/functions/finfo-buffer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fileinfo
translation_status: ready
translation_reviewed: false
translation_revision: e5c8e7add
order: 23190
---

finfo_buffer

finfo::buffer

Devuelve información acerca de un string de buffer

## Descripción

Estilo procedimental

```php
finfo_buffer(finfo $finfo, string $string, [int $flags], [resource $context]): string
```php

Estilo orientado a objetos

```php
public finfo::buffer(string $string, [int $flags], [resource $context]): string
```

Esta función se utiliza para obtener información acerca de datos binarios en un string.

## Parámetros

`finfo`  
Una instancia `finfo`, retornada por `finfo_open`.

`string`  
Contenido de un fichero a ser verificado.

`flags`  
Una o una unión de varias [constantes Fileinfo](#fileinfo.constants).

`context`  

## Valores devueltos

Devuelve una descripción textual del argumento `string` o `false` si ha ocurrido un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | El parámetro `context` ha quedado obsoleto puesto que es ignorado. |
| 8.1.0 | El parámetro `finfo` ahora espera una instancia de `finfo` ; anteriormente, una `resource` era esperado. |
| 8.0.0 | `context` ahora es nullable. |

## Ejemplos

Ejemplo con `finfo_buffer`

```php
<?php
$finfo = new finfo(FILEINFO_MIME);
echo $finfo->buffer($_POST["script"]) . "\n";
?>

   
```

Resultado del ejemplo anterior es similar a:

    application/x-sh; charset=us-ascii

## Véase también

finfo_file
