---
title: bzdecompress
description: Descomprime una cadena bzip2
source_url: https://www.php.net/manual/es/function.bzdecompress.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bzip2/functions/bzdecompress.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bzip2
translation_status: ready
translation_reviewed: true
translation_revision: 5fdeb11b1
order: 6420
---

bzdecompress

Descomprime una cadena bzip2

## Descripción

```php
bzdecompress(string $data, [bool $use_less_memory]): string
```php

`bzdecompress` descomprime la cadena dada que contiene datos comprimidos bzip2.

## Parámetros

`data`  
La cadena a descomprimir.

`use_less_memory`  
Si este argumento es `true`, se utilizará otro algoritmo de descompresión: consume menos memoria (el máximo solicitado ronda los 2300 ko), pero funciona globalmente a la mitad de la velocidad.

Consulte la [documentación bzip2](https://www.sourceware.org/bzip2/) para obtener más detalles sobre esta funcionalidad.

## Valores devueltos

La cadena descomprimida, o `false`, o un número de error si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | El tipo de `use_less_memory` ha sido modificado de `int` a `bool`. Anteriormente, el valor por omisión era `0`. |

## Ejemplos

Descompresión de una cadena

```
<?php
$start_str = "frase a comprimir";
$bzstr = bzcompress($start_str);

echo "Cadena comprimida : ";
echo $bzstr;
echo "\n<br />\n";

$str = bzdecompress($bzstr);
echo "Cadena descomprimida : ";
echo $str;
echo "\n<br />\n";
?>

   
```php

## Véase también

bzcompress
