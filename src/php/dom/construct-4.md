---
title: DOMDocument::__construct
description: Crea un nuevo objeto DOMDocument
source_url: https://www.php.net/manual/es/domdocument.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 12990
---

DOMDocument::\_\_construct

Crea un nuevo objeto DOMDocument

## Descripción

```php
public DOMDocument::__construct([string $version], [string $encoding])
```php

Crea un nuevo objeto `DOMDocument` .

## Parámetros

`version`  
El numero de versión del documento como parte de la declaración XML.

`encoding`  
La codificación del documento como parte de la declaración XML.

## Ejemplos

Creando un nuevo DOMDocument

```
<?php

$dom = new DOMDocument('1.0', 'iso-8859-1');

echo $dom->saveXML(); /*  */

?>

    
```php

## Véase también

DOMImplementation::createDocument
