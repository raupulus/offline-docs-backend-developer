---
title: PharData::__construct
description: Construye un objeto de archivo tar o zip no ejecutable
source_url: https://www.php.net/manual/es/phardata.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64510
---

PharData::\_\_construct

Construye un objeto de archivo tar o zip no ejecutable

## Descripción

```php
public PharData::__construct(string $filename, [int $flags], [string $alias], [int $format])
```php

## Parámetros

`filename`  
Ruta hacia un archivo tar/zip existente o a crear

`flags`  
Banderas a pasar a la clase padre `Phar` `RecursiveDirectoryIterator`.

`alias`  
El alias del archivo Phar a utilizar durante las llamadas a las funcionalidades de flujo.

`format`  
Una de las [constantes de formato de archivo](#phar.constants.fileformat) disponibles en la clase `Phar`.

## Errores/Excepciones

Levanta una excepción `BadMethodCallException` si es llamada dos veces, una excepción `UnexpectedValueException` si el archivo phar no puede ser abierto.

## Ejemplos

Un ejemplo con `PharData::__construct`

```
<?php
try {
    $p = new PharData('/path/to/my.tar', Phar::CURRENT_AS_FILEINFO | Phar::KEY_AS_FILENAME);
} catch (UnexpectedValueException $e) {
    die('No puede abrir my.tar');
} catch (BadMethodCallException $e) {
    echo 'técnicamente, esto no puede ocurrir';
}
echo file_get_contents('phar:///ruta/vers/my.tar/ejemplo.txt');
?>
      
     
```php
