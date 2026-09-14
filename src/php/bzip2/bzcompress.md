---
title: bzcompress
description: Comprime una cadena con bzip2
source_url: https://www.php.net/manual/es/function.bzcompress.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bzip2/functions/bzcompress.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bzip2
translation_status: ready
translation_reviewed: true
translation_revision: 5fdeb11b1
order: 6410
---

bzcompress

Comprime una cadena con bzip2

## Descripción

```php
bzcompress(string $data, [int $block_size], [int $work_factor]): string
```php

`bzcompress` comprime la cadena dada y devuelve los datos así codificados.

## Parámetros

`data`  
La cadena a comprimir.

`block_size`  
Especifica el tamaño de bloque utilizado durante la compresión y debe ser un número de 1 a 9, siendo 9 la mejor compresión, pero que utiliza más recursos para realizarse.

`work_factor`  
Controla el comportamiento de la compresión en los peores casos de datos altamente repetitivos. Este valor puede ir de 0 a 250 (0 es un valor especial).

Fuera de `work_factor`, el resultado será el mismo.

## Valores devueltos

La cadena comprimida o un número de error si ocurre un error.

## Ejemplos

Compresión de datos

```
<?php
$str = "datos simples";
$bzstr = bzcompress($str, 9);
echo $bzstr;
?>

   
```php

## Véase también

bzdecompress
