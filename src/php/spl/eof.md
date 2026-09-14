---
title: SplFileObject::eof
description: Comprueba si es el final del fichero
source_url: https://www.php.net/manual/es/splfileobject.eof.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/eof.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84330
---

SplFileObject::eof

Comprueba si es el final del fichero

## Descripción

```php
public SplFileObject::eof(): bool
```php

Determina si el final de el fichero ha sido alcanzado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si es el final de el fichero, en caso contrario `false`.

## Ejemplos

Ejemplo de SplFileObject::eof

```
<?php
$fichero = new SplFileObject("frutas.txt");
while ( ! $fichero->eof()) {
    echo $fichero->fgets();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    manzana
    banana
    cereza
    naranja
    baya

## Véase también

SplFileObject::valid, `feof`
