---
title: SplFileObject::ftell
description: Devuelve la posición del fichero actual
source_url: https://www.php.net/manual/es/splfileobject.ftell.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/ftell.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84460
---

SplFileObject::ftell

Devuelve la posición del fichero actual

## Descripción

```php
public SplFileObject::ftell(): int
```php

Devuelve la posición de el puntero de fichero que representa el índice actual en el flujo del fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la posición de el puntero de fichero como un integer, o `false` en caso de error.

## Ejemplos

Ejemplo de SplFileObject::ftell

```
<?php
$file = new SplFileObject("/etc/passwd");

// Lee la primera línea
$data = $file->fgets();

// ¿Dónde estamos?
echo $file->ftell();
?>

    
```php

## Véase también

`ftell`
