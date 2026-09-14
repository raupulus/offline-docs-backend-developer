---
title: bcscale
description: Define o recupera la precisión por defecto para todas las funciones bc
  math
source_url: https://www.php.net/manual/es/function.bcscale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/functions/bcscale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: ddb05f882
order: 6330
---

bcscale

Define o recupera la precisión por defecto para todas las funciones bc math

## Descripción

```php
bcscale(int $scale): int
```php

Define la precisión por defecto para todas las llamadas posteriores a las funciones bc math que omiten el argumento de precisión.

```php
bcscale([null $scale]): int
```

Recupera el factor de precisión actual.

## Parámetros

`scale`  
El factor de precisión.

## Valores devueltos

Retorna la precisión anterior cuando se utiliza como definidor. De lo contrario, se retorna la precisión actual.

## Errores/Excepciones

Esta función levanta una excepción ValueError si `scale` está fuera del rango válido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `scale` ahora es nullable. |
| 7.3.0 | `bcscale` ahora puede ser utilizada para recuperar la precisión actual; cuando se utiliza para definir una nueva precisión, ahora retorna la precisión anterior. Anteriormente, `scale` era obligatorio, y `bcscale` siempre retornaba `true`. |

## Ejemplos

Ejemplo con `bcscale`

```php
<?php

// precisión por defecto: 3
bcscale(3);
echo bcdiv('105', '6.55957'); // 16.007

// lo mismo sin utilizar bcscale()
echo bcdiv('105', '6.55957', 3); // 16.007

?>

    
```
