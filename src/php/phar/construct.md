---
title: Phar::__construct
description: Construye un objeto de archivo Phar
source_url: https://www.php.net/manual/es/phar.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 63970
---

Phar::\_\_construct

Construye un objeto de archivo Phar

## Descripción

```php
public Phar::__construct(string $filename, [int $flags], [string $alias])
```php

## Parámetros

`filename`  
La ruta hacia un archivo Phar existente o a crear. El nombre del fichero debe contener la extensión .phar.

`flags`  
Los flags a pasar a la clase padre `RecursiveDirectoryIterator`.

`alias`  
Alias con el cual se debe hacer referencia al archivo al llamar a las funcionalidades de flujo.

## Errores/Excepciones

Levanta una excepción `BadMethodCallException` si el método es llamado dos veces, o `UnexpectedValueException` si el archivo no puede ser abierto.

## Ejemplos

Un ejemplo con `Phar::__construct`

```
<?php
try {
    $p = new Phar('/path/to/my.phar', FilesystemIterator::CURRENT_AS_FILEINFO | FilesystemIterator::KEY_AS_FILENAME,
                  'mon.phar');
} catch (UnexpectedValueException $e) {
    die('No puede abrir mon.phar');
} catch (BadMethodCallException $e) {
    echo 'técnicamente, esto no puede ocurrir';
}
// ahora funciona
echo file_get_contents('phar://mon.phar/ejemplo.txt');
// y funciona como si hubiéramos escrito
echo file_get_contents('phar:///ruta/al/mon.phar/ejemplo.txt');
?>
      
     
```php
