---
title: SimpleXMLElement::children
description: Busca los hijos de un nodo dado
source_url: https://www.php.net/manual/es/simplexmlelement.children.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/children.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: 770c6faca
order: 74470
---

SimpleXMLElement::children

Busca los hijos de un nodo dado

## Descripción

```php
public SimpleXMLElement::children([string $namespaceOrPrefix], [bool $isPrefix]): SimpleXMLElement
```php

Este método busca los hijos de un elemento. El resultado sigue las reglas de la iteración normal.

> [!NOTE]
> SimpleXML añade propiedades iterativas para casi todos sus métodos. Estas no pueden ser vistas utilizando `var_dump` o cualquier otra función que examine los objetos.

## Parámetros

`namespaceOrPrefix`  
Un espacio de nombres XML.

`isPrefix`  
Si `isPrefix` vale `true`, `namespaceOrPrefix` será considerado como un prefijo. Si vale `false`, `namespaceOrPrefix` será considerado como una URL hacia un espacio de nombres.

## Valores devueltos

Devuelve un elemento `SimpleXMLElement` si el nodo tiene un hijo o no, excepto si el nodo representa un atributo, en cuyo caso se devuelve `null`.

## Ejemplos

Recorrido de un pseudo-array `children()`

```
<?php
$xml = new SimpleXMLElement(
'<person>
 <child role="son">
  <child role="daughter"/>
 </child>
 <child role="daughter">
  <child role="son">
   <child role="son"/>
  </child>
 </child>
</person>');

foreach ($xml->children() as $second_gen) {
    echo ' The person begot a ' . $second_gen['role'];

    foreach ($second_gen->children() as $third_gen) {
        echo ' who begot a ' . $third_gen['role'] . ';';

        foreach ($third_gen->children() as $fourth_gen) {
            echo ' and that ' . $third_gen['role'] .
                ' begot a ' . $fourth_gen['role'];
        }
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    The person begot a son who begot a daughter; The person
    begot a daughter who begot a son; and that son begot a son

Uso de espacios de nombres

```
<?php
$xml = '<example xmlns:foo="my.foo.urn">
  <foo:a>Apple</foo:a>
  <foo:b>Banana</foo:b>
  <c>Cherry</c>
</example>';

$sxe = new SimpleXMLElement($xml);

$kids = $sxe->children('foo');
var_dump(count($kids));

$kids = $sxe->children('foo', TRUE);
var_dump(count($kids));

$kids = $sxe->children('my.foo.urn');
var_dump(count($kids));

$kids = $sxe->children('my.foo.urn', TRUE);
var_dump(count($kids));

$kids = $sxe->children();
var_dump(count($kids));
?>

    
```php

    int(0)
    int(2)
    int(2)
    int(0)
    int(1)

## Véase también

SimpleXMLElement::count, `count`
