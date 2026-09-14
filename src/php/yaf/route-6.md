---
title: Yaf_Route_Static::route
description: Enviar una petición
source_url: https://www.php.net/manual/es/yaf-route-static.route.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_route_static/route.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 37a12bad6
order: 106880
---

Yaf_Route_Static::route

Enviar una petición

## Descripción

```php
public Yaf_Route_Static::route(Yaf_Request_Abstract $request): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`request`  

## Valores devueltos

Siempre es `true`

## Ejemplos

Ejemplo de `Yaf_Route_Static::route`

```
// se asume que sólo existe un módulo definido: Index
Request: http://yourdomain.com/a/b
=> module = index, controller=a, action=b

//se asume ap.action_prefer = On
Request: http://yourdomain.com/b
=> module = default(index), controller = default(index), action = b

//se asume ap.action_prefer = Off
Request: http://yourdomain.com/b
=> module = default(index), controller = b, action = default(index)

Request: http://yourdomain.com/a/b/foo/bar/test/a/id/4
=> module = default(index), controller = a, action = b, request parameters: foo = bar, test = a, id = 4

   
```php

## Véase también

Yaf_Route_Supervar::route

Yaf_Route_Simple::route

Yaf_Route_Regex::route

Yaf_Route_Rewrite::route

Yaf_Route_Map::route
