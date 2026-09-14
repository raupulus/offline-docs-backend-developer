---
title: Phar::delMetadata
description: Elimina los metadatos globales del phar
source_url: https://www.php.net/manual/es/phar.delmetadata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/delMetadata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: c8ba91f7e
order: 64050
---

Phar::delMetadata

Elimina los metadatos globales del phar

## Descripción

```php
public Phar::delMetadata(): true
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Elimina los metadatos globales del phar

## Parámetros

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Genera una excepción `PharException` si ocurren errores durante la escritura en el disco.

## Ejemplos

Un ejemplo con `Phar::delMetaData`

```
<?php
try {
    $phar = new Phar('monphar.phar');
    var_dump($phar->getMetadata());
    $phar->setMetadata("salut");
    var_dump($phar->getMetadata());
    $phar->delMetadata();
    var_dump($phar->getMetadata());
} catch (Exception $e) {
    // manejo de errores
}
?>

    
```php

El ejemplo anterior mostrará:

    NULL
    string(8) "salut"
    NULL

## Véase también

`Phar::getMetadata`, `Phar::setMetadata`, `Phar::hasMetadata`
