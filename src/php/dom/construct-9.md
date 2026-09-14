---
title: DOMProcessingInstruction::__construct
description: Crea un nuevo objeto DOMProcessingInstruction
source_url: https://www.php.net/manual/es/domprocessinginstruction.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domprocessinginstruction/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 14220
---

DOMProcessingInstruction::\_\_construct

Crea un nuevo objeto

DOMProcessingInstruction

## Descripción

```php
public DOMProcessingInstruction::__construct(string $name, [string $value])
```php

Crea un nuevo objeto `DOMProcessingInstruction`. Este objeto es de sólo lectura. Se puede añadir a un documento, pero no se pueden añadir nodos adicionales a este nodo hata que el nodo esté asociado con un documento. Para crear un nodo modificable, use [???](#domdocument.createprocessinginstruction).

## Parámetros

`name`  
El nombre de la etiqueta de la instrucción en proceso.

`value`  
El valor de la intrucción en proceso.

## Ejemplos

Crear un nuevo objeto `DOMProcessingInstruction`

```
<?php

$dom = new DOMDocument('1.0', 'UTF-8');
$html = $dom->appendChild(new DOMElement('html'));
$body = $html->appendChild(new DOMElement('body'));
$pinode = new DOMProcessingInstruction('php', 'echo "Hola Mundo"; ');
$body->appendChild($pinode);
echo $dom->saveXML();

?>

    
```php

El ejemplo anterior mostrará:

```
<html><body><?php echo "Hola Mundo"; ?></body></html>

    
```php

## Véase también

DOMDocument::createProcessingInstruction
