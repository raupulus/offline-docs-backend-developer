---
title: SeasLog::setRequestID
description: Define los request_id de las peticiones diferenciadas de SeasLog
source_url: https://www.php.net/manual/es/seaslog.setrequestid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/setrequestid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73370
---

SeasLog::setRequestID

Define los request_id de las peticiones diferenciadas de SeasLog

## Descripción

```php
public static SeasLog::setRequestID(string $request_id): bool
```php

Para distinguir una sola petición, sin invocar la función SeasLog::setRequestId, el valor único generado por la función interna \`static char \*get_uniqid () se utiliza durante la inicialización de la petición.

## Parámetros

`request_id`  
String.

## Valores devueltos

Devuelve TRUE en caso de éxito en la definición, FALSE en caso de fallo.

## Ejemplos

Ejemplo de `SeasLog::setRequestID`

```
<?php

var_dump(SeasLog::setRequestID(time() . rand()));

?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)

## Véase también

SeasLog::getRequestID
