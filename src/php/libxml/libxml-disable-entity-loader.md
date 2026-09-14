---
title: libxml_disable_entity_loader
description: Desactiva la carga de entidades externas
source_url: https://www.php.net/manual/es/function.libxml-disable-entity-loader.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/libxml/functions/libxml-disable-entity-loader.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: libxml
translation_status: ready
translation_reviewed: false
translation_revision: 9b1673cf1
order: 43660
---

libxml_disable_entity_loader

Desactiva la carga de entidades externas

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] libxml_disable_entity_loader([bool $disable]): bool
```php

Activa o desactiva la carga de entidades externas. Se debe tener en cuenta que desactivar la carga de entidades externas puede causar problemas al cargar documentos XML.

A partir de libxml 2.9.0, la sustitución de entidades está desactivada por defecto, por lo que no es necesario desactivar la carga de entidades externas, a menos que sea necesario resolver referencias de entidades internas con `LIBXML_NOENT`, `LIBXML_DTDVALID`, o `LIBXML_DTDLOAD`. Generalmente, es preferible utilizar `libxml_set_external_entity_loader` para suprimir la carga de entidades externas. La constante `LIBXML_NO_XXE` también puede ser utilizada para evitar esto (disponible únicamente en Libxml \>= 2.13.0, a partir de PHP 8.4.0).

## Parámetros

`disable`  
Desactiva (`true`) o activa (`false`) la carga de entidades externas por las extensiones libxml (tales como [???](#book.dom), [???](#book.xmlwriter) y [???](#book.xmlreader)).

## Valores devueltos

Devuelve la configuración anterior.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | Esta función ha sido deprecada. |

## Véase también

`libxml_use_internal_errors`, `libxml_set_external_entity_loader`, La constante `LIBXML_NOENT`, La constante `LIBXML_DTDVALID`, La constante `LIBXML_NO_XXE`
