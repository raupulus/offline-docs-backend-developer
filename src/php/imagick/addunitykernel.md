---
title: ImagickKernel::addUnityKernel
description: Añade un núcleo Unity a la lista de núcleos
source_url: https://www.php.net/manual/es/imagickkernel.addunitykernel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickkernel/addunitykernel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1534707f6
order: 37420
---

ImagickKernel::addUnityKernel

Añade un núcleo Unity a la lista de núcleos

## Descripción

```php
public ImagickKernel::addUnityKernel(float $scale): void
```php

Añade una cantidad dada del núcleo de convolución 'Unity' al núcleo de convolución pre-escalado y normalizado dado. Esto tiene como efecto añadir esta cantidad de la imagen original en el núcleo de convolución resultante. El efecto resultante es convertir los núcleos definidos en desenfoques suaves mezclados, en núcleos no afilados o en núcleos de nitidez.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

## Ejemplos

`ImagickKernel::addUnityKernel`

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

    $matrix = [
        [-1, 0, -1],
        [ 0, 4,  0],
        [-1, 0, -1],
    ];

    $kernel = \ImagickKernel::fromMatrix($matrix);
    $kernel->scale(1, \Imagick::NORMALIZE_KERNEL_VALUE);
    $output = "Before adding unity kernel: <br/>";
    $output .= renderKernelTable($kernel->getMatrix());
    $kernel->addUnityKernel(0.5);
    $output .= "After adding unity kernel: <br/>";
    $output .= renderKernelTable($kernel->getMatrix());

    $kernel->scale(1, \Imagick::NORMALIZE_KERNEL_VALUE);
    $output .= "After renormalizing kernel: <br/>";
    $output .= renderKernelTable($kernel->getMatrix());

    echo $output;

?>

      
```php

`ImagickKernel::addUnityKernel`

```
      
<?php
function addUnityKernel($imagePath) {

    $matrix = [
        [-1, 0, -1],
        [ 0, 4,  0],
        [-1, 0, -1],
    ];

    $kernel = ImagickKernel::fromMatrix($matrix);

    $kernel->scale(4, \Imagick::NORMALIZE_KERNEL_VALUE);
    $kernel->addUnityKernel(0.5);

    $imagick = new \Imagick(realpath($imagePath));
    $imagick->filter($kernel);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();

}

?>

      
```php
