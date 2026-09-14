---
title: GearmanClient::doStatus
description: Recupera el estado de la tarea en curso
source_url: https://www.php.net/manual/es/gearmanclient.dostatus.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/dostatus.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25110
---

GearmanClient::doStatus

Recupera el estado de la tarea en curso

## Descripción

```php
public GearmanClient::doStatus(): array
```php

Devuelve el estado de la tarea en curso. Puede ser utilizado durante múltiples llamadas al método GearmanClient::doNormal.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array que representa el porcentaje de realización proporcionado en forma de fracción, donde el primer elemento es el numerador, y el segundo, el denominador.

## Ejemplos

Recupera el estado de un trabajo cuya ejecución tarda tiempo

El agente en este ejemplo tiene un retraso artificial añadido durante la ejecución de la función. Después de cada retraso, llama al método GearmanJob::status del cual el cliente recupera la información.

```
<?php

echo "Inicio\n";

## Crea un cliente.
$gmclient= new GearmanClient();

## Añade un servidor por defecto (localhost).
$gmclient->addServer();

echo "Envío de un trabajo\n";

## Envío del trabajo
do
{
  $result = $gmclient->doNormal("reverse", "Hello!");

  # Verifica los diferentes paquetes y errores devueltos.
  switch($gmclient->returnCode())
  {
    case GEARMAN_WORK_DATA:
      break;
    case GEARMAN_WORK_STATUS:
      # Recupera el estado del trabajo en curso
      list($numerator, $denominator)= $gmclient->doStatus();
      echo "Estado : $numerator/$denominator complete\n";
      break;
    case GEARMAN_WORK_FAIL:
      echo "Fallo \n";
      exit;
    case GEARMAN_SUCCESS:
      break;
    default:
      echo "RET : " . $gmclient->returnCode() . "\n";
      exit;
  }
}
while($gmclient->returnCode() != GEARMAN_SUCCESS);

echo "Éxito : $result\n";

?>

   
```php

Resultado del ejemplo anterior es similar a:

    Inicio
    Envío de un trabajo
    Estado : 1/6 complete
    Estado : 2/6 complete
    Estado : 3/6 complete
    Estado : 4/6 complete
    Estado : 5/6 complete
    Estado : 6/6 complete
    Éxito : !olleH

## Véase también

GearmanClient::doNormal

GearmanJob::status
