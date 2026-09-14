---
title: Imagick::setProgressMonitor
description: Define una función de retrollamada a ser llamada durante el procesamiento
source_url: https://www.php.net/manual/es/imagick.setprogressmonitor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setprogressmonitor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1534707f6
order: 35660
---

Imagick::setProgressMonitor

Define una función de retrollamada a ser llamada durante el procesamiento

## Descripción

```php
public Imagick::setProgressMonitor(callable $callback): bool
```php

Define una función de retrollamada que será llamada durante el procesamiento de la imagen Imagick.

## Parámetros

`callback`  
La función de progreso a llamar. Debe retornar true si el procesamiento de la imagen debe continuar, o false si debe ser cancelado. El argumento offset indica la progresión y el argumento span indica la cantidad total de trabajo a realizar.

```php
callback(mixed $offset, mixed $span): bool
```

> [!CAUTION]
> Los valores pasados a la función de retrollamada no son consistentes. En particular, el argumento span puede aumentar durante el procesamiento de la imagen. Debido a esto, el cálculo del porcentaje completo de una operación de imagen no es trivial.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::setProgressMonitor`

```php
      
<?php
        $abortReason = null;

        try {
            $imagick = new \Imagick(realpath($this->control->getImagePath()));
            $startTime = time();

            $callback = function ($offset, $span)  use ($startTime, &$abortReason) {
                if (((100 * $offset) / $span)  > 20) {
                    $abortReason = "Processing reached 20%";
                    return false;
                }

                $nowTime = time();

                if ($nowTime - $startTime > 5) {
                    $abortReason = "Image processing took more than 5 seconds";
                    return false;
                }
                if (($offset % 5) == 0) {
                    echo "Progress: $offset / $span <br/>";
                }
                return true;
            };

            $imagick->setProgressMonitor($callback);

            $imagick->waveImage(2, 15);

            echo "Data len is: ".strlen($imagick->getImageBlob());
        }
        catch(\ImagickException $e) {
            if ($abortReason != null) {
                echo "Image processing was aborted: ".$abortReason."<br/>";
            }
            else {
                echo "ImagickException caught: ".$e->getMessage()." Exception type is ".get_class($e);
            }
        }

?>

      
```
