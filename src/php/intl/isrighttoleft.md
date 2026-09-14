---
title: Locale::isRightToLeft
description: Comprueba si una configuración regional usa un sistema de escritura de
  derecha a izquierda
source_url: https://www.php.net/manual/es/locale.isrighttoleft.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/isrighttoleft.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: fe74bcd7c
order: 41970
---

Locale::isRightToLeft

locale_is_right_to_left

Comprueba si una configuración regional usa un sistema de escritura de derecha a izquierda

## Descripción

Estilo orientado a objetos

```php
public static Locale::isRightToLeft([string $locale]): bool
```php

Estilo procedimental

```php
locale_is_right_to_left(string $locale): bool
```

Determina si una configuración regional usa un sistema de escritura de derecha a izquierda.

Este método se basa en la biblioteca ICU y evalúa el script dominante asociado a la configuración regional.

## Parámetros

`locale`  
El identificador de configuración regional. Si está vacío, se usa la configuración regional predeterminada.

## Valores devueltos

Devuelve `true` si la configuración regional usa un sistema de escritura de derecha a izquierda, o `false` en caso contrario.

## Historial de cambios

| Versión | Descripción                          |
|---------|--------------------------------------|
| 8.5.0   | Se ha añadido Locale::isRightToLeft. |

## Ejemplos

Comprobar la dirección del texto para una configuración regional

```php
<?php

var_dump(Locale::isRightToLeft('en-US'));
var_dump(Locale::isRightToLeft('ar'));

   
```

El ejemplo anterior mostrará:

    bool(false)
    bool(true)
