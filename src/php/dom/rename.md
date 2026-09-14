---
title: Dom\Attr::rename
description: Cambia el nombre calificado o el espacio de nombres de un atributo
source_url: https://www.php.net/manual/es/dom-attr.rename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/attr/rename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 2c9920402
order: 12110
---

Dom\Attr::rename

Cambia el nombre calificado o el espacio de nombres de un atributo

## Descripción

```php
public Dom\Attr::rename(string $namespaceURI, string $qualifiedName): void
```php

Este método cambia el nombre calificado o el espacio de nombres de un atributo.

## Parámetros

`namespaceURI`  
El nuevo espacio de nombres URI del atributo.

`qualifiedName`  
El nuevo nombre calificado del atributo.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

`DOMException` con el código `Dom\NAMESPACE_ERR`  
Lanzada si hay un error con el espacio de nombres, tal como se determina por `qualifiedName`.

`DOMException` con el código `Dom\INVALID_MODIFICATION_ERR`  
Lanzada si un atributo ya existe en el elemento con el mismo nombre calificado.

## Ejemplos

Ejemplo de Dom\Attr::rename para cambiar el espacio de nombres y el nombre calificado

Esto cambia el nombre calificado de `my-attr` a `my-new-attr` y también cambia su espacio de nombres a `urn:my-ns`.

```
<?php

$doc = Dom\XMLDocument::createFromString('<root my-attr="value"/>');

$root = $doc->documentElement;
$attribute = $root->attributes['my-attr'];
$attribute->rename('urn:my-ns', 'my-new-attr');

echo $doc->saveXml();

?>

   
```php

El ejemplo anterior mostrará:

    <root xmlns:ns1="urn:my-ns" ns1:my-new-attr="value"/>

Ejemplo de Dom\Attr::rename para cambiar solo el nombre calificado

Esto cambia solo el nombre calificado de `my-attr` y mantiene el espacio de nombres URI sin cambios.

```
<?php

$doc = Dom\XMLDocument::createFromString('<root my-attr="value"/>');

$root = $doc->documentElement;
$attribute = $root->attributes['my-attr'];
$attribute->rename($attribute->namespaceURI, 'my-new-attr');

echo $doc->saveXml();

?>

   
```php

El ejemplo anterior mostrará:

    <root my-new-attr="value"/>

## Notas

> [!NOTE]
> A veces es necesario cambiar el nombre calificado y el espacio de nombres URI juntos en un solo paso para no infringir las reglas de los espacios de nombres.

## Véase también

Dom\Element::rename
