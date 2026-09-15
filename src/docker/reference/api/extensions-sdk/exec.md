---
title: 'Interface: Exec'
description: Docker extension API reference
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: reference/api/extensions-sdk/Exec.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: reference
order: 8160
---

## Callable

### Exec

▸ **Exec**(`cmd`, `args`, `options?`): `Promise`<[`ExecResult`](execresult.md)\>

Executes a command.

**`Since`**

0.2.0

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cmd` | `string` | The command to execute. |
| `args` | `string`[] | The arguments of the command to execute. |
| `options?` | [`ExecOptions`](execoptions.md) | The list of options. |

#### Returns

`Promise`<[`ExecResult`](execresult.md)\>

A promise that will resolve once the command finishes.

### Exec

▸ **Exec**(`cmd`, `args`, `options`): [`ExecProcess`](execprocess.md)

Streams the result of a command if `stream` is specified in the `options` parameter.

Specify the `stream` if the output of your command is too long or if you need to stream things indefinitely (for example container logs).

**`Since`**

0.2.2

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cmd` | `string` | The command to execute. |
| `args` | `string`[] | The arguments of the command to execute. |
| `options` | [`SpawnOptions`](spawnoptions.md) | The list of options. |

#### Returns

[`ExecProcess`](execprocess.md)

The spawned process.
