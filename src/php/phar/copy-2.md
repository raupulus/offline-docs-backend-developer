---
title: PharData::copy
description: Copia un fichero interno del archivo tar/zip a otro fichero dentro del
  mismo archivo
source_url: https://www.php.net/manual/es/phardata.copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: 8d09722b6
order: 64540
---

PharData::copy

Copia un fichero interno del archivo tar/zip a otro fichero dentro del mismo archivo

## Descripción

```php
public PharData::copy(string $from, string $to): true
```php

Copia un fichero interno del archivo tar/zip a otro fichero dentro del mismo archivo. Es una alternativa orientada a objetos al uso de `copy` con el gestor de flujos phar.

## Parámetros

`from`  

`to`  

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Se lanza una excepción `UnexpectedValueException` si el fichero de origen no existe, si el fichero de destino ya existe, si el soporte de escritura está desactivado, si falla la apertura de alguno de los dos ficheros o si falla la lectura del fichero de origen; o se lanza una excepción `PharException` si falla la escritura de los cambios del archivo phar.

## Ejemplos

Un ejemplo con `PharData::copy`

Este ejemplo muestra el uso de `PharData::copy` y su equivalente en términos de gestor de flujos. La principal diferencia entre ambos enfoques radica en la gestión de errores. Todos los métodos PharData lanzan excepciones, mientras que el gestor de flujos utiliza `trigger_error`.

```
<?php

try {
    $phar = new PharData('monphar.tar');
    $phar['a'] = 'salut';
    $phar->copy('a', 'b');
    echo $phar['b']; // Muestra "phar://myphar.tar/b"
} catch (Exception $e) {
    // Se manejan los errores
}

// El equivalente en términos de flujo del ejemplo anterior.
// Se lanzan E_WARNING en caso de error en lugar de excepciones.
copy('phar://monphar.tar/a', 'phar//monphar.tar/c');
echo file_get_contents('phar://monphar.tar/c'); // Muestra "salut"
?>

    
```php
