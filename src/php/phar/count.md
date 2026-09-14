---
title: Phar::count
description: Devuelve el número de entradas (ficheros) en el archivo Phar
source_url: https://www.php.net/manual/es/phar.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: e96ebdfe8
order: 64010
---

Phar::count

Devuelve el número de entradas (ficheros) en el archivo Phar

## Descripción

```php
public Phar::count([int $mode]): int
```php

## Parámetros

`mode`  
`mode` es un valor entero que especifica el modo de conteo a utilizar. Por omisión, se define como `COUNT_NORMAL`, que solo cuenta el número de elementos en el archivo que no han sido eliminados o ocultados. Cuando se define como `COUNT_RECURSIVE`, cuenta todos los elementos del archivo, incluyendo aquellos que han sido eliminados o ocultados.

## Valores devueltos

El número de ficheros contenidos en el phar, o `0` (el número cero) si no hay ninguno.

## Ejemplos

Un ejemplo con `Phar::count`

```
<?php
// se asegura de que el phar no exista
@unlink('lenouveauphar.phar');
try {
    $p = new Phar(dirname(__FILE__) . '/lenouveauphar.phar', 0, 'le nouveauphar.phar');
} catch (Exception $e) {
    echo 'No puede crear el phar:', $e;
}
echo 'El nuevo phar tiene ' . $p->count() . " entradas\n";
$p['file.txt'] = 'salut';
echo 'El nuevo phar tiene ' . $p->count() . " entradas\n";
?>

    
```php

El ejemplo anterior mostrará:

    El nuevo phar tiene 0 entradas
    El nuevo phar tiene 1 entradas
