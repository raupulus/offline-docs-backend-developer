---
title: tidyNode::isAsp
description: Comprueba si el nodo es ASP
source_url: https://www.php.net/manual/es/tidynode.isasp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidynode/isasp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 94250
---

tidyNode::isAsp

Comprueba si el nodo es ASP

## Descripción

```php
public tidyNode::isAsp(): bool
```php

Indica cuando el nodo actual es ASP.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el nodo es código ASP, `false` de lo contrario.

## Ejemplos

Extraer el código ASP embebido en un documento HTML

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
    if($node->isAsp()) {
        echo "\n\n# asp node #" . ++$GLOBALS['num'] . "\n";
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

    # asp node #1
    <%
      /* código ASP */
      response.write("Hola Mundo!")
    %>
