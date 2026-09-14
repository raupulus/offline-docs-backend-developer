---
title: Collator::__construct
description: Creación de un collator
source_url: https://www.php.net/manual/es/collator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39380
---

Collator::\_\_construct

Creación de un collator

## Descripción

```php
public Collator::__construct(string $locale)
```php

Creación de una nueva instancia de `Collator`.

## Parámetros

`locale`  
La configuración local cuyos reglas de ordenación deben ser respetadas. Valores especiales pueden ser pasados en este argumento: si un `string` vacío es pasado, la configuración local por omisión será utilizada. Si la palabra clave `"root"` es pasada, las reglas [UCA](https://www.unicode.org/reports/tr10/) serán utilizadas.

El atributo Locale es generalmente el atributo más importante para asegurar ordenaciones y comparaciones válidas, en función de las expectativas de los usuarios. El orden por omisión [UCA](https://www.unicode.org/reports/tr10/) ordenará únicamente algunas lenguas, tales como holandés o portugués (correctamente significa que el resultado será conforme a las expectativas de los usuarios de estas lenguas). De otro modo, debe ser proporcionada una configuración local adaptada a los usuarios. Por consiguiente, un valor específico de configuración local debe ser proporcionado para asegurar un servicio correcto. La elección de la configuración local configurará los valores de todos sus atributos que son los más pertinentes para una configuración local. Por consiguiente, la mayoría del tiempo, los atributos no necesitan ser explícitamente atribuidos. Al mismo tiempo, la elección de la configuración local tendrá un impacto en las prestaciones de comparación y ordenación.

## Errores/Excepciones

Devuelve un objeto "vacío" en caso de error. Utilizar `intl_get_error_code` y / o `intl_get_error_message` para obtener más información.

## Ejemplos

Ejemplo con `Collator::__construct`

```
<?php
$coll = new Collator('en_CA');
?>

    
```php

## Véase también

`Collator::create`, `collator_create`
