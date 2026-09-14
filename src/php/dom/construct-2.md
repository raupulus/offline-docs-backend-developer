---
title: DOMCdataSection::__construct
description: Construye un nuevo objeto DOMCdataSection
source_url: https://www.php.net/manual/es/domcdatasection.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domcdatasection/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 4f5e2b225
order: 12780
---

DOMCdataSection::\_\_construct

Construye un nuevo objeto DOMCdataSection

## Descripción

```php
public DOMCdataSection::__construct(string $data)
```php

Construye un nuevo nodo CDATA. Funciona igual que la clase `DOMText`.

## Parámetros

`data`  
El valor del nodo CDATA. Si no se proporciona, se crea un nodo CDATA vacío.

## Ejemplos

Crear un nuevo objeto DOMCdataSection

```
<?php

$dom = new DOMDocument('1.0', 'utf-8');
$elemento = $dom->appendChild(new DOMElement('root'));
$texto = $elemento->appendChild(new DOMCdataSection('root value'));
echo $dom->saveXML();

?>

    
```php

El ejemplo anterior mostrará:

    <root><![CDATA[root value]]></root>

## Véase también

DOMText::\_\_construct, DOMDocument::createTextNode
