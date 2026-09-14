---
title: SplFileObject::rewind
description: Rebobina el fichero hasta la primera línea
source_url: https://www.php.net/manual/es/splfileobject.rewind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/rewind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84570
---

SplFileObject::rewind

Rebobina el fichero hasta la primera línea

## Descripción

```php
public SplFileObject::rewind(): void
```php

Rebobina el fichero hasta la primera línea.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una `RuntimeException` si no se puede rebobinar.

## Ejemplos

Ejemplo de SplFileObject::rewind

```
<?php
$file = new SplFileObject("variado.txt");

// Recorrer todo el fichero
foreach ($file as $line) { }

// Rebobinar hasta la primera línea
$file->rewind();

// Imprime la primera línea
echo $file->current();
?>

    
```php

## Véase también

SplFileObject::current, SplFileObject::key, SplFileObject::seek, SplFileObject::next, SplFileObject::valid
