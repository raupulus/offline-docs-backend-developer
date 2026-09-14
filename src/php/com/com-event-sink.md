---
title: com_event_sink
description: Conecta eventos de un objeto COM a un objeto PHP
source_url: https://www.php.net/manual/es/function.com-event-sink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/functions/com-event-sink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 20216b916
order: 7690
---

com_event_sink

Conecta eventos de un objeto COM a un objeto PHP

## Descripción

```php
com_event_sink(variant $variant, object $sink_object, [array $sink_interface]): bool
```php

Conecta eventos del objeto COM `variant` a un objeto PHP `sink_object`.

Sea prudente al utilizar esta funcionalidad; si se hace algo similar al ejemplo a continuación, no tiene sentido ejecutarlo en un servidor web.

## Parámetros

`variant`  

`sink_object`  
`sink_object` debe ser una instancia de la clase con nombres de métodos que sigan el dispinterface deseado; se debe utilizar `com_print_typeinfo` para ayudar a generar una plantilla de clase para esto.

`sink_interface`  
PHP debe ser capaz de utilizar el tipo por defecto de dispinterface especificado por la Typelib asociada con el objeto `variant`, pero se puede cambiar esto especificando en el parámetro `sink_interface` el dispinterface que se desea utilizar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                         |
|---------|-------------------------------------|
| 8.0.0   | `sink_interface` ahora es nullable. |

## Ejemplos

Ejemplo de conexiones de eventos COM

```
<?php
class IEEventSinker {
    var $terminated = false;

   function ProgressChange($progress, $progressmax) {
      echo "Progreso de la descarga: $progress / $progressmax\n";
    }

    function DocumentComplete(&$dom, $url) {
      echo "Documento $url terminado\n";
    }

    function OnQuit() {
      echo "¡Salir!\n";
      $this->terminated = true;
    }
}
$ie = new COM("InternetExplorer.Application");
$sink = new IEEventSinker();
com_event_sink($ie, $sink, "DWebBrowserEvents2");
$ie->Visible = true;
$ie->Navigate("http://www.example.org");
while(!$sink->terminated) {
  com_message_pump(4000);
}
$ie = null;
?>

    
```php

## Notas

> [!CAUTION]
> Antes de PHP 8.0.0, llamar a `exit` desde cualquier gestor de eventos no es soportado, y puede causar que PHP se bloquee. Esto puede evitarse lanzando una excepción desde un gestor de eventos, capturando la excepción en el código principal, y llamando a `exit` allí.

## Véase también

`com_print_typeinfo`, `com_message_pump`
