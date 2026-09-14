---
title: ResourceBundle::getLocales
description: Obtiene las configuraciones locales admitidas
source_url: https://www.php.net/manual/es/resourcebundle.locales.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/resourcebundle/locales.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42420
---

ResourceBundle::getLocales

resourcebundle_locales

Obtiene las configuraciones locales admitidas

## Descripción

Estilo orientado a objetos

```php
public static ResourceBundle::getLocales(string $bundle): array
```php

Estilo procedimental

```php
resourcebundle_locales(string $bundle): array
```

Obtiene la lista de configuraciones locales desde el nombre ResourceBundle.

## Parámetros

`bundle`  
Ruta para ResourceBundle desde la cual se obtienen las configuraciones locales disponibles, o una cadena vacía para la lista de configuraciones locales por omisión.

## Valores devueltos

Devuelve la lista de configuraciones locales admitidas por este paquete, o `false` en caso de error.

## Ejemplos

Ejemplo con `resourcebundle_locales`

```php
<?php
$bundle = "/user/share/data/myapp";
echo join(PHP_EOL, resourcebundle_locales($bundle));
?>

   
```

Resultado del ejemplo anterior es similar a:

    es
    root

Ejemplo orientado a objetos

```php
<?php
$bundle = "/usr/share/data/myapp";
$r = new ResourceBundle( 'es', $bundle);
echo join("\n", $r->getLocales($bundle));
?>

   
```

Resultado del ejemplo anterior es similar a:

    es
    root

## Véase también

`resourcebundle_get`
