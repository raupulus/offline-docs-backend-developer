---
title: DOMText::__construct
description: Crea un nuevo objeto DOMText
source_url: https://www.php.net/manual/es/domtext.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domtext/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 14240
---

DOMText::\_\_construct

Crea un nuevo objeto

DOMText

## Descripción

```php
public DOMText::__construct([string $data])
```php

Crea un nuevo objeto `DOMText`.

## Parámetros

`data`  
El valor del nodo de texto. Si no se proporciona, se crea un nodo de texto vacío.

## Ejemplos

Crear un nuevo objeto DOMText

```
<?php

$dom = new DOMDocument('1.0', 'iso-8859-1');
$element = $dom->appendChild(new DOMElement('root'));
$text = $element->appendChild(new DOMText('root value'));
echo $dom->saveXML(); /* <root>root value</root> */

?>

    
```php

## Véase también

DOMDocument::createTextNode
