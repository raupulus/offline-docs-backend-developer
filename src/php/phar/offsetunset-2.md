---
title: PharData::offsetUnset
description: Elimina un fichero de un archivo tar/zip
source_url: https://www.php.net/manual/es/phardata.offsetunset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/offsetUnset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64630
---

PharData::offsetUnset

Elimina un fichero de un archivo tar/zip

## Descripción

```php
public PharData::offsetUnset(string $localName): void
```php

Es una implementación de la interfaz ArrayAccess que permite la manipulación directa del contenido de un archivo tar/zip utilizando los corchetes, operadores de acceso al array. offsetUnset es utilizado para borrar un fichero existente y es llamado por la construcción de lenguaje `unset`.

## Parámetros

`localName`  
La ruta (relativa) del fichero a modificar dentro del archivo tar o zip.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Genera una excepción `PharException` si se han encontrado problemas al escribir en el disco los cambios del archivo tar/zip.

## Ejemplos

Un ejemplo con `PharData::offsetUnset`

```
<?php
$p = new PharData('/ruta/al/mon.zip');
try {
    // borra archivo.txt de mon.zip llamando a offsetUnset
    unset($p['archivo.txt']);
} catch (Exception $e) {
    echo 'No puede borrar archivo.txt: ', $e;
}
?>

    
```php

## Véase también

`Phar::offsetUnset`
