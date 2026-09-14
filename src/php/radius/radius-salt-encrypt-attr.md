---
title: radius_salt_encrypt_attr
description: Cifra un valor utilizando un Salt
source_url: https://www.php.net/manual/es/function.radius-salt-encrypt-attr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-salt-encrypt-attr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67780
---

radius_salt_encrypt_attr

Cifra un valor utilizando un Salt

## Descripción

```php
radius_salt_encrypt_attr(resource $radius_handle, string $data): string
```php

Se aplica el algoritmo RADIUS salt al valor proporcionado.

Generalmente, esto se realiza automáticamente al proporcionar la opción `RADIUS_OPTION_SALT` a la función que define el atributo, pero esta función puede ser utilizada si se requiere una construcción de consulta a bajo nivel.

## Parámetros

`data`  
Los datos a cifrar con un salt.

## Valores devueltos

Devuelve los datos cifrados utilizando un salt o `false` si ocurre un error.

## Véase también

radius_put_addr

radius_put_attr

radius_put_int

radius_put_string
