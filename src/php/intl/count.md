---
title: ResourceBundle::count
description: Obtiene el número de elementos en el paquete
source_url: https://www.php.net/manual/es/resourcebundle.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/resourcebundle/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42370
---

ResourceBundle::count

resourcebundle_count

Obtiene el número de elementos en el paquete

## Descripción

Estilo orientado a objetos

```php
public ResourceBundle::count(): int
```php

Estilo procedimental

```php
resourcebundle_count(ResourceBundle $bundle): int
```

Obtiene el número de elementos en el paquete.

## Parámetros

`bundle`  
Un objeto `ResourceBundle`.

## Valores devueltos

Devuelve el número de elementos del paquete.

## Ejemplos

Ejemplo con `resourcebundle_count`

```php
<?php
$r = resourcebundle_create( 'es', "/usr/share/data/myapp");
echo resourcebundle_count($r);
?>

   
```

Ejemplo orientado a objetos

```php
<?php
$r = new ResourceBundle( 'es', "/usr/share/data/myapp");
echo $r->count();
?>

   
```

El ejemplo anterior mostrará:

    42

## Véase también

`resourcebundle_get`
