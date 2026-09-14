---
title: Yaf_Request_Abstract::setActionName
description: Establece el nombre de la acción
source_url: https://www.php.net/manual/es/yaf-request-abstract.setactionname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_request_abstract/setactionname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 85ff79512
order: 106330
---

Yaf_Request_Abstract::setActionName

Establece el nombre de la acción

## Descripción

```php
public Yaf_Request_Abstract::setActionName(string $action, [bool $format_name]): void
```php

Establecer el nombre de la acción a solicitar, esto es usualmente usado por el enrutador personalizado para establecer el nombre del controlador de resultado de ruta.

## Parámetros

`action`  
nombre de la acción como `string`, debe ser en minúsculas, como "index" o "foo_bar"

`format_name`  
esto se introduce en Yaf 3.2.0, por omisión Yaf formateará el nombre en minúsculas, si este se establece a `false` , Yaf pondrá el nombre original a la petición.

## Valores devueltos
