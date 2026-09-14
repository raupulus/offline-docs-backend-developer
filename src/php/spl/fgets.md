---
title: SplFileObject::fgets
description: Obtener la línea de el fichero
source_url: https://www.php.net/manual/es/splfileobject.fgets.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/fgets.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 857bcd5c6
order: 84370
---

SplFileObject::fgets

Obtener la línea de el fichero

## Descripción

```php
public SplFileObject::fgets(): string
```php

Obtener la línea de el fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un string conteniendo la siguiente línea de el fichero.

## Errores/Excepciones

Lanza una `RuntimeException` si el fichero no puede ser leído.

## Ejemplos

Ejemplo de SplFileObject::fgets

Este ejemplo simplemente imprime el contenido de `texto.txt` línea por línea.

```
<?php
$fichero = new SplFileObject("texto.txt");
while (!$fichero->eof()) {
    echo $fichero->fgets();
}
?>

    
```php

## Véase también

`fgets`, SplFileObject::fgetss, SplFileObject::fgetc, SplFileObject::current
