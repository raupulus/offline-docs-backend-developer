---
title: PharFileInfo::__construct
description: Construye un objeto de entrada Phar
source_url: https://www.php.net/manual/es/pharfileinfo.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharFileInfo/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64730
---

PharFileInfo::\_\_construct

Construye un objeto de entrada Phar

## Descripción

```php
public PharFileInfo::__construct(string $filename)
```php

Este método no debe ser llamado directamente. En su lugar, un objeto PharFileInfo es inicializado llamando `Phar::offsetGet` mediante un acceso de tipo array.

## Parámetros

`filename`  
La URL completa para recuperar un fichero. Si se desea recuperar la información del fichero `mi/fichero.php` del phar `boo.phar`, se deberá especificar `phar://boo.phar/mi/fichero.php`.

## Errores/Excepciones

Genera una excepción `BadMethodCallException` si [\_\_construct()](#object.construct) es llamado dos veces. Genera una excepción `UnexpectedValueException` si la URL del phar solicitado está mal formada, si el phar no puede ser abierto o si el fichero no puede ser encontrado dentro del phar.

## Ejemplos

Ejemplo con `PharFileInfo::__construct`

```
<?php
try {
    $p = new Phar('/ruta/hacia/mon.phar', 0, 'mon.phar');
    $p['fichierdetest.txt'] = "hola\nmi\namigo";
    $file = $p['fichierdetest.txt'];
    foreach ($file as $line => $text) {
        echo "línea número $line: $text";
    }
    // esto también funciona
    $file = new PharFileInfo('phar:///ruta/hacia/mon.phar/fichierdetest.txt');
    foreach ($file as $line => $text) {
        echo "línea número $line: $text";
    }
} catch (Exception $e) {
    echo 'La operación Phar ha fallado: ', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    línea número 1: hola
    línea número 2: mi
    línea número 3: amigo
    línea número 1: hola
    línea número 2: mi
    línea número 3: amigo
