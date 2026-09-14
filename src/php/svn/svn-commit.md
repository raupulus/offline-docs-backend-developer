---
title: svn_commit
description: Envía los cambios desde la copia local al repositorio
source_url: https://www.php.net/manual/es/function.svn-commit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-commit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: true
translation_revision: 997700a58
order: 89960
---

svn_commit

Envía los cambios desde la copia local al repositorio

## Descripción

```php
svn_commit(string $log, array $targets, [bool $recursive]): array
```php

Envía los cambios realizados en los ficheros locales enumerados por el array `targets` al repositorio, con el mensaje `log`. Los directorios contenidos en el array `targets` serán enviados recursivamente a menos que el parámetro `recursive` haya sido definido como `false`.

> [!NOTE]
> Esta función no contiene ningún parámetro específico de identificación, por lo tanto, el nombre de usuario y la contraseña deben ser definidos utilizando la función `svn_auth_set_parameter`

## Parámetros

`log`  
Mensaje de registro a utilizar durante el envío.

`targets`  
Array de rutas locales de los ficheros a enviar.

> [!WARNING]
> Este parámetro debe ser un array; una string para un único objetivo no es aceptada.

> [!NOTE]
> Los caminos relativos pueden ser resueltos si el directorio de trabajo actual es uno de los que contienen el binario PHP. Para utilizar el directorio de trabajo, utilice la función `realpath`, o la instrucción dirname(\_\_FILE\_\_).

`recursive`  
Bandera de tipo booleano para desactivar la recursividad al enviar directorios en el array `targets`. Por omisión, vale `true`.

## Valores devueltos

Devuelve un array, en el siguiente formato:

    array(
        0 => número (integer) de revisión del envío
        1 => fecha y hora (formato ISO 8601) del envío
        2 => nombre de usuario de la persona que envió
    )

        

Devuelve `false` si ocurre un error.

## Ejemplos

Ejemplo de uso

Este ejemplo envía el directorio `"calculator"` al repositorio, utilizando como nombre de usuario `"Bob"` y como contraseña `"abc123"`:

```
<?php
svn_auth_set_parameter(SVN_AUTH_PARAM_DEFAULT_USERNAME, 'Bob');
svn_auth_set_parameter(SVN_AUTH_PARAM_DEFAULT_PASSWORD, 'abc123');
var_dump(svn_commit('Mensaje de registro de Bob', array(realpath('calculator'))));
?>

   
```php

El ejemplo anterior mostrará:

    array(
      0 => 1415,
      1 => '2007-05-26T01:44:28.453125Z',
      2 => 'Bob'
    )

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Véase también

svn_auth_set_parameter

Documentación SVN sobre el comando

"svn commit"
