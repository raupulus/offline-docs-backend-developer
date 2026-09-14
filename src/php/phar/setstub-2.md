---
title: PharData::setStub
description: Función inútil (Phar::setStub no es válido para PharData)
source_url: https://www.php.net/manual/es/phardata.setstub.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/setStub.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: d7056bd09
order: 64680
---

PharData::setStub

Función inútil (Phar::setStub no es válido para PharData)

## Descripción

```php
public PharData::setStub(resource $stub, [int $length]): true
```php

Los archivos tar/zip no ejecutables no pueden tener un contenedor de carga, por lo que este método solo genera una excepción.

## Parámetros

`stub`  
Formalmente, un string o un manejador de flujo abierto para usar como contenedor de carga ejecutable para este archivo phar. Este argumento es ignorado.

`length`  
`stub` en bytes. Este argumento es ignorado.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Genera una excepción `PharException` en cualquier llamada al método

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.4.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Véase también

`Phar::setStub`
