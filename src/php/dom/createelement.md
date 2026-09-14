---
title: DOMDocument::createElement
description: Crea un nuevo nodo elemento
source_url: https://www.php.net/manual/es/domdocument.createelement.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/createelement.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 7d5c74c9a
order: 13050
---

DOMDocument::createElement

Crea un nuevo nodo elemento

## Descripción

```php
public DOMDocument::createElement(string $localName, [string $value]): DOMElement
```php

Esta función crea una nueva instancia de la clase `DOMElement`. Este nodo no será mostrado en el documento, a menos que sea insertado con `DOMNode::appendChild`.

## Parámetros

`localName`  
El nombre de etiqueta del elemento.

`value`  
El valor del elemento. De manera predeterminada se creará un elemento vacio. El valor también puede ser asignado más tarde con [DOMElement::\$nodeValue](#domnode.props.nodevalue).

El valor es usado al pie de la letra, excepto que las referencias de entidad \< y \> se escaparán. Tenga en cuenta que & tiene que ser escapado manualmente; de lo contrario, se tomará como inicio de una referencia de entidad. Además " no sera escapado.

## Valores devueltos

Devuelve una nueva instanca de la clase `DOMElement` o `false` si ha ocurrido un error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_INVALID_CHARACTER_ERR`  
Lanzado si `localName` contiene un carácter inválido.

## Ejemplos

Crear un nuevo elemento e insertarlo como raíz

```
<?php

$dom = new DOMDocument('1.0', 'utf-8');

$element = $dom->createElement('test', 'This is the root element!');

// Insertamos el nuevo elemento como raíz (hijo del documento)
$dom->appendChild($element);

echo $dom->saveXML();
?>

    
```php

El ejemplo anterior mostrará:

```
<test>This is the root element!</test>

    
```php

Pasando texto que contiene un & sin escapar como `valor`

```
<?php
$dom = new DOMDocument('1.0', 'utf-8');
$element = $dom->createElement('foo', 'me & you');
$dom->appendChild($element);
echo $dom->saveXML();
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Warning: DOMDocument::createElement(): unterminated entity reference             you in /in/BjTCg on line 4

    <foo/>

## Notas

> [!NOTE]
> El parámetro `value` *no* será escapado. Utilice DOMDocument::createTextNode para crear un nodo de texto con *soporte para escape de caracteres*.

## Véase también

DOMNode::appendChild, DOMDocument::createAttribute, DOMDocument::createAttributeNS, DOMDocument::createCDATASection, DOMDocument::createComment, DOMDocument::createDocumentFragment, DOMDocument::createElementNS, DOMDocument::createEntityReference, DOMDocument::createProcessingInstruction, DOMDocument::createTextNode
