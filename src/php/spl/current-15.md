---
title: SplFileObject::current
description: Recupera la línea actual del fichero
source_url: https://www.php.net/manual/es/splfileobject.current.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/current.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84320
---

SplFileObject::current

Recupera la línea actual del fichero

## Descripción

```php
public SplFileObject::current(): string
```php

Recupera la línea actual del fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Recupera la línea actual del fichero. Si la flag `SplFileObject::READ_CSV` está establecida, este método devuelve un array conteniendo la línea actual analizada como datos CSV. Si se alcanza el final del archivo, se devuelve `false`.

## Ejemplos

Ejemplo de SplFileObject::current

```
<?php
$fichero = new SplFileObject(__FILE__);
foreach ($fichero as $k => $linea) {
   echo ($fichero->key() + 1) . ': ' . $fichero->current();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    1: <?php
    2: $fichero = new SplFileObject(__FILE__);
    3: foreach ($fichero as $linea) {
    4:     echo ($fichero->key() + 1) . ': ' . $fichero->current();
    5: }
    6: ?>

## Véase también

SplFileObject::key, SplFileObject::seek, SplFileObject::next, SplFileObject::rewind, SplFileObject::valid
