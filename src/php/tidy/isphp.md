---
title: tidyNode::isPhp
description: Comprueba si el nodo es PHP
source_url: https://www.php.net/manual/es/tidynode.isphp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidynode/isphp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 94290
---

tidyNode::isPhp

Comprueba si el nodo es PHP

## Descripción

```php
public tidyNode::isPhp(): bool
```php

Indica cuando el nodo actual es PHP.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el nodo es código PHP, `false` de lo contrario.

## Ejemplos

Extraer el código PHP embebido en un documento HTML

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
    if($node->isPhp()) {
        echo "\n\n# php node #" . ++$GLOBALS['num'] . "\n";
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

    # php node #1
    <?php echo '<title>titulo</title>'; ?>

    # php node #2
    <?php
      // código PHP
      echo 'hola mundo!';
    ?>
