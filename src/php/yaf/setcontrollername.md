---
title: Yaf_Request_Abstract::setControllerName
description: Establecer el nombre del controlador
source_url: https://www.php.net/manual/es/yaf-request-abstract.setcontrollername.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_request_abstract/setcontrollername.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 85ff79512
order: 106350
---

Yaf_Request_Abstract::setControllerName

Establecer el nombre del controlador

## Descripción

```php
public Yaf_Request_Abstract::setControllerName(string $controller, [bool $format_name]): void
```php

Establecer el nombre del controlador a solicitar, esto es generalmente utilizado por el enrutador personalizado para establecer el nombre del controlador de resultado de ruta.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`controller`  
`string`, nombre del controlador, debe ser en estilo camel, como "Index" o "Foo_Bar".

`format_name`  
esto se introduce en Yaf 3.2.0, por defecto Yaf formateará el nombre en modo camel, si esto se establece a `false`, Yaf establecerá el nombre original a petición.

## Valores devueltos
