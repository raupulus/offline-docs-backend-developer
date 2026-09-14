---
title: PharData::delMetadata
description: Elimina los metadatos globales de un archivo zip
source_url: https://www.php.net/manual/es/phardata.delmetadata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/delMetadata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: c8ba91f7e
order: 64570
---

PharData::delMetadata

Elimina los metadatos globales de un archivo zip

## Descripción

```php
public PharData::delMetadata(): true
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Elimina los metadatos globales del archivo zip

## Parámetros

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Se genera una excepción `PharException` si se producen errores durante la escritura de los cambios en el disco.

## Ejemplos

Un ejemplo con `PharData::delMetaData`

```
<?php
try {
    $phar = new PharData('monphar.zip');
    var_dump($phar->getMetadata());
    $phar->setMetadata("salut");
    var_dump($phar->getMetadata());
    $phar->delMetadata();
    var_dump($phar->getMetadata());
} catch (Exception $e) {
    // se manejan los errores
}
?>

    
```php

El ejemplo anterior mostrará:

    NULL
    string(5) "salut"
    NULL

## Véase también

`Phar::delMetadata`
