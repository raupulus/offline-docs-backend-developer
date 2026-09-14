---
title: finfo_file
description: Devuelve información acerca de un fichero
source_url: https://www.php.net/manual/es/function.finfo-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fileinfo/functions/finfo-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fileinfo
translation_status: ready
translation_reviewed: false
translation_revision: 82ddd2ec8
order: 23210
---

finfo_file

finfo::file

Devuelve información acerca de un fichero

## Descripción

Estilo procedimental

```php
finfo_file(finfo $finfo, string $filename, [int $flags], [resource $context]): string
```php

Estilo orientado a objetos

```php
public finfo::file(string $filename, [int $flags], [resource $context]): string
```

Esta función se utiliza para obtener información acerca de un fichero.

## Parámetros

`finfo`  
Una instancia `finfo`, retornada por `finfo_open`.

`filename`  
Nombre de un fichero a verificar.

`flags`  
Una o una unión de varias [constantes Fileinfo](#fileinfo.constants).

`context`  
Para una descripción de `contexts`, consúltese [???](#ref.stream).

## Valores devueltos

Devuelve una descripción textual del contenido del argumento `filename` o `false` si ha ocurrido un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `finfo` ahora espera una instancia de `finfo` ; anteriormente, una `resource` era esperado. |
| 8.0.0 | `context` ahora es nullable. |

## Ejemplos

Ejemplo con `finfo_file`

```php
<?php
$finfo = finfo_open(FILEINFO_MIME_TYPE); // Devuelve el tipo mime también llamado extensión mimetype
foreach (glob("*") as $filename) {
    echo finfo_file($finfo, $filename) . "\n";
}
finfo_close($finfo);
?>

   
```

Resultado del ejemplo anterior es similar a:

    text/html
    image/gif
    application/vnd.ms-excel

## Véase también

finfo_buffer
