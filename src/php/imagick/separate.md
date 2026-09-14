---
title: ImagickKernel::separate
description: Separa un conjunto de núcleos vinculados y devuelve un array de ImagickKernels
source_url: https://www.php.net/manual/es/imagickkernel.separate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickkernel/separate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1ef9c7a76
order: 37470
---

ImagickKernel::separate

Separa un conjunto de núcleos vinculados y devuelve un array de ImagickKernels

## Descripción

```php
public ImagickKernel::separate(): array
```php

Separa un conjunto de núcleos vinculados y devuelve un array de ImagickKernels.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

## Ejemplos

`ImagickKernel::separate`

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
    $kernel->scale(4, \Imagick::NORMALIZE_KERNEL_VALUE);
    $diamondKernel = \ImagickKernel::fromBuiltIn(
        \Imagick::KERNEL_DIAMOND,
        "2"
    );

    $kernel->addKernel($diamondKernel);

    $kernelList = $kernel->separate();

    $output = '';
    $count = 0;
    foreach ($kernelList as $kernel) {
        $output .= "<br/>Kernel $count<br/>";
        $output .= renderKernelTable($kernel->getMatrix());
        $count++;
    }

    return $output;

?>

      
```php
