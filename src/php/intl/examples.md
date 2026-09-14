---
title: Ejemplos
source_url: https://www.php.net/manual/es/intl.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: af4410a7e
order: 39770
---

## Ejemplos

## Uso básico de esta extensión

Cada módulo proporciona dos tipos de APIs: una procedimental y otra orientada a objetos. En realidad, ambas son idénticas y están descritas en su correspondiente documentación.

> [!NOTE]
> Todos los strings de entrada deben estar codificados en UTF-8. Del mismo modo, todos los strings de salida deberán estar también en UTF-8.

Ejemplo usando la API procedimental

```php
<?php
$cotejamiento  = collator_create('en_US');
$resultado = collator_compare($cotejamiento, "string#1", "string#2");
?>

   
```

Ejemplo usando la API orientada a objetos

```php
<?php
$cotejamiento = new Collator('en_US');
$al = $cotejamiento->getLocale(Locale::ACTUAL_LOCALE);
echo "Configuración regional real: $al\n";

$formateador = new NumberFormatter('en_US', NumberFormatter::DECIMAL);
echo $formateador->format(1234567);
?>

   
```
