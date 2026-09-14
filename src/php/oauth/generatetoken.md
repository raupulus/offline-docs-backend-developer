---
title: OAuthProvider::generateToken
description: Genera un token aleatorio
source_url: https://www.php.net/manual/es/oauthprovider.generatetoken.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauthprovider/generatetoken.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: false
translation_revision: bdee7e8c1
order: 57000
---

OAuthProvider::generateToken

Genera un token aleatorio

## Descripción

```php
final public static OAuthProvider::generateToken(int $size, [bool $strong]): string
```php

Genera un `string` de bytes pseudo-aleatorios.

## Parámetros

`size`  
La longitud deseada del token, en bytes.

`strong`  
Definido como `true`, indica que se utilizará `/dev/random`, de lo contrario, se utilizará `/dev/urandom`. Este parámetro es ignorado en Windows.

## Valores devueltos

El token generado, en forma de `string` de bytes.

## Errores/Excepciones

Si el parámetro `strong` es `true`, entonces se emitirá una advertencia de nivel `E_WARNING` cuando la función de devolución de llamada `rand` se utilice para completar los bytes aleatorios faltantes (es decir, cuando no hay suficientes datos aleatorios inicialmente).

## Ejemplos

Ejemplo con `OAuthProvider::generateToken`

```
<?php
$p = new OAuthProvider();

$t = $p->generateToken(4);

echo strlen($t),  PHP_EOL;
echo bin2hex($t), PHP_EOL;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    4
    b6a82c27

## Notas

> [!NOTE]
> Cuando no hay suficientes datos aleatorios disponibles en el sistema, esta función completará los bytes faltantes utilizando la función interna de PHP `rand`.

## Véase también

openssl_random_pseudo_bytes

mcrypt_create_iv
