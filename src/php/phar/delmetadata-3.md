---
title: PharFileInfo::delMetadata
description: Elimina las metadatos de la entrada
source_url: https://www.php.net/manual/es/pharfileinfo.delmetadata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharFileInfo/delMetadata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: c8ba91f7e
order: 64750
---

PharFileInfo::delMetadata

Elimina las metadatos de la entrada

## Descripción

```php
public PharFileInfo::delMetadata(): true
```php

Elimina las metadatos de la entrada, si las hay.

## Parámetros

No hay parámetros.

## Valores devueltos

Retorna siempre `true`. Al igual que con todas las funcionalidades que modifican el contenido de un phar, la variable INI [phar.readonly](#ini.phar.readonly) debe estar en off para tener éxito si el fichero está dentro de un archivo `Phar`. Los ficheros dentro de archivos `PharData` no tienen esta restricción.

## Errores/Excepciones

Genera una excepción `PharException` si se han encontrado errores al escribir los cambios en el disco, y una excepción `BadMethodCallException` si el acceso en escritura está desactivado.

## Ejemplos

Un ejemplo con `PharFileInfo::delMetaData`

```
<?php
try {
    $a = new Phar('monphar.phar');
    $a['salut'] = 'salut';
    var_dump($a['salut']->delMetadata());
    $a['salut']->setMetadata('mon pote');
    var_dump($a['salut']->delMetadata());
    var_dump($a['salut']->delMetadata());
} catch (Exception $e) {
    // se manejan los errores
}
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)
    bool(false)

## Véase también

`PharFileInfo::setMetadata`, `PharFileInfo::hasMetadata`, `PharFileInfo::getMetadata`, `Phar::setMetadata`, `Phar::hasMetadata`, `Phar::getMetadata`
