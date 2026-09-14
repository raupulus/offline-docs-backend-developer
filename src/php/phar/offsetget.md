---
title: Phar::offsetGet
description: Obtiene un objeto PharFileInfo a partir de un fichero
source_url: https://www.php.net/manual/es/phar.offsetget.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/offsetGet.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64300
---

Phar::offsetGet

Obtiene un objeto

PharFileInfo

a partir de un fichero

## Descripción

```php
public Phar::offsetGet(string $localName): SplFileInfo
```php

Esta es una implementación de la interfaz ArrayAccess que permite la manipulación directa del contenido de un archivo Phar utilizando los corchetes de acceso a array. `Phar::offsetGet` se utiliza para extraer ficheros de un archivo Phar.

## Parámetros

`localName`  
El nombre de fichero (en ruta relativa) a buscar en el Phar.

## Valores devueltos

Se devuelve un objeto `PharFileInfo` que puede ser utilizado para integrar el contenido de un fichero o para recuperar información sobre el fichero actual.

## Errores/Excepciones

Este método lanza una excepción `BadMethodCallException` si el fichero no existe en el archivo Phar.

## Ejemplos

Ejemplo con `Phar::offsetGet`

Al igual que con todas las clases que implementan la interfaz `ArrayAccess`, `Phar::offsetGet` es llamada automáticamente cuando se utilizan los corchetes de acceso a array (`[]`).

```
<?php
$p = new Phar(dirname(__FILE__) . '/monphar.phar', 0, 'monphar.phar');
$p['existe.txt'] = "el fichero existe\n";
try {
    // llama automáticamente a offsetGet()
    echo $p['existe.txt'];
    echo $p['nexistepas.txt'];
} catch (BadMethodCallException $e) {
    echo $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    el fichero existe
    Entry nexistepas.txt does not exist

## Véase también

`Phar::offsetExists`, `Phar::offsetSet`, `Phar::offsetUnset`
