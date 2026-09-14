---
title: ibase_prepare
description: Prepara una consulta iBase para ligar los argumentos y ejecutarla posteriormente
source_url: https://www.php.net/manual/es/function.ibase-prepare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-prepare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30470
---

ibase_prepare

Prepara una consulta iBase para ligar los argumentos y ejecutarla posteriormente

## Descripción

```php
ibase_prepare(string $query): resource
```php

```php
ibase_prepare(resource $link_identifier, string $query): resource
```

```php
ibase_prepare(resource $link_identifier, string $trans, string $query): resource
```php

Prepara una consulta para ligar posteriormente los argumentos y ejecutarla (a través de la función `ibase_execute`).

## Parámetros

`query`  
Una consulta InterBase.

`link_identifier`  
Un enlace identificador InterBase devuelto por `ibase_connect`. Si se omite, se adopta el último enlace abierto.

`trans`  
Un gestor de transacción InterBase con el cual la consulta debe ser asociada. Si se omite, se adopta la transacción por omisión de la conexión.

## Valores devueltos

Devuelve un gestor de consulta preparada, o `false` si ocurre un error.
