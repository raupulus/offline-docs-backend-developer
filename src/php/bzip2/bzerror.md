---
title: bzerror
description: Devuelve el número de error y la cadena del error de bzip2 en un array
source_url: https://www.php.net/manual/es/function.bzerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bzip2/functions/bzerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bzip2
translation_status: ready
translation_revision: 5fdeb11b1
order: 6440
---

bzerror

Devuelve el número de error y la cadena del error de bzip2 en un array

## Descripción

```php
bzerror(resource $bz): array
```php

Devuelve el número de error y la cadena de error de cualquier error bzip2 devuelto por el puntero del fichero dado.

## Parámetros

`bz`  
El puntero del fichero. Debe ser un puntero a un fichero abierto con `bzopen` satisfactoriamente.

## Valores devueltos

Devuelve un array asociativo, con el código de error en la entrada `errno` y el mensaje de error en la entrada `errstr`.

## Ejemplos

Ejemplo de `bzerror`

```
<?php
$error = bzerror($bz);

echo $error["errno"];
echo $error["errstr"];
?>

   
```php

## Véase también

bzerrno

bzerrstr
