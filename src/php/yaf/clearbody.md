---
title: Yaf_Response_Abstract::clearBody
description: Descarta todo el cuerpo de respuesta existente
source_url: https://www.php.net/manual/es/yaf-response-abstract.clearbody.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_response_abstract/clearbody.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: bdcd9cd09
order: 106590
---

Yaf_Response_Abstract::clearBody

Descarta todo el cuerpo de respuesta existente

## Descripción

```php
public Yaf_Response_Abstract::clearBody([string $key]): bool
```php

Limpia el contenido existente.

## Parámetros

`key`  
La clave del contenido, si no se especifica, todo el contenido será limpiado.

> [!NOTE]
> Este parámetro se introdujo a partir de la versión 2.2.0

## Valores devueltos

## Véase también

Yaf_Response_Abstract::setBody

Yaf_Response_Abstract::appendBody

Yaf_Response_Abstract::prependBody

Yaf_Response_Abstract::getBody
