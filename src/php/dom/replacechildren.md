---
title: Dom\ParentNode::replaceChildren
source_url: https://www.php.net/manual/es/dom-parentnode.replacechildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/parentnode/replacechildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: e64de8bee
order: 12640
---

Dom\ParentNode::replaceChildren

## Descripción

```php
public Dom\ParentNode::replaceChildren(Dom\Node ...$nodes): void
```php

## Ejemplos

Ejemplo de Dom\ParentNode::replaceChildren

```
<?php
$dom = Dom\HTMLDocument::createFromString('<!DOCTYPE HTML><html><p>hi</p> test <p>hi2</p></html>');

$dom->documentElement->replaceChildren('foo', $dom->createElement('p'), 'bar');
echo $dom->saveHtml();
?>

   
```php

El ejemplo anterior mostrará:

    <!DOCTYPE html><html>foo<p></p>bar</html>
