---
title: Cambios incompatibles con versiones anteriores
source_url: https://www.php.net/manual/es/migration83.incompatible.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration83/incompatible.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: 4de6272a1
order: 1020
---

## Cambios incompatibles con versiones anteriores

## Núcleo de PHP

### Programas que estaban muy cerca de desbordar la pila de llamadas

Los programas que estaban muy cerca de desbordar la pila de llamadas ahora pueden lanzar un `Error` cuando usan más de zend.max_allowed_stack_size-zend.reserved_stack_size bytes de pila (fiber.stack_size-zend.reserved_stack_size para fibras).

### Ejecución de proc_get_status() varias veces

Ejecutar `proc_get_status` varias veces ahora siempre devolverá el valor correcto en sistemas POSIX. Anteriormente, sólo la primera llamada de la función devolvía el valor correcto. Ejecutar `proc_close` después de `proc_get_status` ahora también devolverá el código de salida correcto. Anteriormente esto devolvía `-1`. Internamente, esto funciona almacenando en caché el resultado en sistemas POSIX. Si se requiere el comportamiento anterior, es posible verificar la clave `"cached"` en el array devuelto por `proc_get_status` para verificar si el resultado fue almacenado en caché.

### Temporizadores de ejecución máxima de Zend

Los temporizadores de ejecución máxima de Zend ahora están habilitados por defecto para compilaciones ZTS en Linux.

### Uso de traits con propiedades estáticas

El uso de traits con propiedades estáticas ahora redeclarará las propiedades estáticas heredadas de la clase padre. Esto creará un almacenamiento de propiedades estáticas separado para la clase actual. Esto es análogo a agregar la propiedad estática a la clase directamente sin traits.

### Asignación de un índice negativo a un array vacío

Asignar un índice negativo `$n` a un array vacío ahora garantizará que el siguiente índice sea `$n+1` en lugar de `0`.

### Verificación de varianza de visibilidad de constantes de clase

La varianza de visibilidad de constantes de clase ahora se verifica correctamente cuando se hereda de interfaces.

### Entradas de WeakMap cuya clave se mapea a sí misma

Las entradas de `WeakMap` cuya clave se mapea a sí misma (posiblemente de forma transitiva) ahora pueden ser eliminadas durante la recolección de ciclos si la clave no es alcanzable excepto iterando sobre el WeakMap (la alcanzabilidad mediante iteración se considera débil). Anteriormente, dichas entradas nunca se eliminaban automáticamente.

## Fecha

La extensión DateTime ha introducido excepciones y errores específicos de la extensión Date bajo las jerarquías `DateError` y `DateException`, en lugar de advertencias y excepciones genéricas. Esto mejora el manejo de errores, a expensas de tener que verificar errores y excepciones.

## DOM

Llamar a DOMChildNode::after, DOMChildNode::before, DOMChildNode::replaceWith en un nodo que no tiene padre ahora es una operación sin efecto en lugar de una excepción de jerarquía, que es el comportamiento requerido por la especificación DOM.

Usar los métodos de `DOMParentNode` y `DOMChildNode` sin un documento ahora funciona en lugar de lanzar un `DOM_HIERARCHY_REQUEST_ERR` `DOMException`. Esto está en línea con el comportamiento requerido por la especificación DOM.

Llamar a DOMDocument::createAttributeNS sin especificar un prefijo incorrectamente creaba un espacio de nombres predeterminado, colocando el elemento dentro del espacio de nombres en lugar del atributo. Este error ahora está corregido.

DOMDocument::createAttributeNS anteriormente lanzaba incorrectamente un `DOM_NAMESPACE_ERRNAMESPACE_ERR` `DOMException` cuando el prefijo ya se usaba para una URI diferente. Ahora elige correctamente un prefijo diferente cuando hay un conflicto de nombre de prefijo.

Se añadieron nuevos métodos y propiedades a algunas clases DOM. Si una clase de espacio de usuario hereda de estas clases y declara un método o propiedad con el mismo nombre, las declaraciones deben ser compatibles. De lo contrario, se lanzará un error de compilación típico sobre declaraciones incompatibles. Ver la [lista de nuevas funcionalidades](#migration83.new-features.dom) y las [nuevas funciones](#migration83.new-functions.dom) para una lista de los métodos y propiedades recién implementados.

## FFI

Las funciones C que tienen un tipo de retorno `void` ahora devuelven `null` en lugar de devolver el siguiente objeto `object(FFI\CData:void) { }`

## Opcache

La directiva INI [opcache.consistency_checks](#ini.opcache.consistency-checks) fue eliminada. Esta funcionalidad estaba rota con el JIT de rastreo, así como con la caché de herencia, y ha estado deshabilitada sin forma de habilitarla desde PHP 8.1.18 y PHP 8.2.5. Tanto el JIT de rastreo como la caché de herencia pueden modificar la shm después de que el script haya sido persistido al invalidar su suma de verificación. El intento de corrección omitía los punteros modificables pero fue rechazado debido a la complejidad. Por esta razón, se decidió eliminar la funcionalidad.

## Phar

Los tipos de las constantes de la clase `Phar` ahora están declarados.

## Estándar

La función `range` ha tenido varios cambios: Ahora se lanza un TypeError cuando se pasan `object`s, `resource`s, o `array`s como entradas de límite., Se lanza un ValueError más descriptivo cuando se pasa `0` para `step`., Ahora se lanza un ValueError cuando se usa un `step` negativo para rangos crecientes., Si `step` es un float que puede interpretarse como un int, ahora se hace así., Ahora se lanza un ValueError si cualquier argumento es infinito o NAN., Ahora se emite un `E_WARNING` si `start` o `end` es la cadena vacía. El valor continúa siendo convertido al valor `0`., Ahora se emite un `E_WARNING` si `start` o `end` tiene más de un byte, solo si es una cadena no numérica., Ahora se emite un `E_WARNING` si `start` o `end` se convierte a un entero porque la otra entrada de límite es un número. (p.ej. `range(5, 'z');`)., Ahora se emite un `E_WARNING` si `step` es un float al intentar generar un rango de caracteres, excepto si ambas entradas de límite son cadenas numéricas (p.ej. `range('5', '9', 0.5);` no produce una advertencia)., `range` ahora produce una lista de caracteres si una de las entradas de límite es un dígito de cadena en lugar de convertir la otra entrada a int (p.ej. `range('9', 'A');`).

```php
<?php
range('9', 'A');  // ["9", ":", ";", "<", "=", ">", "?", "@", "A"], a partir de PHP 8.3.0
range('9', 'A');  // [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], antes de PHP 8.3.0
?>

    
```

`number_format` ahora maneja valores negativos de `decimals` redondeando `num` a `abs($decimals)` dígitos antes del punto decimal. Anteriormente, los valores negativos de `decimals` eran ignorados.

La verificación de errores de flags de `file` ahora captura todos los flags inválidos. Notablemente, `FILE_APPEND` era anteriormente aceptado silenciosamente.

## SNMP

Los tipos de las constantes de la clase `SNMP` ahora están declarados.
