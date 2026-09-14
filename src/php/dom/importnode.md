---
title: DOMDocument::importNode
description: Importa un nodo dentro del documento actual
source_url: https://www.php.net/manual/es/domdocument.importnode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/importnode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 4f5e2b225
order: 13130
---

DOMDocument::importNode

Importa un nodo dentro del documento actual

## Descripción

```php
public DOMDocument::importNode(DOMNode $node, [bool $deep]): DOMNode
```php

Esta función devuelve una copia del nodo a importar y le asocia con el documento actual.

## Parámetros

`node`  
El nodo que desea importar

`deep`  
Si se establece en `true`, este método importará de forma recursiva el subárbol bajo el `node`.

> [!NOTE]
> Para copiar los atributos de los nodos `deep` debe establecerse a `true`

## Valores devueltos

El nodo copiado o `false`, si no puede ser copiado.

## Errores/Excepciones

`DOMException` es lanzado si el nodo no puede ser importado.

## Ejemplos

`DOMDocument::importNode` ejemplo

Copiando nodos entre documentos.

```
<?php

$orgdoc = new DOMDocument;
$orgdoc->loadXML("<root><element><child>text in child</child></element></root>");

// El nodo que se quiere importar al nuevo documento
$node = $orgdoc->getElementsByTagName("element")->item(0);

// Crear un nuevo documento
$newdoc = new DOMDocument;
$newdoc->formatOutput = true;

// Agregar marcado
$newdoc->loadXML("<root><someelement>text in some element</someelement></root>");

echo "The 'new document' before copying nodes into it:\n";
echo $newdoc->saveXML();

// Importar el nodo y todos sus hijos al documento
$node = $newdoc->importNode($node, true);
// y entonces anexarlo a el nodo "<root>"
$newdoc->documentElement->appendChild($node);

echo "\nThe 'new document' after copying the nodes into it:\n";
echo $newdoc->saveXML();
?>

    
```php

El ejemplo anterior mostrará:

    The 'new document' before copying nodes into it:

    <root>
      <someelement>text in some element</someelement>
    </root>

    The 'new document' after copying the nodes into it:

    <root>
      <someelement>text in some element</someelement>
      <element>
        <child>text in child</child>
      </element>
    </root>
