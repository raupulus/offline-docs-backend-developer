---
title: SplFileObject::fseek
description: Busca una posiciónn
source_url: https://www.php.net/manual/es/splfileobject.fseek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/fseek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84440
---

SplFileObject::fseek

Busca una posiciónn

## Descripción

```php
public SplFileObject::fseek(int $offset, [int $whence]): int
```php

Mueve el puntero interno a una posición en el fichero medido en bytes desde el principio de el fichero obtenido, añadiendo `offset` a la posición especificada por `whence`.

## Parámetros

`offset`  
El índice. Un valor negativo puede ser utilizado para mover hacía atrás por el fichero que será útil cuando SEEK_END es usado como un valor de `whence`.

`whence`  
Los valores de `whence` son: `SEEK_SET` - Establece la posición igual a `offset` bytes., `SEEK_CUR` - Establece la posición a la ubicación actual más `offset`., `SEEK_END` - Establece la posición al final de el fichero más `offset`.

Si no se especifica `whence`, se supone que es `SEEK_SET`.

## Valores devueltos

Devuelve 0 si la búsqueda fué exitosa, -1 en caso contrario. Tenga en cuenta que buscando un EOF pasado no se considera como un error.

## Ejemplos

Ejemplo de SplFileObject::fseek

```
<?php
$file = new SplFileObject("algunfichero.txt");

// Leer la primera línea
$data = $file->fgets();

// Mover atrás a el principio de el fichero
// Igual que $file->rewind();
$file->fseek(0);
?>

    
```php

## Véase también

`fseek`
