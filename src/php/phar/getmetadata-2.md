---
title: PharFileInfo::getMetadata
description: Devuelve las metadatos específicas adjuntas a un fichero
source_url: https://www.php.net/manual/es/pharfileinfo.getmetadata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharFileInfo/getMetadata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64800
---

PharFileInfo::getMetadata

Devuelve las metadatos específicas adjuntas a un fichero

## Descripción

```php
public PharFileInfo::getMetadata([array $unserializeOptions]): mixed
```php

Devuelve las metadatos que han sido guardadas en el manifiesto del archivo Phar para este fichero.

## Parámetros

## Valores devueltos

Cualquier variable PHP que pueda ser serializada y que se almacena como metadatos para el fichero, o `null` si no se almacenan metadatos.

## Historial de cambios

| Versión | Descripción                                        |
|---------|----------------------------------------------------|
| 8.0.0   | El argumento `unserializeOptions` ha sido añadido. |

## Ejemplos

Un ejemplo con `PharFileInfo::getMetadata`

```
<?php
// se asegura de que el phar no esté ya
@unlink('nouveauphar.phar');
try {
    $p = new Phar(dirname(__FILE__) . '/nouveauphar.phar', 0, 'nouveauphar.phar');
    $p['fichier.txt'] = 'salut';
    $p['fichier.txt']->setMetadata(array('utilisateur' => 'PhilDaiguille', 'mime-type' => 'text/plain'));
    var_dump($p['fichier.txt']->getMetadata());
} catch (Exception $e) {
    echo 'No puede crear/modificar nouveauphar.phar: ', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    array(2) {
      ["utilisateur"]=>
      string(7) "PhilDaiguille"
      ["mime-type"]=>
      string(10) "text/plain"
    }

## Véase también

`PharFileInfo::setMetadata`, `PharFileInfo::hasMetadata`, `PharFileInfo::delMetadata`, `Phar::setMetadata`, `Phar::hasMetadata`, `Phar::getMetadata`
