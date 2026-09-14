---
title: Gmagick::levelimage
description: Ajusta los niveles de la imagen
source_url: https://www.php.net/manual/es/gmagick.levelimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/levelimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 27160
---

Gmagick::levelimage

Ajusta los niveles de la imagen

## Descripción

```php
public Gmagick::levelimage(float $blackPoint, float $gamma, float $whitePoint, [int $channel]): mixed
```php

Ajusta los niveles de una imagen escalando la caída de los colores entre los puntos blanco y negro especificados al rango completo de cuantía disponible. Los parámetros proporcionados representan los puntos negro, mitad, y blanco. El punto negro especifica el color más oscuro de la imagen. Los colores más oscuros que el punto negro se establecen a cero. El punto medio especifica una corrección gamma a aplicar a la imagen. Mientras que el punto blanco especifica el color más claro de la imagen. Los colores más claros que el punto blanco se establecen al valor de cuantía máximo.

## Parámetros

`blackPoint`  
El punto negro de la imagen.

`gamma`  
El valor gamma

`whitePoint`  
El punto blanco de la imagen.

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#gmagick.constants.channel).

## Valores devueltos

Objeto `Gmagick` con la imagen nivelada.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
