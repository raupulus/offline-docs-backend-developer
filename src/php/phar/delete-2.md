---
title: PharData::delete
description: Elimina un fichero dentro del archivo tar/zip
source_url: https://www.php.net/manual/es/phardata.delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: c8ba91f7e
order: 64580
---

PharData::delete

Elimina un fichero dentro del archivo tar/zip

## Descripción

```php
public PharData::delete(string $localName): true
```php

Elimina un fichero dentro del archivo. Es equivalente a la llamada a `unlink` utilizando el manejador de flujo phar, como se muestra en el ejemplo a continuación.

## Parámetros

`localName`  
Ruta del fichero a eliminar dentro del archivo.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Genera una excepción `PharException` si se producen errores durante la escritura de los cambios en el disco.

## Ejemplos

Un ejemplo con `PharData::delete`

```
<?php
try {
    $phar = new PharData('monphar.zip');
    $phar->delete('efface/moi.php');
    // es equivalente a:
    unlink('phar://monphar.phar/efface/mon.php');
} catch (Exception $e) {
    // se manejan los errores
}
?>

    
```php

## Véase también

`Phar::delete`
