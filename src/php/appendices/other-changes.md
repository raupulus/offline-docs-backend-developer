---
title: Otros cambios
source_url: https://www.php.net/manual/es/migration70.other-changes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration70/other-changes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: fe70c2fc5
order: 400
---

## Otros cambios

## Relajación de las restricciones de las palabras reservadas

Las palabras reservadas globalmente ahora se pueden usar como nombres de propiedades, constantes y métodos dentro de clases, interfaces y traits. Esto reduce el impacto de la ruptura de compatibilidad hacia atrás cuando se introducen nuevas palabras clave, y evita restricciones de nombres al diseñar APIs.

Esto es particularmente útil cuando se crean DSL internos con interfaces "fluidas":

```php
<?php
// 'new', 'private' y 'for' no se podían usar antes
Project::new('Project Name')->private()->for('purpose here')->with('username here');
?>

   
```

La única limitación es que la palabra clave `class` no se puede usar como nombre de constante, ya que entraría en conflicto con la sintaxis de resolución de nombres de clase (`ClassName::class`).

## Eliminación de la advertencia date.timezone

Anteriormente, se emitía una advertencia si la directiva INI `date.timezone` no se había definido antes de utilizar las funciones de fecha y hora. Ahora esta advertencia se ha eliminado (aunque `date.timezone` sigue estando predeterminado en UTC).
