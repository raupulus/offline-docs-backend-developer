---
title: svn_auth_get_parameter
description: Recupera un parámetro de identificación
source_url: https://www.php.net/manual/es/function.svn-auth-get-parameter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-auth-get-parameter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: true
translation_revision: 997700a58
order: 89890
---

svn_auth_get_parameter

Recupera un parámetro de identificación

## Descripción

```php
svn_auth_get_parameter(string $key): string
```php

Recupera el parámetro de identificación cuya clave es `key`. Para una lista de claves válidas y sus significados, consulte la [lista de constantes de identificación](#svn.constants.auth).

## Parámetros

`key`  
Nombre de la clave. Utilice una [constante de identificación](#svn.constants.auth) definida por esta extensión para especificar una clave.

## Valores devueltos

Devuelve el valor del parámetro cuya clave es `key`; devuelve `null` si el parámetro no existe.

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Véase también

svn_auth_set_parameter

Constantes de identificación
