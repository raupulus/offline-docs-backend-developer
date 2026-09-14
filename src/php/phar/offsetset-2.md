---
title: PharData::offsetSet
description: Rellena un fichero dentro del archivo tar/zip con el contenido de un
  fichero externo o de un string
source_url: https://www.php.net/manual/es/phardata.offsetset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/offsetSet.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64620
---

PharData::offsetSet

Rellena un fichero dentro del archivo tar/zip con el contenido de un fichero externo o de un string

## Descripción

```php
public PharData::offsetSet(string $localName, resource $value): void
```php

Es una implementación de la interfaz ArrayAccess que permite la manipulación directa del contenido de un archivo tar/zip utilizando los corchetes, operadores de acceso al array. offsetSet es utilizado para modificar un fichero existente o para añadir un nuevo fichero al archivo tar/zip.

## Parámetros

`localName`  
La ruta (relativa) del fichero a modificar dentro del archivo tar o zip.

`value`  
Contenido del fichero.

## Valores devueltos

No se devuelve ningún valor.

## Errores/Excepciones

Se lanza una excepción `PharException` si se han encontrado problemas al escribir en el disco los cambios del archivo tar/zip.

## Ejemplos

Un ejemplo con `PharData::offsetSet`

offsetSet no debe ser accedido directamente, sino que debe ser utilizado a través del operador `[]`.

```
<?php
$p = new PharData('/ruta/al/mon.tar');
try {
    // llama a offsetSet
    $p['fichero.txt'] = 'Hola';
} catch (Exception $e) {
    echo 'No se puede modificar fichero.txt:', $e;
}
?>

    
```php

## Notas

> [!NOTE]
> `Phar::addFile`, `Phar::addFromString` y `Phar::offsetSet` registran un nuevo archivo phar cada vez que son llamadas. Si las prestaciones son una preocupación, `Phar::buildFromDirectory` o `Phar::buildFromIterator` deberían ser utilizadas en su lugar.

## Véase también

`Phar::offsetSet`
