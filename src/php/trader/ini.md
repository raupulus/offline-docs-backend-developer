---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/trader.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: d4d5216e7
order: 96100
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [trader.real_precision](#ini.trader.real-precision) | 3 | `INI_ALL` | Desde trader 0.2.1 |
| [trader.real_round_mode](#ini.trader.real-round-mode) | HALF_DOWN | `INI_ALL` | Desde trader 0.3.0 |

Trader Opciones de configuración

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`trader.real_precision` `int`  
Todos los valores de los arrays devueltos serán redondeados a esta precisión. Sin enbargo, los cálculos dentro de TA-Lib se realizarán con valores no redondeados.

`trader.real_round_mode` `string`  
Controla la política de redondeo de números reales de trader. Los valores válidos son `HALF_UP`, `HALF_DOWN`, `HALF_EVEN` y `HALF_ODD`. El comportamiento es idéntico al de la función [round()](#function.round) usada con el argumento de modo.
