---
title: La clase Closure
source_url: https://www.php.net/manual/es/class.closure.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/closure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: a97672ab0
order: 3100
---

## Introducción

Clase utilizada para representar las [funciones anónimas](#functions.anonymous).

Las funciones anónimas producen objetos de este tipo. Esta clase tiene métodos que permiten un control adicional de la función anónima después de su creación.

Además de los métodos especificados aquí, esta clase también posee un método `__invoke`. Esto es por razones de lógica con la implementación de [el método mágico de llamada](#language.oop5.magic.invoke).

## Sinopsis de la clase

final

Closure

Métodos

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | La salida de Closure::\_\_debugInfo incluye ahora el nombre, la línea y el fichero del cierre. |

## Notas

> [!NOTE]
> Los objetos `Closure` no pueden ser serializados, ya que los cierres pueden contener variables vinculadas y un contexto de ejecución específico. Intentar serializar un cierre lanzará una Exception.
