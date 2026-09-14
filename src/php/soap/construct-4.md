---
title: SoapParam::__construct
description: Constructor SoapParam
source_url: https://www.php.net/manual/es/soapparam.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapparam/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75320
---

SoapParam::\_\_construct

Constructor SoapParam

## Descripción

```php
public SoapParam::__construct(mixed $data, string $name)
```php

Construye un nuevo objeto `SoapParam`.

## Parámetros

`data`  
Los datos a pasar o a devolver. Puede pasarse este argumento directamente como un valor PHP, pero en este caso, será nombrado `paramN` y el servicio SOAP no lo comprenderá.

`name`  
El nombre del argumento.

## Ejemplos

Ejemplo con `SoapParam::__construct`

```
<?php
$client = new SoapClient(null,array('location' => "http://localhost/soap.php",
                                    'uri'      => "http://test-uri/"));
$client->SomeFunction(new SoapParam($a, "a"),
                      new SoapParam($b, "b"),
                      new SoapParam($c, "c"));
?>

    
```php

## Véase también

SoapClient::\_\_soapCall, SoapVar::\_\_construct
