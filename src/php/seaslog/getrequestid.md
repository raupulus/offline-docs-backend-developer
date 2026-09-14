---
title: SeasLog::getRequestID
description: Devuelve las solicitudes diferenciadas por request_id de SeasLog
source_url: https://www.php.net/manual/es/seaslog.getrequestid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/getrequestid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73290
---

SeasLog::getRequestID

Devuelve las solicitudes diferenciadas por request_id de SeasLog

## Descripción

```php
public static SeasLog::getRequestID(): string
```php

Para diferenciar una sola solicitud, sin invocar la función SeasLog::setRequestId, el valor único generado por la función interna \`static char \*get_uniqid ()\` se utiliza durante la inicialización de la solicitud.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la cadena generada por la función interna \`static char \*get_uniqid ()\`, o definida por la función SeasLog::setRequestId.

## Ejemplos

Ejemplo de `SeasLog::getRequestID`

```
<?php

var_dump(SeasLog::getRequestID());
var_dump(SeasLog::setRequestID('reqeust_id_test_'.time()));
var_dump(SeasLog::getRequestID());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(13) "5b3f21a209519"
    bool(true)
    string(26) "reqeust_id_test_1530864034"

## Véase también

SeasLog::setRequestID

La variable \`%Q\` en

Tabla de Variables Predeterminadas de Seaslog

.
