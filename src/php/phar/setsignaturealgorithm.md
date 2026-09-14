---
title: Phar::setSignatureAlgorithm
description: Establece y aplica el algoritmo de firma de un phar
source_url: https://www.php.net/manual/es/phar.setsignaturealgorithm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/setSignatureAlgorithm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64370
---

Phar::setSignatureAlgorithm

Establece y aplica el algoritmo de firma de un phar

## Descripción

```php
public Phar::setSignatureAlgorithm(int $algo, [string $privateKey]): void
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Establece y aplica el algoritmo de firma de un phar. El algoritmo de firma debe ser `Phar::MD5`, `Phar::SHA1`, `Phar::SHA256`, `Phar::SHA512`, o `Phar::OPENSSL`.

Tenga en cuenta que todas las archives phar ejecutables tienen una firma creada automáticamente, `SHA1` por omisión. Las archives de datos basadas en tar o en zip (creadas con la clase `PharData`) deben tener su firma creada y asignada explícitamente mediante `Phar::setSignatureAlgorithm`.

## Parámetros

`algo`  
Uno de los algoritmos `Phar::MD5`, `Phar::SHA1`, `Phar::SHA256`, `Phar::SHA512`, o `Phar::OPENSSL`

`privateKey`  
El contenido de una clave privada OpenSSL, tal como se extrae de un certificado o de un archivo de clave OpenSSL:

```
<?php
$private = openssl_get_privatekey(file_get_contents('private.pem'));
$pkey = '';
openssl_pkey_export($private, $pkey);
$p->setSignatureAlgorithm(Phar::OPENSSL, $pkey);
?>
        
       
```php

Consulte [la introducción de phar](#phar.using) para las instrucciones de nombramiento y ubicación del archivo de clave pública.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Genera una excepción `UnexpectedValueException` para muchos errores y una excepción `PharException` si ocurren problemas durante la escritura de los cambios en el disco.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | `privateKey` ahora es nullable. |

## Véase también

`Phar::getSupportedSignatures`, `Phar::getSignature`
