---
title: ImagickKernel::getMatrix
description: Devuelve la matriz 2D de los valores utilizados en este núcleo
source_url: https://www.php.net/manual/es/imagickkernel.getmatrix.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickkernel/getmatrix.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1ef9c7a76
order: 37450
---

ImagickKernel::getMatrix

Devuelve la matriz 2D de los valores utilizados en este núcleo

## Descripción

```php
public ImagickKernel::getMatrix(): array
```php

Devuelve la matriz 2D de los valores utilizados en este núcleo. Los elementos son flotantes para los elementos que son utilizados, o 'false' si el elemento debe ser ignorado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una matriz (array 2D) de los valores que representan el núcleo.

## Ejemplos

`ImagickKernel::getMatrix`

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

    $output = "El nombre de núcleo interno 'ring' con parámetros de '2,3.5':<br/>";
    $kernel = \ImagickKernel::fromBuiltIn(
        \Imagick::KERNEL_RING,
        "2,3.5"
    );
    $matrix = $kernel->getMatrix();
    $output .= renderKernelTable($matrix);

    echo $output;

?>

      
```php
