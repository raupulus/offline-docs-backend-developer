---
title: DOMXPath::registerPhpFunctionNS
description: Registra una función PHP como una función XPath en un espacio de nombres
source_url: https://www.php.net/manual/es/domxpath.registerphpfunctionns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domxpath/registerphpfunctionns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 647105f8c
order: 14340
---

DOMXPath::registerPhpFunctionNS

Registra una función PHP como una función XPath en un espacio de nombres

## Descripción

```php
public DOMXPath::registerPhpFunctionNS(string $namespaceURI, string $name, callable $callable): void
```php

Este método permite utilizar una función PHP como una función XPath con espacio de nombres dentro de expresiones XPath.

## Parámetros

`namespaceURI`  
La URI del espacio de nombres.

`name`  
La función local dentro del espacio de nombres.

`callable`  
La función PHP a llamar cuando la función XPath es llamada en la expresión XPath. Cuando una lista de nodos es pasada como argumento a la retrollamada, el argumento se convierte en un array que contiene los nodos DOM correspondientes.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Registra una función XPath en un espacio de nombres y la llama desde la expresión XPath

```
<?php

$xml = <<<EOB
<books>
<book>
 <title>PHP Basics</title>
 <author>Jim Smith</author>
 <author>Jane Smith</author>
</book>
<book>
 <title>PHP Secrets</title>
 <author>Jenny Smythe</author>
</book>
<book>
 <title>XML basics</title>
 <author>Joe Black</author>
</book>
</books>
EOB;

$doc = new DOMDocument();
$doc->loadXML($xml);

$xpath = new DOMXPath($doc);

// Registra el espacio de nombres my: (obligatorio)
$xpath->registerNamespace("my", "urn:my.ns");

// Registra las funciones PHP
$xpath->registerPhpFunctionNS(
    'urn:my.ns',
    'substring',
    fn (array $arg1, int $start, int $length) => substr($arg1[0]->textContent, $start, $length)
);

// Llamada a la función substr en el título del libro
$nodes = $xpath->query('//book[my:substring(title, 0, 3) = "PHP"]');

echo "Encontrados {$nodes->length} libros cuyo título comienza con 'PHP':\n";
foreach ($nodes as $node) {
   $title  = $node->getElementsByTagName("title")->item(0)->nodeValue;
   $author = $node->getElementsByTagName("author")->item(0)->nodeValue;
   echo "$title por $author\n";
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    Encontrados 2 libros cuyo título comienza con 'PHP':
    PHP Basics por Jim Smith
    PHP Secrets por Jenny Smythe

## Véase también

DOMXPath::registerNamespace

DOMXPath::query

DOMXPath::evaluate

XSLTProcessor::registerPHPFunctions

XSLTProcessor::registerPHPFunctionNS
