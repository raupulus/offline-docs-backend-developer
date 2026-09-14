---
title: strtolower
description: Devuelve una string en minúsculas
source_url: https://www.php.net/manual/es/function.strtolower.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strtolower.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 54ff7bf8e
order: 89480
---

strtolower

Devuelve una string en minúsculas

## Descripción

```php
strtolower(string $string): string
```php

Devuelve `string`, después de haber convertido todos los caracteres alfabéticos ASCII a minúsculas.

Los octetos en el rango `"A"` (0x41) a `"Z"` (0x5a) serán convertidos a su letra minúscula correspondiente sumando 32 a cada valor de octeto.

Esto puede ser utilizado para convertir caracteres ASCII en strings codificadas con UTF-8, ya que los caracteres UTF-8 multioctetos serán ignorados. Para convertir caracteres no ASCII multioctetos, utilice la función `mb_strtolower`.

## Parámetros

`string`  
La string de entrada.

## Valores devueltos

Devuelve la string en minúsculas.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | La conversión de la casilla ya no depende de la configuración local definida con `setlocale`. Solo se convertirán los caracteres ASCII. |

## Ejemplos

Ejemplo con `strtolower`

```
<?php
$str = "Marie A un Petit Agneau, et l'aime TRès fORt.";
$str = strtolower($str);
echo $str; // marie a un petit agneau, et l'aime très fort.
?>

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`strtoupper`, `ucfirst`, `ucwords`, `mb_strtolower`
