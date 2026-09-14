---
title: tidyNode::isHtml
description: Indica si el nodo es un nodo de elemento
source_url: https://www.php.net/manual/es/tidynode.ishtml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidynode/ishtml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 525aa5f19
order: 94270
---

tidyNode::isHtml

Indica si el nodo es un nodo de elemento

## Descripción

```php
public tidyNode::isHtml(): bool
```php

Indica si el nodo actual es un nodo de elemento, pero no el nodo raíz del documento.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna `true` si el nodo es un nodo de elemento, pero no el nodo raíz del documento, `false` de lo contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.3.24, 7.4.12 | Esta función fue corregida para tener un comportamiento razonable. Anteriormente, la mayoría de los nodos eran reportados como nodos HTML. |

## Ejemplos

Extracto del código HTML desde un documento mixto

```
<?php

$html = <<< HTML
<html><head>
<?php echo '<title>title</title>'; ?>
<#
  /* código JSTE */
  alert('Hello World');
#>
</head>
<body>

<?php
  // código PHP
  echo 'hello world!';
?>

<%
  /* código ASP */
  response.write("Hello World!")
%>

<!-- Comentarios -->
Hello World
</body></html>
Fuera de HTML
HTML;

$tidy = tidy_parse_string($html);
$num = 0;

get_nodes($tidy->html());

function get_nodes($node) {
    // Verifica si el nodo actual es del tipo demandado
    if($node->isHtml()) {
        echo "\n\n# Nodo Html #" . ++$GLOBALS['num'] . "\n";
        echo $node->value;
    }

    // Verifica si el nodo actual tiene hijos
    if($node->hasChildren()) {
        foreach($node->child as $child) {
            get_nodes($child);
        }
    }
}

?>

    
```php

El ejemplo anterior mostrará:

    # Nodo html #1
    <html>
    <head>
    <?php echo '<title>title</title>'; ?><#
      /* código JSTE */
      alert('Hello World');
    #>
    <title></title>
    </head>
    <body>
    <?php
      // código PHP
      echo 'hello world!';
    ?><%
      /* código ASP */
      response.write("Hello World!")
    %><!-- Comentarios -->
    Hello WorldFuera de HTML
    </body>
    </html>

    # Nodo html #2
    <head>
    <?php echo '<title>title</title>'; ?><#
      /* código JSTE */
      alert('Hello World');
    #>
    <title></title>
    </head>

    # Nodo html #3
    <title></title>

    # Nodo html #4
    <body>
    <?php
      // código PHP
      echo 'hello world!';
    ?><%
      /* código ASP */
      response.write("Hello World!")
    %><!-- Comentarios -->
    Hello WorldFuera de HTML
    </body>
