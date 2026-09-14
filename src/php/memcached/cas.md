---
title: Memcached::cas
description: Comparar y cambiar un elemento
source_url: https://www.php.net/manual/es/memcached.cas.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/cas.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46400
---

Memcached::cas

Comparar y cambiar un elemento

## Descripción

```php
public Memcached::cas(string $cas_token, string $key, mixed $value, [int $expiration]): bool
```php

`Memcached::cas` realiza una operación de `"check and set"` (literalmente, verificar y asignar), de manera que el elemento solo se almacena si ningún otro cliente lo ha actualizado desde que fue leído por el cliente actual. La verificación se realiza mediante el argumento `cas_token` que es un valor único de 64 bits, asignado al elemento por memcached. Consulte la documentación de Memcached::get\* para saber cómo obtener este valor. Tenga en cuenta que este valor se representa como un número flotante, debido a limitaciones en el espacio de enteros de PHP.

## Parámetros

`cas_token`  
Valor único asociado a un elemento existente. Generado por memcached.

`key`  
La clave bajo la cual almacenar el valor.

`value`  
El valor a almacenar.

`expiration`  
El tiempo de expiración, predeterminado a 0. Véase [Expiration Times](#memcached.expiration) para más información.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. El método Memcached::getResultCode va devolver la constante `Memcached::RES_DATA_EXISTS` si el elemento que se intenta almacenar ha sido modificado desde la última lectura.

## Ejemplos

Ejemplo con `Memcached::cas`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

do {
    /* Lee una IP y su CAS */
    $ips = $m->get('ip_block', null, $cas);
    /* Si la IP no existe aún, se crea y se realiza
       un añadido atómico que fallará si la IP ya ha sido añadida */
    if ($m->getResultCode() == Memcached::RES_NOTFOUND) {
        $ips = array($_SERVER['REMOTE_ADDR']);
        $m->add('ip_block', $ips);
    /* De lo contrario, se añade la IP a la lista, y se almacena con la operación
       compare-and-swap y el token, que fallará si la lista ha sido actualizada */
    } else {
        $ips[] = $_SERVER['REMOTE_ADDR'];
        $m->cas($cas, 'ip_block', $ips);
    }
} while ($m->getResultCode() != Memcached::RES_SUCCESS);

?>

    
```php

## Véase también

Memcached::casByKey
