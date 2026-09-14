---
title: OAuth::setRSACertificate
description: Define el certificado RSA
source_url: https://www.php.net/manual/es/oauth.setrsacertificate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/setrsacertificate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: false
translation_revision: bdee7e8c1
order: 56860
---

OAuth::setRSACertificate

Define el certificado RSA

## Descripción

```php
public OAuth::setRSACertificate(string $cert): mixed
```php

Define el certificado RSA.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`cert`  
El certificado RSA.

## Valores devueltos

Devuelve `true` en caso de éxito, o `false` si ocurre un error (es decir, el certificado RSA no puede ser analizado).

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL oauth 1.0.0 | Antes de esta versión, `null` era devuelto en lugar de `false`. |

## Ejemplos

Ejemplo con OAuth::setRsaCertificate

```
<?php
$consume = new OAuth('1234', '', OAUTH_SIG_METHOD_RSASHA1);

$consume->setRSACertificate(file_get_contents('test.pem'));
?>

   
```php

## Véase también

OAuth::setCaPath
