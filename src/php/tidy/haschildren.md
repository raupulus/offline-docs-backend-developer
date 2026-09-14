---
title: tidyNode::hasChildren
description: Indica si un nodo tiene hijos
source_url: https://www.php.net/manual/es/tidynode.haschildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidynode/haschildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: false
translation_revision: 2b84fa46e
order: 94230
---

tidyNode::hasChildren

Indica si un nodo tiene hijos

## Descripción

```php
public tidyNode::hasChildren(): bool
```php

Indica si el nodo tiene hijos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el nodo tiene hijos, `false` de lo contrario.

## Ejemplos

Ejemplo de `tidyNode::hasChildren`

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

// La etiqueta HEAD
var_dump($tidy->html()->child[0]->hasChildren());

// El código PHP dentro de la etiqueta HEAD
var_dump($tidy->html()->child[0]->child[0]->hasChildren());

?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
