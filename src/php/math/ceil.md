---
title: ceil
description: Redondea al número superior
source_url: https://www.php.net/manual/es/function.ceil.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/ceil.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 761d72245
order: 44570
---

ceil

Redondea al número superior

## Descripción

```php
ceil(int $num): float
```php

Devuelve el entero superior del número `num`.

## Parámetros

`num`  
El valor a redondear

## Valores devueltos

El valor `num` redondeado al entero superior. El valor devuelto es un número de punto flotante (`float`), ya que el intervalo de valores de un `float` es generalmente más amplio que el de un `int`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `num` ya no acepta objetos internos que soportan las conversiones numéricas. |

## Ejemplos

Ejemplo con `ceil`

```
<?php
echo ceil(4.3), PHP_EOL;    // 5
echo ceil(9.999), PHP_EOL;  // 10
echo ceil(-3.14), PHP_EOL;  // -3
?>

    
```php

## Véase también

`floor`, `round`
