---
title: La clase SessionHandlerInterface
source_url: https://www.php.net/manual/es/class.sessionhandlerinterface.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionhandlerinterface.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 8859c8b96
order: 74100
---

## Introducción

`SessionHandlerInterface` es una interfaz que define un prototipo para crear un gestor de sesiones personalizado. Para pasar un gestor de sesiones personalizado a `session_set_save_handler` usando su invocación de `POO`, la clase debe implementar esta interfaz.

Observe que los métodos de llamada de retorno de esta clase están diseñados para ser llamados internamente por PHP y no para ser llamados desde código de espacio de usuario.

## Sinopsis de la interfaz

SessionHandlerInterface

Métodos

## Ejemplos

Ejemplo usando `SessionHandlerInterface`

El siguiente ejemplo proporciona almacenamiento de sesiones basado en ficheros similar al gestor de almacenamiento de sesiones predeterminado de PHP `files`. Este ejemplo podría fácilmente ser extendido para cubrir almacenamiento de bases de datos usando su motor de bases de datos favorito soportado por PHP.

Observe que usamos el prototipo de POO con `session_set_save_handler` y registramos la función de cierre usando la bandera de parámetro de la función. Esto normalmente es aconsejable al registrar objetos como gestores de almacenamiento de sesiones.

> [!CAUTION]
> Por razones de brevedad, este ejemplo omite la validación de entradas. Sin embargo, los parámetros `$id` son en realidad valores suministrados por el usuario que requieren una validación/sanitización adecuada para evitar vulnerabilidades, como problemas de recorrido o cruce en la ruta de acceso. *Así que no utilice este ejemplo sin modificar en entornos de producción.*

```php
<?php
class MySessionHandler implements SessionHandlerInterface
{
    private $savePath;

    public function open($savePath, $sessionName): bool
    {
        $this->savePath = $savePath;
        if (!is_dir($this->savePath)) {
            mkdir($this->savePath, 0777);
        }

        return true;
    }

    public function close(): bool
    {
        return true;
    }

    #[\ReturnTypeWillChange]
    public function read($id)
    {
        return (string) @file_get_contents("$this->savePath/sess_$id");
    }

    public function write($id, $data): bool
    {
        return file_put_contents("$this->savePath/sess_$id", $data) === false ? false : true;
    }

    public function destroy($id): bool
    {
        $file = "$this->savePath/sess_$id";
        if (file_exists($file)) {
            unlink($file);
        }

        return true;
    }

    #[\ReturnTypeWillChange]
    public function gc($maxlifetime)
    {
        foreach (glob("$this->savePath/sess_*") as $file) {
            if (filemtime($file) + $maxlifetime < time() && file_exists($file)) {
                unlink($file);
            }
        }

        return true;
    }
}

$handler = new MySessionHandler();
session_set_save_handler($handler, true);
session_start();

// proceed to set and retrieve values by key from $_SESSION

    
```
