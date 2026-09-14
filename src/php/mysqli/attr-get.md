---
title: mysqli_stmt::attr_get
description: Obtiene el valor actual de un atributo de consulta
source_url: https://www.php.net/manual/es/mysqli-stmt.attr-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/attr-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55730
---

mysqli_stmt::attr_get

mysqli_stmt_attr_get

Obtiene el valor actual de un atributo de consulta

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::attr_get(int $attribute): int
```php

Estilo procedimental

```php
mysqli_stmt_attr_get(mysqli_stmt $statement, int $attribute): int
```

Obtiene el valor actual de un atributo de consulta.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

`attribute`  
El atributo que se desea recuperar.

## Valores devueltos

Devuelve el valor del atributo.
