---
title: Ejemplos
source_url: https://www.php.net/manual/es/fdf.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 22340
---

## Ejemplos

Los siguientes ejemplos muestran cómo evaluar los datos del formulario.

Evaluar un documento FDF

```php
<?php
// Abrir un fichero FDF desde una string proporcionada por la extensión PDF
// El formulario PDF contiene varios campos de texto con los nombres
// volume, date, comment, publisher, preparer y dos casillas de verificación
// show_publisher y show_preparer.
$fdf = fdf_open_string($HTTP_FDF_DATA);
$volume = fdf_get_value($fdf, "volume");
echo 'El campo Volume contiene el valor: "<strong>' . $volume . '</strong>"<br />';

$date = fdf_get_value($fdf, "date");
echo 'El valor del campo date era "<strong>' . $date . '</strong>"<br />';

$comment = fdf_get_value($fdf, "comment");
echo 'El valor del campo comment era "<strong>' . $comment . '</strong>"<br />';

if (fdf_get_value($fdf, "show_publisher") == "On") {
  $publisher = fdf_get_value($fdf, "publisher");
  echo "El valor del campo Publisher era: '<strong>" . $publisher . "</strong><br />";
} else
  echo 'El valor del campo Publisher no debe ser mostrado.<br />';

if (fdf_get_value($fdf, "show_preparer") == "On") {
  $preparer = fdf_get_value($fdf, "preparer");
  echo 'El valor del campo Preparer era "<strong>' . $preparer . '</strong>"<br />';
} else
  echo 'El valor del campo Preparer no debe ser mostrado.<br />';
fdf_close($fdf);
?>

    
```
