---
title: SimpleXMLElement::registerXPathNamespace
description: Crea un contexto prefijo/ns para la próxima consulta XPath
source_url: https://www.php.net/manual/es/simplexmlelement.registerxpathnamespace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/registerXPathNamespace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: 770c6faca
order: 74580
---

SimpleXMLElement::registerXPathNamespace

Crea un contexto prefijo/ns para la próxima consulta XPath

## Descripción

```php
public SimpleXMLElement::registerXPathNamespace(string $prefix, string $namespace): bool
```php

Crea un contexto prefijo/ns para la próxima consulta XPath. En particular, esto es útil si el proveedor del documento XML dado modifica los prefijos de espacio de nombres. `registerXPathNamespace` creará un prefijo para el espacio de nombres asociado, permitiendo el acceso a los nodos en este espacio de nombres sin necesidad de cambiar el código para permitir los nuevos prefijos dictados por el proveedor.

## Parámetros

`prefix`  
El prefijo de espacio de nombres a utilizar en la consulta XPath para el espacio de nombres dado en `namespace`.

`namespace`  
El espacio de nombres a utilizar para la consulta XPath. Esto debe coincidir con un espacio de nombres que es utilizado por el documento XML, de lo contrario la consulta XPath que utiliza `prefix` no retornará ningún resultado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Fija un prefijo de espacio de nombres para utilizar en una consulta XPath

```
<?php

$xml = <<<EOD
<book xmlns:chap="http://example.org/chapter-title">
    <title>My Book</title>
    <chapter id="1">
        <chap:title>Chapter 1</chap:title>
        <para>Donec velit. Nullam eget tellus vitae tortor gravida scelerisque.
            In orci lorem, cursus imperdiet, ultricies non, hendrerit et, orci.
            Nulla facilisi. Nullam velit nisl, laoreet id, condimentum ut,
            ultricies id, mauris.</para>
    </chapter>
    <chapter id="2">
        <chap:title>Chapter 2</chap:title>
        <para>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin
            gravida. Phasellus tincidunt massa vel urna. Proin adipiscing quam
            vitae odio. Sed dictum. Ut tincidunt lorem ac lorem. Duis eros
            tellus, pharetra id, faucibus eu, dapibus dictum, odio.</para>
    </chapter>
</book>
EOD;

$sxe = new SimpleXMLElement($xml);

$sxe->registerXPathNamespace('c', 'http://example.org/chapter-title');
$result = $sxe->xpath('//c:title');

foreach ($result as $title) {
  echo $title . "\n";
}

?>

    
```php

El ejemplo anterior mostrará:

    Chapter 1
    Chapter 2

        

Observe cómo el documento XML mostrado en este ejemplo fija un espacio de nombres con el prefijo `chap`. Imagine que este documento (o otro similar) pudiera haber utilizado un prefijo `c` en el pasado para el mismo espacio de nombres. Dado que ha cambiado, la consulta XPath no retornaría los resultados apropiados y la consulta debería ser modificada. El uso de `registerXPathNamespace` evita las modificaciones futuras de la consulta incluso si el proveedor cambia el prefijo de espacio de nombres.

## Véase también

SimpleXMLElement::xpath, SimpleXMLElement::getDocNamespaces, SimpleXMLElement::getNamespaces
