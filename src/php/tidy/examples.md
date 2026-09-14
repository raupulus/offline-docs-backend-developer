---
title: Ejemplos
source_url: https://www.php.net/manual/es/tidy.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 79dcbe011
order: 93890
---

## Ejemplos

## Ejemplos de Tidy

Este simple ejemplo muestra el uso básico de Tidy.

Uso Básico Tidy

```php
<?php
ob_start();
?>
<html>a html document</html>
<?php
$html = ob_get_clean();

// Specify configuration
$config = array(
           'indent'         => true,
           'output-xhtml'   => true,
           'wrap'           => 200);

// Tidy
$tidy = new tidy;
$tidy->parseString($html, $config, 'utf8');
$tidy->cleanRepair();

// Output
echo $tidy;
?>

    
```
