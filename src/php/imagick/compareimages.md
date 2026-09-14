---
title: Imagick::compareImages
description: Compara una imagen con otra reconstruida
source_url: https://www.php.net/manual/es/imagick.compareimages.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/compareimages.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32940
---

Imagick::compareImages

Compara una imagen con otra reconstruida

## Descripción

```php
public Imagick::compareImages(Imagick $compare, int $metric): array
```php

Devuelve un array que contiene una imagen reconstruida y las diferencias entre las imágenes.

## Parámetros

`compare`  
Una imagen a comparar.

`metric`  
Proporcione una constante de tipo de métrica válida. Consulte esta lista de [constantes métricas](#imagick.constants.metric).

## Valores devueltos

Devuelve un array que contiene una imagen reconstruida y las diferencias entre imágenes.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Uso de `Imagick::compareImages`:

Comparar imágenes y mostrar la imagen reconstruida

```
<?php

$imagen1 = new imagick("imagen1.png");
$imagen1 = new imagick("imagen1.png");

$resultado = $imagen1->compareImages($imagen1, Imagick::METRIC_MEANSQUAREERROR);
$resultado[0]->setImageFormat("png");

header("Content-Type: image/png");
echo $resultado[0];

?>

    
```php
