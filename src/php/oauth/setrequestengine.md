---
title: OAuth::setRequestEngine
description: El propósito de setRequestEngine
source_url: https://www.php.net/manual/es/oauth.setrequestengine.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/setrequestengine.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_revision: bdee7e8c1
order: 56850
---

OAuth::setRequestEngine

El propósito de setRequestEngine

## Descripción

```php
public OAuth::setRequestEngine(int $reqengine): void
```php

Establece el motor de peticiones, que estará enviando las peticiones HTTP.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`reqengine`  
El motor de peticiones deseado. Poner a `OAUTH_REQENGINE_STREAMS` para usar el Stream PHP, o `OAUTH_REQENGINE_CURL` para usar [Curl](#book.curl).

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Emite una excepción `OAuthException` si un motor de peticiones inválido es escogido.

## Ejemplos

Ejemplo de `OAuth::setRequestEngine`

```
<?php
$consumer = new OAuth();

$consumer->setRequestEngine(OAUTH_REQENGINE_STREAMS);
?>

   
```php

## Véase también

Curl

flujos PHP

OAuthException
