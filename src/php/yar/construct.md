---
title: Yar_Client::__construct
description: Crear un cliente
source_url: https://www.php.net/manual/es/yar-client.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yar/yar_client/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yar
translation_status: ready
translation_revision: 167c48c1c
order: 107630
---

Yar_Client::\_\_construct

Crear un cliente

## Descripción

```php
final public Yar_Client::__construct(string $url, [array $options])
```php

Crea un `Yar_Client` hacia un `Yar_Server`.

## Parámetros

`url`  
El URL del servidor de Yar.

## Valores devueltos

Una instancia de `Yar_Client`.

## Ejemplos

Ejemplo de `Yar_Client::__construct`

```
<?php
$cliente = new Yar_Client("http://host/api/");
?>

   
```php

Resultado del ejemplo anterior es similar a:

## Véase también

Yar_Client::\_\_call

Yar_Client::setOpt
