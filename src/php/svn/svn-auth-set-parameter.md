---
title: svn_auth_set_parameter
description: Especifica un parámetro de autenticación
source_url: https://www.php.net/manual/es/function.svn-auth-set-parameter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-auth-set-parameter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: false
translation_revision: 997700a58
order: 89900
---

svn_auth_set_parameter

Especifica un parámetro de autenticación

## Descripción

```php
svn_auth_set_parameter(string $key, string $value): void
```php

Especifica el parámetro de autenticación `key` con el valor `value`. Para una lista de claves válidas y sus significados, consulte la [lista de constantes de autenticación](#svn.constants.auth).

## Parámetros

`key`  
Nombre de la clave. Utilice una [constante de autenticación](#svn.constants.auth) definida por esta extensión para especificar la clave.

`value`  
Valor a establecer para la nueva clave. El formato del valor varía según el parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de autenticación

Este ejemplo configura SVN con el nombre de usuario `"Bob"` y la contraseña `"abc123"`:

```
<?php
svn_auth_set_parameter(SVN_AUTH_PARAM_DEFAULT_USERNAME, 'Bob');
svn_auth_set_parameter(SVN_AUTH_PARAM_DEFAULT_PASSWORD, 'abc123');
?>

   
```php

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Véase también

svn_auth_get_parameter

Constantes de autenticación
