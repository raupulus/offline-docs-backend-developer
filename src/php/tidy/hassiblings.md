---
title: tidyNode::hasSiblings
description: Indica si un nodo tiene hermanos
source_url: https://www.php.net/manual/es/tidynode.hassiblings.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidynode/hassiblings.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: false
translation_revision: 2b84fa46e
order: 94240
---

tidyNode::hasSiblings

Indica si un nodo tiene hermanos

## Descripción

```php
public tidyNode::hasSiblings(): bool
```php

Indica si un nodo tiene hermanos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si un nodo tiene hermanos, `false` de lo contrario.

## Ejemplos

Ejemplo de `tidyNode::hasSiblings`

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

// La etiqueta HTML
var_dump($tidy->html()->hasSiblings());

// La etiqueta HEAD
var_dump($tidy->html()->child[0]->hasSiblings());

?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)
