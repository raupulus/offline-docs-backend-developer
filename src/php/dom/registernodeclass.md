---
title: DOMDocument::registerNodeClass
description: Registra la clase extendida utilizada para crear un tipo de nodo base
source_url: https://www.php.net/manual/es/domdocument.registernodeclass.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/registernodeclass.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 0e2dfef68
order: 13200
---

DOMDocument::registerNodeClass

Registra la clase extendida utilizada para crear un tipo de nodo base

## Descripción

```php
public DOMDocument::registerNodeClass(string $baseClass, string $extendedClass): true
```php

Este método permite registrar su propia clase DOM extendida para ser utilizada posteriormente en la extensión DOM de PHP.

Este método no forma parte del estándar DOM.

> [!CAUTION]
> Los constructores de los objetos de las clases de nodos registrados no son llamados.

## Parámetros

`baseClass`  
La clase DOM que se desea extender. Puede encontrarse una lista de estas clases en la [introducción del capítulo](#book.dom).

`extendedClass`  
El nombre de su clase extendida. Si se proporciona el valor `null`, todas las clases registradas previamente que extienden `baseClass` serán eliminadas.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | DOMDocument::registerNodeClass ahora tiene un tipo de retorno provisional de tipo `true`. |

## Ejemplos

Añadir un nuevo método a DOMElement

```
<?php

class myElement extends DOMElement {
   function appendElement($name) {
      return $this->appendChild(new myElement($name));
   }
}

class myDocument extends DOMDocument {
   function setRoot($name) {
      return $this->appendChild(new myElement($name));
   }
}

$doc = new myDocument();
$doc->registerNodeClass('DOMElement', 'myElement');

// A partir de aquí, la adición de un elemento a otro se realiza en una sola llamada !
$root = $doc->setRoot('root');
$child = $root->appendElement('child');
$child->setAttribute('foo', 'bar');

echo $doc->saveXML();

?>

    
```php

El ejemplo anterior mostrará:

```
<root><child foo="bar"/></root>

    
```php

Recuperación de elementos en forma de clase personalizada

```
<?php
class myElement extends DOMElement {
    public function __toString() {
        return $this->nodeValue;
    }
}

$doc = new DOMDocument;
$doc->loadXML("<root><element><child>Texto en un hijo</child></element></root>");
$doc->registerNodeClass("DOMElement", "myElement");

$element = $doc->getElementsByTagName("child")->item(0);
var_dump(get_class($element));

// Y utilizamos las ventajas del método __toString..
echo $element;
?>

    
```php

El ejemplo anterior mostrará:

```
string(9) "myElement"
Texto en un hijo

    
```php

Recuperación del propietario del documento

Al instanciar un `DOMDocument` personalizado, la propiedad `ownerDocument` se refiere a la clase instanciada. Sin embargo, si todas las referencias a esta clase son eliminadas, será destruida y una nueva instancia de `DOMDocument` será creada en su lugar. Por esta razón, puede utilizarse el método `DOMDocument::registerNodeClass` con `DOMDocument`

```
<?php
class MyDOMDocument extends DOMDocument {
}

class MyOtherDOMDocument extends DOMDocument {
}

// Creación de un documento MyDOMDocument con algunos fragmentos XML
$doc = new MyDOMDocument;
$doc->loadXML("<root><element><child>texto en un hijo</child></element></root>");

$child = $doc->getElementsByTagName("child")->item(0);

// El propietario actual del nodo es MyDOMDocument
var_dump(get_class($child->ownerDocument));
// MyDOMDocument es destruido
unset($doc);
// Y una nueva instancia de DOMDocument es creada
var_dump(get_class($child->ownerDocument));

// Importación de un nodo desde MyDOMDocument
$newdoc = new MyOtherDOMDocument;
$child = $newdoc->importNode($child);

// Registra un DOMDocument personalizado
$newdoc->registerNodeClass("DOMDocument", "MyOtherDOMDocument");

var_dump(get_class($child->ownerDocument));
unset($doc);
// Un nuevo MyOtherDOMDocument es creado
var_dump(get_class($child->ownerDocument));
?>

    
```php

El ejemplo anterior mostrará:

```
string(13) "MyDOMDocument"
string(11) "DOMDocument"
string(18) "MyOtherDOMDocument"
string(18) "MyOtherDOMDocument"

    
```php

Los objetos personalizados son efímeros

> [!CAUTION]
> Los objetos de la clase de nodos registrada son efímeros, es decir, son destruidos cuando ya no son referenciados desde el código PHP, y recreados cuando son recuperados nuevamente. Esto implica que los valores de propiedades personalizadas se perderán después de la recreación.

```
<?php
class MyDOMElement extends DOMElement
{
    public $myProp = 'default value';
}

$doc = new DOMDocument();
$doc->registerNodeClass('DOMElement', 'MyDOMElement');

$node = $doc->createElement('a');
$node->myProp = 'modified value';
$doc->appendChild($node);

echo $doc->childNodes[0]->myProp, PHP_EOL;
unset($node);
echo $doc->childNodes[0]->myProp, PHP_EOL;
?>
    
```php

El ejemplo anterior mostrará:

```
modified value
default value

    
```php
