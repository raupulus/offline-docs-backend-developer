---
title: ReflectionExtension::getConstants
description: Obtiene las constantes
source_url: https://www.php.net/manual/es/reflectionextension.getconstants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/getconstants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70200
---

ReflectionExtension::getConstants

Obtiene las constantes

## Descripción

```php
public ReflectionExtension::getConstants(): array
```php

Obtiene las constantes de una extensión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array asociativo cuyos claves son los nombres de las constantes.

## Ejemplos

Ejemplo con ReflectionExtension::getConstants

```
<?php
$ext = new ReflectionExtension('DOM');

print_r($ext->getConstants());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [XML_ELEMENT_NODE] => 1
        [XML_ATTRIBUTE_NODE] => 2
        [XML_TEXT_NODE] => 3
        [XML_CDATA_SECTION_NODE] => 4
        [XML_ENTITY_REF_NODE] => 5
        [XML_ENTITY_NODE] => 6
        [XML_PI_NODE] => 7
        [XML_COMMENT_NODE] => 8
        [XML_DOCUMENT_NODE] => 9
        [XML_DOCUMENT_TYPE_NODE] => 10
        [XML_DOCUMENT_FRAG_NODE] => 11
        [XML_NOTATION_NODE] => 12
        [XML_HTML_DOCUMENT_NODE] => 13
        [XML_DTD_NODE] => 14
        [XML_ELEMENT_DECL_NODE] => 15
        [XML_ATTRIBUTE_DECL_NODE] => 16
        [XML_ENTITY_DECL_NODE] => 17
        [XML_NAMESPACE_DECL_NODE] => 18
        [XML_LOCAL_NAMESPACE] => 18
        [XML_ATTRIBUTE_CDATA] => 1
        [XML_ATTRIBUTE_ID] => 2
        [XML_ATTRIBUTE_IDREF] => 3
        [XML_ATTRIBUTE_IDREFS] => 4
        [XML_ATTRIBUTE_ENTITY] => 6
        [XML_ATTRIBUTE_NMTOKEN] => 7
        [XML_ATTRIBUTE_NMTOKENS] => 8
        [XML_ATTRIBUTE_ENUMERATION] => 9
        [XML_ATTRIBUTE_NOTATION] => 10
        [DOM_PHP_ERR] => 0
        [DOM_INDEX_SIZE_ERR] => 1
        [DOMSTRING_SIZE_ERR] => 2
        [DOM_HIERARCHY_REQUEST_ERR] => 3
        [DOM_WRONG_DOCUMENT_ERR] => 4
        [DOM_INVALID_CHARACTER_ERR] => 5
        [DOM_NO_DATA_ALLOWED_ERR] => 6
        [DOM_NO_MODIFICATION_ALLOWED_ERR] => 7
        [DOM_NOT_FOUND_ERR] => 8
        [DOM_NOT_SUPPORTED_ERR] => 9
        [DOM_INUSE_ATTRIBUTE_ERR] => 10
        [DOM_INVALID_STATE_ERR] => 11
        [DOM_SYNTAX_ERR] => 12
        [DOM_INVALID_MODIFICATION_ERR] => 13
        [DOM_NAMESPACE_ERR] => 14
        [DOM_INVALID_ACCESS_ERR] => 15
        [DOM_VALIDATION_ERR] => 16
    )

## Véase también

ReflectionExtension::getINIEntries
