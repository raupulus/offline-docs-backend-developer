---
title: tidyNode::isText
description: Comprueba si un nodo representa un texto (no HTML)
source_url: https://www.php.net/manual/es/tidynode.istext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidynode/istext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 94300
---

tidyNode::isText

Comprueba si un nodo representa un texto (no HTML)

## Descripción

```php
public tidyNode::isText(): bool
```php

Indica si un nodo representa sólo texto (sin nada de HTML).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si un nodo representa un texto, `false` de lo contrario.

## Ejemplos

Extraer el texto de un documento HTML

```
<?php

$html = <<< HTML
<html><head>
<?php echo '<title>titulo</title>'; ?>
<#
  /* código JSTE */
  alert('Hola Mundo');
#>
</head>
<body>

<?php
  // código PHP
  echo 'hola mundo!';
?>

<%
  /* código ASP */
  response.write("Hola Mundo!")
%>

<!-- Comentarios -->
Hola Mundo
</body></html>
Fuera del HTML
HTML;

$tidy = tidy_parse_string($html);
$num = 0;

get_nodes($tidy->html());

function get_nodes($node) {

    // Verifica si el nodo actual es del tipo requerido
    if($node->isText()) {
        echo "\n\n# text node #" . ++$GLOBALS['num'] . "\n";
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

    # text node #1
    Hola Mundo

    # text node #2
    Fuera del HTML
