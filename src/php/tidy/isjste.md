---
title: tidyNode::isJste
description: Comprueba si el nodo es JSTE
source_url: https://www.php.net/manual/es/tidynode.isjste.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidynode/isjste.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 94280
---

tidyNode::isJste

Comprueba si el nodo es JSTE

## Descripción

```php
public tidyNode::isJste(): bool
```php

Indica si el nodo es JSTE.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el nodo es código JSTE, `false` de lo contrario.

## Ejemplos

Extrer el código JSTE de un documento HTML

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
    if($node->isJste()) {
        echo "\n\n# jste node #" . ++$GLOBALS['num'] . "\n";
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

    # jste node #1
    <#
      /* código JSTE */
      alert('Hola Mundo');
    #>

    /*
    var_dump($tidy->html()->child[0]->hasChildren());
    var_dump($tidy->html()->child[0]->child[0]->hasChildren());
    */
