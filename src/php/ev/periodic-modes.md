---
title: Modos de operación periódica de un watcher
source_url: https://www.php.net/manual/es/ev.periodic-modes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/periodic-modes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18760
---

## Modos de operación periódica de un watcher

El watcher `EvPeriodic` funciona en diferentes modos según los parámetros `offset`, `interval` y `reschedule_cb`.

1.  El modo *Temporizador absoluto*. En este modo, `interval` = `0`, `reschedule_cb` = `null`. La llamada se realizará a la hora del reloj `offset` y no se repetirá. No se ajustará cuando ocurra un salto en el tiempo, por lo tanto, si debe ejecutarse el *1 de enero de 2014*, se ejecutará cuando la hora del sistema sea alcanzada o superada.

2.  El modo *Temporizador con repetición por intervalo*. En este modo, `interval` \> `0`, `reschedule_cb` = `null` ; el watcher será programado automáticamente para finalizar en la próxima duración `offset` + `N` \* `interval` (para un entero `N`) y luego se repite, independientemente de los saltos en el tiempo.

    Puede utilizarse para crear temporizadores que no derivan respetando el reloj del sistema:

```php
    <?php
    $hourly = EvPeriodic(0, 3600, NULL, function () {
      echo "una vez por hora\n";
    });
    ?>

        
    ```

    Esto no significa que siempre habrá `3600` segundos entre cada llamada, sino solo que la función de retrollamada será llamada cuando el reloj del sistema muestre una hora completa (*UTC*).

    La clase `EvPeriodic` intentará ejecutar la función de retrollamada en este modo a la próxima hora posible donde `time` = `offset` (`mod` `interval`), independientemente de los saltos en el tiempo.

3.  El modo *reprogramación manual*. En este modo, `reschedule_cb` es un `callable`.

    `interval` y `offset` serán ambos ignorados. En su lugar, cada vez que el watcher periódico esté programado, la función de retrollamada de reprogramación (`reschedule_cb`) será llamada con el watcher primero y el tiempo actual como segundo argumento.

    Esta función de retrollamada *no debe* detener ni destruir este watcher periódico, ni otro, y *no debe* llamar a funciones o métodos de bucle de eventos. Para detenerlo, devuelva `1e30` y deténgalo después. Un watcher `EvPrepare` puede ser utilizado para realizar esta tarea.

    Debe devolver la próxima hora de llamada, basada en el valor del tiempo pasado (el valor de tiempo más pequeño debe ser superior o igual al segundo argumento). Será llamada, habitualmente, justo después de que la función de retrollamada sea lanzada, pero posiblemente en otros momentos.

    Utilización de retrollamada de reprogramación

```php
    <?php
    // Cada 10.5 segundos

    function reschedule_cb ($watcher, $now) {
       return $now + (10.5 - fmod($now, 10.5));
    }

    $w = new EvPeriodic(0., 0., "reschedule_cb", function ($w, $revents) {
       echo time(), PHP_EOL;
    });

    Ev::run();
    ?>

        
    ```
