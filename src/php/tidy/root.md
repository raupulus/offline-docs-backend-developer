---
title: tidy::root
description: Devuelve un objeto tidyNode que representa la raíz del árbol analizado
  por tidy
source_url: https://www.php.net/manual/es/tidy.root.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/root.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 2b84fa46e
order: 94170
---

tidy::root

tidy_get_root

Devuelve un objeto

tidyNode

que representa la raíz del árbol analizado por tidy

## Descripción

Estilo orientado a objetos

```php
public tidy::root(): tidyNode
```php

Estilo procedimental

```php
tidy_get_root(tidy $tidy): tidyNode
```

Devuelve un objeto `tidyNode` que representa la raíz del arbol a ser analizada por tidy.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Devuelve el objeto `tidyNode`.

## Ejemplos

`tidy::root` ejemplo

```php
<?php

$html = <<< HTML
<html><body>

<p>paragraph</p>
<br/>

</body></html>
HTML;

$tidy = tidy_parse_string($html);
dump_nodes($tidy->root(), 1);

function dump_nodes($node, $indent) {

    if($node->hasChildren()) {
        foreach($node->child as $child) {
            echo str_repeat('.', $indent*2) . ($child->name ? $child->name : '"'.$child->value.'"'). "\n";

            dump_nodes($child, $indent+1);
        }
    }
}
?>

    
```

El ejemplo anterior mostrará:

    ..html
    ....head
    ......title
    ....body
    ......p
    ........"paragraph"
    ......br
