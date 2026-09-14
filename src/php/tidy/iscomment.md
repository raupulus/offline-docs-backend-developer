---
title: tidyNode::isComment
description: Comprueba el nodo actual es un comentario
source_url: https://www.php.net/manual/es/tidynode.iscomment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidynode/iscomment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 94260
---

tidyNode::isComment

Comprueba el nodo actual es un comentario

## Descripción

```php
public tidyNode::isComment(): bool
```php

Indica el nodo actual es un comentario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el nodo es un comentario, `false` de lo contrario.

## Ejemplos

Extraer los comentarios de un documento HTML

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
  echo 'Hola Mundo!';
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
    if($node->isComment()) {
        echo "\n\n# comment node #" . ++$GLOBALS['num'] . "\n";
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

    # comment node #1
    <!-- Comments -->
