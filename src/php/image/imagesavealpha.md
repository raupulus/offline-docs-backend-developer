---
title: imagesavealpha
description: Determina si la información completa del canal alpha debe conservarse
  al guardar imágenes
source_url: https://www.php.net/manual/es/function.imagesavealpha.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagesavealpha.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 32300
---

imagesavealpha

Determina si la información completa del canal alpha debe conservarse al guardar imágenes

## Descripción

```php
imagesavealpha(GdImage $image, bool $enable): true
```php

`imagesavealpha` define el flag que determina si la información del canal alpha (en oposición a la transparencia de color único) debe conservarse al guardar imágenes. Esto es soportado solo para los formatos de imagen que soportan toda la información de strings alpha, por ejemplo `PNG`, `WebP` y `AVIF`.

> [!NOTE]
> `imagesavealpha` es solo significativo para las imágenes `PNG`, ya que los strings alpha completos siempre son guardados para `WebP` y `AVIF`. No se recomienda confiar en este comportamiento, ya que podría cambiar en el futuro. Por lo tanto, `imagesavealpha` debe ser llamado intencionalmente también para las imágenes `WebP` y `AVIF`.

El alphablending debe ser desactivado (`imagealphablending($im, false)`) para conservar el canal alpha en primer lugar.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`enable`  
Si el canal alpha debe o no ser guardado. Por omisión `false`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Uso simple de `imagesavealpha`

```
<?php
// Carga una imagen PNG con un canal alpha
$png = imagecreatefrompng('./alphachannel_example.png');

// Desactivar el alpha blending
imagealphablending($png, false);

// Realizar las operaciones deseadas

// Definir el flag alpha
imagesavealpha($png, true);

// Mostrar la imagen en el navegador
header('Content-Type: image/png');

imagepng($png);
?>

    
```php

## Véase también

imagealphablending
