---
title: OpenTelemetry support
description: Analyze telemetry data for builds
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/build/debug/opentelemetry.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: build
order: 2110
---

Both Buildx and BuildKit support [OpenTelemetry](https://opentelemetry.io/).

To capture the trace to [Jaeger](https://github.com/jaegertracing/jaeger),
set `JAEGER_TRACE` environment variable to the collection address using a
`driver-opt`.

First create a Jaeger container:

```console
$ docker run -d --name jaeger -p "6831:6831/udp" -p "16686:16686" --restart unless-stopped jaegertracing/all-in-one
```

Then [create a `docker-container` builder](../builders/drivers/docker-container.md)
that will use the Jaeger instance via the `JAEGER_TRACE` environment variable:

```console
$ docker buildx create --use \
  --name mybuilder \
  --driver docker-container \
  --driver-opt "network=host" \
  --driver-opt "env.JAEGER_TRACE=localhost:6831"
```

Boot and [inspect `mybuilder`](/reference/cli/docker/buildx/inspect/):

```console
$ docker buildx inspect --bootstrap
```

Buildx commands should be traced at `http://127.0.0.1:16686/`:

![OpenTelemetry Buildx Bake](../images/opentelemetry.png)
