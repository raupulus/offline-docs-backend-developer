---
title: ImagickPixel::isSimilar
description: Verifica la distancia entre 2 colores
source_url: https://www.php.net/manual/es/imagickpixel.issimilar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/issimilar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 37630
---

ImagickPixel::isSimilar

Verifica la distancia entre 2 colores

## Descripción

```php
public ImagickPixel::isSimilar(ImagickPixel $color, float $fuzz): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Verifica la distancia entre la color descrita por el objeto ImagickPixel y la del objeto proporcionado, colocando sus valores RGB en el cubo de color. Si la distancia entre los 2 puntos es inferior al valor del argumento `fuzz`, la color es similar. Obsoleto en favor del método [ImagickPixel::isPixelSimilar()](#imagickpixel.ispixelsimilar).

## Parámetros

`color`  
El objeto ImagickPixel utilizado para la comparación.

`fuzz`  
La distancia máxima utilizada para considerar que los colores son similares. El valor máximo teórico es la raíz cuadrada de 3 (1.732).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `ImagickPixel::isSimilar`

```
<?php
        // La prueba a continuación fue escrita con una distancia máxima de 255,
        // por lo tanto, debemos escalarla con una raíz cuadrada de 3 -
        // la longitud de la diagonal de un cubo.
        $root3 = 1.732050807568877;

        $tests = array(
            ['rgb(245, 0, 0)',      'rgb(255, 0, 0)',   9 / $root3,         false,],
            ['rgb(245, 0, 0)',      'rgb(255, 0, 0)',  10 / $root3,         true,],
            ['rgb(0, 0, 0)',        'rgb(7, 7, 0)',     9 / $root3,         false,],
            ['rgb(0, 0, 0)',        'rgb(7, 7, 0)',    10 / $root3,         true,],
            ['rgba(0, 0, 0, 1)',    'rgba(7, 7, 0, 1)', 9 / $root3,         false,],
            ['rgba(0, 0, 0, 1)',    'rgba(7, 7, 0, 1)',    10 / $root3,     true,],
            ['rgb(128, 128, 128)',  'rgb(128, 128, 120)',   7 / $root3,     false,],
            ['rgb(128, 128, 128)',  'rgb(128, 128, 120)',   8 / $root3,     true,],
            ['rgb(0, 0, 0)',        'rgb(255, 255, 255)',   254.9,          false,],
            ['rgb(0, 0, 0)',        'rgb(255, 255, 255)',   255,            true,],
            ['rgb(255, 0, 0)',      'rgb(0, 255, 255)',     254.9,          false,],
            ['rgb(255, 0, 0)',      'rgb(0, 255, 255)',     255,            true,],
            ['black',               'rgba(0, 0, 0)',        0.0,            true],
            ['black',               'rgba(10, 0, 0, 1.0)',  10.0 / $root3,  true],);

        $output = "<table width='100%' class='infoTable'><thead>
                <tr>
                <th>
                Color 1
                </th>
                <th>
                Color 2
                </th>
                <th>
                    Test distance * 255
                </th>
                <th>
                    Is within distance
                </th>
                </tr>
        </thead>";

        $output .= "<tbody>";

        foreach ($tests as $testInfo) {
            $color1 = $testInfo[0];
            $color2 = $testInfo[1];
            $distance = $testInfo[2];
            $expectation = $testInfo[3];
            $testDistance = ($distance / 255.0);

            $color1Pixel = new \ImagickPixel($color1);
            $color2Pixel = new \ImagickPixel($color2);

            $isSimilar = $color1Pixel->isPixelSimilar($color2Pixel, $testDistance);

            if ($isSimilar !== $expectation) {
                echo "Test distance failed. Color [$color1] compared to color [$color2] is not within distance $testDistance FAILED.".NL;
            }

            $layout = "<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td style='text-align: center;'>%s</td>
            </tr>";

            $output .= sprintf(
                $layout,
                $color1,
                $color2,
                $distance,
                $isSimilar ? 'yes' : 'no'
            );
        }

        $output .= "</tbody></table>";

        return $output;

?>

     
```php
