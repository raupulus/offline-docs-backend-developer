---
title: mqseries_strerror
description: Devuelve el mensaje de error correspondiente al código de resultado
source_url: https://www.php.net/manual/es/function.mqseries-strerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/functions/mqseries-strerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: false
translation_revision: b5efbef2d
order: 51950
---

mqseries_strerror

Devuelve el mensaje de error correspondiente al código de resultado

## Descripción

```php
mqseries_strerror(int $reason): string
```php

`mqseries_strerror` devuelve el mensaje de error correspondiente al código de resultado.

## Parámetros

`reason`  
La razón que califica el compCode.

## Valores devueltos

La cadena de representación de la razón del mensaje de error.

## Ejemplos

Ejemplo con `mqseries_strerror`

```
<?php
    if ($comp_code !== MQSERIES_MQCC_OK) {
        printf("open CompCode:%d Reason:%d Text:%s<br>\n", $comp_code, $reason, mqseries_strerror($reason));
        exit;
    }
?>

   
```php

El ejemplo anterior mostrará:

    Connx CompCode:2 Reason:2059 Text:Queue manager not available for connection.
