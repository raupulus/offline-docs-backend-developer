---
title: DOMComment::__construct
description: Crea un nuevo objeto DOMComment
source_url: https://www.php.net/manual/es/domcomment.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domcomment/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 12950
---

DOMComment::\_\_construct

Crea un nuevo objeto DOMComment

## Descripción

```php
public DOMComment::__construct([string $data])
```php

Crea un nuevo objeto `DOMComment` . Este objeto es de solo lectura. Puede ser anexado a un documento, pero nodos adicionales no pueden ser anexados a este nodo hasta tando no haya sido asociado con un documento. Para crear un nodo modificable utilice [???](#domdocument.createcomment).

## Parámetros

`data`  
El valor del comentario.

## Ejemplos

Creando un nuevo DOMComment

```
<?php

$dom = new DOMDocument('1.0', 'iso-8859-1');
$element = $dom->appendChild(new DOMElement('root'));
$comment = $element->appendChild(new DOMComment('root comment'));
echo $dom->saveXML(); /* <root><!--root comment--></root> */

?>

    
```php

## Véase también

DOMDocument::createComment
