---
title: is_a
description: Verifica si el objeto es de un cierto tipo o subtipo.
source_url: https://www.php.net/manual/es/function.is-a.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/is-a.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: c558c3af3
order: 6880
---

is_a

Verifica si el objeto es de un cierto tipo o subtipo.

## Descripción

```php
is_a(mixed $object_or_class, string $class, [bool $allow_string]): bool
```php

Determina si el `object_or_class` dado es del tipo de objeto `clase`, o tiene `clase` como uno de sus supertipos.

## Parámetros

`object_or_class`  
Un nombre de clase o una instancia de un objeto.

`class`  
El nombre de la clase o de la interfaz.

`allow_string`  
Si este argumento vale `false`, el nombre de la clase en forma de string en el argumento `object_or_class` no está permitido. Esto permite evitar la llamada al autoloader si la clase no existe.

## Valores devueltos

Retorna `true` si `object_or_class` es del tipo de objeto `clase`, o tiene `clase` como uno de sus supertipos, `false` en caso contrario.

## Ejemplos

Ejemplo con `is_a`

```
<?php
// Define una clase
class WidgetFactory
{
  var $oink = 'moo';
}

// Crea un nuevo objeto
$WF = new WidgetFactory();

if (is_a($WF, 'WidgetFactory')) {
  echo "sí, \$WF es siempre un objeto WidgetFactory\n";
}
?>

    
```php

Uso del operador *instanceof*

```
<?php

// definir una clase
class WidgetFactory
{
  var $oink = 'moo';
}

// crear un nuevo objeto
$WF = new WidgetFactory();

if ($WF instanceof WidgetFactory) {
    echo 'Sí, $WF es un WidgetFactory';
}
?>

    
```php

## Véase también

`get_class`, `get_parent_class`, `is_subclass_of`
