---
title: 'Interface: ExtensionHost'
description: Docker extension API reference
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: reference/api/extensions-sdk/ExtensionHost.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: reference
order: 8240
---

**`Since`**

0.2.0

## Properties

### cli

• `Readonly` **cli**: [`ExtensionCli`](extensioncli.md)

Executes a command in the host.

For example, execute the shipped binary `kubectl -h` command in the host:

```typescript
await ddClient.extension.host.cli.exec("kubectl", ["-h"]);
```

---

Streams the output of the command executed in the backend container or in the host.

Provided the `kubectl` binary is shipped as part of your extension, you can spawn the `kubectl -h` command in the host:

```typescript
await ddClient.extension.host.cli.exec("kubectl", ["-h"], {
           stream: {
             onOutput(data): void {
                 // As we can receive both `stdout` and `stderr`, we wrap them in a JSON object
                 JSON.stringify(
                   {
                     stdout: data.stdout,
                     stderr: data.stderr,
                   },
                   null,
                   "  "
                 );
             },
             onError(error: any): void {
               console.error(error);
             },
             onClose(exitCode: number): void {
               console.log("onClose with exit code " + exitCode);
             },
           },
         });
```
