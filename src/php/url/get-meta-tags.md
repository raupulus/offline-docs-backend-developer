---
title: get_meta_tags
description: Extrae todas las etiquetas meta de un fichero HTML
source_url: https://www.php.net/manual/es/function.get-meta-tags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/url/functions/get-meta-tags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: url
translation_status: ready
translation_reviewed: true
translation_revision: 6ecb3d252
order: 100220
---

get_meta_tags

Extrae todas las etiquetas meta de un fichero HTML

## Descripción

```php
get_meta_tags(string $filename, [bool $use_include_path]): array
```php

`get_meta_tags` abre el fichero `filename` y lo analiza línea por línea en busca de etiquetas `"meta"`. El análisis cesa al encontrar la etiqueta `</head>`.

## Parámetros

`filename`  
La ruta de acceso a un fichero HTML, en forma de `string`. Puede ser un fichero local o una URL.

Lo que analiza la función `get_meta_tags`

```
<meta name="author" content="name">
<meta name="keywords" content="php documentation">
<meta name="DESCRIPTION" content="a php manual">
<meta name="geo.position" content="49.33;-86.59">
</head> <!-- cesa el análisis aquí -->

        
```php

`use_include_path`  
Si el argumento opcional `use_include_path` vale `true`, `get_meta_tags` buscará también el fichero en el [include_path](#ini.include-path). Este argumento se utiliza para ficheros locales, no para URLs.

## Valores devueltos

Devuelve un array que contiene todas las etiquetas meta analizadas.

El valor de la propiedad se utilizará como clave del array, y su valor como valor correspondiente de la clave. Así se podrá recorrer fácilmente este array con las funciones estándar de array. Los caracteres especiales presentes en el valor serán reemplazados por un guion bajo (`"_"`), y el resto se convertirá a minúsculas. Si dos etiquetas meta poseen el mismo nombre, solo se devolverá la última.

Devuelve `false` en caso de error.

## Ejemplos

Lo que devuelve la función `get_meta_tags`

```
<?php
// Supongamos que las etiquetas anteriores están disponibles en example.com
$tags = get_meta_tags('http://www.example.com/');

// Observe que las claves están en minúsculas, y
// el . ha sido reemplazado por _ en la clave
echo $tags['author'];       // name
echo $tags['keywords'];     // php documentation
echo $tags['description'];  // a php manual
echo $tags['geo_position']; // 49.33;-86.59
?>

    
```php

## Notas

> [!NOTE]
> Solo se analizarán las etiquetas meta con un atributo name. Las comillas no son necesarias.

## Véase también

`htmlentities`, `urlencode`
