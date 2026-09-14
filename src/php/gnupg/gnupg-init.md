---
title: gnupg_init
description: Inicializa una conexión
source_url: https://www.php.net/manual/es/function.gnupg-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 29130
---

gnupg_init

Inicializa una conexión

## Descripción

```php
gnupg_init([array $options]): resource
```php

## Parámetros

`options`  
Debe ser un array asociativo. Se utiliza para modificar la configuración por omisión del motor criptográfico.

| Clave | Tipo | Descripción |
|----|----|----|
| file_name | `string` | Es el nombre de fichero del programa ejecutable que implementa este protocolo, que generalmente es la ruta del ejecutable `gpg`. |
| home_dir | `string` | Es el nombre del directorio de configuración. También sustituye a la variable de entorno `GNUPGHOME` que se utiliza con el mismo propósito. |

Sustitución de la configuración

## Valores devueltos

Un recurso de conexión GnuPG, utilizado por otras funciones GnuPG.

## Historial de cambios

| Versión          | Descripción                           |
|------------------|---------------------------------------|
| PECL gnupg 1.5.0 | Se ha añadido el argumento `options`. |

## Ejemplos

Ejemplo con `gnupg_init` con configuración por omisión (Estilo procedimental)

```
<?php
$res = gnupg_init();
?>

    
```php

Ejemplo con `gnupg_init` con nombre de fichero y directorio de origen sobrescritos (Estilo procedimental)

```
<?php
$res = gnupg_init(["file_name" => "/usr/bin/gpg2", "home_dir" => "/var/www/.gnupg"]);
?>

    
```php

Ejemplo con `gnupg_init` con configuración por omisión (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
?>

    
```php

Ejemplo con `gnupg_init` con nombre de fichero y directorio de origen sobrescritos (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg(["file_name" => "/usr/bin/gpg2", "home_dir" => "/var/www/.gnupg"]);
?>

    
```php
