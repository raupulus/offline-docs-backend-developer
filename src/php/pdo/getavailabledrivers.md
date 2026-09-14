---
title: PDO::getAvailableDrivers
description: Devuelve la lista de controladores PDO disponibles
source_url: https://www.php.net/manual/es/pdo.getavailabledrivers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/getavailabledrivers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 661e6858a
order: 61900
---

PDO::getAvailableDrivers

pdo_drivers

Devuelve la lista de controladores PDO disponibles

## Descripción

```php
public static PDO::getAvailableDrivers(): array
```php

```php
pdo_drivers(): array
```

Esta función devuelve la lista de todos los controladores PDO disponibles que pueden ser utilizados con el argumento `DSN` de la función PDO::\_\_construct.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

PDO::getAvailableDrivers devuelve un array de nombres de controladores. Si no hay controladores disponibles, devuelve un array vacío.

## Ejemplos

Ejemplo con PDO::getAvailableDrivers

```php
<?php
print_r(PDO::getAvailableDrivers());
?>

    
```

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => mysql
        [1] => sqlite
    )
