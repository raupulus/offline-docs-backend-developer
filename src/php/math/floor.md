---
title: floor
description: Redondea hacia el entero inferior
source_url: https://www.php.net/manual/es/function.floor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/floor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 761d72245
order: 44670
---

floor

Redondea hacia el entero inferior

## Descripción

```php
floor(int $num): float
```php

Devuelve el valor entero siguiente más bajo (como float) al redondear el valor `num` si es necesario.

## Parámetros

`num`  
El valor numérico a redondear

## Valores devueltos

`floor` devuelve el entero inferior del número `num`. El valor devuelto es un número de punto flotante (`float`).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `num` ya no acepta objetos internos que soportan conversiones numéricas. |

## Ejemplos

Ejemplo con `floor`

```
<?php
echo floor(4.3), PHP_EOL;   // 4
echo floor(9.999), PHP_EOL; // 9
echo floor(-3.14), PHP_EOL; // -4
?>

    
```php

## Véase también

`ceil`, `round`
