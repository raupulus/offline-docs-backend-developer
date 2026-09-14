---
title: ResourceBundle::create
description: Crea un recurso que representa un haz
source_url: https://www.php.net/manual/es/resourcebundle.create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/resourcebundle/create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42380
---

ResourceBundle::create

resourcebundle_create

ResourceBundle::\_\_construct

Crea un recurso que representa un haz

## Descripción

Estilo orientado a objetos (método)

```php
public static ResourceBundle::create(string $locale, string $bundle, [bool $fallback]): ResourceBundle
```php

Estilo procedimental

```php
resourcebundle_create(string $locale, string $bundle, [bool $fallback]): ResourceBundle
```

Estilo orientado a objetos (constructor) :

```php
public ResourceBundle::__construct(string $locale, string $bundle, [bool $fallback])
```php

Crea un recurso que representa un haz.

## Parámetros

`locale`  
Configuración local desde la cual deben cargarse los recursos (nombre de la configuración local, es decir, en_CA).

`bundle`  
El directorio donde se almacenan los datos o el nombre del archivo .dat.

`fallback`  
Si la configuración local debe coincidir exactamente o si se permite el fallback a la configuración local padre.

## Valores devueltos

Devuelve un objeto `ResourceBundle` o `null` si ocurre un error.

## Ejemplos

Ejemplo con `resourcebundle_create`

```
<?php
$r = resourcebundle_create( 'es', "/usr/share/data/myapp");
echo $r['teststring'];
?>

   
```php

Ejemplo con `ResourceBundle::create`

```
<?php
$r = ResourceBundle::create( 'es', "/usr/share/data/myapp");
echo $r['teststring'];
?>

   
```php

El ejemplo anterior mostrará:

    ¡Hola, mundo!

      

## Véase también

`resourcebundle_get`
