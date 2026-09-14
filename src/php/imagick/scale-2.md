---
title: ImagickKernel::scale
description: Redimensiona una lista de núcleos por la cantidad dada
source_url: https://www.php.net/manual/es/imagickkernel.scale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickkernel/scale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 560a2e646
order: 37460
---

ImagickKernel::scale

Redimensiona una lista de núcleos por la cantidad dada

## Descripción

```php
public ImagickKernel::scale(float $scale, [int $normalizeFlag]): void
```php

Redimensiona la lista de núcleos dada por la cantidad dada, con o sin normalización de la suma de los valores del núcleo (según los indicadores dados). El comportamiento exacto de esta función depende del tipo de normalización utilizado consúltense http://www.imagemagick.org/api/morphology.php#ScaleKernelInfo para más detalles.

## Parámetros

`scale`  

`normalizeFlag`  
Imagick::NORMALIZE_KERNEL_NONE, Imagick::NORMALIZE_KERNEL_VALUE, Imagick::NORMALIZE_KERNEL_CORRELATE, Imagick::NORMALIZE_KERNEL_PERCENT

## Valores devueltos

## Ejemplos

`ImagickKernel::scale`

```
      
<?php

    function renderKernelTable($matrix) {
        $output = "<table class='infoTable'>";

        foreach ($matrix as $row) {
            $output .= "<tr>";
            foreach ($row as $cell) {
                $output .= "<td style='text-align:left'>";
                if ($cell === false) {
                    $output .= "false";
                }
                else {
                    $output .= round($cell, 3);
                }
                $output .= "</td>";
            }
            $output .= "</tr>";
        }

        $output .= "</table>";

        return $output;
    }

    $output = "";

    $matrix = [
        [-1, 0, -1],
        [ 0, 4,  0],
        [-1, 0, -1],
    ];

    $kernel = \ImagickKernel::fromMatrix($matrix);
    $kernelClone = clone $kernel;

    $output .= "Núcleo inicial<br/>";
    $output .= renderKernelTable($kernel->getMatrix());

    $output .= "Redimensionamiento con NORMALIZE_KERNEL_VALUE. El  <br/>";
    $kernel->scale(2, \Imagick::NORMALIZE_KERNEL_VALUE);
    $output .= renderKernelTable($kernel->getMatrix());

    $kernel = clone $kernelClone;
    $output .= "Redimensionamiento por porcentaje<br/>";
    $kernel->scale(2, \Imagick::NORMALIZE_KERNEL_PERCENT);
    $output .= renderKernelTable($kernel->getMatrix());

    $matrix2 = [
        [-1, -1, 1],
        [ -1, false,  1],
        [1, 1, 1],
    ];

    $kernel = \ImagickKernel::fromMatrix($matrix2);
    $output .= "Redimensionamiento por correlación<br/>";
    $kernel->scale(1, \Imagick::NORMALIZE_KERNEL_CORRELATE);
    $output .= renderKernelTable($kernel->getMatrix());

    return $output;
?>

      
```php
