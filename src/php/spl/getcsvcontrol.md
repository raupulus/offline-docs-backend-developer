---
title: SplFileObject::getCsvControl
description: Recupera las opciones para CSV
source_url: https://www.php.net/manual/es/splfileobject.getcsvcontrol.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/getcsvcontrol.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 73007ad98
order: 84500
---

SplFileObject::getCsvControl

Recupera las opciones para CSV

## Descripción

```php
public SplFileObject::getCsvControl(): array
```php

Recupera el separador, carácter de escape así como el carácter utilizado para rodear los campos durante un análisis CSV de los datos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array indexado que contiene el carácter utilizado para delimitar los campos así como el utilizado para rodearlos y el carácter de escape.

## Historial de cambios

| Versión | Descripción                                                |
|---------|------------------------------------------------------------|
| 7.4.0   | El carácter de espaciado puede ser ahora una cadena vacía. |
| 7.0.10  | Se añade el carácter de escape al array devuelto.          |

## Ejemplos

Ejemplo con SplFileObject::getCsvControl

```
<?php
$file = new SplFileObject("data.txt");
print_r($file->getCsvControl());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => ,
        [1] => "
        [2] => \
    )

## Véase también

SplFileObject::setCsvControl

SplFileObject::fgetcsv

SplFileObject::fputcsv

fputcsv

fgetcsv

str_getcsv
