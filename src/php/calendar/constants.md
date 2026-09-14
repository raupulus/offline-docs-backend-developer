---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/calendar.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: true
translation_revision: ee1ce6a0e
order: 6520
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`CAL_EASTER_DEFAULT` (`int`)  
Para `easter_days` : calcula Pascua para los años anteriores a 1753 según el calendario juliano, y para los años posteriores según el calendario gregoriano.

`CAL_EASTER_ROMAN` (`int`)  
Para `easter_days` : calcula Pascua para los años anteriores a 1583 según el calendario juliano, y para los años posteriores según el calendario gregoriano.

`CAL_EASTER_ALWAYS_GREGORIAN` (`int`)  
Para `easter_days` : calcula Pascua según el calendario gregoriano proleptico.

`CAL_EASTER_ALWAYS_JULIAN` (`int`)  
Para `easter_days` : calcula Pascua según el calendario juliano.

`CAL_GREGORIAN` (`int`)  
Para `cal_days_in_month`, `cal_from_jd`, `cal_info` y `cal_to_jd` : utiliza el calendario gregoriano proleptico.

`CAL_JULIAN` (`int`)  
Para `cal_days_in_month`, `cal_from_jd`, `cal_info` y `cal_to_jd` : utiliza el calendario juliano.

`CAL_JEWISH` (`int`)  
Para `cal_days_in_month`, `cal_from_jd`, `cal_info` y `cal_to_jd` : utiliza el calendario hebreo.

`CAL_FRENCH` (`int`)  
Para `cal_days_in_month`, `cal_from_jd`, `cal_info` y `cal_to_jd` : utiliza el calendario republicano.

`CAL_NUM_CALS` (`int`)  
El número de calendarios disponibles.

`CAL_JEWISH_ADD_ALAFIM_GERESH` (`int`)  
Para `jdtojewish` : añade un símbolo geresh (que se parece a una apostrofe) como separador de miles al número del año.

`CAL_JEWISH_ADD_ALAFIM` (`int`)  
Para `jdtojewish` : añade la palabra alafim como separador de miles al número del año.

`CAL_JEWISH_ADD_GERESHAYIM` (`int`)  
Para `jdtojewish` : añade un símbolo gershayim (que se parece a una comilla) antes de la letra final de los números de día y año.

`CAL_DOW_DAYNO` (`int`)  
Para `jddayofweek` : el día de la semana como `int`, donde `0` significa Domingo y `6` significa Sábado.

`CAL_DOW_SHORT` (`int`)  
Para `jddayofweek` : el nombre inglés abreviado del día de la semana.

`CAL_DOW_LONG` (`int`)  
Para `jddayofweek` : el nombre inglés del día de la semana.

`CAL_MONTH_GREGORIAN_SHORT` (`int`)  
Para `jdmonthname` : el nombre de mes gregoriano abreviado.

`CAL_MONTH_GREGORIAN_LONG` (`int`)  
Para `jdmonthname` : el nombre de mes gregoriano.

`CAL_MONTH_JULIAN_SHORT` (`int`)  
Para `jdmonthname` : el nombre de mes juliano abreviado.

`CAL_MONTH_JULIAN_LONG` (`int`)  
Para `jdmonthname` : el nombre de mes juliano.

`CAL_MONTH_JEWISH` (`int`)  
Para `jdmonthname` : el nombre de mes hebreo.

`CAL_MONTH_FRENCH` (`int`)  
Para `jdmonthname` : el nombre de mes republicano.
