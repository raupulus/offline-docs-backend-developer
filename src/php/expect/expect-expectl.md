---
title: expect_expectl
description: Espera a que la salida de un proceso coincida con un patrón, se supere
  un determinado periodo de tiempo, o se alcance un EOF
source_url: https://www.php.net/manual/es/function.expect-expectl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/expect/functions/expect-expectl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: expect
translation_status: ready
translation_reviewed: false
translation_revision: ca6054f60
order: 20770
---

expect_expectl

Espera a que la salida de un proceso coincida con un patrón, se supere un determinado periodo de tiempo, o se alcance un

EOF

## Descripción

```php
expect_expectl(resource $expect, array $cases, [array $match]): int
```php

Espera a que la salida de un proceso coincida con un patrón, se supere un determinado periodo de tiempo, o se alcance un EOF.

Si se proporciona el parámetro `match`, se le asignará el resultado de la búsqueda. La cadena que coincide se encuentra en `match[0]`. Las subcadenas que coincidan (de acuerdo a los paréntesis) con el patrón original se encuentran en `match[1]`, `match[2]`, y así hasta `match[9]` (límite establecido por libexpect).

## Parámetros

`expect`  
Flujo de Expect, abierto anteriormente con `expect_popen`.

`cases`  
Matriz con casos de expect. Cada caso será un array indexado, tal como se describe en la siguiente tabla:

| Clave de índice | Tipo de valor | Descripción | Es Obligatorio | Valor por omisión |
|----|----|----|----|----|
| 0 | string | patrón, que buscará coincidencias en la salida del flujo | sí |  |
| 1 | mixto | valor, que devolverá esta función, si coincidiera el patrón | sí |  |
| 2 | integer | tipo de patrón, de entre: [`EXP_GLOB`](#constant.exp-glob), [`EXP_EXACT`](#constant.exp-exact) o [`EXP_REGEXP`](#constant.exp-regexp) | no | [`EXP_GLOB`](#constant.exp-glob) |

Array de Caso de Expect

## Valores devueltos

Devuelve valores asociados con el patrón que coincida.

En caso de error esta función devuelve: [`EXP_EOF`](#constant.exp-eof), [`EXP_TIMEOUT`](#constant.exp-timeout) o [`EXP_FULLBUFFER`](#constant.exp-fullbuffer)

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL expect 0.2.1 | Antes de la versión 0.2.1, en el parámetro `match` se devolvía el string que coincidiera, no un array de substrings coincidentes. |

## Ejemplos

Ejemplo de `expect_expectl`

```
<?php
// Copias de los archivos de host remoto:
ini_set("expect.timeout", 30);

$stream = fopen("expect://scp user@remotehost:/var/log/messages /home/user/messages.txt", "r");

$cases = array(
    // array(patrón, valor que se devolverá si el patrón es encontrado)
    array("password:", "pidió la contraseña"),
    array("yes/no)?",  "pidió sí/no")
);

while (true) {
    switch (expect_expectl($stream, $cases)) {
        case "pidió la contraseña":
            fwrite($stream, "mi_contraseña\n");
            break;
        case "pidió sí/no":
            fwrite($stream, "yes\n");
            break;
        case EXP_TIMEOUT:
        case EXP_EOF:
            break 2; // sale tanto del switch como del bucle while
        default:
            die("¡Ha ocurrido un error!");
    }
}

fclose($stream);
?>

   
```php

## Véase también

expect_popen
