---
title: Ejemplos
source_url: https://www.php.net/manual/es/gmagick.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 26440
---

## Ejemplos

A continuación se muestran algunas operaciones comunes con Gmagick.

Ejemplo de Gmagick

```php
<?php
// Instanciación de un nuevo objeto Gmagick
$image = new Gmagick('example.jpg');

// Crea una miniatura a partir de la imagen cargada. 0 para uno de los ejes preservará la relación de aspecto
$image->thumbnailimage(100, 0);

// Crea un borde alrededor de la imagen, luego simula cómo se renderizará la imagen
// después de un renderizado a pintura al óleo.
// Observe el encadenamiento de métodos soportado por Gmagick
$image->borderimage("yellow", 8, 8)->oilpaintimage(0.3);

// Escribe la imagen actual en un fichero
$image->write('example_thumbnail.jpg');
?>

  
```
