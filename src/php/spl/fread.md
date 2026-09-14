---
title: SplFileObject::fread
description: Leer un fichero
source_url: https://www.php.net/manual/es/splfileobject.fread.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/fread.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84420
---

SplFileObject::fread

Leer un fichero

## Descripción

```php
public SplFileObject::fread(int $length): string
```php

Lee de un fichero el número de bytes dado.

## Parámetros

`length`  
El número de bytes a leer.

## Valores devueltos

Devuelve el string léido desde el fichero o `false` si ocurre un error.

## Ejemplos

Ejemplo de SplFileObject::fread

```
<?php
// Pasar el contenido de un fichero a un string
$nombre_fichero = "/usr/local/something.txt";
$fichero = new SplFileObject($nombre_fichero, "r");
$contenido = $fichero->fread($fichero->getSize());
?>

    
```php

## Notas

> [!NOTE]
> Observe que SplFileObject::fread lee desde la posición actual del puntero del fichero. Use SplFileObject::ftell para conocer la posición actual del puntero, y SplFileObject::rewind (o SplFileObject::fseek) para posicionar el puntero al inicio.

## Véase también

`fread`
