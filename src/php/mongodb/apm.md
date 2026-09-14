---
title: Monitoreo del rendimiento de la aplicación (Application Performance Monitoring
  - APM)
source_url: https://www.php.net/manual/es/mongodb.tutorial.apm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/tutorial/apm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 4de6272a1
order: 51770
---

## Monitoreo del rendimiento de la aplicación (Application Performance Monitoring - APM)

La extensión contiene una API de observaciones de eventos, que permite a las aplicaciones monitorear las órdenes y las actividades internas relacionadas con la [Especificación de descubrimiento y monitoreo del servidor](https://github.com/mongodb/specifications/blob/master/source/server-discovery-and-monitoring/server-discovery-and-monitoring.md). Este tutorial demostrará el monitoreo de las órdenes utilizando la interfaz `MongoDB\Driver\Monitoring\CommandSubscriber`.

La interfaz `MongoDB\Driver\Monitoring\CommandSubscriber` define tres métodos: `commandStarted`, `commandSucceeded`, y `commandFailed`. Cada uno de estos tres métodos acepta un solo argumento `event` de una clase específica para el evento respectivo. Por ejemplo, el argumento `event` de `commandSucceeded` es un objeto `MongoDB\Driver\Monitoring\CommandSucceededEvent`.

En este tutorial, se implementará un observador que crea una lista de todos los perfiles de solicitud y el tiempo promedio que han tomado.

## Estructura de las clases de observaciones

Se comienza con el marco del observador:

```php
<?php

class QueryTimeCollector implements \MongoDB\Driver\Monitoring\CommandSubscriber
{
    public function commandStarted( \MongoDB\Driver\Monitoring\CommandStartedEvent $event ): void
    {
    }

    public function commandSucceeded( \MongoDB\Driver\Monitoring\CommandSucceededEvent $event ): void
    {
    }

    public function commandFailed( \MongoDB\Driver\Monitoring\CommandFailedEvent $event ): void
    {
    }
}

?>

  
```

## Registro del observador

Una vez que un objeto observador es instanciado, debe ser registrado con el sistema de monitoreo de la extensión. Esto se hace llamando a MongoDB\Driver\Monitoring\addSubscriber o MongoDB\Driver\Manager::addSubscriber para registrar el observador globalmente o con un Manager específico, respectivamente.

```php
<?php

\MongoDB\Driver\Monitoring\addSubscriber( new QueryTimeCollector() );

?>

  
```

## Implementar la lógica

Con el objeto registrado, la única cosa que queda es implementar la lógica en la clase observadora. Para correlacionar los dos eventos que componen una orden ejecutada con éxito (commandStarted y commandSucceeded), cada objeto de evento expone un campo `requestId`.

Para registrar el tiempo promedio por forma de solicitud, se comenzará verificando una orden `find` en el evento commandStarted. Luego, se añadirá un elemento a la propiedad `pendingCommands` indexado por su `requestId` y con su valor representando la forma de solicitud.

Si se recibe un evento commandSucceeded correspondiente con el mismo `requestId`, se añade la duración del evento (desde `durationMicros`) al tiempo total e incrementa el contador de operaciones.

Si se encuentra un evento commandFailed correspondiente, simplemente se elimina la entrada de la propiedad `pendingCommands`.

```php
<?php

class QueryTimeCollector implements \MongoDB\Driver\Monitoring\CommandSubscriber
{
    private $pendingCommands = [];
    private $queryShapeStats = [];

    /* Crear una forma de solicitud a partir del argumento de filtro. Por ahora, solo se consideran
     * los campos de primer nivel */
    private function createQueryShape( array $filter )
    {
        return json_encode( array_keys( $filter ) );
    }

    public function commandStarted( \MongoDB\Driver\Monitoring\CommandStartedEvent $event ): void
    {
        if ( 'find' === $event->getCommandName() )
        {
            $queryShape = $this->createQueryShape( (array) $event->getCommand()->filter );
            $this->pendingCommands[$event->getRequestId()] = $queryShape;
        }
    }

    public function commandSucceeded( \MongoDB\Driver\Monitoring\CommandSucceededEvent $event ): void
    {
        $requestId = $event->getRequestId();
        if ( array_key_exists( $requestId, $this->pendingCommands ) )
        {
            $this->queryShapeStats[$this->pendingCommands[$requestId]]['count']++;
            $this->queryShapeStats[$this->pendingCommands[$requestId]]['duration'] += $event->getDurationMicros();
            unset( $this->pendingCommands[$requestId] );
        }
    }

    public function commandFailed( \MongoDB\Driver\Monitoring\CommandFailedEvent $event ): void
    {
        if ( array_key_exists( $event->getRequestId(), $this->pendingCommands ) )
        {
            unset( $this->pendingCommands[$event->getRequestId()] );
        }
    }

    public function __destruct()
    {
        foreach( $this->queryShapeStats as $shape => $stats )
        {
            echo "Shape: ", $shape, " (", $stats['count'], ")\n  ",
                $stats['duration'] / $stats['count'], "µs\n\n";
        }
    }
}

$m = new \MongoDB\Driver\Manager( 'mongodb://localhost:27016' );

/* Añadir el observador */
\MongoDB\Driver\Monitoring\addSubscriber( new QueryTimeCollector() );

/* Realizar una serie de solicitudes */
$query = new \MongoDB\Driver\Query( [
    'region_slug' => 'scotland-highlands', 'age' => [ '$gte' => 20 ]
] );
$cursor = $m->executeQuery( 'dramio.whisky', $query );

$query = new \MongoDB\Driver\Query( [
    'region_slug' => 'scotland-lowlands', 'age' => [ '$gte' => 15 ]
] );
$cursor = $m->executeQuery( 'dramio.whisky', $query );

$query = new \MongoDB\Driver\Query( [ 'region_slug' => 'scotland-lowlands' ] );
$cursor = $m->executeQuery( 'dramio.whisky', $query );

?>

  
```
