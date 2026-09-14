---
title: PharData::setSignatureAlgorithm
description: Asigna el algoritmo de firma de un phar y lo aplica
source_url: https://www.php.net/manual/es/phardata.setsignaturealgorithm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/setSignatureAlgorithm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64670
---

PharData::setSignatureAlgorithm

Asigna el algoritmo de firma de un phar y lo aplica

## Descripción

```php
public PharData::setSignatureAlgorithm(int $algo, [string $privateKey]): void
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Asigna el algoritmo de firma de un phar y lo aplica. El algoritmo de firma debe ser `Phar::MD5`, `Phar::SHA1`, `Phar::SHA256`, `Phar::SHA512`, o `Phar::OPENSSL`.

## Parámetros

`algo`  
Un algoritmo entre `Phar::MD5`, `Phar::SHA1`, `Phar::SHA256`, `Phar::SHA512`, o `Phar::OPENSSL`.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Levanta una excepción `UnexpectedValueException` para muchos errores, una excepción `BadMethodCallException` si la llamada se realiza para un archivo phar basado en tar o en zip, una excepción `PharException` si se encuentran problemas al escribir los cambios en el disco.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | `privateKey` ahora es nullable. |

## Véase también

`Phar::getSupportedSignatures`, `Phar::getSignature`
