---
title: ResourceBundle::get
description: Recupera los datos desde el haz
source_url: https://www.php.net/manual/es/resourcebundle.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/resourcebundle/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: f7f861700
order: 42410
---

ResourceBundle::get

resourcebundle_get

Recupera los datos desde el haz

## Descripción

Estilo orientado a objetos

```php
public ResourceBundle::get(string $index, [bool $fallback]): ResourceBundle
```php

Estilo procedimental

```php
resourcebundle_get(ResourceBundle $bundle, string $index, [bool $fallback]): ResourceBundle
```

Recupera los datos desde el haz mediante el índice o la clave.

## Parámetros

`bundle`  
Un objeto `ResourceBundle`.

`index`  
El índice de los datos; puede ser un `string` o un `integer`.

`fallback`  
Las configuraciones regionales deben coincidir exactamente o se permite el retorno a las configuraciones regionales padres.

## Valores devueltos

Devuelve los datos situados en un índice dado o `null` si ocurre un error. Las cadenas de caracteres, los enteros y los datos binarios son devueltos en sus formas correspondientes en tipos PHP; los arrays de enteros son devueltos en forma de array PHP. Los tipos complejos son devueltos en forma de objeto `ResourceBundle`.

## Errores/Excepciones

Se lanza una TypeError si el tipo del desplazamiento es inválido.

Se lanza una ValueError si `index` es un `string` y está vacío o es un `int` y no puede ser contenido en un entero de 32 bits.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Se lanza una TypeError si el tipo del desplazamiento es inválido. Se lanza una ValueError si `index` es un `string` y está vacío o es un `int` y no puede ser contenido en un entero de 32 bits. |

## Ejemplos

Ejemplo con `resourcebundle_get`

```php
<?php
$r = resourcebundle_create( 'es', "/usr/share/data/myapp");
echo resourcebundle_get($r, 'somestring');
?>

   
```

Ejemplo orientado a objetos

```php
<?php
$r = new ResourceBundle( 'es', "/usr/share/data/myapp");
echo $r->get('somestring');
?>

   
```

El ejemplo anterior mostrará:

    ?Hola, mundo!

## Véase también

`resourcebundle_count`
