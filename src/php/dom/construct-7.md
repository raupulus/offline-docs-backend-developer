---
title: DOMEntityReference::__construct
description: Crea un nuevo objeto DOMEntityReference
source_url: https://www.php.net/manual/es/domentityreference.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domentityreference/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 4f5e2b225
order: 13720
---

DOMEntityReference::\_\_construct

Crea un nuevo objeto DOMEntityReference

## Descripción

```php
public DOMEntityReference::__construct(string $name)
```php

Crea un nuevo objeto `DOMEntityReference`.

## Parámetros

`name`  
El nombre de la referencia de entidad.

## Ejemplos

Crear un nuevo objeto DOMEntityReference

```
<?php

$dom = new DOMDocument('1.0', 'iso-8859-1');
$elemento = $dom->appendChild(new DOMElement('root'));
$entidad = $elemento->appendChild(new DOMEntityReference('nbsp'));
echo $dom->saveXML(); /* <root></root> */

?>

    
```php

## Véase también

DOMDocument::createEntityReference
