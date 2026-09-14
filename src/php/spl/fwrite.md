---
title: SplFileObject::fwrite
description: Escribe en el fichero
source_url: https://www.php.net/manual/es/splfileobject.fwrite.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/fwrite.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: aa120f36c
order: 84480
---

SplFileObject::fwrite

Escribe en el fichero

## Descripción

```php
public SplFileObject::fwrite(string $data, [int $length]): int
```php

Escribe el contenido del argumento `data` en el fichero.

## Parámetros

`data`  
El `string` a escribir en el fichero.

`length`  
Si el argumento `length` es de tipo `int`, la escritura se detendrá después de escribir `length` bytes o bien cuando se alcance el final de `data`; según lo que ocurra primero.

## Valores devueltos

Devuelve el número de bytes escritos, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | `length` ahora acepta `null`. |
| 7.4.0 | Esta función devuelve ahora `false` en lugar de cero en caso de fallo. |

## Ejemplos

Ejemplo con SplFileObject::fwrite

```
<?php
$file = new SplFileObject("fwrite.txt", "w");
$written = $file->fwrite("12345");
echo "$written bytes han sido escritos en el fichero";
?>

    
```php

Resultado del ejemplo anterior es similar a:

    5 bytes han sido escritos en el fichero

## Véase también

`fwrite`
