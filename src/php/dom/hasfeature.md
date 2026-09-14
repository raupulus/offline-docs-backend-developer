---
title: DOMImplementation::hasFeature
description: Verifica si la implementación DOM implementa una funcionalidad específica
source_url: https://www.php.net/manual/es/domimplementation.hasfeature.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domimplementation/hasfeature.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: cb7d16cf1
order: 13780
---

DOMImplementation::hasFeature

Verifica si la implementación DOM implementa una funcionalidad específica

## Descripción

```php
public DOMImplementation::hasFeature(string $feature, string $version): bool
```php

Verifica si la implementación DOM implementa una funcionalidad `feature` específica.

Se puede encontrar una lista de todas las funcionalidades en la sección [Conformance](http://www.w3.org/TR/2000/REC-DOM-Level-2-Core-20001113/introduction.html#ID-Conformance) de la especificación DOM.

## Parámetros

`feature`  
La funcionalidad a verificar.

`version`  
El número de versión de la funcionalidad `feature` a verificar. En el nivel 2, esto puede ser `2.0` o `1.0`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Llamar a esta función de manera estática ahora lanzará una `Error`. Anteriormente, se generaba un error `E_DEPRECATED`. |

## Ejemplos

Pruebe su implementación DOM

```
<?php

$features = array(
  'Core'           => 'Core module',
  'XML'            => 'XML module',
  'HTML'           => 'HTML module',
  'Views'          => 'Views module',
  'Stylesheets'    => 'Style Sheets module',
  'CSS'            => 'CSS module',
  'CSS2'           => 'CSS2 module',
  'Events'         => 'Events module',
  'UIEvents'       => 'User interface Events module',
  'MouseEvents'    => 'Mouse Events module',
  'MutationEvents' => 'Mutation Events module',
  'HTMLEvents'     => 'HTML Events module',
  'Range'          => 'Range module',
  'Traversal'      => 'Traversal module'
);

$implementation = new DOMImplementation;

foreach ($features as $key => $name) {
  if ($implementation->hasFeature($key, '2.0')) {
    echo "Tiene la funcionalidad $name\n";
  } else {
    echo "No tiene la funcionalidad $name\n";
  }
}

?>

   
```php

## Véase también

DOMNode::isSupported
