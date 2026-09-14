---
title: SeasLog::getRequestVariable
description: Devuelve la variable de petición de SeasLog
source_url: https://www.php.net/manual/es/seaslog.getrequestvariable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/getrequestvariable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73300
---

SeasLog::getRequestVariable

Devuelve la variable de petición de SeasLog

## Descripción

```php
public static SeasLog::getRequestVariable(int $key): bool
```php

Devuelve la variable de petición de SeasLog.

## Parámetros

`key`  
Un entero de constante. [SEASLOG_REQUEST_VARIABLE_DOMAIN_PORT](#constant.seaslog-request-variable-domain-port), [SEASLOG_REQUEST_VARIABLE_REQUEST_URI](#constant.seaslog-request-variable-request-uri), [SEASLOG_REQUEST_VARIABLE_REQUEST_METHOD](#constant.seaslog-request-variable-request-method), [SEASLOG_REQUEST_VARIABLE_CLIENT_IP](#constant.seaslog-request-variable-client-ip)

## Valores devueltos

Devuelve el valor de la variable de petición en caso de éxito.

## Ejemplos

Ejemplo de SeasLog::getRequestVariable

```
<?php

$sDomainPort = 'domain:port';
$sRequestUri = 'uri';
$sRequestMethod = 'method';
$sClientIp = 'client_ip';

$iErrorKey = 1000;

$oSeasLog = new SeasLog();

var_dump($oSeasLog->setRequestVariable(SEASLOG_REQUEST_VARIABLE_DOMAIN_PORT, $sDomainPort));
var_dump($oSeasLog->setRequestVariable(SEASLOG_REQUEST_VARIABLE_REQUEST_URI, $sRequestUri));
var_dump($oSeasLog->setRequestVariable(SEASLOG_REQUEST_VARIABLE_REQUEST_METHOD, $sRequestMethod));
var_dump($oSeasLog->setRequestVariable(SEASLOG_REQUEST_VARIABLE_CLIENT_IP, $sClientIp));

var_dump($oSeasLog->setRequestVariable($iErrorKey,NULL));

var_dump($oSeasLog->getRequestVariable(SEASLOG_REQUEST_VARIABLE_DOMAIN_PORT) == $sDomainPort);
var_dump($oSeasLog->getRequestVariable(SEASLOG_REQUEST_VARIABLE_REQUEST_URI) == $sRequestUri);
var_dump($oSeasLog->getRequestVariable(SEASLOG_REQUEST_VARIABLE_REQUEST_METHOD) == $sRequestMethod);
var_dump($oSeasLog->getRequestVariable(SEASLOG_REQUEST_VARIABLE_CLIENT_IP) == $sClientIp);

var_dump($oSeasLog->getRequestVariable($iErrorKey));

?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(true)
    bool(true)
    bool(true)
    bool(false)
    bool(true)
    bool(true)
    bool(true)
    bool(true)
    bool(false)

## Véase también

SeasLog::setRequestVariable
