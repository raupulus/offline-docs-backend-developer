---
title: Yaf_Request_Abstract::setModuleName
description: Establecer el nombre del módulo
source_url: https://www.php.net/manual/es/yaf-request-abstract.setmodulename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_request_abstract/setmodulename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 85ff79512
order: 106370
---

Yaf_Request_Abstract::setModuleName

Establecer el nombre del módulo

## Descripción

```php
public Yaf_Request_Abstract::setModuleName(string $module, [bool $format_name]): void
```php

Establecer el nombre del módulo a la petición, esto se utiliza generalmente por un enrutador personalizado para establecer el nombre del módulo del resultado de la ruta.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`module`  
`string` nombre del módulo, debe estar en estilo camel, como "Index" o "Foo_Bar"

`format_name`  
Esto se introdujo en Yaf 3.2.0, por omisión Yaf formateará el nombre en modo camel, si esto se establece como `false`, Yaf establecerá el nombre original a la petición.

## Valores devueltos
