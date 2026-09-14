---
title: bzwrite
description: Escritura binaria en un archivo bzip2
source_url: https://www.php.net/manual/es/function.bzwrite.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bzip2/functions/bzwrite.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bzip2
translation_status: ready
translation_reviewed: true
translation_revision: 5fdeb11b1
order: 6490
---

bzwrite

Escritura binaria en un archivo bzip2

## Descripción

```php
bzwrite(resource $bz, string $data, [int $length]): int
```php

`bzwrite` escribe una cadena en el flujo de archivo bzip2 dado.

## Parámetros

`bz`  
El puntero de archivo. Debe ser válido y debe apuntar a un archivo abierto correctamente por la función `bzopen`.

`data`  
Los datos escritos.

`length`  
Si se proporciona, la escritura se detendrá después de que `length` (no comprimidos) bytes hayan sido escritos o bien se alcance el final de `data`, el primero de los dos que ocurra.

## Valores devueltos

Devuelve el número de bytes escritos o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 8.0.0   | `length` ahora es nullable. |

## Ejemplos

Ejemplo con `bzwrite`

```
<?php
$str = "datos no comprimidos";
$bz = bzopen("/tmp/foo.bz2", "w");
bzwrite($bz, $str, strlen($str));
bzclose($bz);
?>

   
```php

## Véase también

bzread

bzopen
