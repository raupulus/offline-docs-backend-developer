# pnpm vmain — Documentación técnica oficial

> **Espejo Offline de Documentación Técnica**
> Licencia: MIT | Documentos incluidos: 140 | Versión: main
> Descargado/sincronizado: 2026-08-02
> Documentación oficial en línea: https://pnpm.io/motivation
> Mantenedor del espejo: Raúl Caro Pastorino (@raupulus) · https://raupulus.dev

---

## Índice de contenidos


### Cli

- [pnpm access](#pnpm-access)
- [pnpm add <pkg>](#pnpm-add-pkg)
- [pnpm approve-builds](#pnpm-approve-builds)
- [pnpm audit](#pnpm-audit)
- [pnpm bin](#pnpm-bin)
- [pnpm bugs](#pnpm-bugs)
- [pnpm cache delete](#pnpm-cache-delete)
- [pnpm cache list-registries](#pnpm-cache-list-registries)
- [pnpm cache list](#pnpm-cache-list)
- [pnpm cache view](#pnpm-cache-view)
- [pnpm cache](#pnpm-cache)
- [pnpm cat-file](#pnpm-cat-file)
- [pnpm cat-index](#pnpm-cat-index)
- [pnpm change](#pnpm-change)
- [pnpm ci](#pnpm-ci)
- [pnpm clean](#pnpm-clean)
- [pnpm config](#pnpm-config)
- [pnpm create](#pnpm-create)
- [pnpm dedupe](#pnpm-dedupe)
- [pnpm deploy](#pnpm-deploy)
- [pnpm deprecate](#pnpm-deprecate)
- [pnpm dist-tag](#pnpm-dist-tag)
- [pnpm docs](#pnpm-docs)
- [pnpm doctor](#pnpm-doctor)
- [pnpm env <cmd>](#pnpm-env-cmd)
- [pnpm exec](#pnpm-exec)
- [pnpm fetch](#pnpm-fetch)
- [pnpm find-hash](#pnpm-find-hash)
- [pnpm help <command>](#pnpm-help-command)
- [pnpm ignored-builds](#pnpm-ignored-builds)
- [pnpm import](#pnpm-import)
- [pnpm init](#pnpm-init)
- [pnpm install-test](#pnpm-install-test)
- [pnpm install](#pnpm-install)
- [pnpm lane](#pnpm-lane)
- [pnpm licenses](#pnpm-licenses)
- [pnpm link](#pnpm-link)
- [pnpm list](#pnpm-list)
- [pnpm login](#pnpm-login)
- [pnpm logout](#pnpm-logout)
- [pnpm outdated](#pnpm-outdated)
- [pnpm owner](#pnpm-owner)
- [pnpm pack-app](#pnpm-pack-app)
- [pnpm pack](#pnpm-pack)
- [pnpm patch-commit <path>](#pnpm-patch-commit-path)
- [pnpm patch-remove <pkg...>](#pnpm-patch-remove-pkg)
- [pnpm patch <pkg>](#pnpm-patch-pkg)
- [pnpm peers](#pnpm-peers)
- [pnpm ping](#pnpm-ping)
- [pnpm pkg](#pnpm-pkg)
- [pnpm pm](#pnpm-pm)
- [pnx](#pnx)
- [pnpm prefix](#pnpm-prefix)
- [pnpm prune](#pnpm-prune)
- [pnpm publish](#pnpm-publish)
- [pnpm rebuild](#pnpm-rebuild)
- [pnpm -r, --recursive](#pnpm--r---recursive)
- [pnpm remove](#pnpm-remove)
- [pnpm repo](#pnpm-repo)
- [pnpm root](#pnpm-root)
- [pnpm run](#pnpm-run)
- [pnpm runtime <cmd>](#pnpm-runtime-cmd)
- [pnpm sbom](#pnpm-sbom)
- [pnpm search](#pnpm-search)
- [pnpm self-update](#pnpm-self-update)
- [pnpm set-script](#pnpm-set-script)
- [pnpm setup](#pnpm-setup)
- [pnpm stage](#pnpm-stage)
- [pnpm star](#pnpm-star)
- [pnpm start](#pnpm-start)
- [pnpm store](#pnpm-store)
- [pnpm team](#pnpm-team)
- [pnpm test](#pnpm-test)
- [pnpm unlink](#pnpm-unlink)
- [pnpm unpublish](#pnpm-unpublish)
- [pnpm update](#pnpm-update)
- [pnpm version](#pnpm-version)
- [pnpm view](#pnpm-view)
- [pnpm whoami](#pnpm-whoami)
- [pnpm why](#pnpm-why)
- [pnpm with](#pnpm-with)

### Settings

- [Catalogmode](#catalogmode)
- [Cleanupunusedcatalogs](#cleanupunusedcatalogs)
- [Cpuflag](#cpuflag)
- [Enableprepostscripts](#enableprepostscripts)
- [Findby](#findby)
- [Libcflag](#libcflag)
- [Osflag](#osflag)
- [Scriptshell](#scriptshell)
- [Shellemulator](#shellemulator)
- [Build Settings](#build-settings)
- [CLI & Node.js Settings](#cli-node-js-settings)
- [Dependency Resolution Settings](#dependency-resolution-settings)
- [Network & Request Settings](#network-request-settings)
- [Node-Modules & Hoisting Settings](#node-modules-hoisting-settings)
- [Other Settings](#other-settings)
- [Peer Dependency Settings](#peer-dependency-settings)
- [Store & Lockfile Settings](#store-lockfile-settings)
- [Versioning Settings](#versioning-settings)

### Pnpm

- [Aliases](#aliases)
- [Catalogs](#catalogs)
- [Command line tab-completion](#command-line-tab-completion)
- [Config Dependencies](#config-dependencies)
- [Configuring](#configuring)
- [Continuous Integration](#continuous-integration)
- [Working with Docker](#working-with-docker)
- [Error Codes](#error-codes)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Feature Comparison](#feature-comparison)
- [Filtering](#filtering)
- [Finders](#finders)
- [pnpm + Git Worktrees for Multi-Agent Development](#pnpm-git-worktrees-for-multi-agent-development)
- [Working with Git](#working-with-git)
- [Git Branch Lockfiles](#git-branch-lockfiles)
- [Global Packages](#global-packages)
- [Global Virtual Store](#global-virtual-store)
- [How peers are resolved](#how-peers-are-resolved)
- [Installation](#installation)
- [Limitations](#limitations)
- [Logos](#logos)
- [Migrating from v10 to v11](#migrating-from-v10-to-v11)
- [Motivation](#motivation)
- [Authentication Settings](#authentication-settings)
- [Only allow pnpm](#only-allow-pnpm)
- [Supported package sources](#supported-package-sources)
- [package.json](#package-json)
- [pnpm CLI](#pnpm-cli)
- [pnpm vs npm](#pnpm-vs-npm)
- [.pnpmfile.mjs](#pnpmfile-mjs)
- [Working with Podman](#working-with-podman)
- [Production](#production)
- [Scripts](#scripts)
- [Settings (pnpm-workspace.yaml)](#settings-pnpm-workspace-yaml)
- [Mitigating supply chain attacks](#mitigating-supply-chain-attacks)
- [Symlinked nodemodules structure](#symlinked-nodemodules-structure)
- [Working with TypeScript](#working-with-typescript)
- [Uninstalling pnpm](#uninstalling-pnpm)
- [Using Changesets with pnpm](#using-changesets-with-pnpm)
- [Release management](#release-management)
- [Workspace](#workspace)

---



---

# pnpm access

*Sección: Cli*

Added in: v11.11.0

Manages package access and visibility on the registry.

```sh
pnpm access list packages [<user>|<scope>|<scope:team>]
pnpm access list collaborators <package> [<user>]
pnpm access get status <package>
pnpm access set status=public|private <package>
pnpm access set mfa=none|publish|automation <package>
pnpm access grant <read-only|read-write> <scope:team> <package>
pnpm access revoke <scope:team> <package>
```

## Subcommands

### list packages

List the packages a user, scope, or team can access. With no argument, your own packages are listed.

```sh
pnpm access list packages
pnpm access list packages alice
pnpm access list packages @myorg
pnpm access list packages @myorg:developers
```

The argument type is inferred from its shape: a value containing `:` is a team, a value starting with `@` is an organization, and anything else is a user.

`ls` is accepted as an alias, so `pnpm access ls` is equivalent to `pnpm access list packages`.

### list collaborators

List the collaborators on a package, optionally filtered to a single user.

```sh
pnpm access list collaborators @myorg/pkg
pnpm access list collaborators @myorg/pkg alice
```

### get status

Show whether a package is public or restricted.

```sh
pnpm access get status @myorg/pkg
```

### set status

Set the package visibility.

```sh
pnpm access set status=public @myorg/pkg
pnpm access set status=private @myorg/pkg
```

Only scoped packages can change visibility. Unscoped packages are always public, and attempting to change one fails with `ERR_PNPM_ACCESS_SET_STATUS_UNSCOPED`.

### set mfa

Set the two-factor authentication requirement for publishing a package.

```sh
pnpm access set mfa=none @myorg/pkg
pnpm access set mfa=publish @myorg/pkg
pnpm access set mfa=automation @myorg/pkg
```

`none` disables the requirement, while `publish` and `automation` both require two-factor authentication for publishing.

### grant

Grant a team read-only or read-write access to a package.

```sh
pnpm access grant read-only @myorg:developers @myorg/pkg
pnpm access grant read-write @myorg:developers @myorg/pkg
```

### revoke

Revoke a team's access to a package.

```sh
pnpm access revoke @myorg:developers @myorg/pkg
```

## Options

### --registry &lt;url\&gt;

The base URL of the npm registry to use for the operation. Per-scope and named registries (configured via [`registries`](../settings/dependency-resolution.md#registries) and [`namedRegistries`](../settings/dependency-resolution.md#namedregistries)) are respected for the package being modified.

### --json

Output results in JSON format. Applies to `list packages`, `list collaborators`, and `get status`.

### --otp &lt;code\&gt;

When the registry requires two-factor authentication, this option supplies a one-time password. It applies to the subcommands that modify state: `set status`, `set mfa`, `grant`, and `revoke`.


---

# pnpm add <pkg>

*Sección: Cli*

Installs a package and any packages that it depends on.
By default, any new package is installed as a production dependency.

## TL;DR

| Command                                | Meaning                            |
|----------------------------------------|------------------------------------|
| `pnpm add sax`                         | Save to `dependencies`             |
| `pnpm add -D sax`                      | Save to `devDependencies`          |
| `pnpm add -O sax`                      | Save to `optionalDependencies`     |
| `pnpm add -g sax `                     | Install package globally           |
| `pnpm add sax@next`                    | Install from the `next` tag        |
| `pnpm add sax@3.0.0`                   | Specify version `3.0.0`            |

## Supported package sources

pnpm supports installing packages from various sources. See the [Supported package sources](../package-sources.md) page for detailed documentation on:

- npm registry
- JSR registry
- Workspace packages
- Local file system (tarballs and directories)
- Remote tarballs
- Git repositories (with semver, subdirectories, and more)

## Options

### --save-prod, -P, -p

Install the specified packages as regular `dependencies`.

### --save-dev, -D, -d

Install the specified packages as `devDependencies`.

### --save-optional, -O, -o

Install the specified packages as `optionalDependencies`.

### --save-exact, -E, -e

Saved dependencies will be configured with an exact version rather than using
pnpm's default semver range operator.

### --save-peer

Using `--save-peer` will add one or more packages to `peerDependencies` and
install them as dev dependencies.

### --save-catalog

Added in: v10.12.1

Save the new dependency to the default [catalog].

### --save-catalog-name &lt;catalog_name\>

Added in: v10.12.1

Save the new dependency to the specified [catalog].

[catalog]: ../catalogs.md

### --config

Added in: v10.8.0

Save the dependency to [configDependencies](../config-dependencies.md).

### --ignore-workspace-root-check

Adding a new dependency to the root workspace package fails, unless the
`--ignore-workspace-root-check` or `-w` flag is used.

For instance, `pnpm add debug -w`.

### --global, -g

Install a package globally. See [Global Packages](../global-packages.md) for details.

Each space-separated package is installed into its own isolated directory. To bundle several packages into a single isolated install (so they share dependencies and are removed together), pass them as a comma-separated list, e.g. `pnpm add -g eslint,prettier`.

### --workspace

Only adds the new dependency if it is found in the workspace.

### --allow-build

Added in: v10.4.0

A list of package names that are allowed to run postinstall scripts during installation.

Example:

```
pnpm --allow-build=esbuild add my-bundler
```

This will run `esbuild`'s postinstall script and also add it to the `allowBuilds` field of `pnpm-workspace.yaml`. So, `esbuild` will always be allowed to run its scripts in the future.

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)


---

# pnpm approve-builds

*Sección: Cli*

Added in: v10.1.0

Approve dependencies for running scripts during installation.

The approved dependencies are added to the [`allowBuilds`] map in `pnpm-workspace.yaml` with a value of `true`, while unapproved ones are saved with a value of `false`. You can also update these settings manually if you prefer.

[`allowBuilds`]: ../settings/build.md#allowbuilds

## Usage

You can run `pnpm approve-builds` without arguments to get an interactive prompt, or pass package names as positional arguments:

```sh
pnpm approve-builds esbuild fsevents !core-js
```

Prefix a package name with `!` to deny it. Only mentioned packages are affected; the rest are left untouched.

During install, packages with ignored builds that are not yet listed in `allowBuilds` are automatically added to `pnpm-workspace.yaml` with a placeholder value, so you can manually set them to `true` or `false`.

## Options

### --all

Added in: v10.32.0

Approve all pending builds without interactive prompts.

### ~~--global, -g~~

:::warning Removed in v11.0.0

`pnpm approve-builds -g` is no longer supported with isolated global packages. Instead, use `--allow-build` when installing globally (e.g., `pnpm add -g --allow-build=esbuild esbuild`), or approve builds via the interactive prompt that pnpm shows during global install.

:::


---

# pnpm audit

*Sección: Cli*

Checks for known security issues with the installed packages.

If security issues are found, try to update your dependencies via `pnpm update`.
If a simple update does not fix all the issues, use [overrides] to force
versions that are not vulnerable. For instance, if `lodash@<2.1.0` is vulnerable,
use this overrides to force `lodash@^2.1.0`:

```yaml title="pnpm-workspace.yaml"
overrides:
  "lodash@<2.1.0": "^2.1.0"
```

Or alternatively, run `pnpm audit --fix`.

If you want to tolerate some vulnerabilities as they don't affect your project, you may use the [`audit.ignore`] setting.

Since v11, `pnpm audit` queries the registry's `/-/npm/v1/security/advisories/bulk` endpoint. The response does not include CVE identifiers, so advisories are filtered by GitHub advisory ID (GHSA) instead. If you previously listed CVEs under `auditConfig.ignoreCves`, replace each entry with the corresponding `GHSA-xxxx-xxxx-xxxx` value (shown in the `More info` column of `pnpm audit` output) under [`audit.ignore`].

[overrides]: ../settings/dependency-resolution.md#overrides
[`audit.ignore`]: #auditignore

## Commands

### signatures

Added in: v11.1.0

```sh
pnpm audit signatures
```

Verifies the ECDSA registry signatures of installed packages against the public keys published by each registry at `/-/npm/v1/keys`. Scoped registries configured via [`registries`](../settings/dependency-resolution.md#registries) are respected; registries that don't publish signing keys are skipped.

The command exits with code `1` if any package has an invalid signature, or if a registry advertises signing keys but a package was published without a signature. Combine with `--json` to get machine-readable output.

## Options

### --audit-level &lt;severity\>

* Type: **low**, **moderate**, **high**, **critical**
* Default: **low**

Only print advisories with severity greater than or equal to `<severity>`.

This can also be set via [`audit.level`](#auditlevel) in `pnpm-workspace.yaml`.

### --fix

Add overrides to the `pnpm-workspace.yaml` file in order to force non-vulnerable versions of the dependencies.

Use `--fix=update` (added in v11.0.0) to fix vulnerabilities by updating packages in the lockfile instead of adding overrides.

When [`minimumReleaseAge`](../settings/dependency-resolution.md#minimumreleaseage) is set, `--fix` also adds the minimum patched version of each advisory to [`minimumReleaseAgeExclude`](../settings/dependency-resolution.md#minimumreleaseageexclude) in `pnpm-workspace.yaml`, so the security fix can be installed without waiting for the release age window.

### --interactive, -i

Added in: v11.0.0

Review the advisories selected by `--fix` and pick which ones to apply. Only usable together with `--fix`.

### --json

Output audit report in JSON format.

### --dev, -D

Only audit dev dependencies.

### --prod, -P

Only audit production dependencies.

### --no-optional

Don't audit `optionalDependencies`.

### --ignore-registry-errors

If the registry responds with a non-200 status code, the process should exit with 0.
So the process will fail only if the registry actually successfully responds with found vulnerabilities.

### --ignore-unfixable

Added in: v10.11.0

Ignore all advisories with no resolution.

Since v11, unfixable advisories are tracked by GHSA rather than CVE.

### --ignore &lt;vulnerability\>

Added in: v10.11.0

Ignore a vulnerability by its GitHub advisory ID (GHSA). Before v11 this flag accepted CVE identifiers.

## Configuration

`pnpm audit` is configured in the `audit` section of `pnpm-workspace.yaml` (added in v11.16.0):

```yaml
audit:
  level: high
  ignore:
    - GHSA-42xw-2xvc-qx8m
```

### audit.level

* Default: **low**
* Type: **low**, **moderate**, **high**, **critical**

Only print advisories with severity greater than or equal to this level. Same as the [`--audit-level`](#--audit-level-severity) flag.

### audit.ignore

A list of GHSA codes that will be ignored by the `pnpm audit` command.

```yaml
audit:
  ignore:
    - GHSA-42xw-2xvc-qx8m
    - GHSA-4w2v-q235-vp99
    - GHSA-cph5-m8f7-6c5x
    - GHSA-vh95-rmgr-6w4m
```

:::info

Before v11.16.0, these settings were named `auditLevel` and `auditConfig.ignoreGhsas`. The deprecated names keep working until the next major version; when both are set, the `audit` section takes precedence and a warning is printed.

Before v11, `auditConfig.ignoreCves` was used to filter advisories by CVE identifier. That setting is no longer recognized.

:::


---

# pnpm bin

*Sección: Cli*

Prints the directory into which the executables of dependencies are linked.

## Options

### --global, -g

Prints the location of the globally installed executables.


---

# pnpm bugs

*Sección: Cli*

Added in: v11.1.0

Opens a package's bug tracker URL in the browser.

```sh
pnpm bugs [<pkg> ...]
```

## Aliases

`pnpm issues` (added in v11.10.0) is an alias of `pnpm bugs`.

When run without arguments inside a package directory, it opens the bug tracker for the current project (using the `bugs` field from `package.json`).

When one or more package names are passed, pnpm fetches each package's metadata from the registry and opens its bug tracker.

If a package does not declare a `bugs` field, pnpm falls back to `<repository>/issues` derived from the `repository` field.

## Examples

Open the bug tracker for a published package:

```sh
pnpm bugs lodash
```

Open the bug tracker for multiple packages at once:

```sh
pnpm bugs react react-dom
```

Open the bug tracker for the current project:

```sh
pnpm bugs
```


---

# pnpm cache delete

*Sección: Cli*

:::warning

This command is experimental

:::

Deletes metadata cache for the specified package(s). Supports patterns.


---

# pnpm cache list-registries

*Sección: Cli*

:::warning

This command is experimental

:::

Lists all registries that have their metadata cache locally.


---

# pnpm cache list

*Sección: Cli*

:::warning

This command is experimental

:::

Lists the available packages metadata cache. Supports filtering by glob.


---

# pnpm cache view

*Sección: Cli*

:::warning

This command is experimental

:::

Views information from the specified package's cache.


---

# pnpm cache

*Sección: Cli*

Commands:
* [cache list](cache-list.md)
* [cache list-registries](cache-list-registries.md)
* [cache delete](cache-delete.md)
* [cache view](cache-view.md)


---

# pnpm cat-file

*Sección: Cli*

Prints the contents of a file based on the hash value stored in the index file. For example:

```
pnpm cat-file sha512-mvavhfVcEREI7d8dfvfvIkuBLnx7+rrkHHnPi8mpEDUlNpY4CUY+CvJ5mrrLl18iQYo1odFwBV7z/cOypG7xxQ==
```


---

# pnpm cat-index

*Sección: Cli*

Prints the index file of a specific package from the store. The package is specified by its name and version:

```
pnpm cat-index <pkg name>@<pkg version>
```


---

# pnpm change

*Sección: Cli*

Added in: v11.13.0

Records a change intent: which packages a change affects, the bump type for each, and a summary that becomes the changelog entry. The intent file is written to `.changeset/` in the [changesets](https://github.com/changesets/changesets) format.

```sh
pnpm change [--bump <type>] [--summary <text>] [<pkg>...]
pnpm change status
```

Change intents are consumed later by [`pnpm version -r`](version.md#recursive-releases). See [Release management](../versioning.md) for the whole workflow.

## Usage

Run without arguments to record an intent interactively:

```sh
pnpm change
```

You are asked three questions:

1. **Which packages does this change affect?** Packages changed since the merge base with `main` (or `master`) are preselected.
2. **Which packages should have a major bump?**, then the same for `minor`. Anything left over is bumped as `patch`.
3. **Summary of the change**, which becomes the changelog entry.

The result is a file such as `.changeset/calm-cats-resolve.md`:

```markdown
---
"@example/core": minor
"@example/cli": patch
---

Added a `--watch` flag to the build command.
```

Commit this file along with your change.

Passing package names together with `--bump` and `--summary` records an intent without prompting, which is useful in scripts:

```sh
pnpm change --bump patch --summary "Fixed a crash on empty input" @example/core
```

## Subcommands

### status

Show the pending change intents and the release plan they produce.

```sh
pnpm change status
```

```
Pending change intents:
  .changeset/calm-cats-resolve.md

Release plan:
  @example/core: 1.2.0 → 1.3.0 (minor, via intent)
  @example/cli: 0.4.1 → 0.4.2 (patch, via intent+dependencies)
```

The cause of each bump is one of `intent` (a change intent named the package), `dependencies` (a dependent was pulled in by propagation), `fixed` (a [fixed group](../versioning.md#fixed-groups) companion), or `epic` (an [epic](../versioning.md#epics) re-base).

## Options

### --bump &lt;type\&gt;

The bump type for the named packages: `none`, `patch`, `minor`, or `major`. `none` records an explicit decline — the change needs no release.

### --summary &lt;text\&gt;

The summary for the changelog entry. Together with package names, this runs the command non-interactively.

## Referencing packages by directory

When two workspace projects publish the same name, a package can be referenced by its workspace-relative directory instead, with a `./` prefix:

```markdown
---
"./packages/cli": minor
---
```

This is the one additive extension pnpm makes to the changesets format. `pnpm change` writes it automatically when a name is ambiguous.


---

# pnpm ci

*Sección: Cli*

Added in: v11.0.0

Aliases: `clean-install`, `ic`, `install-clean`

Perform a clean install. This command runs [`pnpm clean`](clean.md) followed by [`pnpm install --frozen-lockfile`](install.md).

Designed for CI/CD environments where reproducible builds are critical.

```sh
pnpm ci
```


---

# pnpm clean

*Sección: Cli*

Aliases: `purge`

Safely remove `node_modules` contents from all workspace projects. Uses Node.js to remove directories, which correctly handles NTFS junctions on Windows without following them into their targets.

In a workspace, `node_modules` directories are cleaned in the root and every workspace package. Non-pnpm hidden entries (e.g., `.cache`) inside `node_modules` are preserved.

If a custom [`virtualStoreDir`](../settings/node-modules.md#virtualstoredir) is configured and it resides inside the project root (but outside `node_modules`), it is also removed.

## Options

### --lockfile, -l

Also remove `pnpm-lock.yaml` files.


---

# pnpm config

*Sección: Cli*

Aliases: `c`

Manage the configuration files.

pnpm settings are split across two kinds of configuration files:

* **Registry and authentication settings** live in INI files — the global `rc` file and local `.npmrc` files.
* **All other pnpm settings** live in YAML files — the global `config.yaml` and the per-project `pnpm-workspace.yaml`.

The local workspace configuration file is located at the root of the project and is named `pnpm-workspace.yaml`. The global YAML configuration file (`config.yaml`) is located at:

* If the **$XDG_CONFIG_HOME** env variable is set, then **$XDG_CONFIG_HOME/pnpm/config.yaml**
* On Windows: **~/AppData/Local/pnpm/config/config.yaml**
* On macOS: **~/Library/Preferences/pnpm/config.yaml**
* On Linux: **~/.config/pnpm/config.yaml**

The global `rc` file (registry/auth settings only) is at:

* If the **$XDG_CONFIG_HOME** env variable is set, then **$XDG_CONFIG_HOME/pnpm/rc**
* On Windows: **~/AppData/Local/pnpm/config/rc**
* On macOS: **~/Library/Preferences/pnpm/rc**
* On Linux: **~/.config/pnpm/rc**

You can also retrieve the path to your global config file by running (added in v10.21.0):

```sh
pnpm config get globalconfig
```

## Commands

### set &lt;key> &lt;value>

Set the config key to the value provided.

Without the `--json` flag, it parses the value as plain string:

```sh
pnpm config set --location=project nodeVersion 22.0.0
```

With the `--json` flag, it parses the value as JSON:

```sh
pnpm config set --location=project --json nodeVersion '"22.0.0"'
```

The `--json` flag also allows `pnpm config set` to create arrays and objects:

```sh
pnpm config set --location=project --json allowBuilds '{"react": true, "react-dom": true}'
pnpm config set --location=project --json catalog '{ "react": "19" }'
```

The `set` command does not accept a property path.

### get &lt;key>

Print the config value for the provided key.

The `key` can be a simple key:

```sh
pnpm config get nodeVersion
pnpm config get --json nodeVersion
pnpm config get --json packageExtensions
pnpm config get --json allowBuilds
pnpm config get --json catalog
```

It can also be a property path:

```sh
pnpm config get 'packageExtensions["@babel/parser"].peerDependencies["@babel/types"]'
pnpm config get --json 'packageExtensions["@babel/parser"].peerDependencies["@babel/types"]'
pnpm config get 'allowBuilds.react'
pnpm config get --json 'allowBuilds.react'
pnpm config get catalog.react
pnpm config get --json catalog.react
```

The syntax of the property path emulates JavaScript property paths.

### delete &lt;key>

Remove the config key from the config file.

### list

Show all the config settings. Output is a JSON object.

Auth-related settings are hidden from the output; use `pnpm config get <key>` to read them explicitly.

:::note

Since v11, `pnpm config get` (without `--json`) no longer prints INI-formatted text. It prints JSON for objects and arrays, and raw strings for strings, numbers, booleans, and nulls. `pnpm config get --json` prints all values as JSON. `pnpm config list` always prints a JSON object.

:::

## Options

### --global, -g

Set the configuration in the global config file.

### --location

By default, `--location` is set to `global`.

When set to `project`, pnpm writes the setting to `pnpm-workspace.yaml` at the workspace root (or, for registry/auth settings, to the `.npmrc` in the workspace root).

When set to `global`, the behavior is the same as passing the `--global` option.

### --json

Make `get` and `list` show all the config settings in JSON format and make `set` parse the value as JSON.


---

# pnpm create

*Sección: Cli*

Create a project from a `create-*` or `@foo/create-*` starter kit.

## Examples

```
pnpm create react-app my-app
```

## Options

### --allow-build

Added in: v10.2.0

A list of package names that are allowed to run postinstall scripts during installation.

## Security and trust policies

Since v11.0.0, `pnpm create` honors the project-level security and trust policy settings — [`minimumReleaseAge`](../settings/dependency-resolution.md#minimumreleaseage) (and its `Exclude`/`Strict` companions) and [`trustPolicy`](../settings/dependency-resolution.md#trustpolicy) (and its `Exclude`/`IgnoreAfter` companions) — when resolving and fetching the starter kit.


---

# pnpm dedupe

*Sección: Cli*

Perform an install removing older dependencies in the lockfile if a newer version can be used.

## Options

### `--check`

Check if running dedupe would result in changes without installing packages or editing the lockfile. Exits with a non-zero status code if changes are possible.


---

# pnpm deploy

*Sección: Cli*

Deploy a package from a workspace. During deployment, the files of the deployed package are copied to the target directory. All dependencies of the deployed package, including dependencies from the workspace, are installed inside an isolated `node_modules` directory at the target directory. The target directory will contain a portable package that can be copied to a server and executed without additional steps.

:::note

By default, the deploy command only works with workspaces that have the `inject-workspace-packages` setting set to `true`. If you want to use deploy without "injected dependencies", use the `--legacy` flag or set `force-legacy-deploy` to `true`.

:::

:::note

When the [`enableGlobalVirtualStore`](../settings/node-modules.md#enableglobalvirtualstore) option is set, `pnpm deploy` ignores it and always creates a localized virtual store within the deploy directory. This keeps the deploy directory self-contained and portable.

:::

Usage:

```
pnpm --filter=<deployed project name> deploy <target directory>
```

In case you build your project before deployment, also use the `--prod` option to skip `devDependencies` installation.

```
pnpm --filter=<deployed project name> --prod deploy <target directory>
```

Usage in a docker image. After building everything in your monorepo, do this in a second image that uses your monorepo base image as a build context or in an additional build stage:

```Dockerfile
# syntax=docker/dockerfile:1.4

FROM workspace as pruned
RUN pnpm --filter <your package name> --prod deploy pruned

FROM node:18-alpine
WORKDIR /app

ENV NODE_ENV=production

COPY --from=pruned /app/pruned .

ENTRYPOINT ["node", "index.js"]
```

## Options

### --dev, -D

Only `devDependencies` are installed.

### --no-optional

`optionalDependencies` are not installed.

### --prod, -P

Packages in `devDependencies` won't be installed.

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)

### --legacy

Force legacy deploy implementation.

By default, `pnpm deploy` will try creating a dedicated lockfile from a shared lockfile for deployment. The `--legacy` flag disables this behavior and also allows using the deploy command without the `inject-workspace-packages=true` setting.

## Files included in the deployed project

By default, all the files of the project are copied during deployment but this can be modified in _one_ of the following ways which are resolved in order:

1. The project's `package.json` may contain a "files" field to list the files and directories that should be copied.
2. If there is an `.npmignore` file in the application directory then any files listed here are ignored.
3. If there is a `.gitignore` file in the application directory then any files listed here are ignored.

## Configuration

### forceLegacyDeploy

* Default: **false**
* Type: **Boolean**

By default, `pnpm deploy` will try creating a dedicated lockfile from a shared lockfile for deployment. If this setting is set to `true`, the legacy `deploy` behavior will be used.


---

# pnpm deprecate

*Sección: Cli*

Added in: v11.0.0

Set a deprecation message on a published package version. Consumers running `pnpm install` will see this message when the matching version is installed.

```sh
pnpm deprecate <pkg>[@<version-range>] <message>
```

To clear a deprecation message, use [`pnpm undeprecate`](#pnpm-undeprecate) or pass an empty string:

```sh
pnpm deprecate foo@1.0.0 ""
```

## Examples

Deprecate a single version:

```sh
pnpm deprecate foo@1.0.0 "Use foo@2 instead"
```

Deprecate a range of versions:

```sh
pnpm deprecate "foo@<2" "Please upgrade to foo@2"
```

Deprecate all versions:

```sh
pnpm deprecate foo "This package is no longer maintained"
```

## Options

### --registry &lt;url\>

The registry to publish to. Defaults to the registry configured for the package.

### --otp &lt;code\>

When the registry requires two-factor authentication, supply the one-time password via this flag or the `PNPM_CONFIG_OTP` environment variable.

## pnpm undeprecate

Remove a deprecation message from a package version. Equivalent to running `pnpm deprecate <pkg>[@<version-range>] ""`.

```sh
pnpm undeprecate <pkg>[@<version-range>]
```


---

# pnpm dist-tag

*Sección: Cli*

Added in: v11.0.0

Manage distribution tags for a package. Dist-tags provide human-readable aliases (like `latest`, `next`, `beta`) that point to specific package versions on the registry.

```sh
pnpm dist-tag add <pkg>@<version> [<tag>]
pnpm dist-tag rm <pkg> <tag>
pnpm dist-tag ls [<pkg>]
```

## Subcommands

### add &lt;pkg\>@&lt;version\> [&lt;tag\>]

Tag the specified version of a package with a dist-tag. If `<tag>` is omitted, the value of the [`tag`](../settings/other.md#tag) setting is used (defaults to `latest`).

```sh
pnpm dist-tag add foo@1.2.0 next
```

### rm &lt;pkg\> &lt;tag\>

Remove a dist-tag from a package.

```sh
pnpm dist-tag rm foo next
```

### ls [&lt;pkg\>]

List all dist-tags for a package. If no package name is given, the dist-tags for the current package (read from the local `package.json`) are shown.

```sh
pnpm dist-tag ls foo
```

## Options

### --registry &lt;url\>

The registry to operate on. Defaults to the registry configured for the package.

### --otp &lt;code\>

When the registry requires two-factor authentication, supply the one-time password via this flag or the `PNPM_CONFIG_OTP` environment variable.


---

# pnpm docs

*Sección: Cli*

Added in: v11.0.0

Aliases: `home`

Open a package's documentation (or homepage) in the browser.

```sh
pnpm docs [<pkg> ...]
```

When run without arguments inside a package directory, it opens the documentation for the current project.

If the package does not declare a valid `homepage`, pnpm falls back to `https://npmx.dev/package/<name>`.

## Examples

Open the documentation for a published package:

```sh
pnpm docs lodash
```

Open the documentation for multiple packages at once:

```sh
pnpm docs react react-dom
```

Open the documentation for the current project:

```sh
pnpm docs
```


---

# pnpm doctor

*Sección: Cli*

Added in: v11.14.0

Runs diagnostics on the pnpm installation and the environment it runs in.

```sh
pnpm doctor [--offline] [--benchmark] [--json]
```

Each check reports how to fix what it finds, and the command exits with a non-zero code when any check fails. Warnings do not fail the command.

```
✓ Versions: pnpm 11.14.0, Node.js 22.20.0
✓ Install method: pnpm
✓ Global bin directory: /Users/example/Library/pnpm/bin
✓ Cache directory: /Users/example/Library/Caches/pnpm
✓ Store directory: /Users/example/Library/pnpm/store/v10
✓ Filesystem: available: reflink, hardlink, symlink
✓ Registry connectivity: https://registry.npmjs.org/ (128ms)
✓ Install smoke test: offline "file:" install linked its dependency

All checks passed
```

## Checks

### Versions

Reports the running pnpm and Node.js versions.

### Install method

Reports how pnpm was installed — as the `pnpm` package or the `@pnpm/exe` standalone build — and warns when pnpm is being run by Corepack, which manages the pnpm version itself and makes `pnpm self-update` unavailable.

### Global bin directory

Checks that the directory pnpm links global executables into is on `PATH` and writable. If it is missing from `PATH`, the fix is to run [`pnpm setup`](setup.md).

### Cache directory

Checks that the [cache directory](../settings/other.md#cachedir) is writable.

### Store directory

Checks that the [store directory](../settings/store.md#storedir) is writable. Skipped when no store directory is configured.

### Filesystem

Probes which link strategies work from the store's volume: reflink (copy-on-write), hardlink, and symlink. This is what determines how packages land in `node_modules` and how fast an install is — a reflink or hardlink is near-free, a plain copy is not.

If neither reflink nor hardlink works, the check warns that installs will fall back to copying, and suggests putting the store on the same filesystem as your projects.

### Registry connectivity

Pings the configured registry with a 15-second timeout and reports the round-trip time. Fails if the registry cannot be reached or answers with an error status, which usually points at network, proxy, or auth configuration.

Skipped with `--offline`.

### Install smoke test

Installs a throwaway package as a `file:` dependency, entirely offline, in a temporary directory. This exercises the resolve, store, and link path end to end and confirms the running binary can actually perform an install.

This check is always offline by construction, so `--offline` does not skip it.

## Options

### --offline

Skip the checks that need network access.

### --benchmark

Also time the filesystem and install checks, reporting the duration alongside each result.

### --json

Report the results as JSON. The output is an object with a single `checks` array, each entry having `title`, `status` (`pass`, `warn`, or `fail`), and optionally `detail`, `fix`, and `durationMs`.

```json
{
  "checks": [
    {
      "title": "Filesystem",
      "status": "pass",
      "detail": "available: reflink, hardlink, symlink",
      "durationMs": 3
    }
  ]
}
```


---

# pnpm env <cmd>

*Sección: Cli*

:::warning Deprecated

`pnpm env` is deprecated. Use [`pnpm runtime`](runtime.md) instead. For example, `pnpm env use --global lts` becomes `pnpm runtime set node lts -g`.

:::

Manages the Node.js environment.

:::danger

`pnpm env` does not include the binaries for Corepack. If you want to use Corepack to install other package managers, you need to install it separately (e.g. `pnpm add -g corepack`).

:::

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/84-MzN_0Cng" title="The pnpm patch command demo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen"></iframe>

## Commands

### use

Install and use the specified version of Node.js

Install the LTS version of Node.js:

```
pnpm env use --global lts
```

Install Node.js v16:

```
pnpm env use --global 16
```

Install a prerelease version of Node.js:

```
pnpm env use --global nightly
pnpm env use --global rc
pnpm env use --global 16.0.0-rc.0
pnpm env use --global rc/14
```

Install the latest version of Node.js:

```
pnpm env use --global latest
```

Install an LTS version of Node.js using its [codename]:

```
pnpm env use --global argon
```

[codename]: https://github.com/nodejs/Release/blob/main/CODENAMES.md

### add

Installs the specified version(s) of Node.js without activating them as the current version.

Example:

```
pnpm env add --global lts 18 20.0.1
```

### remove, rm

Removes the specified version(s) of Node.js.

Usage example:

```
pnpm env remove --global 14.0.0
pnpm env remove --global 14.0.0 16.2.3
```

### list, ls

List Node.js versions available locally or remotely.

Print locally installed versions:

```
pnpm env list
```

Print remotely available Node.js versions:

```
pnpm env list --remote
```

Print remotely available Node.js v16 versions:

```
pnpm env list --remote 16
```

## Options

### --global, -g

The changes are made systemwide.


---

# pnpm exec

*Sección: Cli*

Execute a shell command in scope of a project.

`node_modules/.bin` is added to the `PATH`, so `pnpm exec` allows executing commands of dependencies.

## Examples

If you have Jest as a dependency of your project, there is no need to install Jest globally, just run it with `pnpm exec`:

```
pnpm exec jest
```

The `exec` part is actually optional when the command is not in conflict with a builtin pnpm command, so you may also just run:

```
pnpm jest
```

## Options

Any options for the `exec` command should be listed before the `exec` keyword.
Options listed after the `exec` keyword are passed to the executed command.

Good. pnpm will run recursively:

```
pnpm -r exec jest
```

Bad, pnpm will not run recursively but `jest` will be executed with the `-r` option:

```
pnpm exec jest -r
```

### --recursive, -r

Execute the shell command in every project of the workspace.

The name of the current package is available through the environment variable
`PNPM_PACKAGE_NAME`.

#### Examples

Prune `node_modules` installations for all packages:

```
pnpm -r exec rm -rf node_modules
```

View package information for all packages. This should be used with the `--shell-mode` (or `-c`) option for the environment variable to work.

```
pnpm -rc exec pnpm view \$PNPM_PACKAGE_NAME
```

### --no-reporter-hide-prefix

Do not hide prefix when running commands in parallel.

### --resume-from &lt;package_name\>

Resume execution from a particular project. This can be useful if you are working with a large workspace and you want to restart a build at a particular project without running through all of the projects that precede it in the build order.

### --parallel

Completely disregard concurrency and topological sorting, running a given script
immediately in all matching packages. This is the
preferred flag for long-running processes over many packages, for instance, a
lengthy build process.

### --shell-mode, -c

Runs the command inside of a shell. Uses `/bin/sh` on UNIX and `\cmd.exe` on Windows.

### --report-summary

[Read about this option in the run command docs](run.md#--report-summary)

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)


---

# pnpm fetch

*Sección: Cli*

Fetch packages from a lockfile into virtual store, package manifest is ignored.

## Usage scenario

This command is specifically designed to improve building a docker image.

You may have read the [official guide] to writing a Dockerfile for a Node.js
app, if you haven't read it yet, you may want to read it first.

From that guide, we learn to write an optimized Dockerfile for projects using
pnpm, which looks like

```Dockerfile
FROM node:20

WORKDIR /path/to/somewhere

RUN corepack enable pnpm && corepack install -g pnpm@latest-11

# Files required by pnpm install
COPY .npmrc package.json pnpm-lock.yaml pnpm-workspace.yaml .pnpmfile.mjs ./

# If you patched any package, include patches before install too
COPY patches patches

RUN pnpm install --frozen-lockfile --prod

# Bundle app source
COPY . .

EXPOSE 8080
CMD [ "node", "server.js" ]
```

As long as there are no changes to `.npmrc`, `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`,
`.pnpmfile.mjs`, docker build cache is still valid up to the layer of
`RUN pnpm install --frozen-lockfile --prod`, which cost most of the time
when building a docker image.

However, modification to `package.json` may happen much more frequently than
we expect, because it does not only contain dependencies, but may also
contain the version number, scripts, and arbitrary configuration for any other
tool.

It's also hard to maintain a Dockerfile that builds a monorepo project, it may
look like

```Dockerfile
FROM node:20

WORKDIR /path/to/somewhere

RUN corepack enable pnpm && corepack install -g pnpm@latest-11

# Files required by pnpm install
COPY .npmrc package.json pnpm-lock.yaml pnpm-workspace.yaml .pnpmfile.mjs ./

# If you patched any package, include patches before install too
COPY patches patches

# for each sub-package, we have to add one extra step to copy its manifest
# to the right place, as docker have no way to filter out only package.json with
# single instruction
COPY packages/foo/package.json packages/foo/
COPY packages/bar/package.json packages/bar/

RUN pnpm install --frozen-lockfile --prod

# Bundle app source
COPY . .

EXPOSE 8080
CMD [ "node", "server.js" ]

```
As you can see, the Dockerfile has to be updated when you add or remove
sub-packages.

`pnpm fetch` solves the above problem perfectly by providing the ability
to load packages into the virtual store using only information from a lockfile and a configuration file (`pnpm-workspace.yaml`).

```Dockerfile
FROM node:20

WORKDIR /path/to/somewhere

RUN corepack enable pnpm && corepack install -g pnpm@latest-11

# pnpm fetch does require only lockfile
COPY pnpm-lock.yaml pnpm-workspace.yaml ./

# If you patched any package, include patches before running pnpm fetch
COPY patches patches

RUN pnpm fetch --prod

COPY . ./
RUN pnpm install -r --offline --prod

EXPOSE 8080
CMD [ "node", "server.js" ]
```

It works for both simple and monorepo projects, `--offline` enforces
pnpm not to communicate with the package registry as all needed packages are
already present in the virtual store.

As long as the lockfile is not changed, the build cache is valid up to the
layer, so `RUN pnpm install -r --offline --prod`, will save you much
time.

:::note

Local `file:` protocol dependencies are skipped during `pnpm fetch`, since they reference directories that may not be available at fetch time (e.g. in Docker builds).

:::

## Options

### --dev, -D

Only development packages will be fetched

### --prod, -P

Development packages will not be fetched

[official guide]: https://github.com/nodejs/docker-node#readme


---

# pnpm find-hash

*Sección: Cli*

:::warning

This command is experimental

:::

Lists the packages that include the file with the specified hash. For example:

```
pnpm find-hash sha512-mvavhfVcEREI7d8dfvfvIkuBLnx7+rrkHHnPi8mpEDUlNpY4CUY+CvJ5mrrLl18iQYo1odFwBV7z/cOypG7xxQ==
```


---

# pnpm help <command>

*Sección: Cli*

Display help information about pnpm.

## Options

### --all, -a

Added in: v10.20.0

Print all the available commands.


---

# pnpm ignored-builds

*Sección: Cli*

Added in: v10.1.0

Print the list of packages with blocked build scripts.


---

# pnpm import

*Sección: Cli*

`pnpm import` generates a `pnpm-lock.yaml` from another package manager's lockfile. Supported source files:
* `package-lock.json`
* `npm-shrinkwrap.json`
* `yarn.lock`

Note that if you have workspaces you wish to import dependencies for, they will need to be declared in a [pnpm-workspace.yaml](../settings.md) file beforehand.


---

# pnpm init

*Sección: Cli*

Create a `package.json` file.

## Options

### --bare

Added in: v10.25.0

Creates a `package.json` with only the required fields.

### --init-type &lt;type\>

* Default: **module**
* Type: **commonjs**, **module**

Set the module system for the package.

### --init-package-manager

Pin the project to the current pnpm version.

Since v11, the pin is written as a [`devEngines.packageManager`](../package-json.md#devenginespackagemanager) entry (instead of the legacy `packageManager` field), so version ranges are supported and the resolved version is captured in `pnpm-lock.yaml`.

Inside a workspace subpackage this flag has no effect — the `devEngines.packageManager` field is only added to the workspace root's `package.json`.


---

# pnpm install-test

*Sección: Cli*

Aliases: `it`

Runs `pnpm install` followed immediately by `pnpm test`. It takes exactly the
same arguments as [`pnpm install`](install.md).


---

# pnpm install

*Sección: Cli*

Aliases: `i`

`pnpm install` is used to install all dependencies for a project.

In a CI environment, installation fails if a lockfile is present but needs an
update.

Inside a [workspace], `pnpm install` installs all dependencies in all the
projects. If you want to disable this behavior, set the `recursive-install`
setting to `false`.

![](/img/demos/pnpm-install.svg)

[workspace]: ../workspaces.md

## TL;DR

| Command                           | Meaning                             |
|-----------------------------------|-------------------------------------|
| `pnpm i --offline`                | Install offline from the store only |
| `pnpm i --frozen-lockfile`        | `pnpm-lock.yaml` is not updated     |
| `pnpm i --lockfile-only`          | Only `pnpm-lock.yaml` is updated    |
| `pnpm i --dry-run`                | Preview changes without writing     |

## Options for filtering dependencies

Without a lockfile, pnpm has to create one, and it must be consistent regardless of dependencies
filtering, so running `pnpm install --prod` on a directory without a lockfile would still resolve the
dev dependencies, and it would error if the resolution is unsuccessful. The only exception for this rule
are `link:` dependencies.

Without `--frozen-lockfile`, pnpm will check for outdated information from `file:` dependencies, so
running `pnpm install --prod` without `--frozen-lockfile` on an environment where the target of `file:`
has been removed would error.

### --prod, -P

* Default: **false**
* Type: **Boolean**

If `true`, pnpm will not install any package listed in `devDependencies` and will remove 
those insofar they were already installed.
If `false`, pnpm will install all packages listed in `devDependencies` and `dependencies`.

### --dev, -D

Only `devDependencies` are installed and `dependencies` are removed insofar they 
were already installed.

### --no-optional

`optionalDependencies` are not installed.

### --no-runtime

Added in: v11.1.0

Skip installing runtime entries (e.g. Node.js downloaded via [`devEngines.runtime`](../package-json.md#devenginesruntime)). The lockfile is left untouched, so frozen installs still validate; only the runtime fetch and bin-linking are skipped.

This is useful in CI matrices where the runtime is provisioned externally (e.g. via `pnpm runtime -g set node <version>`) before `pnpm install` runs.

This can also be set via the `runtime=false` config in `pnpm-workspace.yaml`.

## Options

### --force

Force reinstall dependencies: refetch packages modified in store, recreate a lockfile and/or modules directory created by a non-compatible version of pnpm. Install all optionalDependencies even they don't satisfy the current environment(cpu, os, arch).

### --offline

* Default: **false**
* Type: **Boolean**

If `true`, pnpm will use only packages already available in the store.
If a package won't be found locally, the installation will fail.

### --prefer-offline

* Default: **false**
* Type: **Boolean**

If `true`, staleness checks for cached data will be bypassed, but missing data
will be requested from the server. To force full offline mode, use `--offline`.

### --no-lockfile

Don't read or generate a `pnpm-lock.yaml` file.

### --lockfile-only

* Default: **false**
* Type: **Boolean**

When used, only updates `pnpm-lock.yaml` and `package.json`. Nothing gets written to the `node_modules` directory.

### --dry-run

Added in: v11.8.0

Run a full dependency resolution and report what a real install would change, without writing anything to disk. No lockfile, manifest, or `node_modules` changes are saved.

A completed dry run exits with code 0, even when it reports that a real install would update the lockfile.

`--dry-run` cannot be used with a configured pnpr server, because that install path resolves and links through the server.

### --fix-lockfile

Fix broken lockfile entries automatically.

### --update-checksums

Added in: v11.4.0

Refresh the locked tarball integrity values from what the registry currently serves, when a downloaded tarball's hash doesn't match the integrity recorded in `pnpm-lock.yaml`.

By default, since v11.4.0, an integrity mismatch is a hard failure: `pnpm install` exits with `ERR_PNPM_TARBALL_INTEGRITY` rather than silently re-resolving from the registry and overwriting the locked integrity. This protects projects that ship a committed lockfile from a compromised registry, proxy, or republished version substituting attacker-controlled content on a clean machine.

`--update-checksums` is the narrowly-scoped opt-in for the legitimate case (e.g. a registry rewrote its tarballs and you've verified the new bytes are correct). A warning still prints when the bypass takes effect so the operation is auditable.

`--force` and `pnpm update` deliberately do **not** bypass the integrity check. `--frozen-lockfile` is unchanged, and `--fix-lockfile` keeps its documented purpose (filling in missing lockfile entries) and is also not a bypass.

### --frozen-lockfile

* Default:
  * For non-CI: **false**
  * For CI: **true**, if a lockfile is present
* Type: **Boolean**

If `true`, pnpm doesn't generate a lockfile and fails to install if the lockfile
is out of sync with the manifest / an update is needed or no lockfile is
present.

This setting is `true` by default in [CI environments]. The following code is used to detect CI environments:

```js title="https://github.com/watson/ci-info/blob/44e98cebcdf4403f162195fbcf90b1f69fc6e047/index.js#L54-L61"
exports.isCI = !!(
  env.CI || // Travis CI, CircleCI, Cirrus CI, GitLab CI, Appveyor, CodeShip, dsari
  env.CONTINUOUS_INTEGRATION || // Travis CI, Cirrus CI
  env.BUILD_NUMBER || // Jenkins, TeamCity
  env.RUN_ID || // TaskCluster, dsari
  exports.name ||
  false
)
```

[CI environments]: https://github.com/watson/ci-info#supported-ci-tools

### --merge-git-branch-lockfiles

Merge all git branch lockfiles.
[Read more about git branch lockfiles.](../git_branch_lockfiles)

### --reporter=&lt;name\>

* Default:
    * For TTY stdout: **default**
    * For non-TTY stdout: **append-only**
* Type: **default**, **append-only**, **ndjson**, **silent**

Allows you to choose the reporter that will log debug info to the terminal about
the installation progress.

* **silent** - no output is logged to the console, not even fatal errors
* **default** - the default reporter when the stdout is TTY
* **append-only** - the output is always appended to the end. No cursor manipulations are performed
* **ndjson** - the most verbose reporter. Prints all logs in [ndjson](https://github.com/ndjson/ndjson-spec) format

If you want to change what type of information is printed, use the [loglevel] setting.

[loglevel]: ../settings/cli.md#loglevel

### --shamefully-hoist

* Default: **false**
* Type: **Boolean**

Creates a flat `node_modules` structure, similar to that of `npm` or `yarn`.
**WARNING**: This is highly discouraged.

### --ignore-scripts

* Default: **false**
* Type: **Boolean**

Do not execute any scripts defined in the project `package.json` and its
dependencies.

### --filter &lt;package_selector>

[Read more about filtering.](../filtering.md)

### --resolution-only

Re-runs resolution: useful for printing out peer dependency issues.


---

# pnpm lane

*Sección: Cli*

Added in: v11.13.0

Manages per-package release lanes. A lane is a parallel release track: while a package is on one, the bare [`pnpm version -r`](version.md#recursive-releases) releases it as `X.Y.Z-<lane>.N` prereleases while the rest of the workspace keeps releasing stable versions. Moving a package back to the main lane releases its accumulated stable version on the next run.

```sh
pnpm lane
pnpm lane <name> --filter <pattern>
pnpm lane main --filter <pattern>
```

Membership lives under the [`versioning.lanes`](../settings/versioning.md#versioninglanes) key of `pnpm-workspace.yaml`; this command is a convenience editor for that key.

## Usage

### Show lane membership

```sh
pnpm lane
```

```
Lanes:
  alpha:
    @example/cli
    @example/napi
```

If no package has been assigned a lane, this prints `All packages are on the main lane.`

### Move packages onto a lane

```sh
pnpm lane alpha --filter @example/cli
```

`--filter` is required — it selects the packages to move. Lane names may contain only alphanumerics and hyphens, and cannot be purely numeric.

### Move packages back to the main lane

```sh
pnpm lane main --filter @example/cli
```

`main` is the reserved name of the default lane. Every package is on it unless assigned elsewhere, and packages on it release stable versions. Graduating a package releases the stable version its prereleases were building toward on the next `pnpm version -r` run.

## Versions on a lane

A package on a lane releases `X.Y.Z-<lane>.N`, where `X.Y.Z` is the stable version the lane is building toward and `N` counts up from `0`:

| Current version | Pending intent | Lane | New version |
| --- | --- | --- | --- |
| `2.0.0` | minor | `alpha` | `2.1.0-alpha.0` |
| `2.1.0-alpha.0` | patch | `alpha` | `2.1.0-alpha.1` |
| `2.1.0-alpha.1` | major | `alpha` | `3.0.0-alpha.0` |
| `3.0.0-alpha.0` | — | `main` | `3.0.0` |

`N` restarts at `0` whenever the stable target changes. When a bump escalates the target — a `major` intent while the lane was building a minor — the target is recomputed and the counter resets.

Packages in the same [fixed group](../versioning.md#fixed-groups) must move between lanes together.

## Options

### --filter &lt;package_selector\&gt;

Select the packages to move between lanes. Required when assigning a lane.

[Read more about filtering.](../filtering.md)


---

# pnpm licenses

*Sección: Cli*

## Commands

### list

Aliases: `ls`

List licenses for installed packages.

## Options

### --dev, -D

Check only "devDependencies".

### --json

Show information in JSON format.

### --long

Show more details (such as a link to the repo) are not displayed. To display the details, pass this option.

### --no-optional

Don't check packages from `optionalDependencies`.

### --prod, -P

Check only `dependencies` and `optionalDependencies`.

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)


---

# pnpm link

*Sección: Cli*

Aliases: `ln`

Links a local package to the current project's `node_modules`.

```text
pnpm link <dir>
```

## Options

### `pnpm link <dir>`

Links package from `<dir>` directory to `node_modules` of package from where you're executing this command. `<dir>` must be a relative or absolute path.

> For example, if you are inside `~/projects/foo` and you execute `pnpm link ../bar`, then a link to `bar` will be created in `foo/node_modules/bar`.

:::note Breaking changes in v11

`pnpm link` no longer resolves packages from the global store. Only relative or absolute paths are accepted (use `pnpm link ./foo` instead of `pnpm link foo`).

`pnpm link --global` has been removed. To register a local package's bins globally, use `pnpm add -g .` instead.

`pnpm link` with no arguments has been removed. Always pass an explicit path.

:::

## Use Cases

### Replace an installed package with a local version of it

Let's say you have a project that uses `foo` package. You want to make changes to `foo` and test them in your project. In this scenario, you can use `pnpm link` to link the local version of `foo` to your project:

```bash
cd ~/projects/foo
pnpm install # install dependencies of foo
cd ~/projects/my-project
pnpm link ~/projects/foo # link foo to my-project
```

### Add a binary globally

To make a local package's binaries available system-wide, use `pnpm add -g .` instead:

```bash
cd ~/projects/foo
pnpm install # install dependencies of foo
pnpm add -g . # register foo's bins globally
```

Remember that the binary will be available only if the package has a `bin` field in its `package.json`.

## What's the difference between `pnpm link` and using the `file:` protocol?

When you use `pnpm link`, the linked package is symlinked from the source code. You can modify the source code of the linked package, and the changes will be reflected in your project. With this method pnpm will not install the dependencies of the linked package, you will have to install them manually in the source code. This may be useful when you have to use a specific package manager for the linked package, for example, if you want to use `npm` for the linked package, but pnpm for your project.

When you use the `file:` protocol in `dependencies`, the linked package is hard-linked to your project `node_modules`, you can modify the source code of the linked package, and the changes will be reflected in your project. With this method pnpm will also install the dependencies of the linked package, overriding the `node_modules` of the linked package.

:::info

When dealing with **peer dependencies** it is recommended to use the `file:` protocol. It better resolves the peer dependencies from the project dependencies, ensuring that the linked dependency correctly uses the versions of the dependencies specified in your main project, leading to more consistent and expected behaviors.

:::

| Feature                                      | `pnpm link`                                        | `file:` Protocol                                    |
|----------------------------------------------|----------------------------------------------------|-----------------------------------------------------|
| Symlink/Hard-link                            | Symlink                                            | Hard-link                                           |
| Reflects source code modifications           | Yes                                                | Yes                                                 |
| Installs dependencies of the linked package  | No (manual installation required)                  | Yes (overrides `node_modules` of the linked package)|
| Use different package manager for dependency | Possible (e.g., use `npm` for linked pkg)          | No, it will use pnpm                                |


---

# pnpm list

*Sección: Cli*

Aliases: `ls`

This command will output all the versions of packages that are installed, as
well as their dependencies, in a tree-structure.

Positional arguments are `name-pattern@version-range` identifiers, which will
limit the results to only the packages named. For example,
`pnpm list "babel-*" "eslint-*" semver@5`.

## Options

### --recursive, -r

Perform command on every package in subdirectories or on every workspace
package, when executed inside a workspace.

### --json

Log output in JSON format.

### --long

Show extended information.

### --lockfile-only

Added in: v10.23.0

Read package information from the lockfile instead of checking the actual `node_modules` directory. This is useful for quickly inspecting what would be installed without requiring a full installation.

### --parseable

Outputs package directories in a parseable format instead of their tree view.

### --global, -g

List packages in the global install directory instead of in the current project.

### --depth &lt;number\>

Max display depth of the dependency tree.

`pnpm ls --depth 0` (default) will list direct dependencies only.
`pnpm ls --depth -1` will list projects only. Useful inside a workspace when
used with the `-r` option.
`pnpm ls --depth Infinity` will list all dependencies regardless of depth.

### --prod, -P

Display only the dependency graph for packages in `dependencies` and
`optionalDependencies`.

### --dev, -D

Display only the dependency graph for packages in `devDependencies`.

### --no-optional

Don't display packages from `optionalDependencies`.

### --only-projects

Display only dependencies that are also projects within the workspace.

### --exclude-peers

Exclude peer dependencies from the results (but dependencies of peer dependencies are not ignored).

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)


---

# pnpm login

*Sección: Cli*

Added in: v11.0.0

Aliases: `adduser`

Authenticate with an npm registry.

```sh
pnpm login [--registry <url>] [--scope <scope>]
```

Supports web-based login with QR code as well as classic username/password authentication.

Since v11.19.0, web-based login no longer requires an interactive terminal: without a TTY, `pnpm login` prints the authentication URL (skipping the QR code and the prompt to open the URL in a browser) and polls the registry until the browser approval completes. Only the classic username/password login still fails with `ERR_PNPM_LOGIN_NON_INTERACTIVE` in a non-interactive terminal.

Auth tokens are written to [`<pnpm config>/auth.ini`](../npmrc.md#auth-file-locations).

## Options

### --registry &lt;url\>

The registry to authenticate with. Defaults to the configured default registry.

### --scope &lt;scope\>

Associate the credentials with the specified scope. The registry for that scope will be used.


---

# pnpm logout

*Sección: Cli*

Added in: v11.0.0

Log out of an npm registry. Revokes the authentication token on the registry and removes it from the local auth config file.

```sh
pnpm logout [--registry <url>] [--scope <scope>]
```

If a scope is provided, the registry associated with that scope is used.

The token is removed from [`<pnpm config>/auth.ini`](../npmrc.md#auth-file-locations).

## Options

### --registry &lt;url\>

The registry to log out from. Defaults to the configured default registry.

### --scope &lt;scope\>

Use the registry associated with the given scope.


---

# pnpm outdated

*Sección: Cli*

Checks for outdated packages. The check can be limited to a subset of the
installed packages by providing arguments (patterns are supported).

Examples:
```sh
pnpm outdated
pnpm outdated "*gulp-*" @babel/core
```

## Options

### --recursive, -r

Check for outdated dependencies in every package found in subdirectories, or in
every workspace package when executed inside a workspace.

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)

### --global, -g

List outdated global packages.

### --long

Print details.

### --format &lt;format\>

* Default: **table**
* Type: **table**, **list**, **json**

Prints the outdated dependencies in the given format.

### --compatible

Prints only versions that satisfy specifications in `package.json`.

### --dev, -D

Checks only `devDependencies`.

### --prod, -P

Checks only `dependencies` and `optionalDependencies`.

### --no-optional

Doesn't check `optionalDependencies`.

### --sort-by

Specifies the order in which the output results are sorted. Currently only the value `name` is accepted.

### --include-github-actions

Added in: v11.16.0

Also check the GitHub Actions referenced by the repository's workflow files for updates. You can enable this by default by setting [`update.githubActions`](../settings/dependency-resolution.md#updategithubactions) to `true` in `pnpm-workspace.yaml`. See [Updating GitHub Actions](update.md#updating-github-actions).


---

# pnpm owner

*Sección: Cli*

Added in: v11.1.0

Aliases: `owners`

Manages package owners on the registry.

## Commands

### ls

```sh
pnpm owner ls <package>
```

Aliases: `list`

List all owners of a package. This is the default subcommand if no other subcommand is given.

### add

```sh
pnpm owner add <package> <user>
```

Add a user as an owner of a package. Requires authentication.

### rm

```sh
pnpm owner rm <package> <user>
```

Remove a user from the list of owners of a package. Requires authentication.

## Options

### --registry &lt;url\>

The base URL of the npm registry to use for the operation. Per-scope and named registries (configured via [`registries`](../settings/dependency-resolution.md#registries) and [`namedRegistries`](../settings/dependency-resolution.md#namedregistries)) are respected for the package being modified.

### --otp &lt;otp\>

When the registry requires two-factor authentication, this option supplies a one-time password.


---

# pnpm pack-app

*Sección: Cli*

Added in: v11.0.0

:::warning Experimental

`pnpm pack-app` is experimental. Its flags, `pnpm.app` configuration schema, and output layout may change in future releases.

:::

Pack a CommonJS entry file into a standalone executable for one or more target platforms, using the [Node.js Single Executable Applications](https://nodejs.org/api/single-executable-applications.html) API under the hood.

```sh
pnpm pack-app --entry <path> --target <triplet> [--target <triplet> ...]
```

Each target produces an executable under `<output-dir>/<target>/` (default `dist-app/<target>/`). On Windows targets the output is suffixed with `.exe`; macOS outputs are ad-hoc signed automatically (via `codesign` on macOS hosts or `ldid` on Linux hosts) because SEA injection invalidates the existing code signature.

## Requirements

* The host must run Node.js v25.5+ to perform the SEA injection. If the running Node.js is older (or does not match the embedded runtime version — SEA blobs are not compatible across minor releases), pnpm downloads a matching builder automatically.
* Cross-compiling macOS targets from Linux requires [`ldid`](https://github.com/ProcursusTeam/ldid) on `$PATH`. Windows hosts cannot ad-hoc sign macOS outputs; build macOS targets on macOS or Linux.

## Supported targets

Targets use the format `<os>-<arch>[-<libc>]`:

* `linux-x64`, `linux-x64-musl`, `linux-arm64`, `linux-arm64-musl`
* `darwin-x64`, `darwin-arm64`
* `win32-x64`, `win32-arm64`

The `-musl` suffix is only valid for `linux` targets. The `<os>` segment matches `process.platform` values so the flag is consistent with pnpm's `--os` flag and with `supportedArchitectures.os` in `pnpm-workspace.yaml`.

## Known limitations

### `darwin-x64` binaries crash on Intel Macs

`darwin-x64` outputs segfault at startup on Intel Macs because of an upstream Node.js bug in the `--build-sea` injection step. LIEF's Mach-O surgery for x64 leaves `LC_DYLD_CHAINED_FIXUPS` chain entries pointing at stale targets after the SEA segment is inserted; dyld then dereferences a raw chain-encoded value as a pointer and the binary crashes in `__cxx_global_var_init` before any user code runs. This is reproducible with the canonical `node --build-sea` + `codesign --sign -` flow with no pnpm involvement.

The Node.js team has opted not to fix this on the grounds that x64 macOS is being phased out. Signature-related workarounds do not help — the corruption happens in the injection step, *before* signing, so swapping `ldid` for `codesign` (or vice versa) makes no difference. Re-signing produces a valid signature over already-broken bytes.

Tracking:

* [nodejs/node#62893](https://github.com/nodejs/node/issues/62893) — minimal `node --build-sea` repro
* [nodejs/node#59553](https://github.com/nodejs/node/issues/59553) — long-running SEA test failures on macOS x64 with the same root cause
* [nodejs/node#60250](https://github.com/nodejs/node/pull/60250) — Node.js skipping the SEA tests on x64 macOS rather than fixing them

If you need to ship a CLI that runs on Intel Macs, build the `darwin-x64` artifact with a non-SEA tool such as [`@yao-pkg/pkg`](https://github.com/yao-pkg/pkg) (which appends to the binary tail rather than mutating Mach-O sections). Note that Rosetta is *not* an escape hatch — it only translates x64 → arm64 (for Apple Silicon Macs running Intel binaries), not the other direction, so Intel Macs cannot run a `darwin-arm64` build.

## Examples

Build for Linux and Windows at once:

```sh
pnpm pack-app --entry dist/index.cjs --target linux-x64 --target win32-x64
```

Embed a specific Node.js version:

```sh
pnpm pack-app --entry dist/index.cjs --target linux-x64-musl --runtime node@25.5.0
```

## Options

### --entry &lt;path\>

Path to the CJS entry file to embed in the executable. Required unless [`pnpm.app.entry`](#configuration) is set in `package.json`. A bare positional argument is also accepted (e.g. `pnpm pack-app dist/index.cjs`).

### --target, -t &lt;triplet\>

Target to build for. May be specified multiple times. See [Supported targets](#supported-targets) for the accepted values. Required unless [`pnpm.app.targets`](#configuration) is set. When passed on the CLI, `--target` entirely replaces the configured list so you can narrow the build at invocation time.

### --runtime &lt;spec\>

Runtime to embed in the output executables, as a `<name>@<version>` spec (e.g. `node@25`, `node@25.5.0`). Only `node` is supported today; the `<name>@` prefix leaves room for future runtimes (`bun`, `deno`). The version must be >= v25.5 (the minimum that supports `--build-sea`). Defaults to the running Node.js version.

### --output-dir, -o &lt;dir\>

Output directory for the built executables. Defaults to `dist-app`.

### --output-name &lt;name\>

Name for the output executable (without extension). Defaults to the unscoped `name` from `package.json` (e.g. `my-cli` for `@acme/my-cli`).

## Configuration

Defaults for every flag can be set in `package.json` under `pnpm.app`. CLI flags override the config:

```json title="package.json"
{
  "name": "my-cli",
  "pnpm": {
    "app": {
      "entry": "dist/index.cjs",
      "targets": [
        "linux-x64",
        "linux-arm64",
        "darwin-x64",
        "darwin-arm64",
        "win32-x64"
      ],
      "runtime": "node@25.5.0",
      "outputDir": "dist-app",
      "outputName": "my-cli"
    }
  }
}
```

With this config in place, `pnpm pack-app` can be run with no arguments. `--target` on the CLI replaces the configured `targets` list, which is useful for narrowing a build (e.g. `pnpm pack-app --target linux-x64`).


---

# pnpm pack

*Sección: Cli*

Create a tarball from a package.

## Options

### --recursive, -r

Added in: v10.11.0

Pack all packages from the workspace.

### --out &lt;path\>

Customizes the output path for the tarball. Use `%s` and `%v` to include the package name and version, e.g., `%s.tgz` or `some-dir/%s-%v.tgz`. By default, the tarball is saved in the current working directory with the name `<package-name>-<version>.tgz`.

### --pack-destination &lt;dir\>

Directory in which `pnpm pack` will save tarballs. The default is the current working directory.

### --pack-gzip-level &lt;level\>

Specifying custom compression level.

### --json

Log output in JSON format.

### --filter &lt;package_selector\>

Added in: v10.11.0

[Read more about filtering.](../filtering.md)

### --dry-run

Added in: v10.26.0

Does everything a normal run does, except actually packing the tarball. Useful for verifying the contents of the tarball.

### --skip-manifest-obfuscation

Added in: v11.3.0

Keep the original `packageManager` field and publish lifecycle scripts in the packed manifest instead of stripping them. The pnpm-specific `pnpm` field is still omitted.

## Life Cycle Scripts

* `prepack`
* `prepare`
* `postpack`

:::tip

You can also use the [`beforePacking` hook](../pnpmfile.md#hooksbeforepackingpkg-pkg--promisepkg) to programmatically modify the `package.json` contents before the tarball is created. This is useful for removing development-only fields or adding publication metadata without modifying your local `package.json`.

:::


---

# pnpm patch-commit <path>

*Sección: Cli*

Generate a patch out of a directory and save it (inspired by a similar command in Yarn).

This command will compare the changes from `path` to the package it was supposed to patch, generate a patch file, save the a patch file to `patchesDir` (which can be customized by the `--patches-dir` option), and add an entry to [`patchedDependencies`].

Usage:

```sh
pnpm patch-commit <path>
```

* `path` is the path to a modified copy of the patch target package, it is usually a temporary directory generated by [`pnpm patch`](./patch).

## Options

### ---patches-dir &lt;patchesDir>

The generated patch file will be saved to this directory. By default, patches are saved to the `patches` directory in the root of the project.

[`patchedDependencies`]: patch.md#patcheddependencies


---

# pnpm patch-remove <pkg...>

*Sección: Cli*

Remove existing patch files and settings in `patchedDependencies`.

```sh
pnpm patch-remove foo@1.0.0 bar@1.0.1
```


---

# pnpm patch <pkg>

*Sección: Cli*

Prepare a package for patching (inspired by a similar command in Yarn).

This command will cause a package to be extracted in a temporary directory intended to be editable at will.

Once you're done with your changes, run `pnpm patch-commit <path>` (with `<path>` being the temporary directory you received) to generate a patchfile and register it into your top-level manifest via the [`patchedDependencies`] field.

Usage:

```
pnpm patch <pkg name>@<version>
```

[`patchedDependencies`]: #patcheddependencies

:::note

If you want to change the dependencies of a package, don't use patching to modify the `package.json` file of the package. For overriding dependencies, use [overrides] or a [package hook].

:::

[overrides]: ../settings/dependency-resolution.md#overrides
[package hook]: ../pnpmfile#hooksreadpackagepkg-context-pkg--promisepkg

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/0GjLqRGRbcY" title="The pnpm patch command demo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen"></iframe>

## Options

### --edit-dir &lt;dir>

The package that needs to be patched will be extracted to this directory.

### --ignore-existing

Ignore existing patch files when patching.

## Configuration

### patchedDependencies

This field is added/updated automatically when you run [pnpm patch-commit]. It defines patches for dependencies using a dictionary where:

[pnpm patch-commit]: patch-commit.md

* **Keys**: Package names with an exact version, a version range, or just the name.
* **Values**: Relative paths to patch files.

Example:

```yaml
patchedDependencies:
  express@4.18.1: patches/express@4.18.1.patch
```

Dependencies can be patched by version range. The priority order is:

1. Exact versions (highest priority)
2. Version ranges
3. Name-only patches (applies to all versions unless overridden)

A special case: the version range `*` behaves like a name-only patch but does not ignore patch failures.

Example:

```yaml
patchedDependencies:
  foo: patches/foo-1.patch
  foo@^2.0.0: patches/foo-2.patch
  foo@2.1.0: patches/foo-3.patch
```

* `patches/foo-3.patch` is applied to `foo@2.1.0`.
* `patches/foo-2.patch` applies to all foo versions matching `^2.0.0`, except `2.1.0`.
* `patches/foo-1.patch` applies to all other foo versions.

Avoid overlapping version ranges. If you need to specialize a sub-range, explicitly exclude it from the broader range.

Example:

```yaml
patchedDependencies:
  # Specialized sub-range
  "foo@2.2.0-2.8.0": patches/foo.2.2.0-2.8.0.patch
  # General patch, excluding the sub-range above
  "foo@>=2.0.0 <2.2.0 || >2.8.0": patches/foo.gte2.patch
```

In most cases, defining an exact version is enough to override a broader range.

### allowUnusedPatches

Added in: v10.7.0 (Previously named `allowNonAppliedPatches`)

* Default: **false**
* Type: **Boolean**

When `true`, installation won't fail if some of the patches from the `patchedDependencies` field were not applied.

```yaml
patchedDependencies:
  express@4.18.1: patches/express@4.18.1.patch
allowUnusedPatches: true
```

:::note

In v11, patch application failures always throw an error — the `ignorePatchFailures` setting has been removed. When multiple patches in a group are applied, a failure in one does not prevent the rest from being attempted; all patch errors are reported together at the end.

:::


---

# pnpm peers

*Sección: Cli*

## Commands

### check

Added in: v11.0.0

Checks for unmet and missing peer dependency issues by reading the lockfile.

```sh
pnpm peers check
```

This command analyzes the lockfile and reports any packages with unresolved or incompatible peer dependencies.


---

# pnpm ping

*Sección: Cli*

Added in: v11.0.0

Ping the configured registry to verify connectivity.

```sh
pnpm ping [--registry <url>]
```

On success, the registry's response is printed. This is useful for quickly confirming that the current machine can reach the registry without installing or publishing anything.

## Options

### --registry &lt;url\>

The registry to ping. Defaults to the configured default registry.


---

# pnpm pkg

*Sección: Cli*

Added in: v11.3.0

Manages the contents of `package.json` from the command line.

```sh
pnpm pkg get [<key> [<key> ...]]
pnpm pkg set <key>=<value> [<key>=<value> ...]
pnpm pkg delete <key> [<key> ...]
pnpm pkg fix
```

Nested fields are addressed with dot-separated paths (e.g. `scripts.test`, `repository.url`).

## Commands

### get

Retrieves a value from `package.json`. With no arguments, prints the full manifest. With one or more keys, prints the requested fields.

```sh
pnpm pkg get name
pnpm pkg get name version
pnpm pkg get scripts.test
```

When only one key is requested and it resolves to a string, the raw value is printed; otherwise the value is JSON-encoded. Pass `--json` to always print JSON.

### set

Sets one or more values in `package.json`. Each argument has the `key=value` form.

```sh
pnpm pkg set name=my-package
pnpm pkg set scripts.build="tsc -p ."
pnpm pkg set 'keywords[0]'=cli
```

By default the value is stored as a string. Pass `--json` to parse the value as JSON before storing it (useful for booleans, numbers, arrays, and objects):

```sh
pnpm pkg set private=true --json
pnpm pkg set 'engines={"node":">=22"}' --json
```

### delete

Removes one or more keys from `package.json`.

```sh
pnpm pkg delete scripts.test
pnpm pkg delete keywords
```

### fix

Auto-corrects common errors in `package.json` (e.g. removes a non-string `name` or `version`, drops dependency / `scripts` blocks whose values aren't objects, drops a `bin` field that's neither a string nor an object).

```sh
pnpm pkg fix
```

## Options

### --json

When setting, parses each `value` as JSON before writing. When getting a single key, returns the JSON-encoded form instead of the raw value.

### --recursive, -r

Runs the subcommand on every workspace project, or on every project selected by a `--filter`.

```sh
pnpm -r pkg get name
pnpm -r pkg set version=1.0.0
pnpm --filter "./packages/*" pkg get name
```

`pnpm -r pkg get` returns a JSON object keyed by package name; `set`, `delete`, and `fix` apply to each matched project.


---

# pnpm pm

*Sección: Cli*

The `pnpm pm <command>` syntax always runs the built-in pnpm command, bypassing any same-named script in `package.json`.

Some built-in commands can be overridden by scripts. For example, if your project defines a `"clean"` script in `package.json`, then `pnpm clean` runs that script instead of the built-in [`pnpm clean`](clean.md). Using `pnpm pm clean` forces the built-in command to run.

## Example

```json title="package.json"
{
  "scripts": {
    "clean": "rm -rf dist"
  }
}
```

```sh
# Runs the "clean" script from package.json
pnpm clean
# or explicitly:
pnpm run clean

# Runs the built-in pnpm clean command (removes node_modules)
pnpm pm clean
```


---

# pnx

*Sección: Cli*

Aliases: `pnpm dlx`, `pnpx`

Fetches a package from the registry without installing it as a dependency, hotloads it, and runs whatever default command binary it exposes.

For example, to use `create-vue` anywhere to bootstrap a Vue project without
needing to install it under another project, you can run:

```
pnx create-vue my-app
```

This will fetch `create-vue` from the registry and run it with the given arguments.

You may also specify which exact version of the package you'd like to use:

```
pnx create-vue@next my-app
```

The `catalog:` protocol is also supported, allowing you to use versions defined in your workspace catalogs:

```
pnx shx@catalog:
```

## Options

### --package &lt;name\>

The package to install before running the command.

Example:

```
pnx --package=@pnpm/meta-updater meta-updater --help
pnx --package=@pnpm/meta-updater@0 meta-updater --help
```

Multiple packages can be provided for installation:

```
pnx --package=yo --package=generator-webapp yo webapp --skip-install
```

### --allow-build

Added in: v10.2.0

A list of package names that are allowed to run postinstall scripts during installation.

Example:

```
pnx --allow-build=esbuild my-bundler bundle
```

The actual packages executed by `dlx` are allowed to run postinstall scripts by default. So if in the above example `my-bundler` has to be built before execution, it will be built.

### --shell-mode, -c

Runs the command inside of a shell. Uses `/bin/sh` on UNIX and `\cmd.exe` on Windows.

Example: 

```
pnx --package cowsay --package lolcatjs -c 'echo "hi pnpm" | cowsay | lolcatjs'
```

### --silent, -s

Only the output of the executed command is printed.

## Security and trust policies

Since v11.0.0, `pnx` (and its `pnpm dlx` / `pnpx` aliases) honors the project-level security and trust policy settings when resolving and fetching the requested package:

* [`minimumReleaseAge`](../settings/dependency-resolution.md#minimumreleaseage), [`minimumReleaseAgeExclude`](../settings/dependency-resolution.md#minimumreleaseageexclude), [`minimumReleaseAgeStrict`](../settings/dependency-resolution.md#minimumreleaseagestrict)
* [`trustPolicy`](../settings/dependency-resolution.md#trustpolicy), [`trustPolicyExclude`](../settings/dependency-resolution.md#trustpolicyexclude), [`trustPolicyIgnoreAfter`](../settings/dependency-resolution.md#trustpolicyignoreafter)

This means `pnx` will refuse to execute freshly published or insufficiently trusted packages the same way a regular `pnpm install` would.


---

# pnpm prefix

*Sección: Cli*

Added in: v11.10.0

Prints the current package prefix directory — the directory containing the closest `package.json`.

```sh
pnpm prefix
```

## Options

### --global, -g

Prints the global prefix directory instead.


---

# pnpm prune

*Sección: Cli*

Removes unnecessary packages.

## Options

### --prod

Remove the packages specified in `devDependencies`.

### --no-optional

Remove the packages specified in `optionalDependencies`.

:::warning

The prune command does not support recursive execution on a monorepo currently. To only install production-dependencies in a monorepo `node_modules` folders can be deleted and then re-installed with `pnpm install --prod`.

:::


---

# pnpm publish

*Sección: Cli*

Publishes a package to the registry.

```sh
pnpm [-r] publish [<tarball|folder>] [--tag <tag>]
     [--access <public|restricted>] [options]
```

:::note

Since v11, `pnpm publish` is implemented natively and no longer delegates to the `npm` CLI. If you rely on a feature that is now gone, please open an issue at [pnpm/pnpm](https://github.com/pnpm/pnpm/issues). As a workaround, you can still run `pnpm pack && npm publish *.tgz`.

:::

When publishing a package inside a [workspace](../workspaces.md), the LICENSE file
from the root of the workspace is packed with the package (unless the package
has a license of its own).

You may override some fields before publish, using the
[publishConfig] field in `package.json`.
You also can use the [`publishConfig.directory`](../package-json.md#publishconfigdirectory) to customize the published subdirectory (usually using third party build tools).

When running this command recursively (`pnpm -r publish`), pnpm will publish all
the packages that have versions not yet published to the registry.

[publishConfig]: ../package-json.md#publishconfig

## Options

### --recursive, -r

Publish all packages from the workspace.

### --json

Show information in JSON format.

### --tag &lt;tag\>

Publishes the package with the given tag. By default, `pnpm publish` updates
the `latest` tag.

For example:

```sh
# inside the foo package directory
pnpm publish --tag next
# in a project where you want to use the next version of foo
pnpm add foo@next
```

### --access &lt;public|restricted\>

Tells the registry whether the published package should be public or restricted.

### --no-git-checks

Don't check if current branch is your publish branch, clean, and up-to-date with remote.

### --publish-branch &lt;branch\>

* Default: **master** and **main**
* Types: **String**

The primary branch of the repository which is used for publishing the latest
changes.

### --force

Try to publish packages even if their current version is already found in the
registry.

### --batch

Added in: v11.7.0

When publishing recursively (`pnpm -r publish`), send all selected packages to the registry in a single `PUT /-/pnpm/v1/publish` request instead of one request per package.

The target registry has to implement the batch publish endpoint ([pnpr](https://github.com/pnpm/pnpm/tree/main/pnpr) does); registries that don't are reported with an `ERR_PNPM_BATCH_PUBLISH_UNSUPPORTED` error. The batch is processed all-or-nothing: if any package in the batch fails validation, none of the packages are published.

### --skip-manifest-obfuscation

Added in: v11.3.0

Keep the original `packageManager` field and publish lifecycle scripts in the published manifest instead of stripping them. The pnpm-specific `pnpm` field is still omitted.

### --report-summary

Save the list of published packages to `pnpm-publish-summary.json`. Useful when some other tooling is used to report the list of published packages.

An example of a `pnpm-publish-summary.json` file:

```json
{
  "publishedPackages": [
    {
      "name": "foo",
      "version": "1.0.0"
    },
    {
      "name": "bar",
      "version": "2.0.0"
    }
  ]
}
```

### --dry-run

Does everything a publish would do except actually publishing to the registry.

### --otp

When publishing packages that require two-factor authentication, this option can specify a one-time password.

You can also provide the OTP via the `PNPM_CONFIG_OTP` environment variable:

```sh
pnpm publish --no-git-checks
```

If the registry requests OTP and you have not provided it via the environment variable or the `--otp` flag, pnpm will prompt you directly for an OTP code.

If the registry requests web-based authentication, pnpm will print a scannable QR code along with the URL.

### --provenance

When publishing from a supported cloud CI/CD system, the package will be publicly linked to where it was built and published from.

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)

## Configuration

You can also set `gitChecks`, `publishBranch` options in the `pnpm-workspace.yaml` file.

For example:

```yaml title="pnpm-workspace.yaml"
gitChecks: false
publishBranch: production
```

## Life Cycle Scripts

* `prepublishOnly`
* `prepublish`
* `prepack`
* `prepare`
* `postpack`
* `publish`
* `postpublish`


---

# pnpm rebuild

*Sección: Cli*

Aliases: `rb`

Rebuild a package.

## Options

### --recursive, -r

This command runs the **pnpm rebuild** command in every package of the monorepo.

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)


---

# pnpm -r, --recursive

*Sección: Cli*

Aliases: `m`, `multi`, `recursive`, `<command> -r`

Runs a command in every project of a workspace, when used with the following commands:

* `install`
* `list`
* `outdated`
* `publish`
* `pack`
* `rebuild`
* `remove`
* `unlink`
* `update`
* `why`

Runs a command in every project of a workspace, excluding the root project,
when used with the following commands:

* `exec`
* `run`
* `test`
* `add`

If you want the root project be included even when running scripts, set the [includeWorkspaceRoot] setting to `true`.

Usage example:

```
pnpm -r publish
```

## Options

### --link-workspace-packages

* Default: **false**
* Type: **true, false, deep**

Link locally available packages in workspaces of a monorepo into `node_modules`
instead of re-downloading them from the registry. This emulates functionality
similar to `yarn workspaces`.

When this is set to deep, local packages can also be linked to subdependencies.

Be advised that it is encouraged instead to use [`pnpm-workspace.yaml`] for this setting, to
enforce the same behaviour in all environments. This option exists solely so you
may override that if necessary.

[`pnpm-workspace.yaml`]: ../workspaces.md#linkworkspacepackages

### --workspace-concurrency

* Default: **4**
* Type: **Number**

Set the maximum number of tasks to run simultaneously. For unlimited concurrency
use `Infinity`.

You can set the `workspace-concurrency` as `<= 0` and it will use amount of cores of the host as: `max(1, (number of cores) - abs(workspace-concurrency))`

### --[no-]bail

* Default: **true**
* Type: **Boolean**

If true, stops when a task throws an error.

This config does not affect the exit code.
Even if `--no-bail` is used, all tasks will finish but if any of the tasks fail,
the command will exit with a non-zero code.

Example (run tests in every package, continue if tests fail in one of them):
```sh
pnpm -r --no-bail test
```

### --[no-]sort

* Default: **true**
* Type: **Boolean**

When `true`, packages are sorted topologically (dependencies before dependents).
Pass `--no-sort` to disable.

Example:
```sh
pnpm -r --no-sort test
```

### --reverse

* Default: **false**
* Type: **boolean**

When `true`, the order of packages is reversed.

```
pnpm -r --reverse run clean
```

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)

[includeWorkspaceRoot]: ../workspaces.md#includeworkspaceroot


---

# pnpm remove

*Sección: Cli*

Aliases: `rm`, `uninstall`, `un`

Removes packages from `node_modules` and from the project's `package.json`.

## Options

### --recursive, -r

When used inside a [workspace](../workspaces.md), removes a dependency (or
dependencies) from every workspace package.

When used not inside a workspace, removes a dependency (or dependencies) from
every package found in subdirectories.

### --global, -g

Remove a global package.

### --save-dev, -D

Only remove the dependency from `devDependencies`.

### --save-optional, -O

Only remove the dependency from `optionalDependencies`.

### --save-prod, -P

Only remove the dependency from `dependencies`.

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)


---

# pnpm repo

*Sección: Cli*

Added in: v11.3.0

Opens the URL of a package's repository in the browser.

```sh
pnpm repo [<pkg> ...]
```

With no arguments, opens the repository of the current project (read from the `repository` field of `package.json`).

With one or more package names, fetches each package's metadata from the registry and opens its repository URL.

The repository URL is normalized to its web equivalent — e.g. `git+ssh://git@github.com/foo/bar.git` opens as `https://github.com/foo/bar`. When the `repository` field includes a `directory`, the URL points at that subdirectory inside the repo.

## Examples

```sh
# Open the repo of the current project
pnpm repo

# Open the repo of a package on the registry
pnpm repo lodash

# Open multiple repos at once
pnpm repo react react-dom
```

## Options

### --registry &lt;url\>

The registry from which to fetch package metadata when an explicit package name is given. Per-scope and named registries (configured via [`registries`](../settings/dependency-resolution.md#registries) and [`namedRegistries`](../settings/dependency-resolution.md#namedregistries)) are respected.


---

# pnpm root

*Sección: Cli*

Prints the effective modules directory.

## Options

### --global, -g

The global package's modules directory is printed.


---

# pnpm run

*Sección: Cli*

Aliases: `run-script`

Runs a script defined in the package's manifest file.

## Examples

Let's say you have a `watch` script configured in your `package.json`, like so:

```json
"scripts": {
    "watch": "webpack --watch"
}
```

You can now run that script by using `pnpm run watch`! Simple, right?
Another thing to note for those that like to save keystrokes and time is that
all scripts get aliased in as pnpm commands, so ultimately `pnpm watch` is just
shorthand for `pnpm run watch` (ONLY for scripts that do not share the same name
as already existing pnpm commands).

## Running multiple scripts

You may run multiple scripts at the same time by using a regex instead of the script name.

```sh
pnpm run "/<regex>/"
```

Run all scripts that start with `watch:`:

```sh
pnpm run "/^watch:.*/"
```

The selector must be written as a regular expression literal — that is, wrapped in slashes — and quoted, so the shell does not mangle it. A plain string is always treated as a literal script name, and a script whose name matches the argument exactly takes precedence over regex matching.

Matching is not anchored, so `"/build:.*/"` also matches `prebuild:web`. Anchor the pattern with `^` and `$` when you need an exact prefix.

Matched scripts run in lexicographical order, so the selection is deterministic regardless of the order the scripts appear in `package.json`. To run them strictly one at a time, add [`--sequential`](#--sequential--s).

Regular expression flags are not supported: `pnpm run "/^build:.*/i"` fails with `ERR_PNPM_UNSUPPORTED_SCRIPT_COMMAND_FORMAT`.

## Details

In addition to the shell’s pre-existing `PATH`, `pnpm run` includes
`node_modules/.bin` in the `PATH` provided to `scripts`. This means that so
long as you have a package installed, you can use it in a script like a regular
command. For example, if you have `eslint` installed, you can write up a script
like so:

```json
"lint": "eslint src --fix"
```

And even though `eslint` is not installed globally in your shell, it will run.

For workspaces, `<workspace root>/node_modules/.bin` is also added
to the `PATH`, so if a tool is installed in the workspace root, it may be called
in any workspace package's `scripts`.

## Environment

There are some environment variables that pnpm automatically creates for the executed scripts.
These environment variables may be used to get contextual information about the running process.

These are the environment variables created by pnpm:

* **npm_command** - contains the name of the executed command. If the executed command is `pnpm run`, then the value of this variable will be "run-script".

## Options

Any options for the `run` command should be listed before the script's name.
Options listed after the script's name are passed to the executed script.

All these will run pnpm CLI with the `--silent` option:

```sh
pnpm run --silent watch
pnpm --silent run watch
pnpm --silent watch
```

Any arguments after the command's name are added to the executed script.
So if `watch` runs `webpack --watch`, then this command:

```sh
pnpm run watch --no-color
```

will run:

```sh
webpack --watch --no-color
```

### --recursive, -r

This runs an arbitrary command from each package's "scripts" object.
If a package doesn't have the command, it is skipped.
If none of the packages have the command, the command fails.

### --if-present

You can use the `--if-present` flag to avoid exiting with a non-zero exit code
when the script is undefined. This lets you run potentially undefined scripts
without breaking the execution chain.

### --no-bail

Continue running the remaining matched scripts even if one of them fails. The command still exits with a non-zero exit code if any script failed.

### --parallel

Completely disregard concurrency and topological sorting, running a given script
immediately in all matching packages with prefixed streaming output. This is the
preferred flag for long-running processes over many packages, for instance, a
lengthy build process.

### --sequential, -s

Added in: v11.14.0

Run the selected scripts one by one. This forces [`--workspace-concurrency`](recursive.md#--workspace-concurrency) to `1`, so scripts matched by a [regex selector](#running-multiple-scripts) never overlap — neither across workspace packages nor within a single package.

```sh
pnpm run --sequential "/^build:.*/"
```

In a recursive run this serializes scripts across workspace projects as well as within each one. `--sequential` takes precedence over `--parallel`: concurrency is pinned to `1` whenever it is set, regardless of the order the two flags appear in.

:::note

For `pnpm run`, `-s` is the shorthand for `--sequential`. Everywhere else in the CLI, `-s` remains the shorthand for `--reporter=silent`. The long form `--silent` is unaffected in all commands.

:::

### --stream

Stream output from child processes immediately, prefixed with the originating
package directory. This allows output from different packages to be interleaved.

### --aggregate-output

Aggregate output from child processes that are run in parallel, and only print output when the child process is finished. It makes reading large logs after running `pnpm -r <command>` with `--parallel` or with `--workspace-concurrency=<number>` much easier (especially on CI). Only `--reporter=append-only` is supported.

### --resume-from &lt;package_name\>

Resume execution from a particular project. This can be useful if you are working with a large workspace and you want to restart a build at a particular project without running through all of the projects that precede it in the build order.

### --report-summary

Record the result of the scripts executions into a `pnpm-exec-summary.json` file.

An example of a `pnpm-exec-summary.json` file:

```json
{
  "executionStatus": {
    "/Users/zoltan/src/pnpm/pnpm/cli/command": {
      "status": "passed",
      "duration": 1861.143042
    },
    "/Users/zoltan/src/pnpm/pnpm/cli/common-cli-options-help": {
      "status": "passed",
      "duration": 1865.914958
    }
  }
```

Possible values of `status` are: 'passed', 'queued', 'running'.

### --reporter-hide-prefix

Hide workspace prefix from output from child processes that are run in parallel, and only print the raw output. This can be useful if you are running on CI and the output must be in a specific format without any prefixes (e.g. [GitHub Actions annotations](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-error-message)). Only `--reporter=append-only` is supported.

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)

## pnpm-workspace.yaml settings


---

# pnpm runtime <cmd>

*Sección: Cli*

Manage runtimes.

Alias: `rt`

## Commands

### set

Install the specified version of a runtime.

```
pnpm runtime set <name> <version> [-g]
```

#### Supported runtimes

- `node` - Node.js
- `deno` - Deno
- `bun` - Bun

:::info

Since v11.0.0, installing a Node.js runtime (via `pnpm runtime set node …` or `node@runtime:<version>`) does not extract the bundled `npm`, `npx`, and `corepack` from the Node.js archive. This roughly halves the number of files pnpm has to hash, write to the CAS, and link during a runtime install. If you still need `npm`, install it separately with `pnpm add -g npm`.

:::

#### Examples

Install Node.js v22 globally:

```
pnpm runtime set node 22 -g
```

Install the LTS version of Node.js:

```
pnpm runtime set node lts -g
```

Install the latest version of Node.js:

```
pnpm runtime set node latest -g
```

Install a prerelease version of Node.js:

```
pnpm runtime set node nightly -g
pnpm runtime set node rc -g
pnpm runtime set node rc/22 -g
pnpm runtime set node 22.0.0-rc.4 -g
```

Install an LTS version of Node.js using its [codename]:

```
pnpm runtime set node argon -g
```

Install Deno:

```
pnpm runtime set deno 2 -g
```

Install Bun:

```
pnpm runtime set bun latest -g
```

[codename]: https://github.com/nodejs/Release/blob/main/CODENAMES.md

## Options

### --global, -g

Install the runtime globally.


---

# pnpm sbom

*Sección: Cli*

Added in: v11.0.0

Generate a Software Bill of Materials (SBOM) for the project.

Supported formats:

- **CycloneDX 1.7** (JSON)
- **SPDX 2.3** (JSON)

## Usage

```sh
pnpm sbom --sbom-format cyclonedx
pnpm sbom --sbom-format spdx
pnpm sbom --sbom-format cyclonedx --lockfile-only
pnpm sbom --sbom-format spdx --prod
pnpm sbom --sbom-format cyclonedx --out sbom.cdx.json
pnpm sbom --sbom-format cyclonedx --split
pnpm sbom --sbom-format cyclonedx --exclude-peers
```

Inside a workspace, `pnpm sbom` supports filtering. When a single workspace package is selected, the root component in the SBOM uses that package's metadata.

CycloneDX output marks components reachable only through `devDependencies` with `scope: "excluded"` and the `cdx:npm:package:development` property. Runtime components, including installed optional dependencies, use the default required scope.

## Options

### --sbom-format &lt;cyclonedx|spdx\>

The SBOM output format. This option is required. Supported values: `cyclonedx`, `spdx`.

### --sbom-type &lt;library|application\>

* Default: **library**

The component type for the root package.

### --sbom-spec-version &lt;version\>

Added in: v11.1.0

* Default: **1.7**
* Type: **1.5**, **1.6**, **1.7**

The CycloneDX specification version to emit. Only valid with `--sbom-format cyclonedx`.

### --lockfile-only

Only use lockfile data (skip reading from the store).

### --sbom-authors &lt;names\>

Comma-separated list of SBOM authors. Written to `metadata.authors` in the CycloneDX output.

### --sbom-supplier &lt;name\>

SBOM supplier name. Written to `metadata.supplier` in the CycloneDX output.

### --out &lt;path\>

Added in: v11.8.0

Write the SBOM to a file instead of stdout.

Use `%s` in the path as a placeholder for the package name and `%v` as a placeholder for the package version. In a workspace, a path containing `%s` writes one SBOM per selected package:

```sh
pnpm sbom --sbom-format cyclonedx --out out/%s.cdx.json
pnpm sbom --sbom-format cyclonedx --out out/%s-%v.cdx.json
```

### --split

Added in: v11.8.0

Generate a separate SBOM for each selected workspace package. Without `--out`, the SBOMs are printed to stdout as NDJSON, one JSON document per line.

When `--split` is combined with `--out`, the output path must contain `%s`.

### --exclude-peers

Added in: v11.9.0

Exclude peer dependencies from the SBOM. Dependencies reachable only through those peers are also excluded.

This is useful with `auto-install-peers` because peer dependencies are resolved into the lockfile and otherwise look the same as regular dependencies.

### --prod, -P

Only include `dependencies` and `optionalDependencies`.

### --dev, -D

Only include `devDependencies`.

### --no-optional

Don't include `optionalDependencies`.

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)


---

# pnpm search

*Sección: Cli*

Added in: v11.0.0

Aliases: `s`, `se`, `find`

Search the registry for packages matching the given keywords.

```sh
pnpm search <keyword> [<keyword> ...]
```

## Examples

```sh
pnpm search webpack plugin
pnpm search @types/node
```

## Options

### --json

Output search results in JSON format.

### --search-limit &lt;number\>

* Default: **20**

Maximum number of results to show.


---

# pnpm self-update

*Sección: Cli*

Updates pnpm to the latest version or the one specified.

```
pnpm self-update [<version>]
```

Usage examples:

```
pnpm self-update
pnpm self-update 10
pnpm self-update next-10
pnpm self-update 10.6.5
```

## Behavior

The behavior of `pnpm self-update` depends on the project context:

### In a project that pins pnpm

When the project's `package.json` has a `packageManager` field set to pnpm (or a `devEngines.packageManager` entry for pnpm), `self-update` only updates the pinned version in `package.json` to the resolved one. It does not install pnpm globally. The next time you run a pnpm command, pnpm will automatically download and switch to the specified version.

### Outside a project (or when the pnpm pin is ignored)

If the project does not pin pnpm, or the pin is being ignored via [`pmOnFail: ignore`](../settings/cli.md#pmonfail), `self-update` installs the resolved pnpm version globally and links it to `PNPM_HOME` so it becomes the active pnpm binary on your system.

## Project settings are ignored

Since v11.18.0, `pnpm self-update` takes no instruction from the project it is run in:

* pnpm is fetched through the same trusted registry and auth configuration used when switching pnpm versions, so a project's `.npmrc` or `pnpm-workspace.yaml` cannot redirect the download or attach credentials to it, and the project's default `.pnpmfile.(c|m)js` is not loaded. Pnpmfiles from trusted sources (the [`pnpmfile`](../pnpmfile.md#pnpmfile) setting, the global pnpmfile, config dependencies) still apply.
* The project's [`minimumReleaseAge`](../settings/dependency-resolution.md#minimumreleaseage), [`trustPolicy`](../settings/dependency-resolution.md#trustpolicy), and `ci` settings do not affect `self-update`. They still govern the project's own dependencies; for `self-update`, these values come from the built-in default, your global config, a `PNPM_CONFIG_*` environment variable, or a command-line flag. This stops a repository from either waiving the release-age cooldown or keeping you on an outdated pnpm by raising it, and from weakening the trust check that guards the pnpm download.

When `self-update` refuses a version that is younger than the `minimumReleaseAge` cutoff, an interactive run offers to update anyway; non-interactive runs still fail. CI never prompts, even on a runner that attaches a TTY.

## Installing pnpm v12 (the Rust port)

Since v11.10.0, `pnpm self-update` (and `packageManager` version-switching) can install and link **pnpm v12**, the Rust port. It is published under both the `pnpm` and `@pnpm/exe` names on the `next-12` dist-tag:

```
pnpm self-update next-12
```

v12 ships native binaries as `@pnpm/exe.<platform>-<arch>` packages, which pnpm's built-in installer links directly. There is no Node.js launcher, so the command pays no Node.js startup cost. From v12 onward the install converges on the unscoped `pnpm` package (the Rust executable), even when updating from the SEA `@pnpm/exe` build.


---

# pnpm set-script

*Sección: Cli*

Added in: v11.3.0

Aliases: `ss`

Adds or updates an entry in the `scripts` field of the project manifest.

```sh
pnpm set-script <name> <command>
```

Supports `package.json`, `package.json5`, and `package.yaml` manifest formats.

If the `scripts` field does not exist, it is created. If a script with the same name already exists, it is overwritten.

## Examples

```sh
pnpm set-script test "vitest run"
pnpm set-script build "tsc -p ."
pnpm ss lint "eslint ."
```

The above is equivalent to manually editing `package.json`:

```json
{
  "scripts": {
    "test": "vitest run",
    "build": "tsc -p .",
    "lint": "eslint ."
  }
}
```

## See also

- [`pnpm pkg set`](pkg.md#set) — set arbitrary fields in `package.json`, including individual scripts via `scripts.<name>=<command>`.


---

# pnpm setup

*Sección: Cli*

This command is used by the standalone installation scripts of pnpm. For instance, in [https://get.pnpm.io/install.sh].

Setup does the following actions:

* creates a home directory for the pnpm CLI
* adds the pnpm home directory to the `PATH` by updating the shell configuration file
* copies the pnpm executable to the pnpm home directory

Since v11.18.0, when running on GitHub Actions, `pnpm setup` also appends `PNPM_HOME` and the global bin directory to the GitHub Actions environment files (`GITHUB_ENV` and `GITHUB_PATH`), so later steps in the same job can run `pnpm add --global` and other global commands.

:::tip

After upgrading to pnpm v11, run `pnpm setup` to update your shell configuration. In v11, globally installed binaries are stored in a `bin` subdirectory of `PNPM_HOME`.

:::

[https://get.pnpm.io/install.sh]: https://get.pnpm.io/install.sh


---

# pnpm stage

*Sección: Cli*

Added in: v11.3.0

Stages packages for publishing using npm's [staged publishing](https://docs.npmjs.com/staged-publishing) workflow. Staged versions are not resolved by `pnpm install` until they are explicitly approved, letting you defer proof-of-presence (2FA) to a later point in time — useful for verifying release artifacts, smoke-testing CI, or coordinating multi-package releases.

```sh
pnpm stage <subcommand> [options]
```

## Subcommands

### publish

Stage a package for publishing.

```sh
pnpm stage publish [<tarball>|<dir>] [--tag <tag>] [--access <public|restricted>] [options]
```

Accepts the same arguments as [`pnpm publish`](publish.md), but uploads the tarball to staging instead of promoting it to the live registry. The resulting **stage id** is printed and can be used with the other subcommands.

Use `--recursive` (or `-r`) to stage every publishable package in the workspace.

### list

List all staged package versions, or list the staged versions of a specific package.

```sh
pnpm stage list [<package-spec>]
```

### view

Show details of a specific staged version.

```sh
pnpm stage view <stage-id>
```

### approve

Approve a staged version, promoting it to the live registry. This is the step that consumes the one-time password.

```sh
pnpm stage approve <stage-id> [--otp <otp>]
```

### reject

Reject a staged version and remove it from staging.

```sh
pnpm stage reject <stage-id> [--otp <otp>]
```

### download

Download the tarball of a staged version for inspection.

```sh
pnpm stage download <stage-id>
```

## Options

### --registry &lt;url\>

The base URL of the npm registry. Defaults to the configured default registry.

### --tag &lt;tag\>

Registers the staged package with the given dist-tag. Defaults to `latest`.

### --access &lt;public|restricted\>

Tells the registry whether the staged package should be public or restricted.

### --json

Show information in JSON format. Applies to `list`, `view`, `publish`, and `download`.

### --dry-run

Does everything `stage publish` would do except uploading to the registry.

### --otp &lt;otp\>

One-time password for `approve` and `reject`.

### --recursive, -r

Stage all publishable packages from the workspace.

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)


---

# pnpm star

*Sección: Cli*

Added in: v11.0.0

Mark a package as a favorite on the registry. You must be logged in (see [`pnpm login`](login.md)).

```sh
pnpm star <pkg>
```

## pnpm unstar

Remove a package from your favorites.

```sh
pnpm unstar <pkg>
```

## pnpm stars

List the packages you (or another user) have starred.

```sh
pnpm stars [<user>]
```

When run without a username, pnpm lists the packages starred by the currently authenticated user.


---

# pnpm start

*Sección: Cli*

Aliases: `run start`

Runs an arbitrary command specified in the package's `start` property of its
`scripts` object. If no `start` property is specified on the `scripts` object,
it will attempt to run `node server.js` as a default, failing if neither are
present.

The intended usage of the property is to specify a command that starts your
program.


---

# pnpm store

*Sección: Cli*

Managing the package store.

## Commands

### status

Checks for modified packages in the store.

Returns exit code 0 if the content of the package is the same as it was at the
time of unpacking.

### add

Functionally equivalent to [`pnpm add`], except this adds new packages to the
store directly without modifying any projects or files outside of the store.

[`pnpm add`]: add.md

### prune

Removes _unreferenced packages_ from the store.

Unreferenced packages are packages that are not used by any projects on the
system. Packages can become unreferenced after most installation operations, for
instance when dependencies are made redundant.

For example, during `pnpm install`, package `foo@1.0.0` is updated to
`foo@1.0.1`. pnpm will keep `foo@1.0.0` in the store, as it does not
automatically remove packages. If package `foo@1.0.0` is not used by any other
project on the system, it becomes unreferenced. Running `pnpm store prune` would
remove `foo@1.0.0` from the store.

Running `pnpm store prune` is not harmful and has no side effects on your
projects. If future installations require removed packages, pnpm will download
them again.

It is best practice to run `pnpm store prune` occasionally to clean up the
store, but not too frequently. Sometimes, unreferenced packages become required
again. This could occur when switching branches and installing older
dependencies, in which case pnpm would need to re-download all removed packages,
briefly slowing down the installation process.

After pruning, pnpm displays the total size of removed files.

When the [global virtual store] is enabled, `pnpm store prune` also performs mark-and-sweep garbage collection on the global virtual store's `links/` directory. Projects using the store are registered via symlinks in `{storeDir}/v11/projects/`, allowing pnpm to track active usage and safely remove unused packages from the global virtual store.

[global virtual store]: ../settings/node-modules.md#enableglobalvirtualstore

### path

Returns the path to the active store directory.


---

# pnpm team

*Sección: Cli*

Added in: v11.13.0

Manages organization teams and team memberships on the registry.

```sh
pnpm team create <scope:team> [--otp <code>]
pnpm team destroy <scope:team> [--otp <code>]
pnpm team add <scope:team> <user> [--otp <code>]
pnpm team rm <scope:team> <user> [--otp <code>]
pnpm team ls <scope|scope:team>
```

Team references are always written with a leading `@`: `@myorg` for an organization and `@myorg:developers` for a team within it.

## Subcommands

### create

Create a new team in an organization.

```sh
pnpm team create @myorg:developers
```

### destroy

Destroy an existing team.

```sh
pnpm team destroy @myorg:developers
```

### add

Add a user to an existing team.

```sh
pnpm team add @myorg:developers alice
```

### rm

Remove a user from an existing team.

```sh
pnpm team rm @myorg:developers alice
```

### ls

List the teams in an organization, or the members of a team.

```sh
pnpm team ls @myorg
pnpm team ls @myorg:developers
```

Aliases: `list`. If no subcommand is given and the first argument looks like a scope or team, `ls` is assumed, so `pnpm team @myorg` is equivalent to `pnpm team ls @myorg`.

## Options

### --registry &lt;url\&gt;

The base URL of the npm registry to use for the operation. A registry configured for the organization's scope (via [`registries`](../settings/dependency-resolution.md#registries)) is respected.

### --otp &lt;code\&gt;

When the registry requires two-factor authentication, this option supplies a one-time password. It applies to `create`, `destroy`, `add`, and `rm`.

### --parseable

Print the results of `ls` as bare names, one per line, without headers or indentation.

### --json

Print the results of `ls` as a JSON array of names. Takes precedence over `--parseable`.


---

# pnpm test

*Sección: Cli*

Aliases: `run test`, `t`, `tst`

Runs an arbitrary command specified in the package's `test` property of its
`scripts` object. 

The intended usage of the property is to specify a command that runs unit or
integration testing for your program.


---

# pnpm unlink

*Sección: Cli*

Unlinks a system-wide package (inverse of [`pnpm link`](link.md)).

If called without arguments, all linked dependencies will be unlinked inside the
current project.

This is similar to `yarn unlink`, except pnpm re-installs the dependency after
removing the external link.

:::info

If you want to remove a link made with `pnpm link --global <package>`, you should use `pnpm uninstall --global <package>`. 
`pnpm unlink` only removes the links in your current directory.

:::

## Options

### --recursive, -r

Unlink in every package found in subdirectories or in every workspace package,
when executed inside a [workspace](../workspaces.md).

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)


---

# pnpm unpublish

*Sección: Cli*

Added in: v11.0.0

Remove a published package version from the registry.

```sh
pnpm unpublish [<pkg>[@<version>]] [--force]
```

:::warning

Unpublishing is generally discouraged. Most registries (including the public npm registry) restrict when and how packages can be unpublished. Prefer [`pnpm deprecate`](deprecate.md) whenever possible.

:::

## Examples

Unpublish a specific version:

```sh
pnpm unpublish foo@1.0.0
```

Unpublish a range of versions using a semver specifier:

```sh
pnpm unpublish "foo@<2"
```

Unpublish an entire package (all versions). Requires `--force`:

```sh
pnpm unpublish foo --force
```

When run without arguments inside a package directory, pnpm unpublishes the current package version read from the local `package.json`.

## Options

### --force

Required when removing an entire package (all versions) rather than a specific version or range.

### --registry &lt;url\>

The registry to publish to. Defaults to the registry configured for the package.

### --otp &lt;code\>

When the registry requires two-factor authentication, supply the one-time password via this flag or the `PNPM_CONFIG_OTP` environment variable.


---

# pnpm update

*Sección: Cli*

Aliases: `up`, `upgrade`

`pnpm update` updates packages to their latest version based on the specified
range.

When used without arguments, updates all dependencies.

## TL;DR

| Command              | Meaning                                                                  |
|----------------------|--------------------------------------------------------------------------|
|`pnpm up`             | Updates all dependencies, adhering to ranges specified in `package.json` |
|`pnpm up --latest`    | Updates all dependencies to their latest versions                        |
|`pnpm up foo@2`       | Updates `foo` to the latest version on v2                                |
|`pnpm up "@babel/*"` | Updates all dependencies under the `@babel` scope                        |

## Selecting dependencies with patterns

You can use patterns to update specific dependencies.

Update all `babel` packages:

```sh
pnpm update "@babel/*"
```

Update all dependencies, except `webpack`:

```sh
pnpm update "\!webpack"
```

Patterns may also be combined, so the next command will update all `babel` packages, except `core`:

```sh
pnpm update "@babel/*" "\!@babel/core"
```

## Updating GitHub Actions

Added in: v11.16.0

[`pnpm outdated`](outdated.md) can check the GitHub Actions referenced by the repository's workflow files for updates, and `pnpm update` can update them. This is opt-in for every command: pass [`--include-github-actions`](#--include-github-actions), or set [`update.githubActions`](../settings/dependency-resolution.md#updategithubactions) to `true` in `pnpm-workspace.yaml` to enable it by default.

Updated actions are pinned to exact commit hashes, with their release tags preserved in comments:

```yaml
- uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0
```

Checking for updates runs `git ls-remote` against every referenced repository. Actions whose refs cannot be read — for example, an action in a private repository — are skipped with a warning. If the actions are hosted on a different GitHub server (such as a GitHub Enterprise Server), set [`update.githubActionsServer`](../settings/dependency-resolution.md#updategithubactionsserver) (added in v11.17.0).

## Options

### --recursive, -r

Concurrently runs update in all subdirectories with a `package.json` (excluding
node_modules).

Usage examples:

```sh
pnpm --recursive update
# updates all packages up to 100 subdirectories in depth
pnpm --recursive update --depth 100
# update typescript to the latest version in every package
pnpm --recursive update typescript@latest
```

### --latest, -L

Update the dependencies to their latest stable version as determined by their `latest` tags (potentially upgrading the packages across major versions) as long as the version range specified in `package.json` is lower than the `latest` tag (i.e. it will not downgrade prereleases).

### --global, -g

Update global packages.

### --workspace

Tries to link all packages from the workspace. Versions are updated to match the
versions of packages inside the workspace.

If specific packages are updated, the command will fail if any of the updated
dependencies are not found inside the workspace. For instance, the following
command fails if `express` is not a workspace package:

```sh
pnpm up -r --workspace express
```

### --prod, -P

Only update packages in `dependencies` and `optionalDependencies`.

### --dev, -D

Only update packages in `devDependencies`.

### --no-optional

Don't update packages in `optionalDependencies`.

### --interactive, -i

Show outdated dependencies and select which ones to update.

### --no-save

Don't update the ranges in `package.json`.

### --changeset

Added in: v11.16.0

After the update completes, write a [change intent](../versioning.md) — a changesets-compatible `.changeset/*.md` file — declaring a `patch` bump for every workspace package whose `dependencies` or `optionalDependencies` were changed by the update, and a `major` bump when its `peerDependencies` changed. Packages that consume an updated catalog entry via the `catalog:` protocol are included. Private packages, packages without a name, and packages listed in the `ignore` array of `.changeset/config.json` are skipped. If `.changeset/config.json` does not exist, a warning is printed and no changeset is generated.

Set [`update.changeset`](../settings/dependency-resolution.md#updatechangeset) to `true` in `pnpm-workspace.yaml` to enable this behavior by default, and use `--no-changeset` to override the setting for one update.

### --include-github-actions

Added in: v11.16.0

Also update the GitHub Actions referenced by the repository's workflow files. See [Updating GitHub Actions](#updating-github-actions).

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)


---

# pnpm version

*Sección: Cli*

Added in: v11.0.0

Bump the package version.

```sh
pnpm version <newversion>
pnpm version <major|minor|patch|premajor|preminor|prepatch|prerelease|from-git>
pnpm version -r [--dry-run]
```

`<newversion>` can be any of the bump types above or an explicit semver version (e.g. `1.2.3`). Workspaces and the `workspace:` protocol are supported, so cross-references between workspace packages are updated correctly.

When run inside a git repository, `pnpm version` creates a git commit and an annotated tag for the bump. The working tree must be clean (see `--no-git-checks` below) and commits/tags can be disabled with `--no-git-tag-version`. Git commits and tags are always skipped in recursive mode because multiple packages may be bumped to different versions in a single run.

## Usage

```sh
pnpm version patch
pnpm version minor
pnpm version major
pnpm version 2.0.0
pnpm version prerelease --preid beta
```

## Recursive releases

Added in: v11.13.0

Run with `-r` and **no version argument** to consume the pending change intents recorded by [`pnpm change`](change.md):

```sh
pnpm version -r
```

This assembles a release plan from the `.changeset/*.md` intent files and applies it: every package named by an intent is bumped, and so is every package that depends on it through a `workspace:` range. It then writes changelogs and records the consumed intents in `.changeset/ledger.yaml`.

Preview the plan without touching anything:

```sh
pnpm version -r --dry-run
```

Narrow it to part of the workspace with `--filter`. The selection is expanded until it settles, so fixed-group companions and dependents whose ranges the bump invalidates are pulled in automatically.

The working tree must be clean unless `--dry-run` or `--no-git-checks` is passed. See [Release management](../versioning.md) for the full workflow.

## Options

### --preid &lt;prerelease-id\>

The "prerelease identifier" to use as a prefix for the prerelease part of a semver.

```sh
pnpm version prerelease --preid beta
```

### --message, -m &lt;message\>

Commit message. Any `%s` in the message is replaced with the new version. Defaults to `%s`.

```sh
pnpm version patch --message "chore: release v%s"
```

### --tag-version-prefix &lt;prefix\>

Prefix used when creating the git tag. Defaults to `v` (e.g. `v1.2.3`). Set to an empty string to drop the prefix entirely.

### --no-git-tag-version

Do not create a git commit or tag for the version change.

### --no-commit-hooks

Skip git commit hooks (`--no-verify`) when committing the version bump.

### --sign-git-tag

Sign the generated git tag with GPG (`git tag -s`).

### --no-git-checks

Do not check whether the working tree is clean before bumping the version.

### --allow-same-version

Allow setting the version to the current version. This can be useful for CI pipelines.

### --recursive, -r

Apply the version bump to every package in the workspace (optionally narrowed with `--filter`). Git commit and tag creation are skipped in recursive mode.

### --json

Output the list of bumped packages in JSON format.


---

# pnpm view

*Sección: Cli*

Added in: v11.0.0

Aliases: `info`, `show`

View package metadata from the registry.

```sh
pnpm view <pkg>
pnpm view <pkg> [field]
pnpm view [field]
```

## Usage

Show all metadata for a package:

```sh
pnpm view express
```

Show a specific field:

```sh
pnpm view express version
pnpm view express dependencies
pnpm view express dist-tags
```

Show metadata for a specific version:

```sh
pnpm view express@4.18.0
```

When no package name is provided, `pnpm view` searches upward for the nearest project manifest (`package.json`, `package.yaml`, or `package.json5`) and uses its `name` field. If the manifest exists but has no `name`, the command fails.

## Options

### --json

Output the metadata in JSON format.


---

# pnpm whoami

*Sección: Cli*

Added in: v11.0.0

Print the username associated with the current registry credentials.

```sh
pnpm whoami [--registry <url>]
```

If you are not logged in, the command exits with an error. Use [`pnpm login`](login.md) to authenticate first.

## Options

### --registry &lt;url\>

The registry to check. Defaults to the configured default registry.


---

# pnpm why

*Sección: Cli*

Shows all packages that depend on the specified package.

The output is a reverse dependency tree: the searched package appears at the root, with its dependents as branches, walking back to workspace roots.

Duplicate subtrees are deduplicated in the output and shown as "deduped".

## Options

### --recursive, -r

Show the dependency tree for the specified package on every package in
subdirectories or on every workspace package when executed inside a workspace.

### --json

Show information in JSON format.

### --long

Show verbose output.

### --parseable

Show parseable output instead of tree view.

### --global, -g

List packages in the global install directory instead of in the current project.

### --prod, -P

Only display the dependency tree for packages in `dependencies`.

### --dev, -D

Only display the dependency tree for packages in `devDependencies`.

### --depth &lt;number\>

Display only dependencies within a specific depth.

### --only-projects

Display only dependencies that are also projects within the workspace.

### --exclude-peers

Exclude peer dependencies from the results (but dependencies of peer dependencies are not ignored).

### --filter &lt;package_selector\>

[Read more about filtering.](../filtering.md)


---

# pnpm with

*Sección: Cli*

Added in: v11.0.0

Run pnpm at a specific version (or the currently running one) for a single invocation, ignoring the `packageManager` and `devEngines.packageManager` fields of the project's manifest.

```sh
pnpm with <version|current> <args...>
```

The downloaded pnpm is installed using the same mechanism as [`pnpm self-update`](self-update.md) and cached in the global virtual store for reuse on subsequent runs.

## Examples

Run the globally installed pnpm, ignoring the version pinned in the manifest:

```sh
pnpm with current install
```

Run a specific version:

```sh
pnpm with 11.0.0-rc.1 install
```

Use a dist-tag:

```sh
pnpm with next install
```

## Related settings

### pmOnFail

If you want to permanently skip the `packageManager` / `devEngines.packageManager` check (for example, because version management is handled by asdf, mise, Volta, or a similar tool), set the [`pmOnFail`](../settings/cli.md#pmonfail) setting to `ignore` instead of running every command through `pnpm with`:

```yaml title="pnpm-workspace.yaml"
pmOnFail: ignore
```


---

# Catalogmode

*Sección: Settings*

### catalogMode

Added in: v10.12.1

* Default: **manual**
* Type: **manual**, **strict**, **prefer**

Controls if and how dependencies are added to the default catalog, when running `pnpm add`. There are three modes:

- **strict** - only allows dependency versions from the catalog. Adding a dependency outside the catalog's version range will cause an error.
- **prefer** - prefers catalog versions, but will fall back to direct dependencies if no compatible version is found.
- **manual** (default) - does not automatically add dependencies to the catalog.


---

# Cleanupunusedcatalogs

*Sección: Settings*

### cleanupUnusedCatalogs

Added in: v10.15.0

* Default: **false**
* Type: **Boolean**

When set to `true`, pnpm will remove unused catalog entries during installation.


---

# Cpuflag

*Sección: Settings*

### --cpu=&lt;name\>

Added in: v10.14.0

Override CPU architecture of native modules to install. Acceptable values are same as `cpu` field of `package.json`, which comes from `process.arch`.


---

# Enableprepostscripts

*Sección: Settings*

### enablePrePostScripts

* Default: **true**
* Type: **Boolean**

When `true`, pnpm will run any pre/post scripts automatically. So running `pnpm foo`
will be like running `pnpm prefoo && pnpm foo && pnpm postfoo`.


---

# Findby

*Sección: Settings*

### --find-by &lt;finder_name\>

Added in: v10.16.0

Use a [finder function] defined in `.pnpmfile.mjs` to match dependencies by properties other than name.

[finder function]: ../finders.md


---

# Libcflag

*Sección: Settings*

### --libc=&lt;name\>

Added in: v10.14.0

Override libc of native modules to install. Acceptable values are same as `libc` field of `package.json`.


---

# Osflag

*Sección: Settings*

### --os=&lt;name\>

Added in: v10.14.0

Override OS of native modules to install. Acceptable values are same as `os` field of `package.json`, which comes from `process.platform`.


---

# Scriptshell

*Sección: Settings*

### scriptShell

* Default: **null**
* Type: **path**

The shell to use for scripts run with the `pnpm run` command.

For instance, to force usage of Git Bash on Windows:

```
pnpm config set scriptShell "C:\\Program Files\\git\\bin\\bash.exe"
```


---

# Shellemulator

*Sección: Settings*

### shellEmulator

* Default: **false**
* Type: **Boolean**

When `true`, pnpm will use a JavaScript implementation of a [bash-like shell] to
execute scripts.

This option simplifies cross-platform scripting. For instance, by default, the
next script will fail on non-POSIX-compliant systems:

```json
"scripts": {
  "test": "NODE_ENV=test node test.js"
}
```

But if the `shellEmulator` setting is set to `true`, it will work on all
platforms.

:::note

Node.js 22 or higher supports running scripts without pnpm's assistance. For the example above, you can run the `test` script with `node --run test`. However, the `shellEmulator` option has no effect on this. Scripts that depend on POSIX features are required to be run `pnpm run` instead of `node --run` to work in non-POSIX-compliant environments.

:::

[bash-like shell]: https://www.npmjs.com/package/@yarnpkg/shell


---

# Build Settings

*Sección: Settings*

### ignoreScripts

* Default: **false**
* Type: **Boolean**

Do not execute any scripts defined in the project `package.json` and its
dependencies.

:::note

This flag does not prevent the execution of [.pnpmfile.mjs](../pnpmfile.md)

:::

### childConcurrency

* Default: **5**
* Type: **Number**

The maximum number of child processes to allocate simultaneously to build
node_modules.

### sideEffectsCache

* Default: **true**
* Type: **Boolean**

Use and cache the results of (pre/post)install hooks.

When a pre/post install script modify the contents of a package (e.g. build output), pnpm saves the modified package in the global store. On future installs on the same machine, pnpm reuses this cached, prebuilt version—making installs significantly faster.

:::note

You may want to disable this setting if:

1. The install scripts modify files *outside* the package directory (pnpm cannot track or cache these changes).
1. The scripts perform side effects that are unrelated to building the package.

:::

### sideEffectsCacheReadonly

* Default: **false**
* Type: **Boolean**

Only use the side effects cache if present, do not create it for new packages.

### unsafePerm

* Default: **false** IF running as root, ELSE **true**
* Type: **Boolean**

Set to true to enable UID/GID switching when running package scripts.
If set explicitly to false, then installing as a non-root user will fail.

### nodeOptions

* Default: **NULL**
* Type: **String**

Options to pass through to Node.js via the `NODE_OPTIONS` environment variable. This does not impact how pnpm itself is executed but it does impact how lifecycle scripts are called.

To preserve existing `NODE_OPTIONS` you can reference the existing environment variable using `${NODE_OPTIONS}` in your configuration:

```yaml
nodeOptions: "${NODE_OPTIONS:- } --experimental-vm-modules"
```

### verifyDepsBeforeRun

* Default: **install**
* Type: **install**, **warn**, **error**, **prompt**, **false**

This setting allows the checking of the state of dependencies before running scripts. The check runs on `pnpm run` and `pnpm exec` commands. The following values are supported:

- `install` - Automatically runs install if `node_modules` is not up to date.
- `warn` - Prints a warning if `node_modules` is not up to date.
- `prompt` - Prompts the user for permission to run install if `node_modules` is not up to date.
- `error` - Throws an error if `node_modules` is not up to date.
- `false` - Disables dependency checks.

### strictDepBuilds

Added in: v10.3.0

* Default: **true**
* Type: **Boolean**

When `strictDepBuilds` is enabled, the installation will exit with a non-zero exit code if any dependencies have unreviewed build scripts (aka postinstall scripts).

### allowBuilds
 
Added in: v10.26.0
 
A map of package matchers to explicitly allow (`true`) or disallow (`false`) script execution.
 
```yaml
allowBuilds:
  esbuild: true
  core-js: false
  # nx versions with build scripts not listed below will
  # fail by default with ERR_PNPM_IGNORED_BUILDS
  nx@21.6.4 || 21.6.5: true
  nx@21.6.0: false
```

**Git-hosted packages:** a package name on its own never approves builds for a git or tarball dependency — the name alone does not identify the artifact. Approve one either by its exact resolved path (including the commit) or, since v11.11.0, by its repository URL:

```yaml
allowBuilds:
  # Approves any commit from this repository
  'foo@git+ssh://git@example.com/org/foo.git': true
  # Approves only this exact commit
  'bar@git+https://github.com/org/bar.git#abc123': true
```

The repository form lets a trusted git dependency keep running its build scripts across branch updates without re-approving each new commit. The key is the package name, followed by `@` and the git URL, with no `#<ref>` suffix. Matching is exact, so `git+ssh://` and `git+https://` URLs for the same repository are separate keys.

Since v11.19.0, the repository form also approves git-hosted packages that pnpm downloads as a tarball rather than clones — such as `github:` dependencies, which are fetched from `codeload.github.com`. A `foo@git+https://github.com/org/foo.git` entry approves `foo` whether pnpm clones the repository or downloads a tarball. GitLab and Bitbucket tarball downloads are matched the same way. Approving or denying a specific resolved commit by its full tarball dep path continues to work.

Denials by package name are not restricted this way: `foo: false` blocks `foo` whether it comes from the registry or from git.

**Default behavior:** Packages not listed in `allowBuilds` are disallowed by default and are treated as unreviewed. By default, an error is printed ([`strictDepBuilds`](#strictdepbuilds) defaults to `true`). If `strictDepBuilds` is set to `false`, a warning is printed instead.

During install, dependencies with ignored builds that are not yet listed in `allowBuilds` are automatically added to `pnpm-workspace.yaml` with a placeholder value, so you can manually set them to `true` or `false`. The [`--allow-build`](../cli/add.md) flag on `pnpm add` and `pnpm approve-builds` writes its entries here as well.

:::info Migrating from older settings

To migrate these settings automatically, run `pnpx codemod run pnpm-v10-to-v11` from the [Migrating from v10 to v11](../migration.md) guide.

The following settings have been removed in v11 and replaced by `allowBuilds`: `onlyBuiltDependencies`, `onlyBuiltDependenciesFile`, `neverBuiltDependencies`, `ignoredBuiltDependencies`, and `ignoreDepScripts`.

Before:

```yaml
onlyBuiltDependencies:
  - electron
neverBuiltDependencies:
  - core-js
ignoredBuiltDependencies:
  - esbuild
```

After:

```yaml
allowBuilds:
  electron: true
  core-js: false
  esbuild: false
```

:::

### dangerouslyAllowAllBuilds

Added in: v10.9.0

* Default: **false**
* Type: **Boolean**

If set to `true`, all build scripts (e.g. `preinstall`, `install`, `postinstall`) from dependencies will run automatically, without requiring approval.

:::warning

This setting allows all dependencies—including transitive ones—to run install scripts, both now and in the future.
Even if your current dependency graph appears safe:

* Future updates may introduce new, untrusted dependencies.
* Existing packages may add scripts in later versions.
* Packages can be hijacked or compromised and begin executing malicious code.

For maximum safety, only enable this if you’re fully aware of the risks and trust the entire ecosystem you’re pulling from. It’s recommended to review and allow builds explicitly.

:::


---

# CLI & Node.js Settings

*Sección: Settings*

## CLI Settings

### [no-]color

* Default: **auto**
* Type: **auto**, **always**, **never**

Controls colors in the output.

* **auto** - output uses colors when the standard output is a terminal or TTY.
* **always** - ignore the difference between terminals and pipes. You’ll rarely
  want this; in most scenarios, if you want color codes in your redirected
  output, you can instead pass a `--color` flag to the pnpm command to force it
  to use color codes. The default setting is almost always what you’ll want.
* **never** - turns off colors. This is the setting used by `--no-color`.

### loglevel

* Default: **info**
* Type: **debug**, **info**, **warn**, **error**

Any logs at or higher than the given level will be shown.
You can instead pass `--silent` to turn off all output logs.

### useBetaCli

* Default: **false**
* Type: **Boolean**

Experimental option that enables beta features of the CLI. This means that you
may get some changes to the CLI functionality that are breaking changes, or
potentially bugs.

### recursiveInstall

* Default: **true**
* Type: **Boolean**

If this is enabled, the primary behaviour of `pnpm install` becomes that of
`pnpm install -r`, meaning the install is performed on all workspace or
subdirectory packages.

Else, `pnpm install` will exclusively build the package in the current
directory.

### engineStrict

* Default: **false**
* Type: **Boolean**

If this is enabled, pnpm will not install any package that claims to not be
compatible with the current Node version.

Regardless of this configuration, installation will always fail if a project
(not a dependency) specifies an incompatible version in its `engines` field.

### npmPath

* Type: **path**

The location of the npm binary that pnpm uses for some actions, like publishing.

### pmOnFail

Added in: v11.0.0

* Default: **download**
* Type: **download**, **error**, **warn**, **ignore**

Overrides the `onFail` behavior of both the `packageManager` field and `devEngines.packageManager` when the running pnpm version does not match the declared one.

* `download` — download and run the declared pnpm version (this is the default and matches the previous `managePackageManagerVersions: true` behavior).
* `error` — fail the command (equivalent to the previous `packageManagerStrictVersion: true`).
* `warn` — print a warning but continue (equivalent to the previous `packageManagerStrict: false` or `COREPACK_ENABLE_STRICT=0`).
* `ignore` — skip the check entirely (equivalent to the previous `managePackageManagerVersions: false`). Useful when version management is handled by an external tool such as asdf, mise, or Volta.

Can be set via CLI flag, environment variable, or `pnpm-workspace.yaml`:

```sh
pnpm install --pm-on-fail=ignore
pnpm_config_pm_on_fail=ignore pnpm install
```

```yaml title="pnpm-workspace.yaml"
pmOnFail: ignore
```

This setting replaces the removed `managePackageManagerVersions`, `packageManagerStrict`, and `packageManagerStrictVersion` settings, as well as the `COREPACK_ENABLE_STRICT` environment variable.

Migration:

| Removed setting                       | Replace with                   |
| ------------------------------------- | ------------------------------ |
| `managePackageManagerVersions: true`  | `pmOnFail: download` (default) |
| `managePackageManagerVersions: false` | `pmOnFail: ignore`             |
| `packageManagerStrict: false`         | `pmOnFail: warn`               |
| `packageManagerStrictVersion: true`   | `pmOnFail: error`              |
| `COREPACK_ENABLE_STRICT=0`            | `pmOnFail: warn`               |

See also [`pnpm with`](../cli/with.md) for running pnpm at a specific version without changing this setting.

### ignoreWorkspaceRootCheck

* Default: **false**
* Type: **Boolean**

If this is enabled, running `pnpm install`/`pnpm add` from the project's root 
folder will no longer error when `-w`/`--ignore-workspace-root-check` is not 
provided.

## Node.js Settings

### nodeVersion

* Default: the value returned by **node -v**, without the v prefix
* Type: **exact semver version (not a range)**

The Node.js version to use when checking a package's `engines` setting.

If you want to prevent contributors of your project from adding new incompatible dependencies, use `nodeVersion` and `engineStrict` in a `pnpm-workspace.yaml` file at the root of the project:

```yaml
nodeVersion: 12.22.0
engineStrict: true
```

This way, even if someone is using Node.js v22, they will not be able to install a new dependency that doesn't support Node.js v12.22.0.

### runtimeOnFail

Added in: v11.0.0

* Default: **undefined**
* Type: **download**, **error**, **warn**, **ignore**

Overrides the `onFail` field of [`devEngines.runtime`](../package-json.md#devenginesruntime) (and `engines.runtime`) in the root project's `package.json`. This is useful when you want a different local behavior than what is written in the manifest — for instance, forcing pnpm to download the declared runtime even when the manifest sets `onFail: "warn"`:

```yaml title="pnpm-workspace.yaml"
runtimeOnFail: download
```

### nodeDownloadMirrors

Added in: v11.0.0

* Default: **undefined**
* Type: **Record&lt;string, string&gt;**

Configure custom Node.js download mirrors in `pnpm-workspace.yaml`. The keys are release channels (`release`, `rc`, `nightly`, `v8-canary`, etc.) and the values are base URLs.

Here is how pnpm may be configured to download Node.js from a mirror in China:

```yaml
nodeDownloadMirrors:
  release: https://npmmirror.com/mirrors/node/
  rc: https://npmmirror.com/mirrors/node-rc/
  nightly: https://npmmirror.com/mirrors/node-nightly/
```


---

# Dependency Resolution Settings

*Sección: Settings*

### overrides

This field allows you to instruct pnpm to override any dependency in the
dependency graph, including peer dependencies. This is useful for enforcing all your packages to use a single
version of a dependency, backporting a fix, replacing a dependency with a fork, or
removing an unused dependency.

Note that the overrides field can only be set at the root of the project.

An example of the `overrides` field:

```yaml
overrides:
  "foo": "^1.0.0"
  "quux": "npm:@myorg/quux@^1.0.0"
  "bar@^2.1.0": "3.0.0"
  "qar@1>zoo": "2"
```

You may specify the package the overridden dependency belongs to by
separating the package selector from the dependency selector with a ">", for
example `qar@1>zoo` will only override the `zoo` dependency of `qar@1`, not for
any other dependencies.

To keep an overridden version in sync with the version used elsewhere in your workspace, define the version in a [catalog](../catalogs.md) and reference it with the `catalog:` protocol. This way the version is maintained in a single place and referenced from both your dependencies and your overrides:

```yaml title="pnpm-workspace.yaml"
catalog:
  foo: "^1.0.0"

overrides:
  foo: "catalog:"
```

You may also reference a named catalog with `catalog:<name>`. See [Catalogs](../catalogs.md) for more details.

If you find that your use of a certain package doesn't require one of its dependencies, you may use `-` to remove it. For example, if package `foo@1.0.0` requires a large package named `bar` for a function that you don't use, removing it could reduce install time:

```yaml
overrides:
  "foo@1.0.0>bar": "-"
```

This feature is especially useful with `optionalDependencies`, where most optional packages can be safely skipped.

#### Convergence overrides

Added in: v11.13.0

A selector with an **empty range** — `"pkg@"` — is a convergence override. Unlike a regular override, which rewrites every matching edge unconditionally, a convergence override rewrites a dependency edge only when its version satisfies the range that edge declares:

```yaml title="pnpm-workspace.yaml"
overrides:
  "form-data@": 4.0.6
```

With the above, a dependency that declares `form-data: "^4.0.5"` is pinned to `4.0.6`, while one that declares `^3.0.0` keeps its own resolution. This lets compatible consumers converge on a single version — now and for any dependent added in the future — without forcing an incompatible version on the rest of the graph.

Rules:

- The value must be an **exact version**. A range, a dist-tag, or a `-` removal fails with `ERR_PNPM_INVALID_CONVERGENCE_OVERRIDE`. A `catalog:` reference is allowed as long as the catalog entry resolves to an exact version.
- Only plain semver edges participate. Edges declared with `workspace:`, `catalog:`, `npm:`, a dist-tag, or a git/URL specifier have no meaningful "satisfies" relation and are left untouched.
- Convergence overrides cannot be combined with a parent selector: `"parent>pkg@"` is rejected.
- A regular override always wins over a convergence override for the same edge.

When a full resolution finds that every declared range also admits a newer version, pnpm warns that the override is stale and names the version to converge on instead.

:::note

Before v11.13.0, an empty range in an override selector was undocumented and behaved like a bare (unscoped) override.

:::

#### Overriding peer dependencies

Overrides also apply to `peerDependencies`. The behavior depends on the type of version specifier used in the override:

- **Semver ranges** (e.g., `^1.0.0`), **workspace**, and **catalog** protocols: the peer dependency is overridden and remains a peer dependency.
- **Non-range specifiers** such as `link:` or `file:` protocols: the peer dependency is overridden and moved to `dependencies`, since these are not valid peer dependency ranges.
- **Removal** (`-`): the peer dependency is removed entirely.

For example, to override the `react` peer dependency of `react-dom`:

```yaml title="pnpm-workspace.yaml"
overrides:
  "react-dom>react": "18.1.0"
```

### packageExtensions

The `packageExtensions` fields offer a way to extend the existing package definitions with additional information. For example, if `react-redux` should have `react-dom` in its `peerDependencies` but it has not, it is possible to patch `react-redux` using `packageExtensions`:

```yaml
packageExtensions:
  react-redux:
    peerDependencies:
      react-dom: "*"
```

The keys in `packageExtensions` are package names or package names and semver ranges, so it is possible to patch only some versions of a package:

```yaml
packageExtensions:
  react-redux@1:
    peerDependencies:
      react-dom: "*"
```

The following fields may be extended using `packageExtensions`: `dependencies`, `optionalDependencies`, `peerDependencies`, and `peerDependenciesMeta`.

A bigger example:

```yaml
packageExtensions:
  express@1:
    optionalDependencies:
      typescript: "2"
  fork-ts-checker-webpack-plugin:
    dependencies:
      "@babel/core": "1"
    peerDependencies:
      eslint: ">= 6"
    peerDependenciesMeta:
      eslint:
        optional: true
```

:::tip

Together with Yarn, we maintain a database of `packageExtensions` to patch broken packages in the ecosystem.
If you use `packageExtensions`, consider sending a PR upstream and contributing your extension to the [`@yarnpkg/extensions`] database.

:::

[`@yarnpkg/extensions`]: https://github.com/yarnpkg/berry/blob/master/packages/yarnpkg-extensions/sources/index.ts

### allowedDeprecatedVersions

This setting allows muting deprecation warnings of specific packages.

Example:

```yaml
allowedDeprecatedVersions:
  express: "1"
  request: "*"
```

With the above configuration pnpm will not print deprecation warnings about any version of `request` and about v1 of `express`.

### update

Added in: v11.16.0

Settings in this section tune the [`pnpm update`](../cli/update.md) and [`pnpm outdated`](../cli/outdated.md) commands.

#### update.ignoreDeps

Sometimes you can't update a dependency. For instance, the latest version of the dependency started to use ESM but your project is not yet in ESM. Annoyingly, such a package will be always printed out by the `pnpm outdated` command and updated, when running `pnpm update --latest`. However, you may list packages that you don't want to upgrade in the `ignoreDeps` field:

```yaml
update:
  ignoreDeps:
  - load-json-file
```

Patterns are also supported, so you may ignore any packages from a scope: `@babel/*`.

#### update.changeset

Added in: v11.16.0

* Default: **false**
* Type: **Boolean**

When `true`, `pnpm update` writes a [change intent](../versioning.md) after updating workspace manifests, declaring a `patch` bump for every workspace package whose `dependencies` or `optionalDependencies` were changed by the update and a `major` bump when its `peerDependencies` changed. Same as passing [`--changeset`](../cli/update.md#--changeset); pass `--no-changeset` to override the setting for a single run.

#### update.githubActions

Added in: v11.16.0

* Default: **false**
* Type: **Boolean**

When `true`, `pnpm update` and `pnpm outdated` also check the GitHub Actions referenced by the repository's workflow files. Same as passing [`--include-github-actions`](../cli/update.md#--include-github-actions). See [Updating GitHub Actions](../cli/update.md#updating-github-actions).

#### update.githubActionsServer

Added in: v11.17.0

* Default: the `GITHUB_SERVER_URL` environment variable, falling back to **https://github.com**
* Type: **URL**

The base URL of the GitHub server that hosts the repositories of the GitHub Actions referenced by the workflow files (for example, a GitHub Enterprise Server). The URL must use the `https://` or `http://` protocol. Only use `http://` for a trusted server on a trusted network: the refs used to pin actions to commit hashes are fetched over this URL, and unencrypted traffic can be tampered with.

:::info

Before v11.16.0, `update.ignoreDeps` was named `updateConfig.ignoreDependencies`. The deprecated `updateConfig` setting keeps working until the next major version; when both are set, the `update` section takes precedence and a warning is printed.

:::

### supportedArchitectures

You can specify architectures for which you'd like to install optional dependencies, even if they don't match the architecture of the system running the install.

For example, the following configuration tells to install optional dependencies for Windows x64:

```yaml
supportedArchitectures:
  os:
  - win32
  cpu:
  - x64
```

Whereas this configuration will install optional dependencies for Windows, macOS, and the architecture of the system currently running the install. It includes artifacts for both x64 and arm64 CPUs:

```yaml
supportedArchitectures:
  os:
  - win32
  - darwin
  - current
  cpu:
  - x64
  - arm64
```

Additionally, `supportedArchitectures` also supports specifying the `libc` of the system.

### ignoredOptionalDependencies

If an optional dependency has its name included in this array, it will be skipped. For example:

```yaml
ignoredOptionalDependencies:
- fsevents
- "@esbuild/*"
```

### minimumReleaseAge

Added in: v10.16.0

* Default: **1440** (since v11), **0** (before v11)
* Type: **number (minutes)**

To reduce the risk of installing compromised packages, you can delay the installation of newly published versions. In most cases, malicious releases are discovered and removed from the registry within an hour.

`minimumReleaseAge` defines the minimum number of minutes that must pass after a version is published before pnpm will install it. This applies to **all dependencies**, including transitive ones.

For example, the following setting ensures that only packages released at least one day ago can be installed:

```yaml
minimumReleaseAge: 1440
```

### minimumReleaseAgeExclude

Added in: v10.16.0

* Default: **undefined**
* Type: **string[]**

If you set `minimumReleaseAge` but need certain dependencies to always install the newest version immediately, you can list them under `minimumReleaseAgeExclude`. The exclusion works by **package name** and applies to all versions of that package.

Example:

```yaml
minimumReleaseAge: 1440
minimumReleaseAgeExclude:
- webpack
- react
```

In this case, all dependencies must be at least a day old, except `webpack` and `react`, which are installed immediately upon release.

Added in: v10.17.0

You may also use patterns. For instance, allow all packages from your org:

```yaml
minimumReleaseAge: 1440
minimumReleaseAgeExclude:
- '@myorg/*'
```

Added in: v10.19.0

You may also exempt specific versions (or a list of specific versions using a disjunction with `||`). This allows pinning exceptions to mature-time rules:

```yaml
minimumReleaseAge: 1440
minimumReleaseAgeExclude:
- nx@21.6.5
- webpack@4.47.0 || 5.102.1
```

### minimumReleaseAgeIgnoreMissingTime

Added in: v11.0.0

* Default: **true**
* Type: **Boolean**

When `true`, pnpm skips the [`minimumReleaseAge`](#minimumreleaseage) check for a package whose registry metadata does not include the `time` field (some private registries and mirrors omit it). Set to `false` to fail resolution in that case instead of installing the package.

```yaml
minimumReleaseAgeIgnoreMissingTime: false
```

### minimumReleaseAgeStrict

Added in: v11.0.0

* Default: **true** if [`minimumReleaseAge`](#minimumreleaseage) is explicitly configured, **false** otherwise
* Type: **Boolean**

Controls how pnpm behaves when no version of a dependency satisfies the [`minimumReleaseAge`](#minimumreleaseage) constraint within the requested range. When `false`, pnpm falls back to a version that doesn't meet the `minimumReleaseAge` constraint so installation can still succeed. When `true`, pnpm fails resolution instead.

The default depends on whether you configured `minimumReleaseAge` yourself: if you set it explicitly (via `pnpm-workspace.yaml`, the CLI, or environment variables), strict mode is on by default so the setting is enforced. The built-in default of `minimumReleaseAge` (1440 minutes) is non-strict for backward compatibility.

```yaml
minimumReleaseAgeStrict: true
```

### trustPolicy

Added in: v10.21.0

* Default: **off**
* Type: **no-downgrade** | **off**

When set to `no-downgrade`, pnpm will fail if a package's trust level has decreased compared to previous releases. For example, if a package was previously published by a trusted publisher but now only has provenance or no trust evidence, installation will fail. This helps prevent installing potentially compromised versions. Trust checks are based solely on publish date, not semver. A package cannot be installed if any earlier-published version had stronger trust evidence. Starting in v10.24.0, prerelease versions are ignored when evaluating trust evidence for a non-prerelease install, so a trusted prerelease cannot block a stable release that lacks trust evidence.

### trustPolicyExclude

Added in: v10.22.0

* Default: **[]**
* Type: **string[]**

A list of package selectors that should be excluded from the trust policy check. This allows you to install specific packages or versions even if they don't satisfy the `trustPolicy` requirement.

For example:

```yaml
trustPolicy: no-downgrade
trustPolicyExclude:
  - 'chokidar@4.0.3'
  - 'webpack@4.47.0 || 5.102.1'
  - '@babel/core@7.28.5'
```

### trustPolicyIgnoreAfter

Added in: v10.27.0

* Default: **undefined**
* Type: **number (minutes)**

Allows ignoring the trust policy check for packages published more than the specified number of minutes ago. This is useful when enabling strict trust policies, as it allows older versions of packages (which may lack a process for publishing with signatures or provenance) to be installed without manual exclusion, assuming they are safe due to their age.

### trustLockfile

Added in: v11.3.0

* Default: **false**
* Type: **Boolean**

When `true`, `pnpm install` skips the supply-chain verification pass that re-applies [`minimumReleaseAge`](#minimumreleaseage) and [`trustPolicy`](#trustpolicy) to every entry in the loaded lockfile. The install treats the lockfile as already trusted.

Useful in environments where the lockfile is effectively part of the trusted base — closed-source projects where every commit comes from a trusted author. A poisoned lockfile (one a contributor authored under a weaker policy than CI enforces) can slip through, so leave this `false` whenever outside collaborators can edit the lockfile.

On large workspaces the verification pass holds per-package registry metadata in memory for the duration of the install; disabling it cuts memory usage at the cost of the supply-chain check. Most projects with the default `frozenLockfile` CI workflow do not need to set this.

### blockExoticSubdeps

Added in: v10.26.0

* Default: **true**
* Type: **Boolean**

When set to `true`, only direct dependencies (those listed in your root `package.json`) may use exotic sources (like git repositories or direct tarball URLs). All transitive dependencies must be resolved from a trusted source, such as the configured registry, local file paths, workspace links, or trusted GitHub repositories (node, bun, deno).

This setting helps secure the dependency supply chain by preventing transitive dependencies from pulling in code from untrusted locations.

Exotic sources include:
* Git repositories (`git+ssh://...`)
* Direct URL links to tarballs (`https://.../package.tgz`)

### registries

Added in: v11.0.0

* Default: **undefined**
* Type: **Record&lt;string, string&gt;**

Configure registries for scoped packages in `pnpm-workspace.yaml`. The `default` key sets the main registry (equivalent to the `registry` `.npmrc` setting). Scoped keys configure registries for specific package scopes.

```yaml
registries:
  default: https://registry.npmjs.org/
  "@my-org": https://private.example.com/
  "@internal": https://nexus.corp.com/
```

Since v11.11.0, this setting may also be defined in the [global configuration file](../cli/config.md) (`config.yaml`), which is useful for registries that should apply to every project on the machine rather than to a single repository.

### namedRegistries

Added in: v11.1.0

* Default: **undefined**
* Type: **Record&lt;string, string&gt;**

Defines named registry aliases that can be used as a prefix when installing packages, in the style of [vlt's named-registry aliases](https://docs.vlt.sh/cli/registries). For example, with the following configuration:

```yaml title="pnpm-workspace.yaml"
namedRegistries:
  gh: https://npm.pkg.github.example.com/
  work: https://npm.work.example.com/
```

`pnpm add work:@corp/lib@^2.0.0` resolves `@corp/lib@^2.0.0` against `https://npm.work.example.com/`.

The `gh:` alias is built in and points at the [GitHub Packages npm registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-npm-registry) (`https://npm.pkg.github.com/`) by default. Override it under `namedRegistries` for GitHub Enterprise Server.

Authentication is picked up from the existing per-URL `.npmrc` entries (e.g. `//npm.pkg.github.com/:_authToken=...`), so no separate auth mechanism is required.

Since v11.11.0, this setting may also be defined in the [global configuration file](../cli/config.md) (`config.yaml`), so an alias like `work:` can be shared across every project on the machine.


---

# Network & Request Settings

*Sección: Settings*

## Network Settings

### httpsProxy

* Default: **null**
* Type: **url**

A proxy to use for outgoing HTTPS requests. If the `HTTPS_PROXY`, `https_proxy`,
`HTTP_PROXY` or `http_proxy` environment variables are set, their values will be
used instead.

If your proxy URL contains a username and password, make sure to URL-encode them.
For instance:

```yaml
httpsProxy: "https://use%21r:pas%2As@my.proxy:1234/foo"
```

Do not encode the colon (`:`) between the username and password.

### httpProxy

* Default: **null**
* Type: **url**

A proxy to use for outgoing HTTP requests. If the `HTTP_PROXY` or `http_proxy`
environment variables are set, proxy settings will be honored by the underlying
request library.

### noProxy

* Default: **null**
* Type: **String**

A comma-separated string of domain extensions that a proxy should not be used for.

### localAddress

* Default: **undefined**
* Type: **IP Address**

The IP address of the local interface to use when making connections to the npm
registry.

### maxsockets

* Default: **networkConcurrency x 3**
* Type: **Number**

The maximum number of connections to use per origin (protocol/host/port combination).

### strictSsl

* Default: **true**
* Type: **Boolean**

Whether or not to do SSL key validation when making requests to the registry via
HTTPS.

## Request Settings

### gitShallowHosts

* Default: **['github.com', 'gist.github.com', 'gitlab.com', 'bitbucket.com', 'bitbucket.org']**
* Type: **string[]**

When fetching dependencies that are Git repositories, if the host is listed in this setting, pnpm will use shallow cloning to fetch only the needed commit, not all the history.

### networkConcurrency

* Default: **auto (workers × 3 clamped to 16-64)**
* Type: **Number**

Controls the maximum number of HTTP(S) requests to process simultaneously.

As of v10.24.0, pnpm automatically selects a value between 16 and 64 based on the number of workers (networkConcurrency = clamp(workers × 3, 16, 64)). Set this value explicitly to override the automatic scaling.

### fetchRetries

* Default: **2**
* Type: **Number**

How many times to retry if pnpm fails to fetch from the registry.

### fetchRetryFactor

* Default: **10**
* Type: **Number**

The exponential factor for retry backoff.

### fetchRetryMintimeout

* Default: **10000 (10 seconds)**
* Type: **Number**

The lower bound (in milliseconds) of the retry exponential backoff.

### fetchRetryMaxtimeout

* Default: **60000 (1 minute)**
* Type: **Number**

The upper bound (in milliseconds) of the retry exponential backoff.

### fetchTimeout

* Default: **60000 (1 minute)**
* Type: **Number**

The maximum amount of time to wait for HTTP requests to connect and complete.
This time should be enough to download the largest package over a reasonable connection.

### fetchWarnTimeoutMs

Added in: v10.18.0

* Default: **10000 ms (10 seconds)**
* Type: **Number**

A warning message is displayed if a metadata request to the registry takes longer than the specified threshold (in milliseconds).

### fetchMinSpeedKiBps

Added in: v10.18.0

* Default: **50 KiB/s**
* Type: **Number**

A warning message is displayed if the download speed of a tarball from the registry falls below the specified threshold (in KiB/s).


---

# Node-Modules & Hoisting Settings

*Sección: Settings*

## Node-Modules Settings

### modulesDir

* Default: **node_modules**
* Type: **path**

The directory in which dependencies will be installed (instead of
`node_modules`).

### nodeLinker

* Default: **isolated**
* Type: **isolated**, **hoisted**, **pnp**

Defines what linker should be used for installing Node packages.

* **isolated** - dependencies are symlinked from a virtual store at `node_modules/.pnpm`.
* **hoisted** - a flat `node_modules` without symlinks is created. Same as the `node_modules` created by npm or Yarn Classic. One of Yarn's libraries is used for hoisting, when this setting is used. Legitimate reasons to use this setting:
  1. Your tooling doesn't work well with symlinks. A React Native project will most probably only work if you use a hoisted `node_modules`.
  1. Your project is deployed to a serverless hosting provider. Some serverless providers (for instance, AWS Lambda) don't support symlinks. An alternative solution for this problem is to bundle your application before deployment.
  1. If you want to publish your package with [`"bundledDependencies"`].
  1. If you are running Node.js with the [--preserve-symlinks] flag.
* **pnp** - no `node_modules`. Plug'n'Play is an innovative strategy for Node that is [used by Yarn Berry][pnp]. It is recommended to also set `symlink` setting to `false` when using `pnp` as
your linker.

[pnp]: https://yarnpkg.com/features/pnp
[--preserve-symlinks]: https://nodejs.org/api/cli.html#cli_preserve_symlinks
[`"bundledDependencies"`]: https://docs.npmjs.com/cli/v8/configuring-npm/package-json#bundleddependencies

### nodeExperimentalPackageMap

Added in: v11.8.0

* Default: **false**
* Type: **Boolean**

When `true`, pnpm injects the generated `node_modules/.package-map.json` into pnpm-managed Node.js script environments by adding Node's `--experimental-package-map` option to `NODE_OPTIONS`.

The package map is generated during isolated and hoisted installs. This setting only controls whether pnpm passes the generated map to scripts.

CLI and environment configuration use the kebab-case name `node-experimental-package-map`.

```yaml
nodeExperimentalPackageMap: true
```

### nodePackageMapType

Added in: v11.8.0

* Default: **standard**
* Type: **standard**, **loose**

Controls how `node_modules/.package-map.json` is generated.

* **standard** - only declared dependencies are available through the package map.
* **loose** - also maps packages that are reachable through the installed `node_modules` layout, which can allow undeclared hoisted dependencies to resolve.

CLI and environment configuration use the kebab-case name `node-package-map-type`.

```yaml
nodePackageMapType: loose
```

### symlink

* Default: **true**
* Type: **Boolean**

When `symlink` is set to `false`, pnpm creates a virtual store directory without
any symlinks. It is a useful setting together with `nodeLinker=pnp`.

### enableModulesDir

* Default: **true**
* Type: **Boolean**

When `false`, pnpm will not write any files to the modules directory
(`node_modules`). This is useful for when the modules directory is mounted with
filesystem in userspace (FUSE). There is an experimental CLI that allows you to
mount a modules directory with FUSE: [@pnpm/mount-modules].

[@pnpm/mount-modules]: https://www.npmjs.com/package/@pnpm/mount-modules

### virtualStoreDir

* Default: **node_modules/.pnpm**
* Types: **path**

The directory with links to the store. All direct and indirect dependencies of
the project are linked into this directory.

This is a useful setting that can solve issues with long paths on Windows. If
you have some dependencies with very long paths, you can select a virtual store
in the root of your drive (for instance `C:\my-project-store`).

Or you can set the virtual store to `.pnpm` and add it to `.gitignore`. This
will make stacktraces cleaner as paths to dependencies will be one directory
higher.

**NOTE:** the virtual store cannot be shared between several projects. Every
project should have its own virtual store (except for in workspaces where the
root is shared).

### virtualStoreDirMaxLength

* Default:
  * On Linux/macOS: **120**
  * On Windows: **60**
* Types: **number**

Sets the maximum allowed length of directory names inside the virtual store directory (`node_modules/.pnpm`). You may set this to a lower number if you encounter long path issues on Windows.

### virtualStoreOnly

Added in: v11.0.0

* Default: **false**
* Type: **Boolean**

When set to `true`, pnpm populates the virtual store without creating importer symlinks, hoisting, bin links, or running lifecycle scripts. This is useful for pre-populating a store (e.g., in Nix builds) without creating unnecessary project-level artifacts. `pnpm fetch` uses this mode internally.

### packageImportMethod

* Default: **auto**
* Type: **auto**, **hardlink**, **copy**, **clone**, **clone-or-copy**

Controls the way packages are imported from the store (if you want to disable symlinks inside `node_modules`, then you need to change the [nodeLinker] setting, not this one).

* **auto** - try to clone packages from the store. If cloning is not supported
then hardlink packages from the store. If neither cloning nor linking is
possible, fall back to copying
* **hardlink** - hard link packages from the store
* **clone-or-copy** - try to clone packages from the store. If cloning is not supported then fall back to copying
* **copy** - copy packages from the store
* **clone** - clone (AKA copy-on-write or reference link) packages from the store

Cloning is the best way to write packages to node_modules. It is the fastest way and safest way. When cloning is used, you may edit files in your node_modules and they will not be modified in the central content-addressable store.

Unfortunately, not all file systems support cloning. We recommend using a copy-on-write (CoW) file system (for instance, Btrfs instead of Ext4 on Linux) for the best experience with pnpm.

[nodeLinker]: #nodelinker

### modulesCacheMaxAge

* Default: **10080** (7 days in minutes)
* Type: **number**

The time in minutes after which orphan packages from the modules directory should be removed.
pnpm keeps a cache of packages in the modules directory. This boosts installation speed when
switching branches or downgrading dependencies.

### dlxCacheMaxAge

* Default: **1440** (1 day in minutes)
* Type: **number**

The time in minutes after which dlx cache expires.
After executing a dlx command, pnpm keeps a cache that omits the installation step for subsequent calls to the same dlx command.

### enableGlobalVirtualStore

Added in: v10.12.1

* Default: **false**
* Type: **Boolean**

:::note

In pnpm v11, global installs (`pnpm add -g`) and `pnpm dlx` use the global virtual store by default.

:::

When enabled, `node_modules` contains only symlinks to a central virtual store, rather than to `node_modules/.pnpm`. By default, this central store is located at `<store-path>/links` (use `pnpm store path` to find `<store-path>`).

In the central virtual store, each package is hard linked into a directory whose name is the hash of its dependency graph. As a result, all projects on the system can symlink their dependencies from this shared location on disk. This approach is conceptually similar to how [NixOS manages packages], using dependency graph hashes to create isolated and shareable package directories in the Nix store.

> This should not be confused with the global content-addressable store. The actual package files are still hard linked from the content-addressable store—but instead of being linked directly into `node_modules/.pnpm`, they are linked into the global virtual store.

Using a global virtual store can significantly speed up installations when a warm cache is available. However, in CI environments (where caches are typically absent), it may slow down installation. If pnpm detects that it is running in CI, this setting is automatically disabled.

:::important

To support hoisted dependencies when using a global virtual store, pnpm relies on the `NODE_PATH` environment variable. This allows Node.js to resolve packages from the hoisted `node_modules` directory. However, **this workaround does not work with ESM modules**, because Node.js no longer respects `NODE_PATH` when using ESM.

If your dependencies are ESM and they import packages **not declared in their own `package.json`** (which is considered bad practice), you’ll likely run into resolution errors. There are two ways to fix this:
* Use [packageExtensions] to explicitly add the missing dependencies.
* Add the [@pnpm/plugin-esm-node-path] config dependency to your project. This plugin registers a custom ESM loader that restores `NODE_PATH` support for ESM, allowing hoisted dependencies to be resolved correctly.

:::

[packageExtensions]: dependency-resolution.md#packageextensions
[@pnpm/plugin-esm-node-path]: https://github.com/pnpm/plugin-esm-node-path
[NixOS manages packages]: https://nixos.org/guides/how-nix-works/

## Dependency Hoisting Settings

### hoist

* Default: **true**
* Type: **boolean**

When `true`, all dependencies are hoisted to `node_modules/.pnpm/node_modules`. This makes
unlisted dependencies accessible to all packages inside `node_modules`.

### hoistWorkspacePackages

* Default: **true**
* Type: **boolean**

When `true`, packages from the workspaces are symlinked to either `<workspace_root>/node_modules/.pnpm/node_modules` or to `<workspace_root>/node_modules` depending on other hoisting settings (`hoistPattern` and `publicHoistPattern`).

### hoistPattern

* Default: **['\*']**
* Type: **string[]**

Tells pnpm which packages should be hoisted to `node_modules/.pnpm/node_modules`. By
default, all packages are hoisted - however, if you know that only some flawed
packages have phantom dependencies, you can use this option to exclusively hoist
the phantom dependencies (recommended).

For instance:

```yaml
hoistPattern:
- "*eslint*"
- "*babel*"
```

You may also exclude patterns from hoisting using `!`.

For instance:

```yaml
hoistPattern:
- "*types*"
- "!@types/react"
```

### publicHoistPattern

* Default: **[]**
* Type: **string[]**

Unlike `hoistPattern`, which hoists dependencies to a hidden modules directory
inside the virtual store, `publicHoistPattern` hoists dependencies matching
the pattern to the root modules directory. Hoisting to the root modules
directory means that application code will have access to phantom dependencies,
even if they modify the resolution strategy improperly.

This setting is useful when dealing with some flawed pluggable tools that don't
resolve dependencies properly.

For instance:

```yaml
publicHoistPattern:
- "*plugin*"
```

Note: Setting `shamefullyHoist` to `true` is the same as setting
`publicHoistPattern` to `*`.

You may also exclude patterns from hoisting using `!`.

For instance:

```yaml
publicHoistPattern:
- "*types*"
- "!@types/react"
```

### shamefullyHoist

* Default: **false**
* Type: **Boolean**

By default, pnpm creates a semistrict `node_modules`, meaning dependencies have
access to undeclared dependencies but modules outside of `node_modules` do not.
With this layout, most of the packages in the ecosystem work with no issues.
However, if some tooling only works when the hoisted dependencies are in the
root of `node_modules`, you can set this to `true` to hoist them for you.

### hoistingLimits

Added in: v11.5.0

* Default: **none**
* Type: **none**, **workspaces**, **dependencies**

Controls how far dependencies are hoisted when using `nodeLinker: hoisted`. This setting mirrors Yarn's `nmHoistingLimits`.

* **none** - hoist as far as possible (the default).
* **workspaces** - hoist only as far as each workspace package, preventing dependencies from being hoisted above the workspace package that depends on them.
* **dependencies** - hoist only up to each workspace package's direct dependencies, preventing transitive dependencies from being hoisted into the workspace package's `node_modules`.


---

# Other Settings

*Sección: Settings*

### savePrefix

* Default: **'^'**
* Type: **'^'**, **'~'**, **''**, **'='**

Configure how versions of packages installed to a `package.json` file get
prefixed.

For example, if a package has version `1.2.3`, by default its version is set to
`^1.2.3` which allows minor upgrades for that package, but after
`pnpm config set save-prefix='~'` it would be set to `~1.2.3` which only allows
patch upgrades.

Since v11.19.0, `=` is also accepted: newly added dependencies are saved with an
explicit `=` operator (`=1.2.3`), which pins the exact version. `pnpm update`
keeps the `=` operator when it updates such a pin.

This setting is ignored when the added package has a range specified. For
instance, `pnpm add foo@2` will set the version of `foo` in `package.json` to
`2`, regardless of the value of `savePrefix`.

### tag

* Default: **latest**
* Type: **String**

If you `pnpm add` a package and you don't provide a specific version, then it
will install the package at the version registered under the tag from this
setting.

This also sets the tag that is added to the `package@version` specified by the
`pnpm tag` command if no explicit tag is given.

### globalDir

* Default:
  * If the **$XDG_DATA_HOME** env variable is set, then **$XDG_DATA_HOME/pnpm/global**
  * On Windows: **~/AppData/Local/pnpm/global**
  * On macOS: **~/Library/pnpm/global**
  * On Linux: **~/.local/share/pnpm/global**
* Type: **path**

Specify a custom directory to store global packages.

### globalBinDir

* Default:
  * If the **$XDG_DATA_HOME** env variable is set, then **$XDG_DATA_HOME/pnpm/bin**
  * On Windows: **~/AppData/Local/pnpm/bin**
  * On macOS: **~/Library/pnpm/bin**
  * On Linux: **~/.local/share/pnpm/bin**
* Type: **path**

Allows to set the target directory for the bin files of globally installed packages.

:::tip

In pnpm v11, globally installed binaries are stored in a `bin` subdirectory of `PNPM_HOME` instead of directly in `PNPM_HOME`. This prevents internal directories like `global/` and `store/` from polluting shell autocompletion when `PNPM_HOME` is on PATH. After upgrading, run `pnpm setup` to update your shell configuration.

:::

### npmrcAuthFile

Added in: v11.0.0

* Default: **~/.npmrc**
* Type: **path**

The path to a file containing registry authentication tokens. By default, pnpm reads auth tokens from `~/.npmrc` as a fallback for registry authentication. Use this setting to point to a different file instead.

This setting cannot be set in `pnpm-workspace.yaml` at the project level; set it in the global configuration file, via the `--npmrc-auth-file` CLI option, or via the `PNPM_CONFIG_NPMRC_AUTH_FILE` environment variable (the npm-style `NPM_CONFIG_USERCONFIG` is honored as a fallback). A relative path is resolved against the working directory.

### stateDir

* Default:
  * If the **$XDG_STATE_HOME** env variable is set, then **$XDG_STATE_HOME/pnpm**
  * On Windows: **~/AppData/Local/pnpm-state**
  * On macOS: **~/.pnpm-state**
  * On Linux: **~/.local/state/pnpm**
* Type: **path**

The directory where pnpm creates the `pnpm-state.json` file that is currently used only by the update checker.

### cacheDir

* Default:
  * If the **$XDG_CACHE_HOME** env variable is set, then **$XDG_CACHE_HOME/pnpm**
  * On Windows: **~/AppData/Local/pnpm-cache**
  * On macOS: **~/Library/Caches/pnpm**
  * On Linux: **~/.cache/pnpm**
* Type: **path**

The location of the cache (package metadata, dlx cache, and some install verification results).

Like the store, the cache directory is intended to be shared only between mutually trusted users, jobs, and processes. If you configure or restore a shared `cacheDir`, protect it with filesystem permissions so untrusted users cannot write to it.

### useStderr

* Default: **false**
* Type: **Boolean**

When true, all the output is written to stderr.

### updateNotifier

* Default: **true**
* Type: **Boolean**

Set to `false` to suppress the update notification when using an older version of pnpm than the latest.

### preferSymlinkedExecutables

* Default: **true**, when **node-linker** is set to **hoisted** and the system is POSIX
* Type: **Boolean**

Create symlinks to executables in `node_modules/.bin` instead of command shims. This setting is ignored on Windows, where only command shims work.

### ignoreCompatibilityDb

* Default: **false**
* Type: **Boolean**

During installation the dependencies of some packages are automatically patched. If you want to disable this, set this config to `true`.

The patches are applied from Yarn's [`@yarnpkg/extensions`] package.

### resolutionMode

* Default: **highest** (was **lowest-direct** from v8.0.0 to v8.6.12)
* Type: **highest**, **time-based**, **lowest-direct**

When `resolutionMode` is set to `time-based`, dependencies will be resolved the following way:

1. Direct dependencies will be resolved to their lowest versions. So if there is `foo@^1.1.0` in the dependencies, then `1.1.0` will be installed.
1. Subdependencies will be resolved from versions that were published before the last direct dependency was published.

With this resolution mode installations with warm cache are faster. It also reduces the chance of subdependency hijacking as subdependencies will be updated only if direct dependencies are updated.

This resolution mode works only with npm's [full metadata]. So it is slower in some scenarios. However, if you use [Verdaccio] v5.15.1 or newer, you may set the `registrySupportsTimeField` setting to `true`, and it will be really fast.

When `resolutionMode` is set to `lowest-direct`, direct dependencies will be resolved to their lowest versions.

### registrySupportsTimeField

* Default: **false**
* Type: **Boolean**

Set this to `true` if the registry that you are using returns the "time" field in the abbreviated metadata. As of now, only [Verdaccio] from v5.15.1 supports this.

### extendNodePath

* Default: **true**
* Type: **Boolean**

When `true`, pnpm sets the `NODE_PATH` environment variable in command shims
(the wrapper scripts created in `node_modules/.bin`). When `false`, `NODE_PATH`
is not set.

#### Why this is needed

pnpm's [isolated `node_modules` layout] means that a package can only access its
own declared dependencies. However, when a CLI tool runs via a command shim, some
libraries (notably [`import-local`], used by jest, eslint, and others) resolve
modules from the **current working directory** rather than from the binary's own
location. Since the working directory is the project root — not the package inside
the virtual store — the standard `node_modules` resolution from the CWD won't
find the binary's transitive dependencies.

To bridge this gap, pnpm includes two types of paths in `NODE_PATH`:

1. **The package's own dependencies directory** (e.g.,
   `.pnpm/pkg@version/node_modules`) — this allows CWD-based resolution to find
   the correct versions of the package's sibling dependencies.
2. **The hoisted `node_modules` directory** (e.g., `.pnpm/node_modules`) — this
   is the directory where hoisted packages are placed when [`hoistPattern`] is
   set. Node.js cannot discover this directory through its standard resolution
   algorithm, so it must be provided via `NODE_PATH`.

`NODE_PATH` is also essential when [`enableGlobalVirtualStore`] is enabled.
With a global virtual store, packages are symlinked from a central location
outside the project, so Node.js's standard upward `node_modules` traversal from
the binary's real path won't reach the project's own `node_modules` or its hoisted
dependencies. In this case, `NODE_PATH` must include both the project's root
`node_modules` and the hoisted directory at `node_modules/.pnpm/node_modules` to
ensure correct resolution.

#### When to disable

You may set this to `false` if you are certain that none of the CLI tools in your
project resolve modules from the working directory and you are not using a global
virtual store. Disabling it produces slightly simpler command shims.

[isolated `node_modules` layout]: ../symlinked-node-modules-structure.md
[`import-local`]: https://github.com/sindresorhus/import-local
[`hoistPattern`]: node-modules.md#hoistpattern
[`enableGlobalVirtualStore`]: node-modules.md#enableglobalvirtualstore

[`@yarnpkg/extensions`]: https://github.com/yarnpkg/berry/blob/master/packages/yarnpkg-extensions/sources/index.ts
[full metadata]: https://github.com/npm/registry/blob/master/docs/responses/package-metadata.md#full-metadata-format
[Verdaccio]: https://verdaccio.org/

### deployAllFiles

* Default: **false**
* Type: **Boolean**

When deploying a package or installing a local package, all files of the package are copied. By default, if the package has a `"files"` field in the `package.json`, then only the listed files and directories are copied.

### dedupeDirectDeps

* Default: **false**
* Type: **Boolean**

When set to `true`, dependencies that are already symlinked to the root `node_modules` directory of the workspace will not be symlinked to subproject `node_modules` directories.

### optimisticRepeatInstall

Added in: v10.1.0

* Default: **true**
* Type: **Boolean**

When enabled, a fast check will be performed before proceeding to installation. This way a repeat install or an install on a project with everything up-to-date becomes a lot faster.

### requiredScripts

Scripts listed in this array will be required in each project of the workspace. Otherwise, `pnpm -r run <script name>` will fail.

```yaml
requiredScripts:
- build
```

### ci

Added in: v10.12.1

* Default: **true** (when the environment is detected as CI)
* Type: **Boolean**

This setting explicitly tells pnpm whether the current environment is a CI (Continuous Integration) environment.


---

# Peer Dependency Settings

*Sección: Settings*

### autoInstallPeers

* Default: **true**
* Type: **Boolean**

When `true`, any missing non-optional peer dependencies are automatically installed.

#### Version Conflicts

If there are conflicting version requirements for a peer dependency from different packages, pnpm will not install any version of the conflicting peer dependency automatically. Instead, a warning is printed. For example, if one dependency requires `react@^16.0.0` and another requires `react@^17.0.0`, these requirements conflict, and no automatic installation will occur.

#### Conflict Resolution

In case of a version conflict, you'll need to evaluate which version of the peer dependency to install yourself, or update the dependencies to align their peer dependency requirements.

### dedupePeerDependents

* Default: **true**
* Type: **Boolean**

When this setting is set to `true`, packages with peer dependencies will be deduplicated after peers resolution.

For instance, let's say we have a workspace with two projects and both of them have `webpack` in their dependencies. `webpack` has `esbuild` in its optional peer dependencies, and one of the projects has `esbuild` in its dependencies. In this case, pnpm will link two instances of `webpack` to the `node_modules/.pnpm` directory: one with `esbuild` and another one without it:

```
node_modules
  .pnpm
    webpack@1.0.0_esbuild@1.0.0
    webpack@1.0.0
project1
  node_modules
    webpack -> ../../node_modules/.pnpm/webpack@1.0.0/node_modules/webpack
project2
  node_modules
    webpack -> ../../node_modules/.pnpm/webpack@1.0.0_esbuild@1.0.0/node_modules/webpack
    esbuild
```

This makes sense because `webpack` is used in two projects, and one of the projects doesn't have `esbuild`, so the two projects cannot share the same instance of `webpack`. However, this is not what most developers expect, especially since in a hoisted `node_modules`, there would only be one instance of `webpack`. Therefore, you may now use the `dedupePeerDependents` setting to deduplicate `webpack` when it has no conflicting peer dependencies (explanation at the end). In this case, if we set `dedupePeerDependents` to `true`, both projects will use the same `webpack` instance, which is the one that has `esbuild` resolved:

```
node_modules
  .pnpm
    webpack@1.0.0_esbuild@1.0.0
project1
  node_modules
    webpack -> ../../node_modules/.pnpm/webpack@1.0.0_esbuild@1.0.0/node_modules/webpack
project2
  node_modules
    webpack -> ../../node_modules/.pnpm/webpack@1.0.0_esbuild@1.0.0/node_modules/webpack
    esbuild
```

**What are conflicting peer dependencies?** By conflicting peer dependencies we mean a scenario like the following one:

```
node_modules
  .pnpm
    webpack@1.0.0_react@16.0.0_esbuild@1.0.0
    webpack@1.0.0_react@17.0.0
project1
  node_modules
    webpack -> ../../node_modules/.pnpm/webpack@1.0.0_react@17.0.0/node_modules/webpack
    react (v17)
project2
  node_modules
    webpack -> ../../node_modules/.pnpm/webpack@1.0.0_react@16.0.0_esbuild@1.0.0/node_modules/webpack
    esbuild
    react (v16)
```

In this case, we cannot dedupe `webpack` as `webpack` has `react` in its peer dependencies and `react` is resolved from two different versions in the context of the two projects.

### dedupePeers

Added in: v10.33.0

* Default: **false**
* Type: **Boolean**

When enabled, peer dependency suffixes use version-only identifiers (`name@version`) instead of full dep paths, eliminating nested suffixes like `(foo@1.0.0(bar@2.0.0))`. This dramatically reduces the number of package instances in projects with many recursive peer dependencies.

This is different from [`dedupePeerDependents`](#dedupepeerdependents), which deduplicates packages that have the same peer dependencies across different workspace projects. `dedupePeers` simplifies the peer dependency suffix format itself.

### strictPeerDependencies

* Default: **false**
* Type: **Boolean**

If this is enabled, commands will fail if there is a missing or invalid peer
dependency in the tree.

### resolvePeersFromWorkspaceRoot

* Default: **true**
* Type: **Boolean**

When enabled, dependencies of the root workspace project are used to resolve peer dependencies of any projects in the workspace.
It is a useful feature as you can install your peer dependencies only in the root of the workspace, and you can be sure that all projects in the workspace use the same versions of the peer dependencies.

### peerDependencyRules

#### peerDependencyRules.ignoreMissing

pnpm will not print warnings about missing peer dependencies from this list.

For instance, with the following configuration, pnpm will not print warnings if a dependency needs `react` but `react` is not installed:

```yaml
peerDependencyRules:
  ignoreMissing:
  - react
```

Package name patterns may also be used:

```yaml
peerDependencyRules:
  ignoreMissing:
  - "@babel/*"
  - "@eslint/*"
```

#### peerDependencyRules.allowedVersions

Unmet peer dependency warnings will not be printed for peer dependencies of the specified range.

For instance, if you have some dependencies that need `react@16` but you know that they work fine with `react@17`, then you may use the following configuration:

```yaml
peerDependencyRules:
  allowedVersions:
    react: "17"
```

This will tell pnpm that any dependency that has react in its peer dependencies should allow `react` v17 to be installed.

It is also possible to suppress the warnings only for peer dependencies of specific packages. For instance, with the following configuration `react` v17 will be only allowed when it is in the peer dependencies of the `button` v2 package or in the dependencies of any `card` package:

```yaml
peerDependencyRules:
  allowedVersions:
    "button@2>react": "17",
    "card>react": "17"
```

#### peerDependencyRules.allowAny

`allowAny` is an array of package name patterns, any peer dependency matching the pattern will be resolved from any version, regardless of the range specified in `peerDependencies`. For instance:

```yaml
peerDependencyRules:
  allowAny:
  - "@babel/*"
  - "eslint"
```

The above setting will mute any warnings about peer dependency version mismatches related to `@babel/` packages or `eslint`.


---

# Store & Lockfile Settings

*Sección: Settings*

## Store Settings

### storeDir

* Default:
  * If the **$PNPM_HOME** env variable is set, then **$PNPM_HOME/store**
  * If the **$XDG_DATA_HOME** env variable is set, then **$XDG_DATA_HOME/pnpm/store**
  * On Windows: **~/AppData/Local/pnpm/store**
  * On macOS: **~/Library/pnpm/store**
  * On Linux: **~/.local/share/pnpm/store**
* Type: **path**

The location where all the packages are saved on the disk.

The store should be always on the same disk on which installation is happening,
so there will be one store per disk. If there is a home directory on the current
disk, then the store is created inside it. If there is no home on the disk,
then the store is created at the root of the filesystem. For
example, if installation is happening on a filesystem mounted at `/mnt`,
then the store will be created at `/mnt/.pnpm-store`. The same goes for Windows
systems.

It is possible to set a store from a different disk but in that case pnpm will
copy packages from the store instead of hard-linking them, as hard links are
only possible on the same filesystem.

:::important

The pnpm store is intended to be shared only between mutually trusted users, jobs, and processes. If you configure a shared `storeDir`, protect it with filesystem permissions so untrusted users cannot write to it. The store is part of pnpm's trust domain: packages may be hard linked from it, and the store index (`index.db`) records the hashes used to verify cached files.

:::

### verifyStoreIntegrity

* Default: **true**
* Type: **Boolean**

By default, if a file in the store has been modified, the content of this file is checked before linking it to a project's `node_modules`. If `verifyStoreIntegrity` is set to `false`, files in the content-addressable store will not be checked during installation.

This setting helps detect accidental store corruption. It does not make a store that is writable by untrusted users safe, because an attacker who can write to the store can alter both cached package contents and the metadata used to verify them.

### useRunningStoreServer

:::danger

Deprecated feature

:::

* Default: **false**
* Type: **Boolean**

Only allows installation with a store server. If no store server is running,
installation will fail.

### strictStorePkgContentCheck

* Default: **true**
* Type: **Boolean**

Some registries allow the exact same content to be published under different package names and/or versions. This breaks the validity checks of packages in the store. To avoid errors when verifying the names and versions of such packages in the store, you may set the `strictStorePkgContentCheck` setting to `false`.

### frozenStore

Added in: v11.7.0

* Default: **false**
* Type: **Boolean**

Lets `pnpm install` run against a package store that lives on a read-only filesystem — for example a [Nix](https://nixos.org/) store, a read-only bind mount, or an OCI image layer. When enabled, pnpm opens the store's SQLite `index.db` in immutable mode (bypassing the WAL/`-shm` sidecar files that otherwise can't be created on a read-only directory) and suppresses every code path that would write to the store.

Pair it with `--offline` and `--frozen-lockfile` against a fully-populated store:

```sh
pnpm install --frozen-store --offline --frozen-lockfile
```

The store must already contain everything the install needs, including the build output of any package whose lifecycle scripts are approved (or that has a patch applied). Under the [global virtual store](node-modules.md#enableglobalvirtualstore), those package directories live inside the store, so if a required build is missing the install fails up front with `ERR_PNPM_FROZEN_STORE_NEEDS_BUILD` — seed the store with those builds first. If the store is missing its content directory entirely, the install fails fast with `ERR_PNPM_FROZEN_STORE_INCOMPLETE` rather than trying to initialize it.

`frozenStore` is incompatible with `--force` and with a configured pnpr server, since both write into the store. The [side effects cache](build.md#sideeffectscache) is not written either.

:::note

The read-only store open requires Node.js >=22.15.0, >=23.11.0, or >=24.0.0. On older runtimes, `--frozen-store` fails with `ERR_PNPM_FROZEN_STORE_UNSUPPORTED_NODE`.

:::

## Lockfile Settings

### lockfile

* Default: **true**
* Type: **Boolean**

When set to `false`, pnpm won't read or generate a `pnpm-lock.yaml` file.

### preferFrozenLockfile

* Default: **true**
* Type: **Boolean**

When set to `true` and the available `pnpm-lock.yaml` satisfies the
`package.json` dependencies directive, a headless installation is performed. A
headless installation skips all dependency resolution as it does not need to
modify the lockfile.

### lockfileIncludeTarballUrl

* Default: **false**
* Type: **Boolean**

Add the full URL to the package's tarball to every entry in `pnpm-lock.yaml`.

### gitBranchLockfile

* Default: **false**
* Type: **Boolean**

When set to `true`, the generated lockfile name after installation will be named 
based on the current branch name to completely avoid merge conflicts. For example,
if the current branch name is `feature-foo`, the corresponding lockfile name will
be `pnpm-lock.feature-foo.yaml` instead of `pnpm-lock.yaml`. It is typically used 
in conjunction with the command line argument `--merge-git-branch-lockfiles` or by
setting `mergeGitBranchLockfilesBranchPattern` in the `pnpm-workspace.yaml` file.

### mergeGitBranchLockfilesBranchPattern

* Default: **null**
* Type: **Array or null**

This configuration matches the current branch name to determine whether to merge 
all git branch lockfile files. By default, you need to manually pass the 
`--merge-git-branch-lockfiles` command line parameter. This configuration allows 
this process to be automatically completed.

For instance:

```yaml
mergeGitBranchLockfilesBranchPattern:
- main
- release*
```

You may also exclude patterns using `!`.

### peersSuffixMaxLength

* Default: **1000**
* Type: **number**

Max length of the peer IDs suffix added to dependency keys in the lockfile. If the suffix is longer, it is replaced with a hash.


---

# Versioning Settings

*Sección: Settings*

Added in: v11.13.0

These settings configure pnpm's native workspace release management, driven by [`pnpm change`](../cli/change.md) and the bare [`pnpm version -r`](../cli/version.md#recursive-releases). See [Release management](../versioning.md) for the workflow they belong to.

Where two workspace projects publish the same name, a project may be referenced by its `./`-prefixed workspace-relative directory instead of its name in `versioning.fixed`, `versioning.ignore`, and the keys of `versioning.lanes`.

### versioning.fixed

* Default: **[]**
* Type: **string[][]**

Groups of packages that always release together at one shared version. The shared version is the highest current version in the group, bumped by the largest bump any member needs.

```yaml title="pnpm-workspace.yaml"
versioning:
  fixed:
    - ['@example/cli', '@example/napi']
```

A fixed group must move between lanes together, and must sit entirely inside or entirely outside an epic.

### versioning.ignore

* Default: **[]**
* Type: **string[]**

Packages permanently excluded from versioning and dependent propagation. A change intent that requests a real bump for an ignored package fails.

```yaml title="pnpm-workspace.yaml"
versioning:
  ignore:
    - '@example/internal'
```

### versioning.maxBump

* Default: **undefined** (no cap)
* Type: **'patch'**, **'minor'**, **'major'**

Caps the bump a release from the current checkout may apply. It is enforced on the final assembled release plan, after dependent propagation and fixed-group resolution, so a patch-only maintenance branch cannot accidentally ship a minor.

```yaml title="pnpm-workspace.yaml"
versioning:
  maxBump: patch
```

### versioning.lanes

* Default: **{}**
* Type: **Record&lt;string, string&gt;**

Maps a package to the release lane it is on. A lane is a parallel release track that emits `X.Y.Z-<lane>.N` prereleases; every unlisted package is on the reserved default lane, `main`, and releases stable versions.

```yaml title="pnpm-workspace.yaml"
versioning:
  lanes:
    '@example/cli': alpha
```

Lane names may contain only alphanumerics and hyphens, and cannot be purely numeric. `main` is reserved and cannot be assigned — remove the entry instead, or use [`pnpm lane main --filter <pkg>`](../cli/lane.md).

### versioning.epics

* Default: **[]**
* Type: **Array&lt;\{ lead: string, packages: string[] \}&gt;**

Ties a group of member packages to a lead package, constraining every member's major version to a band derived from the lead's major: while the lead is on major `M`, members live in `M*100` … `M*100+99`.

```yaml title="pnpm-workspace.yaml"
versioning:
  epics:
    - lead: '@example/app'
      packages:
        - './packages/**'
        - '!./packages/private-*'
```

`lead` is a package name or a `./`-prefixed workspace directory. `packages` is matched with pnpm's package selectors — name globs, `./`-prefixed directory globs, and `!`-prefixed negations — evaluated in order, last match wins. A package can belong to at most one epic.

See [Epics](../versioning.md#epics) for how the band is enforced and re-based.

### versioning.changelog.storage

* Default: **'registry'**
* Type: **'registry'**, **'repository'**

Where release changelogs live.

With `registry`, no `CHANGELOG.md` is committed: each release's section is composed at publish time and packed into the published tarball on top of the previously published version's changelog.

With `repository`, a `CHANGELOG.md` is committed in every package.

```yaml title="pnpm-workspace.yaml"
versioning:
  changelog:
    storage: repository
```


---

# Aliases

*Sección: Pnpm*

Aliases let you install packages with custom names.

Let's assume you use `lodash` all over your project. There is a bug in `lodash`
that breaks your project. You have a fix but `lodash` won't merge it. Normally
you would either install `lodash` from your fork directly (as a git-hosted
dependency) or publish it with a different name. If you use the second solution
you have to replace all the requires in your project with the new dependency
name (`require('lodash')` => `require('awesome-lodash')`). With aliases, you
have a third option.

Publish a new package called `awesome-lodash` and install it using `lodash` as
its alias:

```
pnpm add lodash@npm:awesome-lodash
```

No changes in code are needed. All the requires of `lodash` will now resolve to
`awesome-lodash`.

Sometimes you'll want to use two different versions of a package in your
project. Easy:

```sh
pnpm add lodash1@npm:lodash@1
pnpm add lodash2@npm:lodash@2
```

Now you can require the first version of lodash via `require('lodash1')` and the
second via `require('lodash2')`.

This gets even more powerful when combined with hooks. Maybe you want to replace
`lodash` with `awesome-lodash` in all the packages in `node_modules`. You can
easily achieve that with the following `.pnpmfile.mjs`:

```js
function readPackage(pkg) {
  if (pkg.dependencies && pkg.dependencies.lodash) {
    pkg.dependencies.lodash = 'npm:awesome-lodash@^1.0.0'
  }
  return pkg
}
  readPackage
}
```


---

# Catalogs

*Sección: Pnpm*

"_Catalogs_" are a [workspace feature](workspaces.md) for defining dependency version ranges as reusable constants. Constants defined in catalogs can later be referenced in `package.json` files.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/PuRUk4mV2jc" title="pnpm Catalogs — A New Tool to Manage Dependencies in monorepos" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen"></iframe>

## The Catalog Protocol (`catalog:`)

Once a catalog is defined in `pnpm-workspace.yaml`,

```yaml title="pnpm-workspace.yaml"
packages:
  - packages/*

# Define a catalog of version ranges.
catalog:
  react: ^18.3.1
  redux: ^5.0.1
```

The `catalog:` protocol can be used instead of the version range itself.

```json title="packages/example-app/package.json"
{
  "name": "@example/app",
  "dependencies": {
    "react": "catalog:",
    "redux": "catalog:"
  }
}
```

This is equivalent to writing a version range (e.g. `^18.3.1`) directly.

```json title="packages/example-app/package.json"
{
  "name": "@example/app",
  "dependencies": {
    "react": "^18.3.1",
    "redux": "^5.0.1"
  }
}
```

You may use the `catalog:` protocol in the next fields:

* `package.json`:
  * `dependencies`
  * `devDependencies`
  * `peerDependencies`
  * `optionalDependencies`
* `pnpm-workspace.yaml`
    * `overrides`

The `catalog:` protocol allows an optional name after the colon (ex: `catalog:name`) to specify which catalog should be used. When a name is omitted, the default catalog is used.

Depending on the scenario, the `catalog:` protocol offers a few [advantages](#advantages) compared to writing version ranges directly that are detailed next.

## Advantages

In a workspace (i.e. monorepo or multi-package repo) it's common for the same dependency to be used by many packages. Catalogs reduce duplication when authoring `package.json` files and provide a few benefits in doing so:

- **Maintain unique versions** — It's usually desirable to have only one version of a dependency in a workspace. Catalogs make this easier to maintain. Duplicated dependencies can conflict at runtime and cause bugs. Duplicates also increase size when using a bundler.
- **Easier upgrades** — When upgrading a dependency, only the catalog entry in `pnpm-workspace.yaml` needs to be edited rather than all `package.json` files using that dependency. This saves time — only one line needs to be changed instead of many.
- **Fewer merge conflicts** — Since `package.json` files do not need to be edited when upgrading a dependency, git merge conflicts no longer happen in these files.

## Defining Catalogs

Catalogs are defined in the `pnpm-workspace.yaml` file. There are two ways to define catalogs.

1. Using the (singular) `catalog` field to create a catalog named `default`.
2. Using the (plural) `catalogs` field to create arbitrarily named catalogs.

:::tip

If you have an existing workspace that you want to migrate to using catalogs, you can use the following [codemod](https://go.codemod.com/pnpm-catalog):

```
pnpx codemod pnpm/catalog
```

:::

### Default Catalog

The top-level `catalog` field allows users to define a catalog named `default`.

```yaml title="pnpm-workspace.yaml"
catalog:
  react: ^18.2.0
  react-dom: ^18.2.0
```

These version ranges can be referenced through `catalog:default`. For the default catalog only, a special `catalog:` shorthand can also be used. Think of `catalog:` as a shorthand that expands to `catalog:default`.

### Named Catalogs

Multiple catalogs with arbitrarily chosen names can be configured under the `catalogs` key.

```yaml title="pnpm-workspace.yaml"
catalogs:
  # Can be referenced through "catalog:react17"
  react17:
    react: ^17.0.2
    react-dom: ^17.0.2

  # Can be referenced through "catalog:react18"
  react18:
    react: ^18.2.0
    react-dom: ^18.2.0
```

A default catalog can be defined alongside multiple named catalogs. This might be useful in a large multi-package repo that's migrating to a newer version of a dependency piecemeal.

```yaml title="pnpm-workspace.yaml"
catalog:
  react: ^16.14.0
  react-dom: ^16.14.0

catalogs:
  # Can be referenced through "catalog:react17"
  react17:
    react: ^17.0.2
    react-dom: ^17.0.2

  # Can be referenced through "catalog:react18"
  react18:
    react: ^18.2.0
    react-dom: ^18.2.0
```

## Publishing

The `catalog:` protocol is removed when running `pnpm publish` or `pnpm pack`. This is similar to the [`workspace:` protocol](workspaces.md#workspace-protocol-workspace), which is [also replaced on publish](workspaces.md#publishing-workspace-packages).

For example,

```json title="packages/example-components/package.json"
{
  "name": "@example/components",
  "dependencies": {
    "react": "catalog:react18",
  }
}
```

Will become the following on publish.

```json title="packages/example-components/package.json"
{
  "name": "@example/components",
  "dependencies": {
    "react": "^18.3.1",
  }
}
```

The `catalog:` protocol replacement process allows the `@example/components` package to be used by other workspaces or package managers.

## Settings


---

# Command line tab-completion

*Sección: Pnpm*

:::info

Completion for pnpm v9+ is incompatible with completion for older pnpm versions.
If you have already installed pnpm completion for a version older than v9, you must uninstall it first to ensure that completion for v9+ works properly.
You can do this by removing the section of code that contains `__tabtab` in your dot files.

:::

Unlike other popular package managers, which usually require plugins, pnpm
supports command line tab-completion for Bash, Zsh, Fish, and similar shells.

To setup autocompletion for Bash, run:

```text
pnpm completion bash > ~/completion-for-pnpm.bash
echo 'source ~/completion-for-pnpm.bash' >> ~/.bashrc
```

To setup autocompletion for Fish, run:

```text
pnpm completion fish > ~/.config/fish/completions/pnpm.fish
```

## g-plane/pnpm-shell-completion

[pnpm-shell-completion] is a shell plugin maintained by Pig Fang on Github.

Features:

- Provide completion for `pnpm --filter <package>`.
- Provide completion for `pnpm remove` command, even in workspace's packages (by specifying `--filter` option).
- Provide completion for scripts in `package.json`.

[pnpm-shell-completion]: https://github.com/g-plane/pnpm-shell-completion


---

# Config Dependencies

*Sección: Pnpm*

Config dependencies allow you to share and centralize configuration files, settings, and hooks across multiple projects. They are installed before all regular dependencies ("dependencies", "devDependencies", "optionalDependencies"), making them ideal for setting up custom hooks, patches, and catalog entries.

Config dependencies help you keep all the hooks, settings, patches, overrides, catalogs, rules in a single place and use them across multiple repositories.

If your config dependency is named following the `pnpm-plugin-*`, `@*/pnpm-plugin-*`, or `@pnpm/plugin-*` pattern, pnpm will automatically load its `pnpmfile.mjs` (falling back to `pnpmfile.cjs`) from the package root.

## How to Add a Config Dependency

Config dependencies are defined in your `pnpm-workspace.yaml`. Their integrity checksums are stored in `pnpm-lock.yaml` (in a dedicated env lockfile document).

For example, running `pnpm add --config my-configs` will add this entry to your `pnpm-workspace.yaml`:

```yaml title="pnpm-workspace.yaml"
configDependencies:
  my-configs: "1.0.0"
```

**Important:**

* Config dependencies **cannot** have their own regular `dependencies`. They **can** declare `optionalDependencies`, but only one level deep — `optionalDependencies` of `optionalDependencies` are ignored.
* Config dependencies **cannot** define lifecycle scripts (like `preinstall`, `postinstall`, etc.).

### Platform-specific binaries via `optionalDependencies`

A config dependency may ship platform-specific binaries via `optionalDependencies`, the same pattern used by tools like esbuild and swc. Each platform-binary package declares its supported platform with `os`, `cpu`, and/or `libc` fields, and pnpm installs only the variant that matches the current host. The matching binary is symlinked next to the parent config dependency in the global virtual store, so `require('my-config-platform-arch')` from inside the config dependency resolves at runtime.

The env lockfile records all platform variants regardless of host platform, so the lockfile stays portable across machines.

Each entry in `optionalDependencies` must be declared with an **exact** version (e.g. `"1.2.3"`) — ranges (`"^1.0.0"`, `"~1.0.0"`) and tags (`"latest"`) are rejected. This keeps config-dep installs reproducible: the resolved subdep can't drift between machines for a parent that's pinned by integrity.

## Usage

### Installing Dependencies Used in Hooks

Config dependencies are installed **before** hooks from your [`.pnpmfile.mjs`] are loaded, allowing you to import logic from config packages.

Example:

```js title=".pnpmfile.mjs"
  readPackage
}
```

[`.pnpmfile.mjs`]: pnpmfile.md

### Updating pnpm Settings Dynamically

Using the [`updateConfig`] hook, you can dynamically update pnpm’s settings using config dependencies.

For example, the following `pnpmfile` adds a new [catalog] entry to pnpm's configuration:

```js title="@myorg/pnpm-plugin-my-catalogs/pnpmfile.mjs"
  updateConfig (config) {
    config.catalogs.default ??= {}
    config.catalogs.default['is-odd'] = '1.0.0'
    return config
  }
}
```

If you install it as config dependency:

```
pnpm add --config @myorg/pnpm-plugin-my-catalogs
```

Then you can run:

```
pnpm add is-odd@catalog:
```

This will install `is-odd@1.0.0` and add the following to your `package.json`:

```json
{
  "dependencies": {
    "is-odd": "catalog:"
  }
}
```

This makes it easy to maintain and share centralized configuration and dependency versions across projects.

[`updateConfig`]: pnpmfile.md#hooksupdateconfigconfig-config--promiseconfig
[catalog]: catalogs.md

### Loading Patch Files

You can reference [patch files] stored inside config dependencies.

Example:

```yaml title="pnpm-workspace.yaml"
configDependencies:
  my-patches: "1.0.0"
patchedDependencies:
  react: "node_modules/.pnpm-config/my-patches/react.patch"
```

[patch files]: cli/patch.md


---

# Configuring

*Sección: Pnpm*

pnpm settings are divided into two categories:

- **Authentication and certificate settings** are stored in INI files. These contain sensitive credentials and should not be committed to your repository. See [Authentication Settings](npmrc.md#auth-file-locations) for details.
- **All other settings** are stored in YAML files: the project `pnpm-workspace.yaml` and the global `config.yaml`.

pnpm also no longer reads settings from the `pnpm` field of `package.json`. Settings should be defined in `pnpm-workspace.yaml`.

## Local project configuration

Project-level settings go in `pnpm-workspace.yaml`:

```yaml title="pnpm-workspace.yaml"
nodeVersion: "22"
saveExact: true
```

## Global configuration

The global YAML config file (`config.yaml`) is located at one of the following paths:

* If the **$XDG_CONFIG_HOME** env variable is set, then **$XDG_CONFIG_HOME/pnpm/config.yaml**
* On Windows: **~/AppData/Local/pnpm/config/config.yaml**
* On macOS: **~/Library/Preferences/pnpm/config.yaml**
* On Linux: **~/.config/pnpm/config.yaml**

The global `rc` file (for registry and auth settings only) is at:

* If the **$XDG_CONFIG_HOME** env variable is set, then **$XDG_CONFIG_HOME/pnpm/rc**
* On Windows: **~/AppData/Local/pnpm/config/rc**
* On macOS: **~/Library/Preferences/pnpm/rc**
* On Linux: **~/.config/pnpm/rc**

## Environment variables

Environment variables whose names start with `pnpm_config_` (or `PNPM_CONFIG_`) are loaded into configuration. These override settings from `pnpm-workspace.yaml` but not CLI arguments.

:::warning

pnpm no longer reads `npm_config_*` environment variables. Use `pnpm_config_*` environment variables instead (e.g., `pnpm_config_registry` instead of `npm_config_registry`).

:::

For example:

```sh
pnpm_config_save_exact=true pnpm add foo
```

If you need pnpm to work across multiple hard drives or filesystems,
please read [the FAQ].

See the [`config` command] for more information on managing configuration.

[the FAQ]: faq.md#does-pnpm-work-across-multiple-drives-or-filesystems
[`config` command]: cli/config.md


---

# Continuous Integration

*Sección: Pnpm*

pnpm can easily be used in various continuous integration systems.

:::note

In all the provided configuration files the store is cached. However, this is not required, and it is not guaranteed that caching the store will make installation faster. So feel free to not cache the pnpm store in your job.

:::

:::important

Only cache pnpm's store and cache directories in locations writable by trusted jobs. Do not let untrusted CI jobs write to a store or metadata cache that trusted jobs later restore. These directories are trusted caches; see the [`storeDir`](settings/store.md#storedir) and [`cacheDir`](settings/other.md#cachedir) settings for details.

:::

:::tip Lockfile behavior in CI

When pnpm detects that it is running in CI, it switches to frozen-lockfile mode automatically. Since v11, pnpm also fails on incompatible lockfiles in CI — if the lockfile was written by a newer pnpm major version, the install will error out instead of silently rewriting it. Upgrade your CI pnpm version to match the one used to generate the lockfile.

:::

## AppVeyor

On [AppVeyor], you can use pnpm for installing your dependencies by adding this
to your `appveyor.yml`:

```yaml title="appveyor.yml"
install:
  - ps: Install-Product node $env:nodejs_version
  - npm install --global corepack@latest
  - corepack enable
  - corepack prepare pnpm@latest-11 --activate
  - pnpm install
```

[AppVeyor]: https://www.appveyor.com

## Azure Pipelines

On Azure Pipelines, you can use pnpm for installing and caching your dependencies by adding this to your `azure-pipelines.yml`:

```yaml title="azure-pipelines.yml"
variables:
  pnpm_config_cache: $(Pipeline.Workspace)/.pnpm-store

steps:
  - task: Cache@2
    inputs:
      key: 'pnpm | "$(Agent.OS)" | pnpm-lock.yaml'
      path: $(pnpm_config_cache)
    displayName: Cache pnpm

  - script: |
      npm install --global corepack@latest
      corepack enable
      corepack prepare pnpm@latest-11 --activate
      pnpm config set store-dir $(pnpm_config_cache)
    displayName: "Setup pnpm"

  - script: |
      pnpm install
      pnpm run build
    displayName: "pnpm install and build"
```

## Bitbucket Pipelines

You can use pnpm for installing and caching your dependencies:

```yaml title=".bitbucket-pipelines.yml"
definitions:
  caches:
    pnpm: $BITBUCKET_CLONE_DIR/.pnpm-store

pipelines:
  pull-requests:
    "**":
      - step:
          name: Build and test
          image: node:24.14.1
          script:
            - npm install --global corepack@latest
            - corepack enable
            - corepack prepare pnpm@latest-11 --activate
            - pnpm install
            - pnpm run build # Replace with your build/test…etc. commands
          caches:
            - pnpm
```

## CircleCI

On CircleCI, you can use pnpm for installing and caching your dependencies by adding this to your `.circleci/config.yml`:

```yaml title=".circleci/config.yml"
version: 2.1

jobs:
  build: # this can be any name you choose
    docker:
      - image: node:18
    resource_class: large
    parallelism: 10

    steps:
      - checkout
      - restore_cache:
          name: Restore pnpm Package Cache
          keys:
            - pnpm-packages-{{ checksum "pnpm-lock.yaml" }}
      - run:
          name: Install pnpm package manager
          command: |
            npm install --global corepack@latest
            corepack enable
            corepack prepare pnpm@latest-11 --activate
            pnpm config set store-dir .pnpm-store
      - run:
          name: Install Dependencies
          command: |
            pnpm install
      - save_cache:
          name: Save pnpm Package Cache
          key: pnpm-packages-{{ checksum "pnpm-lock.yaml" }}
          paths:
            - .pnpm-store
```

## GitHub Actions

On GitHub Actions, you can use pnpm for installing and caching your dependencies
like so (belongs in `.github/workflows/NAME.yml`):

```yaml title=".github/workflows/NAME.yml"
name: pnpm Example Workflow
on:
  push:

jobs:
  build:
    runs-on: ubuntu-24.04
    strategy:
      matrix:
        node-version: [24]
    steps:
      - uses: actions/checkout@v6
      - name: Install pnpm
        uses: pnpm/action-setup@8912a9102ac27614460f54aedde9e1e7f9aec20d # v6.0.5
        with:
          version: 11
      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v6
        with:
          node-version: ${{ matrix.node-version }}
          cache: "pnpm"
      - name: Install dependencies
        run: pnpm install
```

## GitLab CI

On GitLab, you can use pnpm for installing and caching your dependencies
like so (belongs in `.gitlab-ci.yml`):

```yaml title=".gitlab-ci.yml"
stages:
  - build

build:
  stage: build
  image: node:24.14.1
  before_script:
    - npm install --global corepack@latest
    - corepack enable
    - corepack prepare pnpm@latest-11 --activate
    - pnpm config set store-dir .pnpm-store
  script:
    - pnpm install # install dependencies
  cache:
    key:
      files:
        - pnpm-lock.yaml
    paths:
      - .pnpm-store
```

## Jenkins

You can use pnpm for installing and caching your dependencies:

```title="Jenkinsfile"
pipeline {
    agent {
        docker {
            image 'node:lts-bullseye-slim'
            args '-p 3000:3000'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'npm install --global corepack@latest'
                sh 'corepack enable'
                sh 'corepack prepare pnpm@latest-11 --activate'
                sh 'pnpm install'
            }
        }
    }
}
```

## Semaphore

On [Semaphore], you can use pnpm for installing and caching your dependencies by
adding this to your `.semaphore/semaphore.yml` file:

```yaml title=".semaphore/semaphore.yml"
version: v1.0
name: Semaphore CI pnpm example
agent:
  machine:
    type: e1-standard-2
    os_image: ubuntu2404
blocks:
  - name: Install dependencies
    task:
      jobs:
        - name: pnpm install
          commands:
            - npm install --global corepack@latest
            - corepack enable
            - corepack prepare pnpm@latest-11 --activate
            - checkout
            - cache restore node-$(checksum pnpm-lock.yaml)
            - pnpm install
            - cache store node-$(checksum pnpm-lock.yaml) $(pnpm store path)
```

[Semaphore]: https://semaphoreci.com

## Travis

On [Travis CI], you can use pnpm for installing your dependencies by adding this
to your `.travis.yml` file:

```yaml title=".travis.yml"
cache:
  npm: false
  directories:
    - "~/.pnpm-store"
before_install:
  - npm install --global corepack@latest
  - corepack enable
  - corepack prepare pnpm@latest-11 --activate
  - pnpm config set store-dir ~/.pnpm-store
install:
  - pnpm install
```

[Travis CI]: https://travis-ci.org


---

# Working with Docker

*Sección: Pnpm*

:::note

It is impossible to create reflinks or hardlinks between a Docker container and the host filesystem during build time.
The next best thing you can do is using BuildKit cache mount to share cache between builds. Alternatively, you may use
[podman] because it can mount Btrfs volumes during build time.
If you use BuildKit cache mounts, keep the pnpm store cache scoped to mutually trusted builds. A store cache that can be written by an untrusted build should not be reused by trusted builds.

:::

[podman]: podman.md

## Official pnpm base image

An official pnpm base image is published to GitHub Container Registry as [`ghcr.io/pnpm/pnpm`](https://github.com/pnpm/pnpm/pkgs/container/pnpm). It is based on `debian:stable-slim` and contains only the pnpm [standalone binary] — Node.js is **not** bundled. This lets you pick the Node.js version yourself (inside your Dockerfile or at runtime) instead of being locked to whatever Node version a base image ships with.

[standalone binary]: installation.md#using-a-standalone-script

### Tags

| Tag                   | Meaning                                                                 |
| --------------------- | ----------------------------------------------------------------------- |
| `<version>`           | Exact, immutable (e.g. `11.0.0`). Includes prereleases.                 |
| `<major>`             | Tracks the latest stable release within that major (e.g. `11`).         |
| `latest`              | Most recent stable pnpm release. Not updated for prereleases.           |

Supported platforms: `linux/amd64`, `linux/arm64`.

### Installing Node.js

Use [`pnpm runtime set`](cli/runtime.md) with the global flag so the `node` binary is discoverable on `PATH` in subsequent layers and at runtime:

```dockerfile
FROM ghcr.io/pnpm/pnpm:11
RUN pnpm runtime set node 22 -g
WORKDIR /app
COPY . .
RUN pnpm install --frozen-lockfile
CMD ["node", "index.js"]
```

Or let pnpm install Node.js automatically from [`devEngines.runtime`](package-json.md#devenginesruntime) in your `package.json`:

```json title="package.json"
{
  "devEngines": {
    "runtime": {
      "name": "node",
      "version": "22.x",
      "onFail": "download"
    }
  }
}
```

```dockerfile
FROM ghcr.io/pnpm/pnpm:11
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile
COPY . .
CMD ["pnpm", "start"]
```

### When to use this image

- You want the Node.js version to be pinned by your project (via `pnpm runtime set` or `devEngines.runtime`) rather than by the base image.
- You want to upgrade pnpm and Node.js independently.
- You prefer a minimal Debian base without the Node.js build toolchain.

If you already have a preferred Node.js base image (e.g. `node:XX-slim`), the recipes further down this page remain a fine choice.

## Minimizing Docker image size and build time

* Use a small image, e.g. `node:XX-slim`.
* Leverage multi-stage if possible and makes sense.
* Leverage BuildKit cache mounts.

### Example 1: Build a bundle in a Docker container

Since `devDependencies` is only necessary for building the bundle, `pnpm install --prod` will be a separate stage
from `pnpm install` and `pnpm run build`, allowing the final stage to copy only necessary files from the earlier
stages, minimizing the size of the final image.

```text title=".dockerignore"
node_modules
.git
.gitignore
*.md
dist
```

```dockerfile title="Dockerfile"
FROM node:24-slim AS base
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME/bin:$PATH"
RUN corepack enable
COPY . /app
WORKDIR /app

FROM base AS prod-deps
RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --prod --frozen-lockfile

FROM base AS build
RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --frozen-lockfile
RUN pnpm run build

FROM base
COPY --from=prod-deps /app/node_modules /app/node_modules
COPY --from=build /app/dist /app/dist
EXPOSE 8000
CMD [ "pnpm", "start" ]
```

### Example 2: Build multiple Docker images in a monorepo

Assuming you have a monorepo with 3 packages: app1, app2, and common; app1 and app2 depend on common but not each other.

You want to save only necessary dependencies for each package, `pnpm deploy` should help you with copying only necessary files and packages.

```text title="Structure of the monorepo"
./
├── Dockerfile
├── .dockerignore
├── .gitignore
├── packages/
│   ├── app1/
│   │   ├── dist/
│   │   ├── package.json
│   │   ├── src/
│   │   └── tsconfig.json
│   ├── app2/
│   │   ├── dist/
│   │   ├── package.json
│   │   ├── src/
│   │   └── tsconfig.json
│   └── common/
│       ├── dist/
│       ├── package.json
│       ├── src/
│       └── tsconfig.json
├── pnpm-lock.yaml
├── pnpm-workspace.yaml
└── tsconfig.json
```

```yaml title="pnpm-workspace.yaml"
packages:
  - 'packages/*'
syncInjectedDepsAfterScripts:
- build
injectWorkspacePackages: true
```

```text title=".dockerignore"
node_modules
.git
.gitignore
*.md
dist
```

```dockerfile title="Dockerfile"
FROM node:24-slim AS base
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME/bin:$PATH"
RUN corepack enable

FROM base AS build
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --frozen-lockfile
RUN pnpm run -r build
RUN pnpm deploy --filter=app1 --prod /prod/app1
RUN pnpm deploy --filter=app2 --prod /prod/app2

FROM base AS app1
COPY --from=build /prod/app1 /prod/app1
WORKDIR /prod/app1
EXPOSE 8000
CMD [ "pnpm", "start" ]

FROM base AS app2
COPY --from=build /prod/app2 /prod/app2
WORKDIR /prod/app2
EXPOSE 8001
CMD [ "pnpm", "start" ]
```

Run the following commands to build images for app1 and app2:

```sh
docker build . --target app1 --tag app1:latest
docker build . --target app2 --tag app2:latest
```

### Example 3: Build on CI/CD

On CI or CD environments, the BuildKit cache mounts might not be available, because the VM or container is ephemeral and only normal docker cache will work.

So an alternative is to use a typical Dockerfile with layers that are built incrementally, for this scenario, `pnpm fetch` is the best option, as it only needs the `pnpm-lock.yaml` file and the layer cache will only be lost when you change the dependencies.

```dockerfile title="Dockerfile"
FROM node:24-slim AS base

ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME/bin:$PATH"
RUN corepack enable

FROM base AS prod

COPY pnpm-lock.yaml /app
WORKDIR /app
RUN pnpm fetch --prod

COPY . /app
RUN pnpm run build

FROM base
COPY --from=prod /app/node_modules /app/node_modules
COPY --from=prod /app/dist /app/dist
EXPOSE 8000
CMD [ "pnpm", "start" ]
```


---

# Error Codes

*Sección: Pnpm*

## ERR_PNPM_UNEXPECTED_STORE

A modules directory is present and is linked to a different store directory.

If you changed the store directory intentionally, run `pnpm install` and pnpm will reinstall the dependencies using the new store.

## ERR_PNPM_NO_MATCHING_VERSION_INSIDE_WORKSPACE

A project has a workspace dependency that does not exist in the workspace.

For instance, package `foo` has `bar@1.0.0` in the `dependencies`:

```json
{
  "name": "foo",
  "version": "1.0.0",
  "dependencies": {
    "bar": "workspace:1.0.0"
  }
}
```

However, there is only `bar@2.0.0` in the workspace, so `pnpm install` will fail.

To fix this error, all dependencies that use the [workspace protocol] should be updated to use versions of packages that are present in the workspace. This can be done either manually or using the `pnpm -r update` command.

[workspace protocol]: workspaces.md#workspace-protocol-workspace

## ERR_PNPM_PEER_DEP_ISSUES

`pnpm install` will fail if the project has unresolved peer dependencies or the peer dependencies are not matching the wanted ranges. To fix this, install the missing peer dependencies.

You may also selectively ignore these errors using the [peerDependencyRules.ignoreMissing] and [peerDependencyRules.allowedVersions] settings.

[peerDependencyRules.ignoreMissing]: settings/peer-dependencies.md#peerdependencyrulesignoremissing
[peerDependencyRules.allowedVersions]: settings/peer-dependencies.md#peerdependencyrulesallowedversions

## ERR_PNPM_OUTDATED_LOCKFILE

This error happens when installation cannot be performed without changes to the lockfile. This might happen in a CI environment if someone has changed a `package.json` file in the repository without running `pnpm install` afterwards. Or someone forgot to commit the changes to the lockfile.

To fix this error, just run `pnpm install` and commit the changes to the lockfile.

## ERR\_PNPM\_TARBALL\_INTEGRITY

This error indicates that the downloaded package's tarball did not match the expected integrity checksum.

If you use the npm registry (`registry.npmjs.org`), then this probably means that the integrity in your lockfile is incorrect.
This might happen if a lockfile had badly resolved merge conflicts.

If you use a registry that allows to override existing versions of a package, then it might mean that in your local metadata cache you have the integrity checksum of an older version of the package. In this case, you should run `pnpm store prune`. This command will remove your local metadata cache. Then you can retry the command that failed.

But also be careful and verify that the package is downloaded from the right URL. The URL should be printed in the error message.

## ERR_PNPM_MISMATCHED_RELEASE_CHANNEL

The config field `use-node-version` defines a release channel different from version suffix.

For example:
* `rc/20.0.0` defines an `rc` channel but the version is that of a stable release.
* `release/20.0.0-rc.0` defines a `release` channel but the version is that of an RC release.

To fix this error, either remove the release channel prefix or correct the version suffix.

Note that it is not allowed to specify node versions like `lts/Jod`.
The correct syntax for stable release is strictly X.Y.Z or release/X.Y.Z.

## ERR_PNPM_INVALID_NODE_VERSION

The value of config field `use-node-version` has an invalid syntax.

Below are the valid forms of `use-node-version`:
* Stable release:
  * `X.Y.Z` (`X`, `Y`, `Z` are integers)
  * `release/X.Y.Z` (`X`, `Y`, `Z` are integers)
* RC release:
  * `X.Y.Z-rc.W` (`X`, `Y`, `Z`, `W` are integers)
  * `rc/X.Y.Z-rc.W` (`X`, `Y`, `Z`, `W` are integers)


---

# Frequently Asked Questions

*Sección: Pnpm*

## Why does my `node_modules` folder use disk space if packages are stored in a global store?

pnpm creates [hard links] from the global store to the project's `node_modules`
folders. Hard links point to the same place on the disk where the original
files are. So, for example, if you have `foo` in your project as a dependency
and it occupies 1MB of space, then it will look like it occupies 1MB of space in
the project's `node_modules` folder and the same amount of space in the global
store. However, that 1MB is *the same space* on the disk addressed from two
different locations. So in total `foo` occupies 1MB, not 2MB.

[hard links]: https://en.wikipedia.org/wiki/Hard_link

For more on this subject:

* [Why do hard links seem to take the same space as the originals?](https://unix.stackexchange.com/questions/88423/why-do-hard-links-seem-to-take-the-same-space-as-the-originals)
* [A thread from the pnpm chat room](https://gist.github.com/zkochan/106cfef49f8476b753a9cbbf9c65aff1)
* [An issue in the pnpm repo](https://github.com/pnpm/pnpm/issues/794)

## Does it work on Windows?

Short answer: Yes.
Long answer: Using symbolic linking on Windows can sometimes be problematic,
however, pnpm has a workaround. For Windows, if the [Developer Mode](https://learn.microsoft.com/windows/advanced-settings/developer-mode) is off, we use [junctions] instead.

[junctions]: https://docs.microsoft.com/en-us/windows/win32/fileio/hard-links-and-junctions

## But the nested `node_modules` approach is incompatible with Windows?

Early versions of npm had issues because of nesting all `node_modules` (see
[this issue]). However, pnpm does not create deep folders, it stores all packages
flatly and uses symbolic links to create the dependency tree structure.

[this issue]: https://github.com/nodejs/node-v0.x-archive/issues/6960

## What about circular symlinks?

Although pnpm uses linking to put dependencies into `node_modules` folders,
circular symlinks are avoided because parent packages are placed into the same
`node_modules` folder in which their dependencies are. So `foo`'s dependencies
are not in `foo/node_modules`, but `foo` is in `node_modules` together with its
own dependencies.

## Why have hard links at all? Why not symlink directly to the global store?

One package can have different sets of dependencies on one machine.

In project **A** `foo@1.0.0` can have a dependency resolved to `bar@1.0.0`, but
in project **B** the same dependency of `foo` might resolve to `bar@1.1.0`; so,
pnpm hard links `foo@1.0.0` to every project where it is used, in order to
create different sets of dependencies for it.

Direct symlinking to the global store would work with Node's
`--preserve-symlinks` flag, however, that approach comes with a plethora of its
own issues, so we decided to stick with hard links. For more details about why
this decision was made, see [this issue][eps-issue].

[eps-issue]: https://github.com/nodejs/node-eps/issues/46

## Does pnpm work across different subvolumes in one Btrfs partition?

While Btrfs does not allow cross-device hardlinks between different subvolumes in a single partition, it does permit reflinks. As a result, pnpm utilizes reflinks to share data between these subvolumes.

## Does pnpm work across multiple drives or filesystems?

The package store should be on the same drive and filesystem as installations,
otherwise packages will be copied, not linked. This is due to a limitation in
how hard linking works, in that a file on one filesystem cannot address a
location in another. See [Issue #712] for more details.

pnpm functions differently in the 2 cases below:

[Issue #712]: https://github.com/pnpm/pnpm/issues/712

### Store path is specified

If the store path is specified via [the store config](configuring.md), then copying
occurs between the store and any projects that are on a different disk.

If you run `pnpm install` on disk `A`, then the pnpm store must be on disk `A`.
If the pnpm store is located on disk `B`, then all required packages will be
directly copied to the project location instead of being linked. This severely
inhibits the storage and performance benefits of pnpm.

### Store path is NOT specified

If the store path is not set, then multiple stores are created (one per drive or
filesystem).

If installation is run on disk `A`, the store will be created on `A`
`.pnpm-store` under the filesystem root.  If later the installation is run on
disk `B`, an independent store will be created on `B` at `.pnpm-store`. The
projects would still maintain the benefits of pnpm, but each drive may have
redundant packages.

## What does `pnpm` stand for?

`pnpm` stands for `performant npm`.
[@rstacruz](https://github.com/rstacruz/) came up with the name.

## `pnpm` does not work with &lt;YOUR-PROJECT-HERE>?

In most cases it means that one of the dependencies require packages not
declared in `package.json`. It is a common mistake caused by flat
`node_modules`. If this happens, this is an error in the dependency and the
dependency should be fixed. That might take time though, so pnpm supports
workarounds to make the buggy packages work.

### Solution 1

In case there are issues, you can use the [`nodeLinker: hoisted`] setting.
This creates a flat `node_modules` structure similar to the one created by `npm`.

[`nodeLinker: hoisted`]: settings/node-modules.md#nodelinker

### Solution 2

In the following example, a dependency does **not** have the `iterall` module in
its own list of deps.

The easiest solution to resolve missing dependencies of the buggy packages is to
**add `iterall` as a dependency to our project's `package.json`**.

You can do so, by installing it via `pnpm add iterall`, and will be
automatically added to your project's `package.json`.

```json
  "dependencies": {
    ...
    "iterall": "^1.2.2",
    ...
  }
```

### Solution 3

One of the solutions is to use [hooks](pnpmfile.md#hooks) for adding the missing
dependencies to the package's `package.json`.

An example was [Webpack Dashboard] which wasn't working with `pnpm`. It has
since been resolved such that it works with `pnpm` now.

It used to throw an error:

```console
Error: Cannot find module 'babel-traverse'
  at /node_modules/inspectpack@2.2.3/node_modules/inspectpack/lib/actions/parse
```

The problem was that `babel-traverse` was used in `inspectpack` which
was used by `webpack-dashboard`, but `babel-traverse` wasn't specified in
`inspectpack`'s `package.json`. It still worked with `npm` and `yarn` because
they create flat `node_modules`.

The solution was to create a `.pnpmfile.mjs` with the following contents:

```js
  readPackage: (pkg) => {
    if (pkg.name === "inspectpack") {
      pkg.dependencies['babel-traverse'] = '^6.26.0';
    }
    return pkg;
  }
}
```

After creating a `.pnpmfile.mjs`, delete `pnpm-lock.yaml` only - there is no need
to delete `node_modules`, as pnpm hooks only affect module resolution. Then,
rebuild the dependencies & it should be working.

[Webpack Dashboard]: https://github.com/pnpm/pnpm/issues/1043


---

# Feature Comparison

*Sección: Pnpm*

| Feature                          |pnpm              |Yarn              |npm               | Notes |
| ---                              |:--:              |:--:              |:--:              | ---   |
| [Workspace support]              |:white_check_mark:|:white_check_mark:|:white_check_mark:|
| Isolated `node_modules`          |:white_check_mark:|:white_check_mark:|:white_check_mark:| Default in pnpm. |
| [Hoisted `node_modules`]         |:white_check_mark:|:white_check_mark:|:white_check_mark:| Default in npm. |
| Plug'n'Play                      |:white_check_mark:|:white_check_mark:|:x:               | Default in Yarn. |
| [Autoinstalling peers]           |:white_check_mark:|:x:               |:white_check_mark:|
| Zero-Installs                    |:x:               |:white_check_mark:|:x:               |
| [Patching dependencies]          |:white_check_mark:|:white_check_mark:|:x:               |
| [Managing runtimes]              |:white_check_mark:|:x:               |:x:               |
| [Managing versions of itself]    |:white_check_mark:|:white_check_mark:|:x:               |
| Has a lockfile                   |:white_check_mark:|:white_check_mark:|:white_check_mark:| `pnpm-lock.yaml`, `yarn.lock`, `package-lock.json`. |
| [Overrides support]              |:white_check_mark:|:white_check_mark:|:white_check_mark:| Known as "resolutions" in Yarn. |
| Content-addressable storage      |:white_check_mark:|:white_check_mark:|:x:               | Yarn uses a CAS when `nodeLinker` is set to `pnpm`. |
| [Dynamic package execution]      |:white_check_mark:|:white_check_mark:|:white_check_mark:| `pnpm dlx`, `yarn dlx`, `npx`. |
| [Side-effects cache]             |:white_check_mark:|:x:               |:x:               |
| [Catalogs]                       |:white_check_mark:|:x:               |:x:               |
| [Config dependencies]            |:white_check_mark:|:x:               |:x:               |
| [JSR registry support]           |:white_check_mark:|:white_check_mark:|:x:               |
| [Auto-install before script run] |:white_check_mark:|:x:               |:x:               | In Yarn, Plug'n'Play ensures dependencies are always up to date. |
| [Hooks]                          |:white_check_mark:|:white_check_mark:|:x:               |
| [Build script security]          |:white_check_mark:|:x:               |:x:               |
| [SBOM generation]                |:white_check_mark:|:x:               |:white_check_mark:| `pnpm sbom`, `npm sbom`. |
| [Listing licenses]               |:white_check_mark:|:white_check_mark:|:x:               | pnpm supports it via `pnpm licenses list`. Yarn has a plugin for it. |

[Auto-install before script run]: settings/build.md#verifydepsbeforerun
[Autoinstalling peers]: settings/peer-dependencies.md#autoinstallpeers
[Catalogs]: catalogs.md
[Config dependencies]: config-dependencies.md
[Dynamic package execution]: cli/pnx.md
[Hoisted `node_modules`]: settings/node-modules.md#nodelinker
[JSR registry support]: cli/add.md#install-from-the-jsr-registry
[Listing licenses]: cli/licenses.md
[Build script security]: settings/build.md#allowbuilds
[Managing runtimes]: cli/runtime.md
[Managing versions of itself]: settings/cli.md#pmonfail
[Overrides support]: settings/dependency-resolution.md#overrides
[Patching dependencies]: cli/patch.md
[SBOM generation]: cli/sbom.md
[Side-effects cache]: settings/build.md#sideeffectscache
[Workspace support]: workspaces.md
[hooks]: pnpmfile.md

**Note:** To keep the comparison concise, we include only features likely to be used frequently.


---

# Filtering

*Sección: Pnpm*

Filtering allows you to restrict commands to specific subsets of packages.

pnpm supports a rich selector syntax for picking packages by name or by
relation.

Selectors may be specified via the `--filter` (or `-F`) flag:

```sh
pnpm --filter <package_selector> <command>
```

## Matching

### --filter &lt;package_name>

To select an exact package, just specify its name (`@scope/pkg`) or use a
pattern to select a set of packages (`@scope/*`).

Examples:

```sh
pnpm --filter "@babel/core" test
pnpm --filter "@babel/*" test
pnpm --filter "*core" test
```

Specifying the scope of the package is optional, so `--filter=core` will pick `@babel/core` if `core` is not found.
However, if the workspace has multiple packages with the same name (for instance, `@babel/core` and `@types/core`),
then filtering without scope will pick nothing.

### --filter &lt;package_name>...

To select a package and its dependencies (direct and non-direct), suffix the
package name with an ellipsis: `<package_name>...`. For instance, the next
command will run tests of `foo` and all of its dependencies:

```sh
pnpm --filter foo... test
```

You may use a pattern to select a set of root packages:

```sh
pnpm --filter "@babel/preset-*..." test
```

### --filter &lt;package_name>^...

To ONLY select the dependencies of a package (both direct and non-direct),
suffix the name with the aforementioned ellipsis preceded by a chevron. For
instance, the next command will run tests for all of `foo`'s
dependencies:

```sh
pnpm --filter "foo^..." test
```

### --filter ...&lt;package_name>

To select a package and its dependent packages (direct and non-direct), prefix
the package name with an ellipsis: `...<package_name>`. For instance, this will
run the tests of `foo` and all packages dependent on it:

```sh
pnpm --filter ...foo test
```

### --filter "...^&lt;package_name>"

To ONLY select a package's dependents (both direct and non-direct), prefix the
package name with an ellipsis followed by a chevron. For instance, this will
run tests for all packages dependent on `foo`:

```text
pnpm --filter "...^foo" test
```

### --filter `./<glob>`, --filter `{<glob>}`

A glob pattern relative to the current working directory matching projects.

```sh
pnpm --filter "./packages/**" <cmd>
```

Includes all projects that are under the specified directory.

It may be used with the ellipsis and chevron operators to select
dependents/dependencies as well:

```sh
pnpm --filter ...{<directory>} <cmd>
pnpm --filter {<directory>}... <cmd>
pnpm --filter ...{<directory>}... <cmd>
```

It may also be combined with `[<since>]`. For instance, to select all changed
projects inside a directory:

```sh
pnpm --filter "{packages/**}[origin/master]" <cmd>
pnpm --filter "...{packages/**}[origin/master]" <cmd>
pnpm --filter "{packages/**}[origin/master]..." <cmd>
pnpm --filter "...{packages/**}[origin/master]..." <cmd>
```

Or you may select all packages from a directory with names matching the given
pattern:

```text
pnpm --filter "@babel/*{components/**}" <cmd>
pnpm --filter "@babel/*{components/**}[origin/master]" <cmd>
pnpm --filter "...@babel/*{components/**}[origin/master]" <cmd>
```

### --filter "[&lt;since>]"

Selects all the packages changed since the specified commit/branch. May be
suffixed or prefixed with `...` to include dependencies/dependents.

For example, the next command will run tests in all changed packages since
`master` and on any dependent packages:

```sh
pnpm --filter "...[origin/master]" test
```

### --fail-if-no-match

Use this flag if you want the CLI to fail if no packages have matched the filters.

You may also set this permanently with a [`failIfNoMatch` setting].

[`failIfNoMatch` setting]: workspaces.md#failifnomatch

## Excluding

Any of the filter selectors may work as exclusion operators when they have a
leading "!". In zsh (and possibly other shells), "!" should be escaped: `\!`.

For instance, this will run a command in all projects except for `foo`:

```sh
pnpm --filter=!foo <cmd>
```

And this will run a command in all projects that are not under the `lib`
directory:

```sh
pnpm --filter=!./lib <cmd>
```

## Multiplicity

When packages are filtered, every package is taken that matches at least one of
the selectors. You can use as many filters as you want:

```sh
pnpm --filter ...foo --filter bar --filter baz... test
```

## --filter-prod &lt;filtering_pattern>

Acts the same a `--filter` but omits `devDependencies` when selecting dependency projects
from the workspace.

## --test-pattern &lt;glob>

`test-pattern` allows detecting whether the modified files are related to tests.
If they are, the dependent packages of such modified packages are not included.

This option is useful with the "changed since" filter. For instance, the next
command will run tests in all changed packages, and if the changes are in the
source code of the package, tests will run in the dependent packages as well:

```sh
pnpm --filter="...[origin/master]" --test-pattern="test/*" test
```

## --changed-files-ignore-pattern &lt;glob>

Allows to ignore changed files by glob patterns when filtering for changed projects since the specified commit/branch.

Usage example:

```sh
pnpm --filter="...[origin/master]" --changed-files-ignore-pattern="**/README.md" run build
```


---

# Finders

*Sección: Pnpm*

Added in: v10.16.0

Finder functions let you **search your dependency graph** by any property of a package, not just its name.
They can be declared in [.pnpmfile.mjs] and used with [pnpm list] and [pnpm why].

[.pnpmfile.mjs]: pnpmfile.md
[pnpm list]: cli/list.md
[pnpm why]: cli/why.md

## Defining finder functions

Finder functions are declared in your project’s [.pnpmfile.mjs] file under the finders export.
Each function receives a context object and must return either:

* `true` → include this dependency in the results,
* `false` → skip it,
* or a `string` → include this dependency and print the string as additional info.

Example: a finder that matches any dependency with **React 17** in `peerDependencies`:

```js title=".pnpmfile.mjs"
  react17: (ctx) => {
    return ctx.readManifest().peerDependencies?.react === "^17.0.0"
  }
}
```

### Finder context (ctx)

Each finder function receives a context object that describes the dependency node being visited.

|Field|Type/Example|Description|
|--|--|--|
|`name`|`"minimist"`|Package name.|
|`version`|`"1.2.8"`|Package version.|
|`readManifest()`|returns the `package.json` object|Load the package manifest (use this for fields like `peerDependencies`, `license`, `engines`, etc.).|

## Using finders

You can invoke a finder with the `--find-by=<functionName>` flag:

```
pnpm why --find-by=react17
```

Output:

```
@apollo/client 4.0.4
├── @graphql-typed-document-node/core 3.2.0
└── graphql-tag 2.12.6
```

## Returning extra metadata

A finder can also return a string. That string will be shown alongside the matched package in the output.

Example: print the package license:

```js
  react17: (ctx) => {
    const manifest = ctx.readManifest()
    if (manifest.peerDependencies?.react === "^17.0.0") {
      return `license: ${manifest.license}`
    }
    return false
  }
}
```

Output:

```
@apollo/client 4.0.4
├── @graphql-typed-document-node/core 3.2.0
│   license: MIT
└── graphql-tag 2.12.6
    license: MIT
```

Othere example use cases:
* Find all packages with a specific license.
* Detect packages requiring a minimum Node.js version.
* List all dependencies that expose binaries.
* Print funding URLs for all packages.


---

# pnpm + Git Worktrees for Multi-Agent Development

*Sección: Pnpm*

When multiple AI agents need to work on the same monorepo simultaneously, they each need an isolated working copy with fully functional `node_modules`. Git worktrees combined with pnpm's [global virtual store](global-virtual-store.md) make this practical: each worktree gets its own checkout and its own `node_modules`, but dependencies are shared across all of them through a single content-addressable store on disk.

## What is a git worktree?

Normally, a git repository has a single working directory tied to one branch at a time. If you want to look at another branch, you have to stash or commit your changes and switch. A [git worktree](https://git-scm.com/docs/git-worktree) lets you check out multiple branches simultaneously, each in its own directory. All worktrees share the same repository history and objects — they're just different views into the same repo.

```
git worktree add ../feature-branch feat/my-feature
```

This creates a new directory `../feature-branch` with `feat/my-feature` checked out, while your original working directory stays on its current branch. You can work in both directories independently.

A common pattern is to use a **bare repository** (one with no working directory of its own) as the hub, and create all working directories as worktrees:

```
git clone --bare https://github.com/your-org/your-repo.git your-repo
cd your-repo
git worktree add ./main main
git worktree add ./feature feat/something
```

## Why worktrees?

Even before AI agents, worktrees are useful for maintaining multiple major versions of a project. On my dev machine, I use a pnpm repository with at least two worktrees: one on `main` for pnpm v11, and another on the `v10` branch for backports and maintenance releases. This way, I can fix a bug on v10 without stashing my in-progress v11 work — both versions are always checked out and ready to go. In the past, 2 or 3 worktrees were usually enough for me in the pnpm repository. However, since I started using AI agents extensively, I need a lot more worktrees to let my agents work on many tasks in parallel.

## Why this matters even more with AI agents

With AI coding agents, worktrees go from convenient to essential. Each agent needs its own working directory to edit files, run builds, and execute tests without interfering with other agents. Without worktrees, this means cloning the repository multiple times, duplicating git history for each copy.

Worktrees solve the git side — every agent gets its own isolated checkout while sharing the underlying git objects. But each worktree still needs its own `node_modules`, which can be hundreds of megabytes. That's where pnpm's [global virtual store](global-virtual-store.md) comes in: with it enabled, each worktree's `node_modules` contains only symlinks into a single content-addressable store on disk. This means adding a new agent is fast and costs almost no extra disk space.

:::important

This setup assumes the worktrees and agents share the same trust boundary. Do not use one writable pnpm store for mutually untrusted agents or users.

:::

## Setting it up

### 1. Create a bare repository

```sh
git clone --bare https://github.com/your-org/your-monorepo.git your-monorepo
cd your-monorepo
```

### 2. Create worktrees for each branch

```sh
# Main development worktree
git worktree add ./main main

# A feature branch for agent A
git worktree add ./feature-auth feat/auth

# A bugfix branch for agent B
git worktree add ./fix-api fix/api-error
```

Each worktree is a full checkout with its own files, but they all share the same `.git` object store.

### 3. Enable the global virtual store

Add `enableGlobalVirtualStore: true` to the `pnpm-workspace.yaml` in your repository:

```yaml
packages:
  - 'packages/*'

enableGlobalVirtualStore: true
```

### 4. Install dependencies in each worktree

```sh
cd main && pnpm install
cd ../feature-auth && pnpm install
cd ../fix-api && pnpm install
```

The first `pnpm install` downloads packages into the global store. Subsequent installs in other worktrees are nearly instant because they only create symlinks to the same store.

## How it works

Without the global virtual store, each worktree would have its own `.pnpm` virtual store inside `node_modules`, with hardlinks or copies of every package. With `enableGlobalVirtualStore: true`, pnpm keeps all package contents in a single shared directory (the global store, which you can find by running `pnpm store path`), and each worktree's `node_modules` contains symlinks pointing there:

```
your-monorepo/                      (bare git repo)
├── main/                           (worktree: main branch)
│   ├── packages/
│   └── node_modules/
│       ├── lodash → <global-store>/links/@/lodash/...
│       └── express → <global-store>/links/@/express/...
├── feature-auth/                   (worktree: feat/auth branch)
│   └── node_modules/
│       ├── lodash → <global-store>/links/@/lodash/...  ← same target
│       └── express → <global-store>/links/@/express/...
└── fix-api/                        (worktree: fix/api-error branch)
    └── node_modules/
        ├── lodash → <global-store>/links/@/lodash/...  ← same target
        └── express → <global-store>/links/@/express/...
```

This means:
- **Near-zero per-worktree overhead** — the local `node_modules` contains only symlinks to the shared global virtual store. Unlike pnpm's default behavior, which hardlinks files from the content-addressable store into a local `node_modules/.pnpm` directory, the global virtual store means no files are copied or hardlinked into the worktree at all.
- **Instant installs for new worktrees** — packages are already in the global store.
- **No conflicts** — each worktree has its own `node_modules` tree, so agents can install different dependency versions on different branches without interference.

## Example: the pnpm monorepo itself

The [pnpm repository](https://github.com/pnpm/pnpm) uses this exact setup with a bare git repo and `enableGlobalVirtualStore: true`. It includes helper scripts to make worktree management easier:

**`pnpm worktree:new <branch-name|pr-number>`** — creates a new worktree and sets it up:

```sh
# Create a worktree for a branch (creates it from main if it doesn't exist)
pnpm worktree:new feat/my-feature

# Create a worktree for a GitHub PR (fetches the PR ref automatically)
pnpm worktree:new 10834
```

The script handles a few things beyond plain `git worktree add`:
- PR numbers are fetched via `git fetch origin pull/<number>/head` so they work for forks too.
- Branch names with slashes (e.g. `feat/my-feature`) are converted to dashes for the directory name (e.g. `feat-my-feature`).
- The `.claude` directory is symlinked from the bare repo's git common directory into the new worktree, so all worktrees share the same Claude Code settings and approved commands.

There's also a shell helper [`shell/wt.sh`](https://github.com/pnpm/pnpm/blob/main/shell/wt.sh) that wraps the script and `cd`s into the new worktree:

```sh
# Source it in your shell config, then:
wt feat/my-feature
wt 10834
```

## Tips

- **Creating worktrees for agents**: When launching an AI agent, create a dedicated worktree for it. The agent gets full isolation to edit files, run tests, and install packages without affecting other agents.
- **Cleanup**: Remove a worktree when it's no longer needed with `git worktree remove ./feature-auth`. Leftover worktrees are cheap but can accumulate.


---

# Working with Git

*Sección: Pnpm*

## Lockfiles

You should always commit the lockfile (`pnpm-lock.yaml`). This is for a
multitude of reasons, the primary of which being:
- it enables faster installation for CI and production environments, due to
being able to skip package resolution
- it enforces consistent installations and resolution between development,
testing, and production environments, meaning the packages used in testing
and production will be exactly the same as when you developed your project

### Merge conflicts

pnpm can automatically resolve merge conflicts in `pnpm-lock.yaml`.
If you have conflicts, just run `pnpm install` and commit the changes.

Be warned, however. It is advised that you review the changes prior to
staging a commit, because we cannot guarantee that pnpm will choose the correct
head - it instead builds with the most updated of lockfiles, which is ideal in
most cases.


---

# Git Branch Lockfiles

*Sección: Pnpm*

Git branch lockfiles allows you to totally avoid lockfile merge conflicts and solve it later.

## Use git branch lockfiles

You can turn on this feature by configuring the `pnpm-workspace.yaml` file.

```yaml
gitBranchLockfile: true
```

By doing this, lockfile name will be generated based on the current branch name.

For instance, the current branch name is `feature-1`. Then, the generated lockfile name will
be `pnpm-lock.feature-1.yaml`. You can commit it to the Git, and merge all git branch lockfiles later.

```
- <project_folder>
|- pnpm-lock.yaml
|- pnpm-lock.feature-1.yaml
|- pnpm-lock.<branch_name>.yaml
```

:::note

`feature/1` is special in that the `/` is automatically converted to `!`, so the corresponding
lockfile name would be `pnpm-lock.feature!1.yaml`.

:::

## Merge git branch lockfiles

### `pnpm install --merge-git-branch-lockfiles`

To merge all git branch lockfiles, just specify `--merge-git-branch-lockfiles` to `pnpm install` command.

After that, all git branch lockfiles will be merged into one `pnpm-lock.yaml`

### Branch Matching

pnpm allows you to specify `--merge-git-branch-lockfiles` by matching the current branch name.

For instance, by the following setting in `pnpm-workspace.yaml` file, `pnpm install` will merge all git branch lockfiles when 
running in the `main` branch and the branch name starts with `release`.

```yaml
mergeGitBranchLockfilesBranchPattern:
- main
- release*
```


---

# Global Packages

*Sección: Pnpm*

Global packages are CLI tools and utilities installed system-wide with `pnpm add -g`. In pnpm v11, global package management was redesigned for better isolation and reliability.

## Installing global packages

```sh
pnpm add -g <pkg>
```

For example:

```sh
pnpm add -g typescript prettier eslint
```

## Isolated installations

Each globally installed package (or group of packages installed together) gets its own isolated installation directory with its own `package.json`, `node_modules/`, and lockfile. This prevents global packages from interfering with each other through peer dependency conflicts, hoisting changes, or version resolution shifts.

Isolated installations are stored at `{pnpmHomeDir}/global/v11/{hash}/`, where the hash is derived from the set of packages installed together.

For example, running the following two commands:

```sh
pnpm add -g typescript
pnpm add -g prettier
```

creates two separate isolated installations — `typescript` and `prettier` each get their own `node_modules` tree and cannot affect each other's dependency resolution.

Installing multiple **space-separated** packages in a single command also creates a separate isolated install for each one:

```sh
pnpm add -g eslint prettier
```

`eslint` and `prettier` each get their own `node_modules` tree and lockfile and can be removed independently — `pnpm remove -g eslint` leaves `prettier` untouched.

To bundle multiple packages into the *same* isolated install — so they share a `node_modules` tree and lockfile, resolve peer dependencies against each other, and are removed together — pass them as a **comma-separated** list:

```sh
pnpm add -g eslint,prettier
```

Here `eslint` and `prettier` form a single install group. Removing either with `pnpm remove -g` removes the whole group.

The two forms can be mixed. For example:

```sh
pnpm add -g eslint,prettier typescript
```

bundles `eslint` and `prettier` into one isolated install while installing `typescript` on its own.

## Directory layout

The contents of `{pnpmHomeDir}/global/v11/` look like:

```text
{pnpmHomeDir}/global/v11/
├── {hash-A}              → symlink → ./{hash-A-target}/
├── {hash-A-target}/      ← isolated install dir
│   ├── package.json      ← lists the packages installed together
│   ├── pnpm-lock.yaml    ← lockfile for this install group
│   └── node_modules/
│       ├── <pkg>/        ← top-level dep, symlinked into the global virtual store
│       └── .pnpm/
├── {hash-B}              → symlink → ./{hash-B-target}/
├── {hash-B-target}/      ← another isolated install dir
└── store/                ← shared global virtual store
    └── ...
```

- The `{hash}` entries are symlinks; pnpm scans for them to enumerate active installs.
- The targets are real directories that act as ordinary pnpm projects — each has its own `package.json` and lockfile.
- The shared `store/` directory holds the [global virtual store](global-virtual-store.md). Each install group's direct dependencies — the entries at the root of its `node_modules/` — are symlinks into that store, so the actual package contents are shared rather than copied per group.
- Bin shims live in `{pnpmHomeDir}/bin/` and point through the appropriate install group's `node_modules`.

When a package is removed or its install group is replaced, the hash symlink is updated and orphaned target directories are eventually cleaned up by `pnpm store prune`.

## Listing global packages

```sh
pnpm list -g
pnpm list -g --json        # machine-readable
pnpm list -g --parseable   # paths only
```

Because each install group has its own lockfile, listing across multiple groups can only reliably aggregate the top-level packages they were installed with — transitive dependency trees from different groups can't be coherently merged. As a result:

- `pnpm list -g` (default `--depth=0`) always works and shows every globally installed package.
- `pnpm list -g --depth=<n>` (with `n > 0`) shows the full dependency tree only when:
  - there is just one global install group, or
  - a positional argument narrows the request to a single install group, e.g. `pnpm list -g eslint --depth=1`.

If `--depth>0` is requested but the request can't be narrowed to a single install group, pnpm errors with `ERR_PNPM_GLOBAL_LS_DEPTH_NOT_SUPPORTED`.

## Managing global packages

| Command | Description |
|---|---|
| `pnpm add -g <pkg>` | Install a package globally |
| `pnpm remove -g <pkg>` | Remove a globally installed package (if it was bundled into an install group, the whole group is removed) |
| `pnpm update -g [pkg]` | Update global packages (re-installs into new isolated directories) |
| `pnpm list -g` | List all globally installed packages |

:::note

`pnpm install -g` (without arguments) is not supported. Use `pnpm add -g <pkg>` to install specific packages.

:::

## Binaries location

Globally installed binaries are stored in a `bin` subdirectory of `PNPM_HOME` (i.e., `$PNPM_HOME/bin/`). This keeps the `PNPM_HOME` directory clean — internal directories like `global/` and `store/` don't pollute shell autocompletion when `PNPM_HOME` is on PATH.

After upgrading to pnpm v11, run [`pnpm setup`](cli/setup.md) to update your shell configuration so that `$PNPM_HOME/bin` is on your PATH.

You can check the current global bin directory with:

```sh
pnpm bin -g
```

## Global virtual store

Global installs use the [global virtual store](global-virtual-store.md). Packages are stored at `{storeDir}/links` and shared across global installations. This avoids redundant fetches when multiple global packages depend on the same libraries.

## Registering local packages globally

To make a local package's binaries available system-wide, use `pnpm add -g .` from the package directory:

```sh
cd ~/projects/my-tool
pnpm add -g .
```

This registers the package's `bin` entries so they can be invoked from anywhere. See [`pnpm link`](cli/link.md#add-a-binary-globally) for more details.

## Build script approval

Global packages that have build scripts (e.g., `postinstall`) require approval. When you install a global package that needs to run build scripts, pnpm will prompt you to approve or deny the build interactively.

You can also pre-approve builds using the `--allow-build` flag:

```sh
pnpm add -g --allow-build=esbuild esbuild
```


---

# Global Virtual Store

*Sección: Pnpm*

By default, pnpm creates a `.pnpm` directory inside each project's `node_modules` — this is the "virtual store". It contains hardlinks to files in the [content-addressable store](settings/store.md#storedir). Every project gets its own projection of this virtual store — pnpm hardlinks files from the content-addressable store into the `.pnpm` directory structure. The actual file contents exist only once on disk, but the directory structure is recreated for each project so that Node.js's module resolution algorithm can find the right dependencies for each package.

The **global virtual store** (`enableGlobalVirtualStore: true`) changes this. Instead of each project having its own `node_modules/.pnpm` directory, pnpm maintains a single shared virtual store (located at `<store-path>/links/`, run `pnpm store path` to find `<store-path>`). Each project's `node_modules` contains only symlinks pointing into this shared location.

## Default behavior vs global virtual store

### Default (per-project virtual store)

```
project-a/
└── node_modules/
    ├── lodash → .pnpm/lodash@4.17.21/node_modules/lodash
    └── .pnpm/
        └── lodash@4.17.21/
            └── node_modules/
                └── lodash/            ← hardlinks to content-addressable store
project-b/
└── node_modules/
    ├── lodash → .pnpm/lodash@4.17.21/node_modules/lodash
    └── .pnpm/
        └── lodash@4.17.21/
            └── node_modules/
                └── lodash/            ← same hardlinks, duplicated directory structure
```

Each project has its own `.pnpm` with hardlinks. The file contents aren't duplicated on disk (hardlinks share inodes), but the directory structure is. With large monorepos or many parallel checkouts, the time spent creating thousands of hardlinks during `pnpm install` adds up.

### With global virtual store

```
project-a/
└── node_modules/
    └── lodash → <global-store>/links/@/lodash/4.17.21/<hash>/node_modules/lodash
project-b/
└── node_modules/
    └── lodash → <global-store>/links/@/lodash/4.17.21/<hash>/node_modules/lodash  ← same target
```

Both projects symlink directly to the same location in the global virtual store. There's no per-project `.pnpm` directory. The global virtual store itself contains the hardlinks to the content-addressable store — but that happens only once per dependency graph (more on that below), not per project.

## How package identity works

In the global virtual store, each package directory is named by the hash of its dependency graph. Two projects that use `lodash@4.17.21` with the same transitive dependency tree will point to the exact same directory. If the dependency trees differ (e.g., different peer dependencies), pnpm creates separate entries. This is conceptually similar to how [NixOS manages packages](https://nixos.org/guides/how-nix-works/) using dependency graph hashes.

## When to use it

The global virtual store is most useful when you have multiple checkouts of the same project on disk — for example, when using [git worktrees for multi-agent development](git-worktrees.md). In that scenario, each worktree gets a nearly free `node_modules` because all the real package content already exists in the shared store.

It also speeds up installations across unrelated projects on the same machine, since any package version that's already been installed by any project is available instantly.

## Limitations

- **CI environments**: In CI, caches are typically absent, so there's no warm global store to benefit from. The global virtual store is generally not useful in CI.
- **Shared trust domain**: The global virtual store and the content-addressable store are shared writable state. Use them only for projects, users, and jobs that trust each other, and protect the store path with filesystem permissions.
- **ESM hoisting**: pnpm uses the `NODE_PATH` environment variable to support hoisted dependencies with the global virtual store. However, Node.js does not respect `NODE_PATH` for ESM imports. If ESM dependencies try to import packages not declared in their own `package.json`, resolution will fail. You can work around this with [packageExtensions](settings/dependency-resolution.md#packageextensions) or the [@pnpm/plugin-esm-node-path](https://github.com/pnpm/plugin-esm-node-path) config dependency.

:::note

The global virtual store is currently disabled by default for project installs and marked as experimental, as some tools may not work correctly with symlinked `node_modules`. You need to explicitly set `enableGlobalVirtualStore: true` in `pnpm-workspace.yaml` to use it for project installs. In pnpm v11, the global virtual store is enabled by default for packages installed via `pnpm dlx` (`pnpx`) and globally installed packages. The goal is to enable it by default for all installations in a future version.

:::

## Global packages

In pnpm v11, global installs (`pnpm add -g`) and `pnpm dlx` use the global virtual store by default. See [Global Packages](global-packages.md) for the full guide on how global package management works in v11, including isolated installations and the new binaries location.

## Configuration

See the [`enableGlobalVirtualStore`](settings/node-modules.md#enableglobalvirtualstore) setting reference for all configuration details.


---

# How peers are resolved

*Sección: Pnpm*

One of the best features of pnpm is that in one project, a specific version of a
package will always have one set of dependencies. There is one exception from
this rule, though - packages with [peer dependencies].

[peer dependencies]: https://docs.npmjs.com/cli/v10/configuring-npm/package-json#peerdependencies

Peer dependencies are resolved from dependencies installed higher in the
dependency graph, since they share the same version as their parent. That means
that if `foo@1.0.0` has two peers (`bar@^1` and `baz@^1`) then it might have
multiple different sets of dependencies in the same project.

```text
- foo-parent-1
  - bar@1.0.0
  - baz@1.0.0
  - foo@1.0.0
- foo-parent-2
  - bar@1.0.0
  - baz@1.1.0
  - foo@1.0.0
```

In the example above, `foo@1.0.0` is installed for `foo-parent-1` and
`foo-parent-2`. Both packages have `bar` and `baz` as well, but they depend on
different versions of `baz`. As a result, `foo@1.0.0` has two different sets of
dependencies: one with `baz@1.0.0` and the other one with `baz@1.1.0`. To
support these use cases, pnpm has to hard link `foo@1.0.0` as many times as
there are different dependency sets.

Normally, if a package does not have peer dependencies, it is hard linked to a
`node_modules` folder next to symlinks of its dependencies, like so:

```text
node_modules
└── .pnpm
    ├── foo@1.0.0
    │   └── node_modules
    │       ├── foo
    │       ├── qux   -> ../../qux@1.0.0/node_modules/qux
    │       └── plugh -> ../../plugh@1.0.0/node_modules/plugh
    ├── qux@1.0.0
    ├── plugh@1.0.0
```

However, if `foo` has peer dependencies, there may be multiple sets of
dependencies for it, so we create different sets for different peer dependency
resolutions:

```text
node_modules
└── .pnpm
    ├── foo@1.0.0_bar@1.0.0+baz@1.0.0
    │   └── node_modules
    │       ├── foo
    │       ├── bar   -> ../../bar@1.0.0/node_modules/bar
    │       ├── baz   -> ../../baz@1.0.0/node_modules/baz
    │       ├── qux   -> ../../qux@1.0.0/node_modules/qux
    │       └── plugh -> ../../plugh@1.0.0/node_modules/plugh
    ├── foo@1.0.0_bar@1.0.0+baz@1.1.0
    │   └── node_modules
    │       ├── foo
    │       ├── bar   -> ../../bar@1.0.0/node_modules/bar
    │       ├── baz   -> ../../baz@1.1.0/node_modules/baz
    │       ├── qux   -> ../../qux@1.0.0/node_modules/qux
    │       └── plugh -> ../../plugh@1.0.0/node_modules/plugh
    ├── bar@1.0.0
    ├── baz@1.0.0
    ├── baz@1.1.0
    ├── qux@1.0.0
    ├── plugh@1.0.0
```

We create symlinks either to the `foo` that is inside
`foo@1.0.0_bar@1.0.0+baz@1.0.0` or to the one in
`foo@1.0.0_bar@1.0.0+baz@1.1.0`.
As a consequence, the Node.js module resolver will find the correct peers.

*If a package has no peer dependencies but has dependencies with peers that are
resolved higher in the graph*, then that transitive package can appear in the
project with different sets of dependencies. For instance, there's package
`a@1.0.0` with a single dependency `b@1.0.0`. `b@1.0.0` has a peer dependency
`c@^1`. `a@1.0.0` will never resolve the peers of `b@1.0.0`, so it becomes
dependent from the peers of `b@1.0.0` as well.

Here's how that structure will look in `node_modules`. In this example,
`a@1.0.0` will need to appear twice in the project's `node_modules` - resolved
once with `c@1.0.0` and again with `c@1.1.0`.

```text
node_modules
└── .pnpm
    ├── a@1.0.0_c@1.0.0
    │   └── node_modules
    │       ├── a
    │       └── b -> ../../b@1.0.0_c@1.0.0/node_modules/b
    ├── a@1.0.0_c@1.1.0
    │   └── node_modules
    │       ├── a
    │       └── b -> ../../b@1.0.0_c@1.1.0/node_modules/b
    ├── b@1.0.0_c@1.0.0
    │   └── node_modules
    │       ├── b
    │       └── c -> ../../c@1.0.0/node_modules/c
    ├── b@1.0.0_c@1.1.0
    │   └── node_modules
    │       ├── b
    │       └── c -> ../../c@1.1.0/node_modules/c
    ├── c@1.0.0
    ├── c@1.1.0
```


---

# Installation

*Sección: Pnpm*

## Prerequisites

If you don't use the standalone script or `@pnpm/exe` to install pnpm, then you need to have Node.js (at least v22) to be installed on your system.

:::info

Looking for pnpm 12? It is currently in beta and installed differently from pnpm 11. See [Installing the pnpm 12 beta](#installing-the-pnpm-12-beta).

:::

## Using a standalone script

You may install pnpm even if you don't have Node.js installed, using the following scripts.

### On Windows

:::warning

Sometimes, Windows Defender may block our executable if you install pnpm this way.

Due to this issue, we currently recommend installing pnpm using [npm](#using-npm) or [Corepack](#using-corepack) on Windows.

:::

Using PowerShell:

```powershell
Invoke-WebRequest https://get.pnpm.io/install.ps1 -UseBasicParsing | Invoke-Expression
```

On Windows, Microsoft Defender can significantly slow down installation of packages. You can add pnpm to Microsoft Defender's list
of excluded folders in a PowerShell window with administrator rights by executing:

```powershell
Add-MpPreference -ExclusionPath $(pnpm store path)
```

### On POSIX systems

:::warning Not supported on Intel macOS in pnpm 11

On pnpm 11, the standalone script does not run on Intel Macs (`darwin-x64`). Use [npm](#using-npm), [Corepack](#using-corepack), or [Homebrew](#using-homebrew) instead. See [#11423](https://github.com/pnpm/pnpm/issues/11423) for context.

pnpm 12 ships an Intel macOS build again, so this limitation doesn't apply to it.

:::

```sh
curl -fsSL https://get.pnpm.io/install.sh | sh -
```

If you don't have curl installed, you would like to use wget:

```sh
wget -qO- https://get.pnpm.io/install.sh | sh -
```

:::info Linux runtime requirements

The install script picks a glibc or musl build based on your system's libc, and a separate musl build is provided for Alpine and other musl-based distros. The glibc build requires glibc 2.27 or newer plus `libatomic.so.1` — both are present on most full distros but may be missing from minimal container images. If you see `error while loading shared libraries: libatomic.so.1`, install it with your distro's package manager:

- Debian/Ubuntu: `apt-get install -y libatomic1`
- Fedora/RHEL: `dnf install -y libatomic`

:::

:::tip

You may use the [pnpm runtime] command then to install Node.js.

:::

### In a Docker container

```sh
# bash
wget -qO- https://get.pnpm.io/install.sh | ENV="$HOME/.bashrc" SHELL="$(which bash)" bash -
# sh
wget -qO- https://get.pnpm.io/install.sh | ENV="$HOME/.shrc" SHELL="$(which sh)" sh -
# dash
wget -qO- https://get.pnpm.io/install.sh | ENV="$HOME/.dashrc" SHELL="$(which dash)" dash -
```

### Installing a specific version

Prior to running the install script, you may optionally set an env variable `PNPM_VERSION` to install a specific version of pnpm:

```sh
curl -fsSL https://get.pnpm.io/install.sh | env PNPM_VERSION=<version> sh -
```

## Using Corepack

Due to an issue with [outdated signatures in Corepack](https://github.com/nodejs/corepack/issues/612), Corepack should be updated to its latest version first:

```
npm install --global corepack@latest
```

Since v16.13, Node.js is shipping [Corepack](https://nodejs.org/api/corepack.html) for managing package managers. This is an experimental feature, so you need to enable it by running:

:::info

If you have installed Node.js with `pnpm runtime` Corepack won't be installed on your system, you will need to install it separately. See [#4029](https://github.com/pnpm/pnpm/issues/4029).

:::

```
corepack enable pnpm
```

This will automatically install pnpm on your system.

You can pin the version of pnpm used on your project using the following command:

```
corepack use pnpm@latest-11
```

This will add a `"packageManager"` field in your local `package.json` which will instruct Corepack to always use a specific version on that project. This can be useful if you want reproducability, as all developers who are using Corepack will use the same version as you. When a new version of pnpm is released, you can re-run the above command.

:::warning

Corepack cannot install pnpm 12 yet. It expects the pnpm package to contain a `bin/pnpm.mjs` file, which the native pnpm 12 package does not have. Use [`pnpm self-update`](#pnpm-12-using-pnpm), [npm](#pnpm-12-using-npm), or the [standalone script](#pnpm-12-using-a-standalone-script) to install the beta.

:::

## Using other package managers

### Using npm

We provide two packages of pnpm CLI, `pnpm` and `@pnpm/exe`. On pnpm 12 the two are identical, so there is no reason to prefer one over the other; the difference below applies to pnpm 11.

- [`pnpm`](https://www.npmjs.com/package/pnpm) is an ordinary version of pnpm, which needs Node.js to run. Since v11, pnpm is distributed as pure ESM.
- [`@pnpm/exe`](https://www.npmjs.com/package/@pnpm/exe) is packaged with Node.js into an executable, so it may be used on a system with no Node.js installed. On Linux, glibc and musl builds are both provided and the right one is selected automatically; the glibc build requires glibc 2.27 or newer and `libatomic.so.1` (see [Linux runtime requirements](#on-posix-systems) for details). **Not available for Intel macOS** (`darwin-x64`) — install `pnpm` instead, see [#11423](https://github.com/pnpm/pnpm/issues/11423).

```sh
npx pnpm@latest-11 dlx @pnpm/exe@latest-11 setup
```

or

```sh
npm install -g pnpm@latest-11
```

### Using Homebrew

If you have the package manager installed, you can install pnpm using the following command:

```
brew install pnpm
```

### Using winget

If you have winget installed, you can install pnpm using the following command:

```
winget install -e --id pnpm.pnpm
```

### Using Scoop

If you have Scoop installed, you can install pnpm using the following command:

```
scoop install nodejs-lts pnpm
```

### Using Choco

If you have Chocolatey installed, you can install pnpm using the following command:

```
choco install pnpm
```

:::tip

Do you wanna use pnpm on CI servers? See: [Continuous Integration](continuous-integration.md).

:::

## Installing the pnpm 12 beta

:::warning

pnpm 12 is a rewrite of pnpm in Rust and is currently in **beta**. It is not recommended for production use yet. Please [report any issues](https://github.com/pnpm/pnpm/issues) you run into.

:::

pnpm 12 has no intentional breaking changes compared to pnpm 11, so the rest of this documentation applies to both versions. Only installation differs while v12 is in beta: it is published under the `next-12` tag on npm and as a prerelease on GitHub, so Homebrew, winget, Scoop and Chocolatey don't offer it yet.

### Using pnpm {#pnpm-12-using-pnpm}

If you already have pnpm v11.10.0 or newer, this is the easiest way to switch:

```
pnpm self-update next-12
```

pnpm links the native binary directly, so nothing else is needed. Note that inside a project that pins pnpm through the `packageManager` field, [`self-update`] only updates that pin instead of installing pnpm globally.

### Using npm {#pnpm-12-using-npm}

If you don't have pnpm installed yet:

```sh
npm install -g --allow-scripts=pnpm pnpm@next-12
```

:::info

`--allow-scripts=pnpm` is required on npm 11.16 and newer, which blocks install scripts by default. The published package is a small wrapper whose `preinstall` script replaces it with the native binary for your platform, so without the flag `pnpm` is left as a placeholder file that fails to run. Older versions of npm run install scripts anyway and ignore the flag, so the command above works on any version. For the same reason, don't install pnpm 12 with `--ignore-scripts` or `--no-optional`. If you install it with pnpm or Bun, allow the build scripts of the `pnpm` package.

:::

Node.js 18 or newer is needed to run that install script, but not to run pnpm afterwards — pnpm 12 is a native binary.

### Using a standalone script {#pnpm-12-using-a-standalone-script}

Set `PNPM_VERSION` to the exact beta version (the POSIX script does not accept npm dist-tags).

On POSIX systems:

```sh
curl -fsSL https://get.pnpm.io/install.sh | env PNPM_VERSION=12.0.0-beta.2 sh -
```

On Windows, using PowerShell:

```powershell
$env:PNPM_VERSION="12.0.0-beta.2"; Invoke-WebRequest https://get.pnpm.io/install.ps1 -UseBasicParsing | Invoke-Expression
```

This installs pnpm without requiring Node.js, and unlike pnpm 11 it also works on Intel macOS.

## Compatibility

Here is a list of past pnpm versions with respective Node.js version support.

| Node.js    | pnpm 8 | pnpm 9 | pnpm 10 | pnpm 11 | pnpm 12 |
|------------|--------|--------|---------|---------|---------|
| Node.js 14 | ❌     | ❌     | ❌      | ❌      | ❌      |
| Node.js 16 | ✔️      | ❌     | ❌      | ❌      | ❌      |
| Node.js 18 | ✔️      | ✔️      | ✔️       | ❌      | ✔️       |
| Node.js 20 | ✔️      | ✔️      | ✔️       | ❌      | ✔️       |
| Node.js 22 | ✔️      | ✔️      | ✔️       | ✔️       | ✔️       |
| Node.js 24 | ✔️      | ✔️      | ✔️       | ✔️       | ✔️       |
| Node.js 26 | ✔️      | ✔️      | ✔️       | ✔️       | ✔️       |

pnpm 12 only needs Node.js when it is installed from npm; the version installed by the standalone script runs without Node.js.

## Troubleshooting

If pnpm is broken and you cannot fix it by reinstalling, you might need to remove it manually from the PATH.

Let's assume you have the following error when running `pnpm install`:

```
C:\src>pnpm install
internal/modules/cjs/loader.js:883
  throw err;
  ^

Error: Cannot find module 'C:\Users\Bence\AppData\Roaming\npm\pnpm-global\4\node_modules\pnpm\bin\pnpm.js'
←[90m    at Function.Module._resolveFilename (internal/modules/cjs/loader.js:880:15)←[39m
←[90m    at Function.Module._load (internal/modules/cjs/loader.js:725:27)←[39m
←[90m    at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:72:12)←[39m
←[90m    at internal/main/run_main_module.js:17:47←[39m {
  code: ←[32m'MODULE_NOT_FOUND'←[39m,
  requireStack: []
}
```

First, try to find the location of pnpm by running: `which pnpm`. If you're on Windows, run `where.exe pnpm.*`.
You'll get the location of the pnpm command, for instance:

```
$ which pnpm
/c/Program Files/nodejs/pnpm
```

Now that you know where the pnpm CLI is, open that directory and remove any pnpm-related files (`pnpm.cmd`, `pnpx.cmd`, `pnpm`, etc).
Once done, install pnpm again and it should work as expected.

## Updating pnpm

To update pnpm, run the [`self-update`] command:

```
pnpm self-update
```

[`self-update`]: cli/self-update.md

## Uninstalling pnpm

If you need to remove the pnpm CLI from your system and any files it has written to your disk, see [Uninstalling pnpm].

[Uninstalling pnpm]: uninstall.md
[pnpm runtime]: cli/runtime.md


---

# Limitations

*Sección: Pnpm*

1. `npm-shrinkwrap.json` and `package-lock.json` are ignored. Unlike pnpm, npm
can install the same `name@version` multiple times and with different sets of
dependencies. npm's lockfile is designed to reflect the flat `node_modules`
layout, however, as pnpm creates an isolated layout by default, it cannot respect
npm's lockfile format. See [pnpm import] if you wish to convert a lockfile to
pnpm's format, though.
1. Binstubs (files in `node_modules/.bin`) are always shell files, not
symlinks to JS files. The shell files are created to help pluggable CLI apps
in finding their plugins in the unusual `node_modules` structure. This is very
rarely an issue and if you expect the file to be a JS file, reference the
original file directly instead, as described in [#736].

Got an idea for workarounds for these issues?
[Share them.](https://github.com/pnpm/pnpm/issues/new)

[pnpm import]: cli/import.md
[#736]: https://github.com/pnpm/pnpm/issues/736


---

# Logos

*Sección: Pnpm*

## Standard logo

**SVG:**

![](/img/logos/pnpm-standard.svg)

**PNG:**

![](/img/logos/pnpm-standard.png)

## Standard logo with no text

**SVG:**

![](/img/logos/pnpm-standard-no-text.svg)

**PNG:**

![](/img/logos/pnpm-standard-no-text.png)

## Standard light logo

**SVG:**

> ![](/img/logos/pnpm-light.svg)

**PNG:**

> ![](/img/logos/pnpm-light.png)

## Standard light logo with no text

**SVG:**

> ![](/img/logos/pnpm-light-no-text.svg)

**PNG:**

> ![](/img/logos/pnpm-light-no-text.png)


---

# Migrating from v10 to v11

*Sección: Pnpm*

pnpm v11 introduces several breaking changes to how configuration is read and which settings are available. Most config changes are mechanical and can be applied by a codemod; the remainder require human attention. pnpm prints a pointer to this page when `pnpm self-update 11` is run from a v10 install.

## Run the codemod

```sh
cd /path/to/your/project
pnpx codemod run pnpm-v10-to-v11
# or
pnpm add --global codemod
codemod run pnpm-v10-to-v11
```

The codemod applies the following automatically:

- **Moves settings out of `package.json#pnpm` into `pnpm-workspace.yaml`**. In v11, pnpm no longer reads configuration from the `pnpm` field in `package.json`.
- **Splits `.npmrc` into auth/registry vs. everything else**. v11 only reads auth and registry settings from `.npmrc`. Every other setting (`hoist-pattern`, `node-linker`, `save-exact`, …) is moved into `pnpm-workspace.yaml` with a camelCase key. Per-subproject `.npmrc` files land under `packageConfigs["<project-name>"]`.
- **Consolidates build-dependency settings into `allowBuilds`**. `onlyBuiltDependencies`, `neverBuiltDependencies`, `ignoredBuiltDependencies`, and `onlyBuiltDependenciesFile` are merged into a single `allowBuilds` map (`{ name: true | false }`).
- **Replaces the package-manager strictness settings with `pmOnFail`**. `managePackageManagerVersions`, `packageManagerStrict`, and `packageManagerStrictVersion` are collapsed into one `pmOnFail: download | ignore | warn | error` setting.
- **Renames** `allowNonAppliedPatches` → `allowUnusedPatches`, and `auditConfig.ignoreCves` → `auditConfig.ignoreGhsas` (the key is renamed; CVE IDs still need to be converted to GHSA IDs manually — see below).
- **Converts `useNodeVersion`** into a `devEngines.runtime` entry on the root `package.json`.
- **Bumps `packageManager`** in `package.json` to the target pnpm v11 version.

## Manual follow-ups

The following changes are not automatable and need human attention:

- **CVE → GHSA**. `auditConfig.ignoreCves` was renamed to `auditConfig.ignoreGhsas`. Replace each `CVE-YYYY-NNNNN` entry with the matching `GHSA-xxxx-xxxx-xxxx` ID (visible in the "More info" column of `pnpm audit` output).
- **`ignorePatchFailures`** has been removed. Failed patches now always throw; fix the patch or remove the dependency.
- **`executionEnv.nodeVersion`** in a workspace subpackage's `package.json#pnpm` is removed. Declare the runtime in that subpackage's `devEngines.runtime` instead.
- **`npm_config_*` environment variables** are no longer read. Rename them to `pnpm_config_*` wherever they are set (CI configs, shell profiles, Docker images).
- **`pnpm link <pkg-name>`** no longer resolves packages from the global store. Use a relative or absolute path (`pnpm link ./foo`).
- **`pnpm install -g`** (with no arguments) is no longer supported. Use `pnpm add -g <pkg>` instead.
- **`pnpm server`** has been removed with no replacement.
- **Script names shadow built-in commands**. If your `package.json` defines a script named `clean`, `setup`, `deploy`, or `rebuild`, `pnpm <name>` now runs the script instead of the built-in command. Use [`pnpm pm <name>`](cli/pm.md) to force the built-in.

For the full list of breaking changes, see the [v11 changelog](https://github.com/pnpm/pnpm/blob/main/pnpm/CHANGELOG.md).


---

# Motivation

*Sección: Pnpm*

## Saving disk space

![An illustration of the pnpm content-addressable store. On the illustration there are two projects with node_modules. The files in the node_modules directories are hard links to the same files in the content-addressable store.](/img/pnpm-store.svg)

When using npm, if you have 100 projects using a dependency, you will
have 100 copies of that dependency saved on disk. With pnpm, the dependency will be
stored in a content-addressable store, so:

1. If you depend on different versions of the dependency, only the files that
differ are added to the store. For instance, if it has 100 files, and a new
version has a change in only one of those files, `pnpm update` will only add 1
new file to the store, instead of cloning the entire dependency just for the
singular change.
1. All the files are saved in a single place on the disk. When packages are
installed, their files are hard-linked from that single place, consuming no
additional disk space. This allows you to share dependencies of the same version
across projects.

As a result, you save a lot of space on your disk proportional to the number of
projects and dependencies, and you have a lot faster installations!

## Boosting installation speed

pnpm performs installation in three stages:

1. Dependency resolution. All required dependencies are identified and fetched to the store.
1. Directory structure calculation. The `node_modules` directory structure is calculated based on the dependencies.
1. Linking dependencies. All remaining dependencies are fetched and hard linked from the store to `node_modules`.

![An illustration of the pnpm install process. Packages are resolved, fetched, and hard linked as soon as possible.](/img/installation-stages-of-pnpm.svg)

This approach is significantly faster than the traditional three-stage installation process of resolving, fetching, and writing all dependencies to `node_modules`.

![An illustration of how package managers like Yarn Classic or npm install dependencies.](/img/installation-stages-of-other-pms.svg)

## Creating a non-flat node_modules directory

When installing dependencies with npm or Yarn Classic, all packages are hoisted to the root of the
modules directory. As a result, source code has access to dependencies that are
not added as dependencies to the project.

By default, pnpm uses symlinks to add only the direct dependencies of the project into the root of the modules directory.

![An illustration of a node_modules directory created by pnpm. Packages in the root node_modules are symlinks to directories inside the node_modules/.pnpm directory](/img/isolated-node-modules.svg)

If you'd like more details about the unique `node_modules` structure that pnpm
creates and why it works fine with the Node.js ecosystem, read:
- [Flat node_modules is not the only way](/blog/2020/05/27/flat-node-modules-is-not-the-only-way)
- [Symlinked node_modules structure](symlinked-node-modules-structure.md)

:::tip

If your tooling doesn't work well with symlinks, you may still use pnpm and set the [nodeLinker](settings/node-modules.md#nodelinker) setting to `hoisted`. This will instruct pnpm to create a node_modules directory that is similar to those created by npm and Yarn Classic.

:::


---

# Authentication Settings

*Sección: Pnpm*

The settings on this page contain sensitive credentials and are stored in INI-formatted files. Do not commit these files to your repository.

For non-sensitive settings (proxy, SSL, registries, etc.), see [Settings (pnpm-workspace.yaml)](settings.md).

## Auth file locations

pnpm reads authentication settings from the following files, in order of priority (highest first):

1. **`<workspace root>/.npmrc`** — project-level auth. This file should be listed in `.gitignore`.
2. **`<pnpm config>/auth.ini`** — the primary user-level auth file. `pnpm login` writes tokens here.
3. **`~/.npmrc`** — read as a fallback for easier migration from npm. Use the [`npmrcAuthFile`](settings/other.md#npmrcauthfile) setting to point to a different file.

The `<pnpm config>` directory is:

* If the **$XDG_CONFIG_HOME** env variable is set: **$XDG_CONFIG_HOME/pnpm/**
* On Windows: **~/AppData/Local/pnpm/config/**
* On macOS: **~/Library/Preferences/pnpm/**
* On Linux: **~/.config/pnpm/**

## Environment variables in auth settings

Values in the **user-level** auth files (`<pnpm config>/auth.ini` and the user `.npmrc`) may reference environment variables using the `${NAME}` syntax:

```ini
//registry.npmjs.org/:_authToken=${NPM_TOKEN}
```

Since v11.5.3, environment variables are **not** expanded in the **project-level** `.npmrc` at the workspace root for the following settings:

* registry and proxy URLs (`registry`, `@scope:registry`, proxy settings);
* URL-scoped keys (keys starting with `//`);
* credential values (`_authToken`, `_auth`, `_password`, `username`, `tokenHelper`, `cert`, `key`).

A setting that contains a `${...}` placeholder in any of these positions is ignored, and pnpm prints a warning. The project `.npmrc` is checked out together with the repository, so expanding environment variables there would allow a malicious repository to exfiltrate secrets from your environment (such as CI tokens) to an attacker-controlled registry during installation ([GHSA-3qhv-2rgh-x77r](https://github.com/pnpm/pnpm/security/advisories/GHSA-3qhv-2rgh-x77r)).

If your project relied on a committed `.npmrc` containing a line like `//registry.npmjs.org/:_authToken=${NPM_TOKEN}`, move the token to a trusted location instead:

* Write the token to the user-level auth file before installing (for example, in a CI step):

  ```sh
  pnpm config set //registry.npmjs.org/:_authToken "$NPM_TOKEN"
  ```

  `pnpm config set` writes to the global location by default (`<pnpm config>/auth.ini` for auth settings), not to the project `.npmrc`, so the token never ends up in the repository.

* **Set the credential through an environment variable, with no `.npmrc` file at all** (since v11.6). pnpm reads URL-scoped registry settings from `pnpm_config_//…` environment variables:

  ```sh
  env "pnpm_config_//registry.npmjs.org/:_authToken=$NPM_TOKEN" pnpm install
  ```

  The variable name contains `/`, `:`, and `.`, which `export` and the `NAME=value` shell assignment syntax reject as invalid identifiers. Use the `env` utility (as shown above) to pass it to a single command, or set it through a tool that accepts arbitrary variable names (for example, your CI provider's environment settings or Node's `process.env`).

  This is the most direct, file-free replacement for a committed `//registry.npmjs.org/:_authToken=${NPM_TOKEN}` line. Because the registry the credential applies to is encoded in the (trusted) variable name, a malicious repository cannot redirect it to another host. Such an environment value overrides the project `.npmrc` but is itself overridden by a command-line option. The `tokenHelper` setting is intentionally not read from environment variables.

* Or keep the `${NPM_TOKEN}` placeholder line, but put it in the user-level `~/.npmrc` (or the file referenced by [`npmrcAuthFile`](settings/other.md#npmrcauthfile)) instead of the repository.
* In GitHub Actions, `actions/setup-node` with the `registry-url` input writes the auth setting to a user-level `.npmrc` (referenced by the `NPM_CONFIG_USERCONFIG` environment variable, which pnpm honors), so authentication via the `NODE_AUTH_TOKEN` environment variable continues to work.
* If you cannot easily modify each CI pipeline, you may declare the project `.npmrc` trusted by setting a single environment variable in the CI environment (for example, at the organization or workspace level):

  ```text
  PNPM_CONFIG_NPMRC_AUTH_FILE=.npmrc
  ```

  This is the env form of the [`npmrcAuthFile`](settings/other.md#npmrcauthfile) setting: it makes pnpm read the project's `.npmrc` as the user-level auth file (a relative path is resolved against the working directory), so environment variables in it are expanded as before. Because the trust declaration comes from the environment — not from the repository — a malicious repository cannot set it for you. The npm-style `NPM_CONFIG_USERCONFIG` variable is also honored as a fallback.

  :::danger

  Only use this in environments that exclusively build trusted repositories. It disables this protection entirely for the checked-out repository, including the restriction that `tokenHelper` may only be set in user-level config.

  :::

The same rule applies to **registry and proxy URLs** in a project `.npmrc` (`registry`, `@scope:registry`, `proxy`, `https-proxy`, `http-proxy`). If you used an environment variable to build a registry URL, move the setting to a trusted source — your user-level `~/.npmrc`, or `pnpm config set "<key>" <value>`. If the URL is not secret, you can also write the resolved value directly in the project `.npmrc`, since only `${...}` placeholders are ignored. For registry settings in `pnpm-workspace.yaml`, see [Settings](settings/dependency-resolution.md#registries).

## Authentication Settings

### &lt;URL&gt;&#58;_authToken

Define the authentication bearer token to use when accessing the specified
registry. For example:

```ini
//registry.npmjs.org/:_authToken=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

You may also use an environment variable. For example:

```ini
//registry.npmjs.org/:_authToken=${NPM_TOKEN}
```

Environment variables are only expanded in user-level auth files, not in the project-level `.npmrc`. See [Environment variables in auth settings](#environment-variables-in-auth-settings).

#### Scope-specific auth tokens

Added in: v11.7.0

pnpm can use different auth tokens for different package scopes, even when those scopes point to the same registry URL. Add the package scope after the registry URL in the auth key:

```ini
@org-a:registry=https://npm.pkg.github.com/
@org-b:registry=https://npm.pkg.github.com/

//npm.pkg.github.com/:@org-a:_authToken=ORG_A_TOKEN
//npm.pkg.github.com/:@org-b:_authToken=ORG_B_TOKEN

//npm.pkg.github.com/:_authToken=FALLBACK_TOKEN
```

When installing or publishing `@org-a/*`, pnpm uses `ORG_A_TOKEN`; for `@org-b/*`, it uses `ORG_B_TOKEN`. Optionally, packages without a matching scope fall back to the registry-wide token (`FALLBACK_TOKEN` above), when provided.

`pnpm login --registry=https://npm.pkg.github.com --scope=@org-a` writes the token to the same scope-specific auth key.

This is useful for registries (such as GitHub Packages) that issue tokens per organization or per scope. Previously, auth was selected only by registry URL, so two scopes sharing a registry had to share a token.

### &lt;URL&gt;&#58;tokenHelper

A token helper is an executable which outputs an auth token. This can be used in situations where the authToken is not a constant value but is something that refreshes regularly, where a script or other tool can use an existing refresh token to obtain a new access token.

The configuration for the path to the helper must be an absolute path, with no arguments. In order to be secure, it is only permitted to set this value in the user `.npmrc`. Otherwise a project could place a value in a project's local `.npmrc` and run arbitrary executables.

Setting a token helper for the default registry:

```ini
tokenHelper=/home/ivan/token-generator
```

Setting a token helper for the specified registry:

```
//registry.corp.com:tokenHelper=/home/ivan/token-generator
```

### _auth

Added in: v11.10.0

Configures registry authentication as a single structured value, keyed by registry URL. This is an alternative to the many `//host/:_authToken=…` entries and is designed for CI, where the URL-scoped form (whose variable name contains `/`, `:`, and `.`) cannot be passed through an environment variable on some runners.

`_auth` is honored **only** from two trusted locations:

* the **global** pnpm config (`config.yaml`);
* the `pnpm_config__auth` environment variable (for CI).

It is **ignored** in a project `pnpm-workspace.yaml` or `.npmrc`, so a checked-out repository can never supply registry auth.

The value is keyed by registry URL, so each secret is explicitly bound to the host that may receive it. Registry URL keys must use `http` or `https` and must not include credentials, query strings, or fragments. Within each registry URL, `@` means registry-wide (default) credentials, and a package scope such as `@org` binds credentials to that scope on the same host. The only supported credential field is `authToken` (it maps to `_authToken` / bearer auth); the deprecated `basicAuth` / `username` + `password` forms and `tokenHelper` are not accepted here.

In the global `config.yaml`:

```yaml
_auth:
  https://registry.npmjs.org:
    "@":
      authToken: npm-token
    "@org":
      authToken: org-token
```

The equivalent environment variable (a JSON string):

```sh
```

Both `pnpm_config__auth` (lowercase) and `PNPM_CONFIG__AUTH` (all-caps, the convention some CI runners apply) are honored. If both are set, lowercase wins unless it is empty, in which case uppercase is used.

Each entry also infers a trusted registry route: `@` routes the default registry (and `pnpm add <pkg>` resolves there), and `@org` routes that scope. Because the credential and its destination host arrive in one trusted value, repo-controlled config cannot redirect the token to a different host.

Precedence, from highest to lowest:

1. CLI flags (`--registry`, `--@scope:registry`)
2. `pnpm_config__auth` / `PNPM_CONFIG__AUTH`
3. global `config.yaml` `_auth`
4. `pnpm-workspace.yaml`

Parsing is strict: a malformed value (bad JSON, wrong shape, an invalid registry URL or scope, or an unsupported credential field) fails fast with an error rather than being silently dropped.

## Certificate Settings

### ca

* Default: **The npm CA certificate**
* Type: **String, Array or null**

The Certificate Authority signing certificate that is trusted for SSL
connections to the registry. Values should be in PEM format (AKA
"Base-64 encoded X.509 (.CER)"). For example:

```sh
ca="-----BEGIN CERTIFICATE-----\nXXXX\nXXXX\n-----END CERTIFICATE-----"
```

Set to null to only allow known registrars, or to a specific CA cert to trust
only that specific signing authority.

Multiple CAs can be trusted by specifying an array of certificates:

```sh
ca[]="..."
ca[]="..."
```

See also the [`strictSsl`](settings/network.md#strictssl) setting.

### cafile

* Default: **null**
* Type: **path**

A path to a file containing one or multiple Certificate Authority signing
certificates. Similar to the `ca` setting, but allows for multiple CAs, as well
as for the CA information to be stored in a file instead of being specified via
CLI.

### &lt;URL&gt;&#58;cafile

Define the path to a Certificate Authority file to use when accessing the specified
registry. For example:

```sh
//registry.npmjs.org/:cafile=ca-cert.pem
```

### &lt;URL&gt;&#58;ca

Added in: v10.25.0

Define an inline Certificate Authority certificate for the specified registry.
The value must be PEM-encoded, like the global `ca` setting, but it only applies
to the matching registry URL.

```sh
//registry.example.com/:ca=-----BEGIN CERTIFICATE-----...-----END CERTIFICATE-----
```

### cert

* Default: **null**
* Type: **String**

A client certificate to pass when accessing the registry. Values should be in
PEM format (AKA "Base-64 encoded X.509 (.CER)"). For example:

```test
cert="-----BEGIN CERTIFICATE-----\nXXXX\nXXXX\n-----END CERTIFICATE-----"
```

It is not the path to a certificate file.

### &lt;URL&gt;&#58;cert

Added in: v10.25.0

Define an inline client certificate to use when accessing the specified
registry. Example:

```sh
//registry.example.com/:cert=-----BEGIN CERTIFICATE-----...-----END CERTIFICATE-----
```

### &lt;URL&gt;&#58;certfile

Define the path to a certificate file to use when accessing the specified
registry. For example:

```sh
//registry.npmjs.org/:certfile=server-cert.pem
```

### key

* Default: **null**
* Type: **String**

A client key to pass when accessing the registry. Values should be in PEM format
(AKA "Base-64 encoded X.509 (.CER)"). For example:

```sh
key="-----BEGIN PRIVATE KEY-----\nXXXX\nXXXX\n-----END PRIVATE KEY-----"
```

It is not the path to a key file. Use `&#58;keyfile` if you need to reference
the file system instead of inlining the key.

This setting contains sensitive information. Don't write it to a local `.npmrc` file committed to the repository.

### &lt;URL&gt;&#58;key

Added in: v10.25.0

Define an inline client key for the specified registry URL.

```sh
//registry.example.com/:key=-----BEGIN PRIVATE KEY-----...-----END PRIVATE KEY-----
```

### &lt;URL&gt;&#58;keyfile

Define the path to a client key file to use when accessing the specified
registry. For example:

```sh
//registry.npmjs.org/:keyfile=server-key.pem
```


---

# Only allow pnpm

*Sección: Pnpm*

When you use pnpm on a project, you don't want others to accidentally run
`npm install` or `yarn`. To prevent devs from using other package managers,
you can add the following `preinstall` script to your `package.json`:

```json
{
	"scripts": {
		"preinstall": "npx only-allow pnpm"
	}
}
```

Now, whenever someone runs `npm install` or `yarn`, they'll get an
error instead and installation will not proceed.

If you use npm v7, use `npx -y` instead.


---

# Supported package sources

*Sección: Pnpm*

pnpm supports installing packages from various sources. These sources are divided into two categories: **trusted sources** and **exotic sources**.

Exotic sources (like Git repositories or direct tarball URLs) can introduce supply chain risks when used by transitive dependencies. You can prevent transitive dependencies from using exotic sources by setting [`blockExoticSubdeps`] to `true`.

[`blockExoticSubdeps`]: settings/dependency-resolution.md#blockexoticsubdeps

## Trusted sources

Trusted sources are considered safe for both direct and transitive dependencies.

### npm registry

`pnpm add package-name` will install the latest version of `package-name` from
the [npm registry](https://www.npmjs.com/) by default.

If executed in a workspace, the command will first try to check whether other
projects in the workspace use the specified package. If so, the already used version range
will be installed.

You may also install packages by:

* tag: `pnpm add express@nightly`
* version: `pnpm add express@1.0.0`
* version range: `pnpm add express@2 react@">=0.1.0 <0.2.0"`

### JSR registry

Added in: v10.9.0

To install packages from the [JSR](https://jsr.io/) registry, use the `jsr:` protocol prefix:

```
pnpm add jsr:@hono/hono
pnpm add jsr:@hono/hono@4
pnpm add jsr:@hono/hono@latest
```

This works just like installing from npm, but tells pnpm to resolve the package through JSR instead.

### Workspace

Note that when adding dependencies and working within a [workspace], packages
will be installed from the configured sources, depending on whether or not
[`linkWorkspacePackages`] is set, and use of the
[`workspace: range protocol`].

[workspace]: workspaces.md
[`linkWorkspacePackages`]: workspaces.md#linkworkspacepackages
[`workspace: range protocol`]: workspaces.md#workspace-protocol-workspace

### Local file system

There are two ways to install from the local file system:

1. from a tarball file (`.tar`, `.tar.gz`, or `.tgz`)
2. from a directory

Examples:

```sh
pnpm add ./package.tar.gz
pnpm add ./some-directory
```

When you install from a directory, a symlink will be created in the current
project's `node_modules`, so it is the same as running `pnpm link`.

## Exotic sources

Exotic sources are useful for development but may pose supply chain risks when used by transitive dependencies.

### Remote tarball

The argument must be a fetchable URL starting with "http://" or "https://".

Example:

```sh
pnpm add https://github.com/indexzero/forever/tarball/v0.5.6
```

### Git repository

```sh
pnpm add <git remote url>
```

Installs the package from the hosted Git provider, cloning it with Git.

You may install packages from Git by:

* Latest commit from default branch:
```
pnpm add kevva/is-positive
```
* Git commit hash:
```
pnpm add kevva/is-positive#97edff6f525f192a3f83cea1944765f769ae2678
```
* Git branch:
```
pnpm add kevva/is-positive#master
```
* Git branch relative to refs:
```
pnpm add zkochan/is-negative#heads/canary
```
* Git tag:
```
pnpm add zkochan/is-negative#2.0.1
```
* V-prefixed Git tag:
```
pnpm add andreineculau/npm-publish-git#v0.0.7
```

#### Install from a Git repository using semver

You can specify version (range) to install using the `semver:` parameter. For example:

* Strict semver:
```
pnpm add zkochan/is-negative#semver:1.0.0
```
* V-prefixed strict semver:
```
pnpm add andreineculau/npm-publish-git#semver:v0.0.7
```
* Semver version range:
```
pnpm add kevva/is-positive#semver:^2.0.0
```
* V-prefixed semver version range:
```
pnpm add andreineculau/npm-publish-git#semver:<=v0.0.7
```

#### Install from a subdirectory of a Git repository

You may also install just a subdirectory from a Git-hosted monorepo using the `path:` parameter. For instance:

```
pnpm add RexSkz/test-git-subfolder-fetch#path:/packages/simple-react-app
```

#### Install from a Git repository via a full URL

If you want to be more explicit or are using alternative Git hosting, you might want to spell out full Git URL:

```
# git+ssh
pnpm add git+ssh://git@github.com:zkochan/is-negative.git#2.0.1

# https
pnpm add https://github.com/zkochan/is-negative.git#2.0.1
```

#### Install from a Git repository using hosting providers shorthand

You can use a protocol shorthand `[provider]:` for certain Git providers:

```
pnpm add github:zkochan/is-negative
pnpm add bitbucket:pnpmjs/git-resolver
pnpm add gitlab:pnpm/git-resolver
```

If `[provider]:` is omitted, it defaults to `github:`.

#### Install from a Git repository combining different parameters

It is possible to combine multiple parameters by separating them with `&`. This can be useful for forks of monorepos:

```
pnpm add RexSkz/test-git-subdir-fetch.git#beta\&path:/packages/simple-react-app
```

Installs from the `beta` branch and only the subdirectory at `/packages/simple-react-app`.


---

# package.json

*Sección: Pnpm*

The manifest file of a package. It contains all the package's metadata,
including dependencies, title, author, et cetera. This is a standard preserved
across all major Node.js package managers, including pnpm.

In addition to the traditional `package.json` format, pnpm also supports `package.json5` (via [json5]) and `package.yaml` (via [js-yaml]).

[json5]: https://www.npmjs.com/package/json5
[js-yaml]: https://www.npmjs.com/package/@zkochan/js-yaml

:::note

Since v11, pnpm no longer reads settings from the `pnpm` field of `package.json`. Settings must be defined in `pnpm-workspace.yaml` instead. See [Configuring](configuring.md).

:::

## engines

You can specify the version of Node and pnpm that your software works on:

```json
{
    "engines": {
        "node": ">=10",
        "pnpm": ">=3"
    }
}
```

During local development, pnpm will always fail with an error message
if its version does not match the one specified in the `engines` field.

Unless the user has set the `engineStrict` config flag (see [settings]), this
field is advisory only and will only produce warnings when your package is
installed as a dependency.

[settings]: settings/cli.md#enginestrict

## engines.runtime

Added in: v10.21.0

Specifies the Node.js runtime required by a dependency. When declared, pnpm will automatically install the specified Node.js version.

```json
{
  "engines": {
    "runtime": {
      "name": "node",
      "version": "^24.11.0",
      "onFail": "download"
    }
  }
}
```

When a package declares a runtime:

1. **For CLI apps**: pnpm binds the CLI to the required Node.js version, ensuring it uses the correct runtime regardless of the globally installed Node.js instance.
2. **For packages with `postinstall` scripts**: The script executes using the specified Node.js version.

This is particularly useful for dependencies that require specific Node.js versions to function correctly.

## devEngines.runtime

Added in: v10.14

Allows to specify one or more JavaScript runtime engines used by the project. Supported runtimes are Node.js, Deno, and Bun.

For instance, here is how to add `node@^24.4.0` to your dependencies:

```json
{
  "devEngines": {
    "runtime": {
      "name": "node",
      "version": "^24.4.0",
      "onFail": "download"
    }
  }
}
```

You can also add multiple runtimes to the same `package.json`:

```json
{
  "devEngines": {
    "runtime": [
      {
        "name": "node",
        "version": "^24.4.0",
        "onFail": "download"
      },
      {
        "name": "deno",
        "version": "^2.4.3",
        "onFail": "download"
      }
    ]
  }
}
```

How it works:

1. `pnpm install` resolves your specified range to the latest matching runtime version.
1. The exact version (and checksum) is saved in the lockfile.
1. Scripts use the local runtime, ensuring consistency across environments.

To override the declared `onFail` behavior without editing the manifest, use the [`runtimeOnFail`](settings/cli.md#runtimeonfail) setting.

## devEngines.packageManager

Added in: v11.0.0

Allows specifying the pnpm version via `devEngines.packageManager` in `package.json`. Unlike the `packageManager` field, this supports version ranges. The resolved version is stored in `pnpm-lock.yaml` under `packageManagerDependencies` and reused if it still satisfies the range.

```json
{
  "devEngines": {
    "packageManager": {
      "name": "pnpm",
      "version": ">=11.0.0 <12.0.0",
      "onFail": "download"
    }
  }
}
```

:::note

When pnpm is declared via the legacy `packageManager` field (not `devEngines.packageManager`), its resolution info is **not** written to `pnpm-lock.yaml` — unless the pinned pnpm version is v12 or newer. This keeps the lockfile stable when upgrading from pnpm v10 to v11 without forcing projects off the legacy field.

:::

To override the `onFail` behavior without editing the manifest, see the [`pmOnFail`](settings/cli.md#pmonfail) setting.

## dependenciesMeta

Additional meta information used for dependencies declared inside `dependencies`, `optionalDependencies`, and `devDependencies`.

### dependenciesMeta.*.injected

If this is set to `true` for a dependency that is a local workspace package, that package will be installed by creating a hard linked copy in the virtual store (`node_modules/.pnpm`).

If this is set to `false` or not set, then the dependency will instead be installed by creating a `node_modules` symlink that points to the package's source directory in the workspace.  This is the default, as it is faster and ensures that any modifications to the dependency will be immediately visible to its consumers.

For example, suppose the following `package.json` is a local workspace package:

```json
{
  "name": "card",
  "dependencies": {
    "button": "workspace:1.0.0"
  }
}
```

The `button` dependency will normally be installed by creating a symlink in the `node_modules` directory of `card`, pointing to the development directory for `button`.

But what if `button` specifies `react` in its `peerDependencies`? If all projects in the monorepo use the same version of `react`, then there is no problem. But what if `button` is required by `card` that uses `react@16` and `form` that uses `react@17`? Normally you'd have to choose a single version of `react` and specify it using `devDependencies` of `button`. Symlinking does not provide a way for the `react` peer dependency to be satisfied differently by different consumers such as `card` and `form`.

The `injected` field solves this problem by installing a hard linked copies of `button` in the virtual store. To accomplish this, the `package.json` of `card` could be configured as follows:

```json
{
  "name": "card",
  "dependencies": {
    "button": "workspace:1.0.0",
    "react": "16"
  },
  "dependenciesMeta": {
    "button": {
      "injected": true
    }
  }
}
```

Whereas the `package.json` of `form` could be configured as follows:

```json
{
  "name": "form",
  "dependencies": {
    "button": "workspace:1.0.0",
    "react": "17"
  },
  "dependenciesMeta": {
    "button": {
      "injected": true
    }
  }
}
```

With these changes, we say that `button` is an "injected dependency" of `card` and `form`.  When `button` imports `react`, it will resolve to `react@16` in the context of `card`, but resolve to `react@17` in the context of `form`.

Because injected dependencies produce copies of their workspace source directory, these copies must be updated somehow whenever the code is modified; otherwise, the new state will not be reflected for consumers. When building multiple projects with a command such as `pnpm --recursive run build`, this update must occur after each injected package is rebuilt but before its consumers are rebuilt. For simple use cases, it can be accomplished by invoking `pnpm install` again, perhaps using a `package.json` lifecycle script such as `"prepare": "pnpm run build"` to rebuild that one project.  Third party tools such as [pnpm-sync](https://www.npmjs.com/package/pnpm-sync-lib) and [pnpm-sync-dependencies-meta-injected](https://www.npmjs.com/package/pnpm-sync-dependencies-meta-injected) provide a more robust and efficient solution for updating injected dependencies, as well as watch mode support.

## peerDependencies

Peer dependency values are normally semver ranges (`^1.0.0`), or a [`workspace:`](workspaces.md#workspace-protocol-workspace) or [`catalog:`](catalogs.md) specifier.

Since v11.14.0, a peer dependency may also be declared with a specifier that carries a scheme:

```json
{
  "peerDependencies": {
    "lib-a": "work:5.x.x",
    "lib-b": "npm:other-lib@^5",
    "lib-c": "file:../lib-c",
    "lib-d": "git+https://example.com/lib-d.git"
  }
}
```

Accepted forms are a [named-registry](settings/dependency-resolution.md#namedregistries) spec (`<registry>:<version>`), an `npm:` alias, and a `file:`, git, or URL spec.

Such a specifier is matched against the semver range it carries — `work:5.x.x` is checked as `5.x.x` and `npm:other-lib@^5` as `^5`. A specifier that carries no version, such as `file:../lib-c`, is matched against `*`, so any version satisfies it. Meanwhile the original specifier is what selects the package when [`autoInstallPeers`](settings/peer-dependencies.md#autoinstallpeers) installs a missing peer, so the peer is fetched from the aliased name, registry, or source you named.

Bare `name@version` values are still rejected with `ERR_PNPM_INVALID_PEER_DEPENDENCY_SPECIFICATION`, as they are almost always a mistake:

```json
{
  "peerDependencies": {
    "lib-a": "lib-a@1.2.3"
  }
}
```

## peerDependenciesMeta

This field lists some extra information related to the dependencies listed in
the `peerDependencies` field.

### peerDependenciesMeta.*.optional

If this is set to true, the selected peer dependency will be marked as optional
by the package manager. Therefore, the consumer omitting it will no longer be
reported as an error.

For example:
```json
{
    "peerDependencies": {
        "foo": "1"
    },
    "peerDependenciesMeta": {
        "foo": {
            "optional": true
        },
        "bar": {
            "optional": true
        }
    }
}
```

Note that even though `bar` was not specified in `peerDependencies`, it is
marked as optional. pnpm will therefore assume that any version of bar is fine.
However, `foo` is optional, but only to the required version specification.

## publishConfig

It is possible to override some fields in the manifest before the package is
packed.
The following fields may be overridden:

* [`bin`](https://github.com/stereobooster/package.json#bin)
* [`main`](https://github.com/stereobooster/package.json#main)
* [`exports`](https://nodejs.org/api/esm.html#esm_package_exports)
* [`types` or `typings`](https://github.com/stereobooster/package.json#types)
* [`module`](https://github.com/stereobooster/package.json#module)
* [`browser`](https://github.com/stereobooster/package.json#browser)
* [`esnext`](https://github.com/stereobooster/package.json#esnext)
* [`es2015`](https://github.com/stereobooster/package.json#es2015)
* [`unpkg`](https://github.com/stereobooster/package.json#unpkg-1)
* [`umd:main`](https://github.com/stereobooster/package.json#microbundle)
* [`typesVersions`](https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html#version-selection-with-typesversions)
* cpu
* os
* `engines` (Added in v10.22.0)
* [`name`](#publishconfigname) (Added in v11.18.0)

To override a field, add the publish version of the field to `publishConfig`.

For instance, the following `package.json`:

```json
{
    "name": "foo",
    "version": "1.0.0",
    "main": "src/index.ts",
    "publishConfig": {
        "main": "lib/index.js",
        "typings": "lib/index.d.ts"
    }
}
```

Will be published as:

```json
{
    "name": "foo",
    "version": "1.0.0",
    "main": "lib/index.js",
    "typings": "lib/index.d.ts"
}
```

### publishConfig.name

Added in: v11.18.0

Publishes the package under a different name than the one its manifest carries in the workspace. This is for a project whose published name is already taken by a sibling project, which otherwise has to be renamed by a build step just before publishing.

```json
{
  "name": "foo-v2",
  "version": "2.0.0",
  "publishConfig": {
    "name": "foo"
  }
}
```

Only the published artifact is renamed — dependents, `pnpm-lock.yaml`, and release tooling keep addressing the project by its manifest name. The new name reaches the packed manifest, the tarball filename, and everything that addresses the package at the registry: the already-published check of `pnpm publish -r`, its registry selection, and the release-planning probes of `pnpm change status` and `pnpm version -r`.

### publishConfig.executableFiles

By default, for portability reasons, no files except those listed in the bin field will be marked as executable in the resulting package archive. The `executableFiles` field lets you declare additional files that must have the executable flag (+x) set even if they aren't directly accessible through the bin field.

```json
{
  "publishConfig": {
    "executableFiles": [
      "./dist/shim.js"
    ]
  }
}
```

### publishConfig.directory

You also can use the field `publishConfig.directory` to customize the published subdirectory relative to the current `package.json`.

It is expected to have a modified version of the current package in the specified directory (usually using third party build tools).

> In this example the `"dist"` folder must contain a `package.json`

```json
{
  "name": "foo",
  "version": "1.0.0",
  "publishConfig": {
    "directory": "dist"
  }
}
```

### publishConfig.linkDirectory

* Default: **true**
* Type: **Boolean**

When set to `true`, the project will be symlinked from the `publishConfig.directory` location during local development.

For example:

```json
{
  "name": "foo",
  "version": "1.0.0",
  "publishConfig": {
    "directory": "dist",
    "linkDirectory": true
  }
}
```


---

# pnpm CLI

*Sección: Pnpm*

## Short aliases

Added in: v11.0.0

`pn` is available as a short alias for `pnpm`, and [`pnx`](cli/pnx.md) as a short alias for `pnpm dlx`. You can use them anywhere you'd use `pnpm` or `pnpx`:

```sh
pn install
pn add express
pn build
pn test
pnx create-vue my-app
```

## Differences vs npm

Unlike npm, pnpm validates all options. For example, `pnpm install --target_arch x64` will
fail as `--target_arch` is not a valid option for `pnpm install`.

However, some dependencies may use the `npm_config_` environment variable, which
is populated from the CLI options. In this case, you have the following options:

1. explicitly set the env variable: `npm_config_target_arch=x64 pnpm install`
1. force the unknown option with `--config.`: `pnpm install --config.target_arch=x64`

## Options

### -C &lt;path\>, --dir &lt;path\>

Run as if pnpm was started in `<path>` instead of the current working directory.

### -w, --workspace-root

Run as if pnpm was started in the root of the [workspace](workspaces.md)
instead of the current working directory.

## Commands

For more information, see the documentation for individual CLI commands. Here is
a list of handy npm equivalents to get you started:

| npm command     | pnpm equivalent    |
|-----------------|--------------------|
| `npm install`   | [`pnpm install`]     |
| `npm i <pkg>`   | [`pnpm add <pkg>`]   |
| `npm run <cmd>` | [`pnpm <cmd>`]       |
| `npx <pkg>`     | [`pnx <pkg>`]      |

When an unknown command is used, pnpm will search for a script with the given name,
so `pnpm run lint` is the same as `pnpm lint`. If there is no script with the specified name,
then pnpm will execute the command as a shell script, so you can do things like `pnpm eslint` (see [`pnpm exec`]).

[`pnpm install`]: cli/install.md
[`pnpm add <pkg>`]: cli/add.md
[`pnpm <cmd>`]: cli/run.md
[`pnpm exec`]: cli/exec.md
[`pnx <pkg>`]: cli/pnx.md

## Environment variables

Some environment variables that are not pnpm related might change the behaviour of pnpm:

* [`CI`](cli/install.md#--frozen-lockfile)

These environment variables may influence what directories pnpm will use for storing global information:

* `XDG_CACHE_HOME`
* `XDG_CONFIG_HOME`
* `XDG_DATA_HOME`
* `XDG_STATE_HOME`

You can search the docs to find the settings that leverage these environment variables.


---

# pnpm vs npm

*Sección: Pnpm*

## npm's flat tree

npm maintains a [flattened dependency tree] as of version 3. This leads to less
disk space bloat, with a messy `node_modules` directory as a side effect.

On the other hand, pnpm manages `node_modules` by using hard linking and
symbolic linking to a global on-disk content-addressable store. This lets you get the benefits of far less disk space usage, while also keeping your
`node_modules` clean. There is documentation on the [store layout] if you wish
to learn more.

The good thing about pnpm's proper `node_modules` structure is that it
"[helps to avoid silly bugs]" by making it impossible to use modules that are not
specified in the project's `package.json`.

[flattened dependency tree]: https://github.com/npm/npm/issues/6912
[store layout]: symlinked-node-modules-structure
[helps to avoid silly bugs]: https://www.kochan.io/nodejs/pnpms-strictness-helps-to-avoid-silly-bugs.html

## Installation

pnpm does not allow installation of packages without saving them to
`package.json`. If no parameters are passed to `pnpm add`, packages are saved as
regular dependencies. Like with npm, `--save-dev` and `--save-optional` can be
used to install packages as dev or optional dependencies.

As a consequence of this limitation, projects won't have any extraneous packages
when they use pnpm unless they remove a dependency and leave it orphaned. That's
why pnpm's implementation of the [prune command] does not allow you to specify
packages to prune - it ALWAYS removes all extraneous and orphaned packages.

[prune command]: cli/prune

## Directory dependencies

Directory dependencies start with the `file:` prefix and point to a directory in
the filesystem. Like npm, pnpm symlinks those dependencies. Unlike npm, pnpm
does not perform installation for the file dependencies.

This means that if you have a package called `foo` (`<root>/foo`) that has
`bar@file:../bar` as a dependency, pnpm won't perform installation for
`<root>/bar` when you run `pnpm install` on `foo`.

If you need to run installations in several packages at the same time, for
instance in the case of a monorepo, you should look at the documentation for
[`pnpm -r`].

[`pnpm -r`]: cli/recursive


---

# .pnpmfile.mjs

*Sección: Pnpm*

pnpm lets you hook directly into the installation process via special functions
(hooks). Hooks can be declared in a file called `.pnpmfile.mjs` (ESM) or `.pnpmfile.cjs` (CommonJS).

By default, `.pnpmfile.mjs` should be located in the same directory as the
lockfile. For instance, in a [workspace](workspaces.md) with a shared lockfile,
`.pnpmfile.mjs` should be in the root of the monorepo.

## Hooks

### TL;DR

| Hook Function                                         | Process                                                    | Uses                                               |
|-------------------------------------------------------|------------------------------------------------------------|----------------------------------------------------|
| `hooks.readPackage(pkg, context): pkg`                | Called after pnpm parses the dependency's package manifest | Allows you to mutate a dependency's `package.json`. |
| `hooks.afterAllResolved(lockfile, context): lockfile` | Called after the dependencies have been resolved.          | Allows you to mutate the lockfile.                 |
| `hooks.beforePacking(pkg): pkg`                       | Called before creating a tarball during pack/publish       | Allows you to customize the published `package.json` |
| `resolvers`                                           | Called during package resolution.                          | Allows you to register custom package resolvers.  |
| `fetchers`                                            | Called during package fetching.                            | Allows you to register custom package fetchers.   |

### `hooks.readPackage(pkg, context): pkg | Promise<pkg>`

Allows you to mutate a dependency's `package.json` after parsing and prior to
resolution. These mutations are not saved to the filesystem, however, they will
affect what gets resolved in the lockfile and therefore what gets installed.

Note that you will need to delete the `pnpm-lock.yaml` if you have already
resolved the dependency you want to modify.

:::tip

If you need changes to `package.json` saved to the filesystem, you need to use the [`pnpm patch`] command and patch the `package.json` file.
This might be useful if you want to remove the `bin` field of a dependency for instance.

:::

#### Arguments

* `pkg` - The manifest of the package. Either the response from the registry or
the `package.json` content.
* `context` - Context object for the step. Method `#log(msg)` allows you to use
a debug log for the step.

#### Usage

Example `.pnpmfile.mjs` (changes the dependencies of a dependency):

```js
function readPackage(pkg, context) {
  // Override the manifest of foo@1.x after downloading it from the registry
  if (pkg.name === 'foo' && pkg.version.startsWith('1.')) {
    // Replace bar@x.x.x with bar@2.0.0
    pkg.dependencies = {
      ...pkg.dependencies,
      bar: '^2.0.0'
    }
    context.log('bar@1 => bar@2 in dependencies of foo')
  }

  // This will change any packages using baz@x.x.x to use baz@1.2.3
  if (pkg.dependencies.baz) {
    pkg.dependencies.baz = '1.2.3';
  }

  return pkg
}
  readPackage
}
```

#### Known limitations

Removing the `scripts` field from a dependency's manifest via `readPackage` will
not prevent pnpm from building the dependency. When building a dependency, pnpm
reads the `package.json` of the package from the package's archive, which is not
affected by the hook. In order to ignore a package's build, use the
[allowBuilds](settings/build.md#allowbuilds) field.

### `hooks.updateConfig(config): config | Promise<config>`

Added in: v10.8.0

Allows you to modify the configuration settings used by pnpm. This hook is most useful when paired with [configDependencies](config-dependencies), allowing you to share and reuse settings across different Git repositories.

For example, [@pnpm/plugin-better-defaults](https://github.com/pnpm/plugin-better-defaults) uses the `updateConfig` hook to apply a curated set of recommended settings.

#### Usage example

```js title=".pnpmfile.mjs"
  updateConfig (config) {
    return Object.assign(config, {
      enablePrePostScripts: false,
      optimisticRepeatInstall: true,
      resolutionMode: 'lowest-direct',
      verifyDepsBeforeRun: 'install',
    })
  }
}
```

### `hooks.afterAllResolved(lockfile, context): lockfile | Promise<lockfile>`

Allows you to mutate the lockfile output before it is serialized.

#### Arguments

* `lockfile` - The lockfile resolutions object that is serialized to
`pnpm-lock.yaml`.
* `context` - Context object for the step. Method `#log(msg)` allows you to use
a debug log for the step.

#### Usage example

```js title=".pnpmfile.mjs"
function afterAllResolved(lockfile, context) {
  // ...
  return lockfile
}
  afterAllResolved
}
```

#### Known Limitations

There are none - anything that can be done with the lockfile can be modified via
this function, and you can even extend the lockfile's functionality.

### `hooks.beforePacking(pkg): pkg | Promise<pkg>`

Added in: v10.28.0

Allows you to modify the `package.json` manifest before it is packed into a tarball during `pnpm pack` or `pnpm publish`. This is useful for customizing the published package without affecting your local development `package.json`.

Unlike `hooks.readPackage`, which modifies how dependencies are resolved during installation, `beforePacking` only affects the contents of the tarball that gets published.

#### Arguments

* `pkg` - The package manifest object that will be included in the published tarball.

#### Usage example

```js title=".pnpmfile.mjs"
function beforePacking(pkg) {
  // Remove development-only fields from published package
  delete pkg.devDependencies
  delete pkg.scripts.test

  // Add publication metadata
  pkg.publishedAt = new Date().toISOString()

  // Modify package exports for production
  if (pkg.name === 'my-package') {
    pkg.main = './dist/index.js'
  }

  return pkg
}
  beforePacking
}
```

:::note

The modifications made by this hook only affect the `package.json` inside the tarball. Your local `package.json` file remains unchanged.

:::

### `hooks.preResolution(options): Promise<void>`

This hook is executed after reading and parsing the lockfiles of the project, but before resolving dependencies. It allows modifications to the lockfile objects.

#### Arguments

* `options.existsCurrentLockfile` - A boolean that is true if the lockfile at `node_modules/.pnpm/lock.yaml` exists.
* `options.currentLockfile` - The lockfile object from `node_modules/.pnpm/lock.yaml`.
* `options.existsNonEmptyWantedLockfile` - A boolean that is true if the lockfile at `pnpm-lock.yaml` exists.
* `options.wantedLockfile` - The lockfile object from `pnpm-lock.yaml`.
* `options.lockfileDir` - The directory where the wanted lockfile is found.
* `options.storeDir` - The location of the store directory.
* `options.registries` - A map of scopes to registry URLs.

### `hooks.importPackage(destinationDir, options): Promise<string | undefined>`

This hook allows to change how packages are written to `node_modules`. The return value is optional and states what method was used for importing the dependency, e.g.: clone, hardlink.

#### Arguments

* `destinationDir` - The destination directory where the package should be written.
* `options.disableRelinkLocalDirDeps`
* `options.filesMap`
* `options.force`
* `options.resolvedFrom`
* `options.keepModulesDir`

### `hooks.fetchers`

:::danger Removed in v11.0.0

`hooks.fetchers` has been removed. Use top-level `fetchers` instead. See the [Custom Fetchers](#custom-fetchers) section for the new API.

:::

## Finders

Added in: v10.16.0

Finder functions are used with `pnpm list` and `pnpm why` via the `--find-by` flag.

Example:

```js title=".pnpmfile.mjs"
  react17: (ctx) => {
    return ctx.readManifest().peerDependencies?.react === "^17.0.0"
  }
}
```

Usage:

```
pnpm why --find-by=react17
```

See [Finders] for more details.

[Finders]: finders.md

## Custom Resolvers and Fetchers

Added in: v11.0.0

Custom resolvers and fetchers allow you to implement custom package resolution and fetching logic for new package identifier schemes (like `my-protocol:package-name`). They are registered as top-level exports in `.pnpmfile.cjs`:

```js
module.exports = {
  resolvers: [customResolver1, customResolver2],
  fetchers: [customFetcher1, customFetcher2],
}
```

#### TypeScript Interfaces

```typescript
interface CustomResolver {
  canResolve?: (wantedDependency: WantedDependency) => boolean | Promise<boolean>
  resolve?: (wantedDependency: WantedDependency, opts: ResolveOptions) => ResolveResult | Promise
  shouldRefreshResolution?: (depPath: string, pkgSnapshot: PackageSnapshot) => boolean | Promise<boolean>
}

interface CustomFetcher {
  canFetch?: (pkgId: string, resolution: Resolution) => boolean | Promise<boolean>
  fetch?: (cafs: Cafs, resolution: Resolution, opts: FetchOptions, fetchers: Fetchers) => FetchResult | Promise
}
```

### Custom Resolvers

Custom resolvers convert package descriptors (e.g., `foo@^1.0.0`) into resolutions that are stored in the lockfile.

#### Resolver Interface

A custom resolver is an object that can implement any combination of the following methods:

##### `canResolve(wantedDependency): boolean | Promise<boolean>`

Determines whether this resolver can resolve a given wanted dependency.

**Arguments:**
- `wantedDependency` - Object with:
  - `alias` - The package name or alias as it appears in package.json
  - `bareSpecifier` - The version range, git URL, file path, or other specifier

**Returns:** `true` if this resolver can handle the package, `false` otherwise. This determines whether `resolve` will be called.

##### `resolve(wantedDependency, opts): ResolveResult | Promise`

Resolves a wanted dependency to specific package metadata and resolution information.

**Arguments:**
- `wantedDependency` - The wanted dependency (same as `canResolve`)
- `opts` - Object with:
  - `lockfileDir` - Directory containing the lockfile
  - `projectDir` - The project root directory
  - `preferredVersions` - Map of package names to preferred versions

**Returns:** Object with:
- `id` - Unique package identifier (e.g., `'custom-pkg@1.0.0'`)
- `resolution` - Resolution metadata. This can be:
  - Standard resolution, e.g. `{ tarball: 'https://...', integrity: '...' }`
  - Custom resolution: `{ type: 'custom:cdn', url: '...' }`

Custom resolutions must be handled by a corresponding custom fetcher.

:::warning Custom Resolution Types

Custom resolutions must use the `custom:` prefix in their type field (e.g., `custom:cdn`, `custom:artifactory`) to differentiate them from pnpm's built-in resolution types.

:::

##### `shouldRefreshResolution(depPath, pkgSnapshot): boolean | Promise<boolean>`

Return `true` to trigger full resolution of all packages, skipping the "Lockfile is up to date" optimization. This is useful for implementing time-based cache invalidation or other custom re-resolution logic.

**Arguments:**
- `depPath` - The package identifier string (e.g., `lodash@4.17.21`)
- `pkgSnapshot` - The lockfile entry for this package, providing direct access to the resolution, dependencies, etc.

**Returns:** `true` to force re-resolution, `false` otherwise.

:::note

`shouldRefreshResolution` is skipped during frozen lockfile installs, as no resolution is allowed in that mode.

:::

### Custom Fetchers

Custom fetchers completely handle fetching for custom package types, downloading package contents from custom sources and storing them in pnpm's content-addressable file system.

#### Fetcher Interface

A custom fetcher is an object that can implement the following methods:

##### `canFetch(pkgId, resolution): boolean | Promise<boolean>`

Determines whether this fetcher can fetch a package with the given resolution.

**Arguments:**
- `pkgId` - The unique package identifier from the resolution phase
- `resolution` - The resolution object from a resolver's `resolve` method

**Returns:** `true` if this fetcher can handle fetching this package, `false` otherwise.

##### `fetch(cafs, resolution, opts, fetchers): FetchResult | CustomFetcherDelegation | Promise`

Fetches package files and returns metadata about the fetched package.

**Arguments:**
- `cafs` - Content-addressable file system interface for storing files
- `resolution` - The resolution object (same as passed to `canFetch`)
- `opts` - Fetch options including:
  - `lockfileDir` - Directory containing the lockfile
  - `filesIndexFile` - Path for the files index
  - `onStart` - Optional callback when fetch starts
  - `onProgress` - Optional progress callback
- `fetchers` - Object containing pnpm's standard fetchers for delegation:
  - `remoteTarball` - Fetcher for remote tarballs
  - `localTarball` - Fetcher for local tarballs
  - `gitHostedTarball` - Fetcher for GitHub/GitLab/Bitbucket tarballs
  - `directory` - Fetcher for local directories
  - `git` - Fetcher for git repositories

**Returns:** either a fetch result, or a [delegation envelope](#delegating-to-the-built-in-fetchers).

A fetch result is an object with:
- `filesIndex` - Map of relative file paths to their physical locations. For remote packages, these are paths in pnpm's content-addressable store (CAFS). For local packages (when `local: true`), these are absolute paths to files on disk.
- `manifest` - Optional. The package.json from the fetched package. If not provided, pnpm will read it from disk when needed. Providing it avoids an extra file I/O operation and is recommended when you have the manifest data readily available (e.g., already parsed during fetch).
- `requiresBuild` - Boolean indicating whether the package has build scripts that need to be executed. Set to `true` if the package has `preinstall`, `install`, or `postinstall` scripts, or contains `binding.gyp` or `.hooks/` files. Standard fetchers determine this automatically using the manifest and file list.
- `local` - Optional. Set to `true` to load the package directly from disk without copying to pnpm's store. When `true`, `filesIndex` should contain absolute paths to files on disk, and pnpm will hardlink them to `node_modules` instead of copying. This is how the directory fetcher handles local dependencies (e.g., `file:../my-package`).

#### Delegating to the built-in fetchers

Added in: v11.12.0

Rather than fetching the package itself, a custom fetcher may hand the work back to pnpm. There are two ways to do this.

**Return a `{ delegate }` envelope.** Instead of a fetch result, return an object with a single `delegate` key holding the resolution pnpm should fetch instead. pnpm rewrites the package's resolution to that shape and runs its built-in fetch path on it:

```js title=".pnpmfile.cjs"
const customFetcher = {
  canFetch: (pkgId, resolution) => resolution.type === 'custom:url',
  fetch: (cafs, resolution) => ({
    delegate: {
      tarball: resolution.customUrl,
      integrity: resolution.integrity,
    },
  }),
}

module.exports = { fetchers: [customFetcher] }
```

The delegated resolution must be a complete, fetchable shape (for example `{ tarball, integrity }`). Delegation is single-step: a `delegate` that is itself custom-typed is rejected.

**Call `fetchers.*` directly.** The `fetchers` argument gives you pnpm's standard fetchers, so you can transform the resolution and invoke one yourself.

:::tip Prefer the envelope for portability

The `{ delegate }` envelope is the only delegation form that works in both pnpm and [pacquet](https://github.com/pnpm/pnpm/tree/main/pacquet) (the Rust port of pnpm). pacquet invokes pnpmfile fetchers over IPC, where `cafs` and `fetchers` cannot exist and both arrive as `null`. A fetcher that should run on either stack must return the envelope rather than calling `fetchers.*`.

:::

#### Usage Examples

##### Basic Custom Resolver

This example shows a custom resolver that resolves packages from a custom registry:

```js title=".pnpmfile.cjs"
const customResolver = {
  // Only handle packages with @company scope
  canResolve: (wantedDependency) => {
    return wantedDependency.alias.startsWith('@company/')
  },

  resolve: async (wantedDependency, opts) => {
    // Fetch metadata from custom registry
    const response = await fetch(
      `https://custom-registry.company.com/${wantedDependency.alias}/${wantedDependency.bareSpecifier}`
    )
    const metadata = await response.json()

    return {
      id: `${metadata.name}@${metadata.version}`,
      resolution: {
        tarball: metadata.tarballUrl,
        integrity: metadata.integrity
      }
    }
  }
}

module.exports = {
  resolvers: [customResolver]
}
```

##### Custom Resolver and Fetcher with `shouldRefreshResolution`

This example shows a resolver and fetcher working together with a custom resolution type and time-based cache invalidation:

```js title=".pnpmfile.cjs"
const customResolver = {
  canResolve: (wantedDependency) => {
    return wantedDependency.alias.startsWith('company-cdn:')
  },

  resolve: async (wantedDependency, opts) => {
    const actualName = wantedDependency.alias.replace('company-cdn:', '')
    const version = await fetchVersionFromCompanyCDN(actualName, wantedDependency.bareSpecifier)

    return {
      id: `company-cdn:${actualName}@${version}`,
      resolution: {
        type: 'custom:cdn',
        cdnUrl: `https://cdn.company.com/packages/${actualName}/${version}.tgz`,
        cachedAt: Date.now(), // Custom metadata for shouldRefreshResolution
      },
    }
  },

  shouldRefreshResolution: (depPath, pkgSnapshot) => {
    // Check custom metadata stored in the resolution
    const cachedAt = pkgSnapshot.resolution?.cachedAt
    if (cachedAt && Date.now() - cachedAt > 24 * 60 * 60 * 1000) {
      return true // Re-resolve if cached more than 24 hours ago
    }
    return false
  },
}

const customFetcher = {
  canFetch: (pkgId, resolution) => {
    return resolution.type === 'custom:cdn'
  },

  fetch: async (cafs, resolution, opts, fetchers) => {
    // Delegate to pnpm's standard tarball fetcher
    const tarballResolution = {
      tarball: resolution.cdnUrl,
      integrity: resolution.integrity,
    }

    return fetchers.remoteTarball(cafs, tarballResolution, opts)
  },
}

module.exports = {
  resolvers: [customResolver],
  fetchers: [customFetcher],
}
```

##### Basic Custom Fetcher

This example shows a custom fetcher that fetches certain packages from a different source:

```js title=".pnpmfile.cjs"
const customFetcher = {
  canFetch: (pkgId, resolution) => {
    return pkgId.startsWith('@company/')
  },

  fetch: async (cafs, resolution, opts, fetchers) => {
    // Delegate to pnpm's tarball fetcher with modified URL
    const tarballResolution = {
      tarball: resolution.tarball.replace(
        'https://registry.npmjs.org/',
        'https://custom-registry.company.com/'
      ),
      integrity: resolution.integrity
    }

    return fetchers.remoteTarball(cafs, tarballResolution, opts)
  }
}

module.exports = {
  fetchers: [customFetcher]
}
```

##### Custom Resolution Type with Resolver and Fetcher

This example shows a custom resolver and fetcher working together with a custom resolution type:

```js title=".pnpmfile.cjs"
const customResolver = {
  canResolve: (wantedDependency) => {
    return wantedDependency.alias.startsWith('@internal/')
  },

  resolve: async (wantedDependency) => {
    return {
      id: `${wantedDependency.alias}@${wantedDependency.bareSpecifier}`,
      resolution: {
        type: 'custom:internal-directory',
        directory: `/packages/${wantedDependency.alias}/${wantedDependency.bareSpecifier}`
      }
    }
  }
}

const customFetcher = {
  canFetch: (pkgId, resolution) => {
    return resolution.type === 'custom:internal-directory'
  },

  fetch: async (cafs, resolution, opts, fetchers) => {
    // Delegate to pnpm's directory fetcher for local packages
    const directoryResolution = {
      type: 'directory',
      directory: resolution.directory
    }

    return fetchers.directory(cafs, directoryResolution, opts)
  }
}

module.exports = {
  resolvers: [customResolver],
  fetchers: [customFetcher]
}
```

#### Priority and Ordering

When multiple resolvers are registered, they are checked in order. The first resolver where `canResolve` returns `true` will be used for resolution. The same applies for fetchers: The first fetcher where `canFetch` returns `true` will be used during the fetch phase.

Custom resolvers are tried before pnpm's built-in resolvers (npm, git, tarball, etc.), giving you full control over package resolution.

#### Performance Considerations

`canResolve()`, `canFetch()`, and `shouldRefreshResolution()` should be cheap checks (ideally synchronous), as they're called for every dependency during resolution.

## Related Configuration

### ignorePnpmfile

* Default: **false**
* Type: **Boolean**

The pnpmfile will be ignored. Useful together with `--ignore-scripts` when you
want to make sure that no script gets executed during install.

### pnpmfile

* Default: **['.pnpmfile.mjs']**
* Type: **path[]**
* Example: **['.pnpm/.pnpmfile.mjs']**

The location of the local pnpmfile(s).

### globalPnpmfile

* Default: **null**
* Type: **path**
* Example: **~/.pnpm/global_pnpmfile.mjs**

The location of a global pnpmfile. A global pnpmfile is used by all projects
during installation.

:::note

It is recommended to use local pnpmfiles. Only use a global pnpmfile
if you use pnpm on projects that don't use pnpm as the primary package manager.

:::

[`pnpm patch`]: cli/patch.md


---

# Working with Podman

*Sección: Pnpm*

## Sharing Files Between a Container and the Host Btrfs Filesystem

:::note

This method only works on copy-on-write filesystems supported by Podman, such as Btrfs. For other filesystems, like Ext4, pnpm will copy the files instead.

:::

Podman support copy-on-write filesystems like Btrfs. With Btrfs, container runtimes create actual Btrfs subvolumes for their mounted volumes. pnpm can leverage this behavior to reflink the files between different mounted volumes.

To share files between the host and the container, mount the store directory and the `node_modules` directory from the host to the container. This allows pnpm inside the container to naturally reuse the files from the host as reflinks.

:::important

Only mount a host pnpm store into containers you trust. A container with write access to the mounted store can affect later installs that reuse that store.

:::

Below is an example container setup for demonstration:

```dockerfile title="Dockerfile"
FROM node:20-slim

# corepack is an experimental feature in Node.js v20 which allows
# installing and managing versions of pnpm, npm, yarn
RUN corepack enable

VOLUME [ "/pnpm-store", "/app/node_modules" ]
RUN pnpm config --global set store-dir /pnpm-store

# You may need to copy more files than just package.json in your code
COPY package.json /app/package.json

WORKDIR /app
RUN pnpm install
RUN pnpm run build
```

Run the following command to build the podman image:

```sh
podman build . --tag my-podman-image:latest -v "$HOME/.local/share/pnpm/store:/pnpm-store" -v "$(pwd)/node_modules:/app/node_modules"
```


---

# Production

*Sección: Pnpm*

There are two ways to bootstrap your package in a production environment with
pnpm. One of these is to commit the lockfile. Then, in your production
environment, run `pnpm install` - this will build the dependency tree using the
lockfile, meaning the dependency versions will be consistent with how they were
when the lockfile was committed. This is the most effective way (and the one we
recommend) to ensure your dependency tree persists across environments.

The other method is to commit the lockfile AND copy the package store to your
production environment (you can change where with the [store location option]).
Then, you can run `pnpm install --offline` and pnpm will use the packages from
the global store, so it will not make any requests to the registry. This is
recommended **ONLY** for environments where external access to the registry is
unavailable for whatever reason.

[store location option]: settings/store.md#storedir


---

# Scripts

*Sección: Pnpm*

How pnpm handles the `scripts` field of `package.json`.

## Hidden Scripts

Added in: v11.0.0

Scripts with names starting with `.` are hidden. They cannot be run directly via `pnpm run` and are omitted from the `pnpm run` listing. Hidden scripts can only be called from other scripts.

```json
{
  "scripts": {
    ".helper": "echo 'I am hidden'",
    "build": "pnpm run .helper && tsc"
  }
}
```

In this example, `pnpm run .helper` would fail, but `pnpm run build` would succeed because `.helper` is called from another script.

## Environment Variables

pnpm sets the following environment variables during lifecycle script execution:

- `npm_package_name` — the package name
- `npm_package_version` — the package version
- `npm_lifecycle_event` — the name of the running script (e.g., `postinstall`)

:::note

Since v11, pnpm no longer populates `npm_config_*` environment variables from the pnpm configuration. Only the well-known `npm_*` variables above are set, matching Yarn's behavior.

:::

## Built-in Command and Script Name Conflicts

Added in: v11.0.0

The following built-in commands prefer user scripts: `clean`, `setup`, `deploy`, and `rebuild`. If your `package.json` defines a script with one of these names, `pnpm <name>` will execute the script instead of the built-in command.

To force the built-in command, use [`pnpm pm <name>`](cli/pm.md).

## Lifecycle Scripts

### `pnpm:devPreinstall`

Runs only on local `pnpm install`.

Runs before any dependency is installed.

This script is executed only when set in the root project's `package.json`.


---

# Settings (pnpm-workspace.yaml)

*Sección: Pnpm*

pnpm gets its configuration from the command line, environment variables, and `pnpm-workspace.yaml`.

Only auth and registry settings are read from `.npmrc` files. All other settings (like `hoistPattern`, `nodeLinker`, `shamefullyHoist`, etc.) must be configured in `pnpm-workspace.yaml` or the global `~/.config/pnpm/config.yaml`.

The `pnpm config` command can be used to read and edit the contents of the project and global configuration files.

The relevant configuration files are:

* Per-project configuration file: `/path/to/my/project/pnpm-workspace.yaml`
* [Global configuration file](cli/config.md)

:::note

Authorization-related settings are handled via [`.npmrc`](npmrc.md).

:::

Values in the configuration files may contain env variables using the `${NAME}` syntax. The env variables may also be specified with default values. Using `${NAME-fallback}` will return `fallback` if `NAME` isn't set. `${NAME:-fallback}` will return `fallback` if `NAME` isn't set, or is an empty string.

:::warning

Since v11.5.3, env variables are **not** expanded in settings of `pnpm-workspace.yaml` that define registry URLs: `registry` and the URL values of [`registries`](settings/dependency-resolution.md#registries) and [`namedRegistries`](settings/dependency-resolution.md#namedregistries). Values containing a `${...}` placeholder in these settings are ignored. Because `pnpm-workspace.yaml` is committed to the repository, expanding env variables in registry URLs could be exploited by a malicious repository to leak secrets from the environment to an attacker-controlled registry. Configure dynamic registry URLs in a trusted location instead: the global configuration file or CLI options.

:::

[INI-formatted]: https://en.wikipedia.org/wiki/INI_file

## packages

Besides settings, `pnpm-workspace.yaml` defines the root of the [workspace] and
enables you to include / exclude directories from the workspace. If the
`packages` field is omitted, only the root package is included in the workspace.

For example:

```yaml title="pnpm-workspace.yaml"
packages:
  # specify a package in a direct subdir of the root
  - 'my-app'
  # all packages in direct subdirs of packages/
  - 'packages/*'
  # all packages in subdirs of components/
  - 'components/**'
  # exclude packages that are inside test directories
  - '!**/test/**'
```

The root package is always included, even when custom location wildcards are
used.

Catalogs are also defined in the `pnpm-workspace.yaml` file. See [_Catalogs_](catalogs.md) for details.

```yaml title="pnpm-workspace.yaml"
packages:
  - 'packages/*'

catalog:
  chalk: ^4.1.2

catalogs:
  react16:
    react: ^16.7.0
    react-dom: ^16.7.0
  react17:
    react: ^17.10.0
    react-dom: ^17.10.0
```

[workspace]: workspaces.md

## packageConfigs

Added in: v11.0.0

Allows setting project-specific configuration for individual workspace packages. This replaces workspace project-specific `.npmrc` files.

`packageConfigs` can be specified as a map of package names to config objects:

```yaml title="pnpm-workspace.yaml"
packages:
  - "packages/project-1"
  - "packages/project-2"
packageConfigs:
  "project-1":
    saveExact: true
  "project-2":
    savePrefix: "~"
```

Or as an array of pattern-matched rules:

```yaml title="pnpm-workspace.yaml"
packages:
  - "packages/project-1"
  - "packages/project-2"
packageConfigs:
  - match: ["project-1", "project-2"]
    modulesDir: "node_modules"
    saveExact: true
```

## Settings

Every setting is listed below, grouped by topic. Follow a setting to read its documentation, or open the full reference of a group.

### Dependency Resolution

[Full reference →](settings/dependency-resolution.md)

* [overrides](settings/dependency-resolution.md#overrides)
  * [Convergence overrides](settings/dependency-resolution.md#convergence-overrides)
  * [Overriding peer dependencies](settings/dependency-resolution.md#overriding-peer-dependencies)
* [packageExtensions](settings/dependency-resolution.md#packageextensions)
* [allowedDeprecatedVersions](settings/dependency-resolution.md#alloweddeprecatedversions)
* [update](settings/dependency-resolution.md#update)
  * [update.ignoreDeps](settings/dependency-resolution.md#updateignoredeps)
  * [update.changeset](settings/dependency-resolution.md#updatechangeset)
  * [update.githubActions](settings/dependency-resolution.md#updategithubactions)
  * [update.githubActionsServer](settings/dependency-resolution.md#updategithubactionsserver)
* [supportedArchitectures](settings/dependency-resolution.md#supportedarchitectures)
* [ignoredOptionalDependencies](settings/dependency-resolution.md#ignoredoptionaldependencies)
* [minimumReleaseAge](settings/dependency-resolution.md#minimumreleaseage)
* [minimumReleaseAgeExclude](settings/dependency-resolution.md#minimumreleaseageexclude)
* [minimumReleaseAgeIgnoreMissingTime](settings/dependency-resolution.md#minimumreleaseageignoremissingtime)
* [minimumReleaseAgeStrict](settings/dependency-resolution.md#minimumreleaseagestrict)
* [trustPolicy](settings/dependency-resolution.md#trustpolicy)
* [trustPolicyExclude](settings/dependency-resolution.md#trustpolicyexclude)
* [trustPolicyIgnoreAfter](settings/dependency-resolution.md#trustpolicyignoreafter)
* [trustLockfile](settings/dependency-resolution.md#trustlockfile)
* [blockExoticSubdeps](settings/dependency-resolution.md#blockexoticsubdeps)
* [registries](settings/dependency-resolution.md#registries)
* [namedRegistries](settings/dependency-resolution.md#namedregistries)

### Node-Modules Settings

[Full reference →](settings/node-modules.md#node-modules-settings)

* [modulesDir](settings/node-modules.md#modulesdir)
* [nodeLinker](settings/node-modules.md#nodelinker)
* [nodeExperimentalPackageMap](settings/node-modules.md#nodeexperimentalpackagemap)
* [nodePackageMapType](settings/node-modules.md#nodepackagemaptype)
* [symlink](settings/node-modules.md#symlink)
* [enableModulesDir](settings/node-modules.md#enablemodulesdir)
* [virtualStoreDir](settings/node-modules.md#virtualstoredir)
* [virtualStoreDirMaxLength](settings/node-modules.md#virtualstoredirmaxlength)
* [virtualStoreOnly](settings/node-modules.md#virtualstoreonly)
* [packageImportMethod](settings/node-modules.md#packageimportmethod)
* [modulesCacheMaxAge](settings/node-modules.md#modulescachemaxage)
* [dlxCacheMaxAge](settings/node-modules.md#dlxcachemaxage)
* [enableGlobalVirtualStore](settings/node-modules.md#enableglobalvirtualstore)

### Dependency Hoisting Settings

[Full reference →](settings/node-modules.md#dependency-hoisting-settings)

* [hoist](settings/node-modules.md#hoist)
* [hoistWorkspacePackages](settings/node-modules.md#hoistworkspacepackages)
* [hoistPattern](settings/node-modules.md#hoistpattern)
* [publicHoistPattern](settings/node-modules.md#publichoistpattern)
* [shamefullyHoist](settings/node-modules.md#shamefullyhoist)
* [hoistingLimits](settings/node-modules.md#hoistinglimits)

### Store Settings

[Full reference →](settings/store.md#store-settings)

* [storeDir](settings/store.md#storedir)
* [verifyStoreIntegrity](settings/store.md#verifystoreintegrity)
* [useRunningStoreServer](settings/store.md#userunningstoreserver)
* [strictStorePkgContentCheck](settings/store.md#strictstorepkgcontentcheck)
* [frozenStore](settings/store.md#frozenstore)

### Lockfile Settings

[Full reference →](settings/store.md#lockfile-settings)

* [lockfile](settings/store.md#lockfile)
* [preferFrozenLockfile](settings/store.md#preferfrozenlockfile)
* [lockfileIncludeTarballUrl](settings/store.md#lockfileincludetarballurl)
* [gitBranchLockfile](settings/store.md#gitbranchlockfile)
* [mergeGitBranchLockfilesBranchPattern](settings/store.md#mergegitbranchlockfilesbranchpattern)
* [peersSuffixMaxLength](settings/store.md#peerssuffixmaxlength)

### Network Settings

[Full reference →](settings/network.md#network-settings)

* [httpsProxy](settings/network.md#httpsproxy)
* [httpProxy](settings/network.md#httpproxy)
* [noProxy](settings/network.md#noproxy)
* [localAddress](settings/network.md#localaddress)
* [maxsockets](settings/network.md#maxsockets)
* [strictSsl](settings/network.md#strictssl)

### Request Settings

[Full reference →](settings/network.md#request-settings)

* [gitShallowHosts](settings/network.md#gitshallowhosts)
* [networkConcurrency](settings/network.md#networkconcurrency)
* [fetchRetries](settings/network.md#fetchretries)
* [fetchRetryFactor](settings/network.md#fetchretryfactor)
* [fetchRetryMintimeout](settings/network.md#fetchretrymintimeout)
* [fetchRetryMaxtimeout](settings/network.md#fetchretrymaxtimeout)
* [fetchTimeout](settings/network.md#fetchtimeout)
* [fetchWarnTimeoutMs](settings/network.md#fetchwarntimeoutms)
* [fetchMinSpeedKiBps](settings/network.md#fetchminspeedkibps)

### Peer Dependency Settings

[Full reference →](settings/peer-dependencies.md)

* [autoInstallPeers](settings/peer-dependencies.md#autoinstallpeers)
  * [Version Conflicts](settings/peer-dependencies.md#version-conflicts)
  * [Conflict Resolution](settings/peer-dependencies.md#conflict-resolution)
* [dedupePeerDependents](settings/peer-dependencies.md#dedupepeerdependents)
* [dedupePeers](settings/peer-dependencies.md#dedupepeers)
* [strictPeerDependencies](settings/peer-dependencies.md#strictpeerdependencies)
* [resolvePeersFromWorkspaceRoot](settings/peer-dependencies.md#resolvepeersfromworkspaceroot)
* [peerDependencyRules](settings/peer-dependencies.md#peerdependencyrules)
  * [peerDependencyRules.ignoreMissing](settings/peer-dependencies.md#peerdependencyrulesignoremissing)
  * [peerDependencyRules.allowedVersions](settings/peer-dependencies.md#peerdependencyrulesallowedversions)
  * [peerDependencyRules.allowAny](settings/peer-dependencies.md#peerdependencyrulesallowany)

### CLI Settings

[Full reference →](settings/cli.md#cli-settings)

* [[no-]color](settings/cli.md#no-color)
* [loglevel](settings/cli.md#loglevel)
* [useBetaCli](settings/cli.md#usebetacli)
* [recursiveInstall](settings/cli.md#recursiveinstall)
* [engineStrict](settings/cli.md#enginestrict)
* [npmPath](settings/cli.md#npmpath)
* [pmOnFail](settings/cli.md#pmonfail)
* [ignoreWorkspaceRootCheck](settings/cli.md#ignoreworkspacerootcheck)

### Node.js Settings

[Full reference →](settings/cli.md#nodejs-settings)

* [nodeVersion](settings/cli.md#nodeversion)
* [runtimeOnFail](settings/cli.md#runtimeonfail)
* [nodeDownloadMirrors](settings/cli.md#nodedownloadmirrors)

### Build Settings

[Full reference →](settings/build.md)

* [ignoreScripts](settings/build.md#ignorescripts)
* [childConcurrency](settings/build.md#childconcurrency)
* [sideEffectsCache](settings/build.md#sideeffectscache)
* [sideEffectsCacheReadonly](settings/build.md#sideeffectscachereadonly)
* [unsafePerm](settings/build.md#unsafeperm)
* [nodeOptions](settings/build.md#nodeoptions)
* [verifyDepsBeforeRun](settings/build.md#verifydepsbeforerun)
* [strictDepBuilds](settings/build.md#strictdepbuilds)
* [allowBuilds](settings/build.md#allowbuilds)
* [dangerouslyAllowAllBuilds](settings/build.md#dangerouslyallowallbuilds)

### Versioning Settings

[Full reference →](settings/versioning.md)

* [versioning.fixed](settings/versioning.md#versioningfixed)
* [versioning.ignore](settings/versioning.md#versioningignore)
* [versioning.maxBump](settings/versioning.md#versioningmaxbump)
* [versioning.lanes](settings/versioning.md#versioninglanes)
* [versioning.epics](settings/versioning.md#versioningepics)
* [versioning.changelog.storage](settings/versioning.md#versioningchangelogstorage)

### Other Settings

[Full reference →](settings/other.md)

* [savePrefix](settings/other.md#saveprefix)
* [tag](settings/other.md#tag)
* [globalDir](settings/other.md#globaldir)
* [globalBinDir](settings/other.md#globalbindir)
* [npmrcAuthFile](settings/other.md#npmrcauthfile)
* [stateDir](settings/other.md#statedir)
* [cacheDir](settings/other.md#cachedir)
* [useStderr](settings/other.md#usestderr)
* [updateNotifier](settings/other.md#updatenotifier)
* [preferSymlinkedExecutables](settings/other.md#prefersymlinkedexecutables)
* [ignoreCompatibilityDb](settings/other.md#ignorecompatibilitydb)
* [resolutionMode](settings/other.md#resolutionmode)
* [registrySupportsTimeField](settings/other.md#registrysupportstimefield)
* [extendNodePath](settings/other.md#extendnodepath)
  * [Why this is needed](settings/other.md#why-this-is-needed)
  * [When to disable](settings/other.md#when-to-disable)
* [deployAllFiles](settings/other.md#deployallfiles)
* [dedupeDirectDeps](settings/other.md#dedupedirectdeps)
* [optimisticRepeatInstall](settings/other.md#optimisticrepeatinstall)
* [requiredScripts](settings/other.md#requiredscripts)
* [enablePrePostScripts](settings/other.md#enableprepostscripts)
* [scriptShell](settings/other.md#scriptshell)
* [shellEmulator](settings/other.md#shellemulator)
* [catalogMode](settings/other.md#catalogmode)
* [ci](settings/other.md#ci)
* [cleanupUnusedCatalogs](settings/other.md#cleanupunusedcatalogs)

### Workspace Settings

These settings are configured in `pnpm-workspace.yaml` as well, but are documented together with the workspace feature they belong to.

[Full reference →](workspaces.md#configuration)

* [linkWorkspacePackages](workspaces.md#linkworkspacepackages)
* [injectWorkspacePackages](workspaces.md#injectworkspacepackages)
* [dedupeInjectedDeps](workspaces.md#dedupeinjecteddeps)
* [syncInjectedDepsAfterScripts](workspaces.md#syncinjecteddepsafterscripts)
* [preferWorkspacePackages](workspaces.md#preferworkspacepackages)
* [sharedWorkspaceLockfile](workspaces.md#sharedworkspacelockfile)
* [saveWorkspaceProtocol](workspaces.md#saveworkspaceprotocol)
* [includeWorkspaceRoot](workspaces.md#includeworkspaceroot)
* [ignoreWorkspaceCycles](workspaces.md#ignoreworkspacecycles)
* [disallowWorkspaceCycles](workspaces.md#disallowworkspacecycles)
* [failIfNoMatch](workspaces.md#failifnomatch)

### Settings documented elsewhere

* [patchedDependencies](cli/patch.md#patcheddependencies)
* [pnpmfile](pnpmfile.md#pnpmfile), [globalPnpmfile](pnpmfile.md#globalpnpmfile) and [ignorePnpmfile](pnpmfile.md#ignorepnpmfile)
* Authorization settings, which are read from [`.npmrc`](npmrc.md)


---

# Mitigating supply chain attacks

*Sección: Pnpm*

Sometimes npm packages are compromised and published with malware. Luckily, there are companies like [Socket], [Snyk], [Xygeni] and [Aikido] that detect these compromised packages early. The npm registry usually removes the affected versions within hours. However, there is always a window of time between when the malware is published and when it is detected, during which you could be exposed. Fortunately, there are some things you can do with pnpm to minimize the risks.

### Block risky postinstall scripts
 
Historically, most compromised packages have used `postinstall` scripts to run code immediately upon installation. To mitigate this, pnpm v10 disables the automatic execution of `postinstall` scripts in dependencies. Although there is a setting to re-enable them globally using [dangerouslyAllowAllBuilds], we recommend explicitly listing only trusted dependencies using [allowBuilds]. This way, if a dependency did not require a build in the past, it won't suddenly run a malicious script if a compromised version is published. Still, we recommend being cautious when updating a trusted package that has a `postinstall` script, as [it might get compromised].
 
### Prevent exotic transitive dependencies
 
You can prevent transitive dependencies from using exotic sources (like git repositories or direct tarball URLs) by setting [blockExoticSubdeps] to `true`. This ensures that all transitive dependencies are resolved from trusted sources, reducing the risk of supply chain attacks.
 
### Delay dependency updates
 
Another way to reduce the risk of installing compromised packages is to delay updates to your dependencies. Since malware is usually detected quickly, delaying updates by 24 hours will most likely prevent you from installing a bad version. The [minimumReleaseAge] setting defines the minimum number of minutes that must pass after a version is published before pnpm will install it. In pnpm v11, this defaults to `1440` (1 day), meaning newly published packages will not be resolved until they are at least 1 day old. To opt out, set `minimumReleaseAge: 0` in `pnpm-workspace.yaml`. You can also set it to `10080` to wait one week before installing a new version.
 
### Enforce trust with trustPolicy
 
To further protect your supply chain, pnpm also supports a [trustPolicy] setting. When set to `no-downgrade`, this setting will prevent installation of a package if its trust level has decreased compared to previous releases (for example, if it was previously published by a trusted publisher but now only has provenance or no trust evidence). This helps you avoid installing potentially compromised or less trustworthy versions.
 
If you need to allow specific packages or versions to bypass the trust policy check, you can use the [trustPolicyExclude] setting. This is useful for known packages that may not meet the trust requirements but are still safe to use.

Additionally, the [trustPolicyIgnoreAfter] setting allows you to ignore trust checks for packages published more than a specified time ago. This is helpful for older versions of packages that lack a process for publishing with signatures or provenance.

### Use a lockfile

It goes without saying that you should always lock your dependencies with a lockfile. Commit your lockfile to your repository to avoid unexpected updates.

[Socket]: https://socket.dev/
[Snyk]: https://snyk.io
[Xygeni]: https://xygeni.io/
[Aikido]: https://www.aikido.dev/
[dangerouslyAllowAllBuilds]: settings/build.md#dangerouslyallowallbuilds
[it might get compromised]: https://socket.dev/blog/nx-packages-compromised
[minimumReleaseAge]: settings/dependency-resolution.md#minimumreleaseage
[trustPolicy]: settings/dependency-resolution.md#trustpolicy
[trustPolicyExclude]: settings/dependency-resolution.md#trustpolicyexclude
[allowBuilds]: settings/build.md#allowbuilds
[blockExoticSubdeps]: settings/dependency-resolution.md#blockexoticsubdeps
[trustPolicyIgnoreAfter]: settings/dependency-resolution.md#trustpolicyignoreafter


---

# Symlinked nodemodules structure

*Sección: Pnpm*

:::info

This article only describes how pnpm's `node_modules` are structured when
there are no packages with peer dependencies. For the more complex scenario of
dependencies with peers, see [how peers are resolved](how-peers-are-resolved.md).

:::

pnpm's `node_modules` layout uses symbolic links to create a nested structure of
dependencies.

Every file of every package inside `node_modules` is a hard link to the
content-addressable store. Let's say you install `foo@1.0.0` that depends on
`bar@1.0.0`. pnpm will hard link both packages to `node_modules` like this:

```text
node_modules
└── .pnpm
    ├── bar@1.0.0
    │   └── node_modules
    │       └── bar
    │           ├── index.js     -> <store>/001
    │           └── package.json -> <store>/002
    └── foo@1.0.0
        └── node_modules
            └── foo
                ├── index.js     -> <store>/003
                └── package.json -> <store>/004
```

These are the only "real" files in `node_modules`. Once all the packages are
hard linked to `node_modules`, symbolic links are created to build the nested
dependency graph structure.

As you might have noticed, both packages are hard linked into a subfolder inside
a `node_modules` folder (`foo@1.0.0/node_modules/foo`). This is needed to:

1. **allow packages to import themselves.** `foo` should be able to
`require('foo/package.json')` or `import * as package from "foo/package.json"`.
2. **avoid circular symlinks.** Dependencies of packages are placed in the same
folder in which the dependent packages are. For Node.js it doesn't make a
difference whether dependencies are inside the package's `node_modules` or in
any other `node_modules` in the parent directories.

The next stage of installation is symlinking dependencies. `bar` is going to be
symlinked to the `foo@1.0.0/node_modules` folder:

```text
node_modules
└── .pnpm
    ├── bar@1.0.0
    │   └── node_modules
    │       └── bar -> <store>
    └── foo@1.0.0
        └── node_modules
            ├── foo -> <store>
            └── bar -> ../../bar@1.0.0/node_modules/bar
```

Next, direct dependencies are handled. `foo` is going to be symlinked into the
root `node_modules` folder because `foo` is a dependency of the project:

```text
node_modules
├── foo -> ./.pnpm/foo@1.0.0/node_modules/foo
└── .pnpm
    ├── bar@1.0.0
    │   └── node_modules
    │       └── bar -> <store>
    └── foo@1.0.0
        └── node_modules
            ├── foo -> <store>
            └── bar -> ../../bar@1.0.0/node_modules/bar
```

This is a very simple example. However, the layout will maintain this structure
regardless of the number of dependencies and the depth of the dependency graph.

Let's add `qar@2.0.0` as a dependency of `bar` and `foo`. This is how the new
structure will look:

```text
node_modules
├── foo -> ./.pnpm/foo@1.0.0/node_modules/foo
└── .pnpm
    ├── bar@1.0.0
    │   └── node_modules
    │       ├── bar -> <store>
    │       └── qar -> ../../qar@2.0.0/node_modules/qar
    ├── foo@1.0.0
    │   └── node_modules
    │       ├── foo -> <store>
    │       ├── bar -> ../../bar@1.0.0/node_modules/bar
    │       └── qar -> ../../qar@2.0.0/node_modules/qar
    └── qar@2.0.0
        └── node_modules
            └── qar -> <store>
```

As you may see, even though the graph is deeper now (`foo > bar > qar`), the
directory depth in the file system is still the same.

This layout might look weird at first glance, but it is completely compatible
with Node's module resolution algorithm! When resolving modules, Node ignores
symlinks, so when `bar` is required from `foo@1.0.0/node_modules/foo/index.js`,
Node does not use `bar` at `foo@1.0.0/node_modules/bar`, but instead, `bar` is
resolved to its real location (`bar@1.0.0/node_modules/bar`). As a consequence,
`bar` can also resolve its dependencies which are in `bar@1.0.0/node_modules`.

A great bonus of this layout is that only packages that are really in the
dependencies are accessible. With a flattened `node_modules` structure, all
hoisted packages are accessible. To read more about why this is an advantage,
see "[pnpm's strictness helps to avoid silly bugs][bugs]"

Unfortunately, many packages in the ecosystem are broken — they use dependencies that are not listed in their `package.json`. To minimize the number of issues new users encounter, pnpm hoists all dependencies by default into `node_modules/.pnpm/node_modules`. To disable this hoisting, set [hoist] to `false`.

[hoist]: settings/node-modules.md#hoist

[bugs]: https://www.kochan.io/nodejs/pnpms-strictness-helps-to-avoid-silly-bugs.html


---

# Working with TypeScript

*Sección: Pnpm*

pnpm should work well with TypeScript out of the box most of the time.

## Do not preserve symlinks

You should not use TypeScript with [`preserveSymlinks`](https://www.typescriptlang.org/tsconfig/#preserveSymlinks) set to `true`. TypeScript will not be able to resolve the type dependencies correctly in the linked `node_modules`. If you do need to preserve symlinks for some reason, then you should set pnpm's `nodeLinker` setting to `hoisted`.

## Workspace usage

You might sometimes have issues if you have different versions of a `@types/` dependency in a workspace. These issues happen when a package requires these types without having the type dependency in dependencies. For instance, if you have `antd` in your dependencies, which relies on `@types/react`, you might get a compilation error if there are multiple versions of `@types/react` in your workspace. This is actually an issue on `antd`'s end because it should've added `@types/react` to `peerDependencies`. Luckily, you can fix this by extending `antd` with the missing peer dependency. You can do this either by adding this to your `pnpm-workspace.yaml`:

```yaml
packageExtensions:
  antd:
    peerDependencies:
      '@types/react': '*'
```

Alternatively, you can install a config dependency that we created to deal with these issues [`@pnpm/plugin-types-fixer`]. Run:

```sh
pnpm add @pnpm/plugin-types-fixer --config
```

[`@pnpm/plugin-types-fixer`]: https://github.com/pnpm/plugin-types-fixer


---

# Uninstalling pnpm

*Sección: Pnpm*

## Removing the globally installed packages

Before removing the pnpm CLI, it might make sense to remove all global packages that were installed by pnpm.

To list all the global packages, run `pnpm ls -g`. There are two ways to remove the global packages:

1. Run `pnpm rm -g <pkg>...` with each global package listed.
2. Run `pnpm root -g` to find the location of the global directory and remove it manually.

## Removing the pnpm CLI

If you used the standalone script to install pnpm, then you should be able to uninstall the pnpm CLI by removing the pnpm home directory:

```
rm -rf "$PNPM_HOME"
```

You might also want to clean the `PNPM_HOME` env variable in your shell configuration file (`$HOME/.bashrc`, `$HOME/.zshrc` or `$HOME/.config/fish/config.fish`).

If you used npm to install pnpm, then you should use npm to uninstall pnpm:

```
npm rm -g pnpm
```

## Removing the global content-addressable store

```
rm -rf "$(pnpm store path)"
```

If you used pnpm in non-primary disks, then you must run the above command in every disk, where pnpm was used.
pnpm creates one store per disk.


---

# Using Changesets with pnpm

*Sección: Pnpm*

:::tip

Since v11.13.0, pnpm can manage workspace releases natively, without the Changesets CLI. It reads and writes the same `.changeset/*.md` files. See [Release management](versioning.md).

Since v11.16.0, [`pnpm update --changeset`](cli/update.md#--changeset) can also write a changeset for the dependency bumps an update makes.

:::

:::note

At the time of writing this documentation, the latest pnpm version was
v10.4.1. The latest [Changesets](https://github.com/changesets/changesets) version was v2.28.0.

:::

## Setup

To setup changesets on a pnpm workspace, install changesets as a dev dependency
in the root of the workspace:

```sh
pnpm add -Dw @changesets/cli
```

Then run changesets' init command to generate a changesets config:

```sh
pnpm changeset init
```

## Adding new changesets

To generate a new changeset, run `pnpm changeset` in the root of the repository.
The generated markdown files in the `.changeset` directory should be committed
to the repository.

## Releasing changes

1. Run `pnpm changeset version`. This will bump the versions of the packages
   previously specified with `pnpm changeset` (and any dependents of those) and
   update the changelog files.
2. Run `pnpm install`. This will update the lockfile and rebuild packages.
3. Commit the changes.
4. Run `pnpm publish -r`. This command will publish all packages that have
   bumped versions not yet present in the registry.

## Integration with GitHub Actions

To automate the process, you can use `changeset version` with GitHub actions. The action will detect when changeset files arrive in the `main` branch, and then open a new PR listing all the packages with bumped versions. The PR will automatically update itself every time a new changeset file arrives in `main`. Once merged the packages will be updated, and if the `publish` input has been specified on the action they will  be published using the given command.

### Add a publish script

Add a new script called `ci:publish` which executes `pnpm publish -r`. This will publish to the registry once the PR created by `changeset version` has been merged. If the package is public and scoped, adding `--access=public` may be necessary to prevent npm rejecting the publish.

**package.json**
```json
{
   "scripts": {
      "ci:publish": "pnpm publish -r"
   },
   ...
}
```

### Add the workflow

Add a new workflow at `.github/workflows/changesets.yml`. This workflow will create a new branch and PR, so Actions should be given **read and write** permissions in the repo settings (`github.com/<repo-owner>/<repo-name>/settings/actions`). If including the `publish` input on the `changesets/action` step, the repo should also include an auth token for npm as a repository secret named `NPM_TOKEN`.

**.github/workflows/changesets.yml**
```yaml
name: Changesets

on:
  push:
    branches:
      - main

env:
  CI: true

jobs:
  version:
    timeout-minutes: 15
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code repository
        uses: actions/checkout@v4

      - name: Setup pnpm
        uses: pnpm/action-setup@v4

      - name: Setup node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'
      
      - name: Install dependencies
        run: pnpm install
      
      - name: Create and publish versions
        uses: changesets/action@v1
        with:
          commit: "chore: update versions"
          title: "chore: update versions"
          publish: pnpm ci:publish
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
```

More info and documentation regarding the changesets action can be found
[here](https://github.com/changesets/action).


---

# Release management

*Sección: Pnpm*

Added in: v11.13.0

pnpm can version and release a workspace on its own, without a separate release tool. The workflow has two halves:

1. As you work, [`pnpm change`](cli/change.md) records **change intents** — small markdown files in `.changeset/` saying which packages a change affects, how each should be bumped, and a summary that becomes the changelog entry. These are committed alongside the change.
2. At release time, the bare [`pnpm version -r`](cli/version.md#recursive-releases) consumes the pending intents: it bumps versions across the workspace, propagates to dependents, writes changelogs, and records what it consumed in a committed ledger.

Intent files use the [changesets](https://github.com/changesets/changesets) format, so an existing `.changeset/` directory keeps working. See [Using Changesets with pnpm](using-changesets.md) if you would rather keep using the Changesets CLI.

## Recording a change

```sh
pnpm change
```

This prompts for the affected packages, their bump types, and a summary, then writes a file like `.changeset/calm-cats-resolve.md`:

```markdown
---
"@example/core": minor
---

Added a `--watch` flag to the build command.
```

To see what the pending intents would produce:

```sh
pnpm change status
```

## Releasing

```sh
pnpm version -r
```

This applies the release plan: every package named by an intent is bumped, and so is every package that depends on it through a `workspace:` range. Preview it first with `--dry-run`, and narrow it with `--filter`.

Because a recursive run can bump many packages to different versions, no git commit or tag is created — there is no single version to tag. Commit the result yourself, then publish with `pnpm publish -r`.

### First releases

Since v11.16.0, the first release of a package publishes the version written in its manifest verbatim, instead of bumping off it. `pnpm version -r` and `pnpm change status` check the registry for each release's current version; when that version is not yet published, the package debuts at it and its pending change intents apply only from the next release. A newly added package seeded at `1100.0.0` with a `minor` intent is therefore published as `1100.0.0` rather than skipping straight to `1100.1.0`.

## Configuration

Release behavior is configured under the `versioning` key of `pnpm-workspace.yaml`:

```yaml title="pnpm-workspace.yaml"
versioning:
  fixed:
    - ['@example/cli', '@example/napi']
  ignore:
    - '@example/internal'
  maxBump: minor
  lanes:
    '@example/cli': alpha
  changelog:
    storage: repository
```

Every key is described in [Versioning Settings](settings/versioning.md).

Where two workspace projects publish the same name, a project can be referenced by its workspace-relative directory instead of its name, with a `./` prefix (e.g. `"./packages/cli"`). This works in intent files and in `versioning.lanes`, `versioning.fixed`, and `versioning.ignore`.

### Fixed groups

Packages listed together in `versioning.fixed` always release at one shared version — the highest current version in the group, bumped by the largest bump any member needs. A fixed group must move between lanes together, and must sit entirely inside or entirely outside an epic.

### Lanes

A lane is a parallel release track. While a package is on one, it releases `X.Y.Z-<lane>.N` prereleases from the same runs that release stable versions of everything on the main lane. This lets a rewrite or a major-version line bake in public while the rest of the workspace keeps shipping.

```sh
pnpm lane alpha --filter @example/cli   # move onto the alpha lane
pnpm lane main --filter @example/cli    # graduate back to stable
pnpm lane                               # show membership
```

See [`pnpm lane`](cli/lane.md) for how the prerelease versions are computed.

### Epics

An epic ties a group of member packages to a lead package, constraining every member's major version to a band derived from the lead's major: while the lead is on major `M`, members live in `M*100` … `M*100+99`.

```yaml title="pnpm-workspace.yaml"
versioning:
  epics:
    - lead: '@example/app'
      packages:
        - './packages/**'
        - '!./packages/private-*'
```

With the lead on `11.x`, members occupy majors `1100`–`1199`. Members move independently inside the band — patch, minor, and even a `major` intent that stays in-band. A bump that would carry a member past the band ceiling is rejected until the lead advances its own major. When a release plan takes the lead to a new stable major, every member re-bases to the band floor in the same plan.

Membership is matched with pnpm's package selectors: name globs, `./`-prefixed directory globs, and `!`-prefixed negations. Selectors are evaluated in order and the last one to match decides, so a later include can re-admit a package an earlier negation excluded. The lead is never a member of its own band.

## Changelogs

By default (`versioning.changelog.storage: registry`) no `CHANGELOG.md` is committed. Each release's section is composed at publish time and packed into the published tarball on top of the previously published version's changelog. Consumed change intents are garbage-collected by a later `pnpm version -r` only once the registry confirms the version was published with its section.

Set `versioning.changelog.storage: repository` to keep committed `CHANGELOG.md` files in every package instead.

## The ledger

`pnpm version -r` records every consumed intent in `.changeset/ledger.yaml`, a committed, append-only file:

```yaml
"@example/core@1.3.0":
  dir: packages/core
  intents:
    - calm-cats-resolve
```

Consumption is tracked per project: an intent file is deleted only once every project it names has released. This is what makes cherry-picks and merge-backs between release branches safe — a release branch that has already consumed an intent will not consume it again when the commit is merged forward, and a package on a lane can half-consume an intent whose prose still has a stable release to compose.


---

# Workspace

*Sección: Pnpm*

pnpm has built-in support for monorepositories (AKA multi-package repositories,
multi-project repositories, or monolithic repositories). You can create a
workspace to unite multiple projects inside a single repository.

A workspace must have a [`pnpm-workspace.yaml`] file in its
root.

[`pnpm-workspace.yaml`]: settings.md

:::tip

If you are looking into monorepo management, you might also want to look into [Bit].
Bit uses pnpm under the hood but automates a lot of the things that are currently done manually in a traditional workspace managed by pnpm/npm/Yarn. There's an article about `bit install` that talks about it: [Painless Monorepo Dependency Management with Bit].

:::

[Bit]: https://bit.dev/?utm_source=pnpm&utm_medium=workspace_page
[Painless Monorepo Dependency Management with Bit]: https://bit.dev/blog/painless-monorepo-dependency-management-with-bit-l4f9fzyw?utm_source=pnpm&utm_medium=workspace_page

## Workspace protocol (workspace:)

If [linkWorkspacePackages] is set to `true`, pnpm will link packages from the workspace if the available packages
match the declared ranges. For instance, `foo@1.0.0` is linked into `bar` if
`bar` has `"foo": "^1.0.0"` in its dependencies and `foo@1.0.0` is in the workspace. However, if `bar` has
`"foo": "2.0.0"` in dependencies and `foo@2.0.0` is not in the workspace,
`foo@2.0.0` will be installed from the registry. This behavior introduces some
uncertainty.

Luckily, pnpm supports the `workspace:` protocol. When
this protocol is used, pnpm will refuse to resolve to anything other than a
local workspace package. So, if you set `"foo": "workspace:2.0.0"`, this time
installation will fail because `"foo@2.0.0"` isn't present in the workspace.

This protocol is especially useful when the [linkWorkspacePackages] option is
set to `false`. In that case, pnpm will only link packages from the workspace if
the `workspace:` protocol is used.

[linkWorkspacePackages]: #linkworkspacepackages

### Referencing workspace packages through aliases

Let's say you have a package in the workspace named `foo`. Usually, you would
reference it as `"foo": "workspace:*"`.

If you want to use a different alias, the following syntax will work too:
`"bar": "workspace:foo@*"`.

Before publish, aliases are converted to regular aliased dependencies. The above
example will become: `"bar": "npm:foo@1.0.0"`.

### Referencing workspace packages through their relative path

In a workspace with 2 packages:

```
+ packages
	+ foo
	+ bar
```

`bar` may have `foo` in its dependencies declared as
`"foo": "workspace:../foo"`. Before publishing, these specs are converted to
regular version specs supported by all package managers.

### Publishing workspace packages

When a workspace package is packed into an archive (whether it's through
`pnpm pack` or one of the publish commands like `pnpm publish`), we dynamically
replace any `workspace:` dependency by:

* The corresponding version in the target workspace (if you use `workspace:`, `workspace:*`, `workspace:~`, or `workspace:^`)
* The associated semver range (for any other range type)

A bare `workspace:` without a version range is treated as `workspace:*`.

So for example, if we have `foo`, `bar`, `qar`, `zoo` in the workspace and they all are at version `1.5.0`, the following:

```json
{
	"dependencies": {
		"foo": "workspace:*",
		"bar": "workspace:~",
		"qar": "workspace:^",
		"zoo": "workspace:^1.5.0"
	}
}
```

Will be transformed into:

```json
{
	"dependencies": {
		"foo": "1.5.0",
		"bar": "~1.5.0",
		"qar": "^1.5.0",
		"zoo": "^1.5.0"
	}
}
```

This feature allows you to depend on your local workspace packages while still
being able to publish the resulting packages to the remote registry without
needing intermediary publish steps - your consumers will be able to use your
published workspaces as any other package, still benefitting from the guarantees
semver offers.

## Release workflow

Versioning packages inside a workspace is a complex task and pnpm currently does
not provide a built-in solution for it. However, there are 2 well tested tools
that handle versioning and support pnpm:
- [changesets](https://github.com/changesets/changesets)
- [Rush](https://rushjs.io)

For how to set up a repository using Rush, read [this page][rush-setup].

For using Changesets with pnpm, read [this guide][changesets-guide].

[rush-setup]: https://rushjs.io/pages/maintainer/setup_new_repo
[changesets-guide]: using-changesets.md

## Troubleshooting

pnpm cannot guarantee that scripts will be run in topological order if there are cycles between workspace dependencies. If pnpm detects cyclic dependencies during installation, it will produce a warning. If pnpm is able to find out which dependencies are causing the cycles, it will display them too.

If you see the message `There are cyclic workspace dependencies`, please inspect workspace dependencies declared in `dependencies`, `optionalDependencies` and `devDependencies`.

## Usage examples

Here are a few of the most popular open source projects that use the workspace feature of pnpm:

| Project | Stars | Migration date | Migration commit |
| --      | --    | --             | --               |
| [Next.js](https://github.com/vercel/next.js) | ![](https://img.shields.io/github/stars/vercel/next.js) | 2022-05-29 | [`f7b81316aea4fc9962e5e54981a6d559004231aa`](https://github.com/vercel/next.js/commit/f7b81316aea4fc9962e5e54981a6d559004231aa) |
| [n8n](https://github.com/n8n-io/n8n) | ![](https://img.shields.io/github/stars/n8n-io/n8n) | 2022-11-09 | [`736777385c54d5b20174c9c1fda38bb31fbf14b4`](https://github.com/n8n-io/n8n/commit/736777385c54d5b20174c9c1fda38bb31fbf14b4) |
| [Material UI](https://github.com/mui/material-ui) | ![](https://img.shields.io/github/stars/mui/material-ui) | 2024-01-03 | [`a1263e3e5ef8d840252b4857f85b33caa99f471d`](https://github.com/mui/material-ui/commit/a1263e3e5ef8d840252b4857f85b33caa99f471d) |
| [Vite](https://github.com/vitejs/vite) | ![](https://img.shields.io/github/stars/vitejs/vite) | 2021-09-26 | [`3e1cce01d01493d33e50966d0d0fd39a86d229f9`](https://github.com/vitejs/vite/commit/3e1cce01d01493d33e50966d0d0fd39a86d229f9) |
| [Nuxt](https://github.com/nuxt/nuxt) | ![](https://img.shields.io/github/stars/nuxt/nuxt) | 2022-10-17 | [`74a90c566c936164018c086030c7de65b26a5cb6`](https://github.com/nuxt/nuxt/commit/74a90c566c936164018c086030c7de65b26a5cb6) |
| [Vue](https://github.com/vuejs/core) | ![](https://img.shields.io/github/stars/vuejs/core) | 2021-10-09 | [`61c5fbd3e35152f5f32e95bf04d3ee083414cecb`](https://github.com/vuejs/core/commit/61c5fbd3e35152f5f32e95bf04d3ee083414cecb) |
| [Astro](https://github.com/withastro/astro) | ![](https://img.shields.io/github/stars/withastro/astro) | 2022-03-08 | [`240d88aefe66c7d73b9c713c5da42ae789c011ce`](https://github.com/withastro/astro/commit/240d88aefe66c7d73b9c713c5da42ae789c011ce) |
| [Prisma](https://github.com/prisma/prisma) | ![](https://img.shields.io/github/stars/prisma/prisma) | 2021-09-21 | [`c4c83e788aa16d61bae7a6d00adc8a58b3789a06`](https://github.com/prisma/prisma/commit/c4c83e788aa16d61bae7a6d00adc8a58b3789a06) |
| [Novu](https://github.com/novuhq/novu) | ![](https://img.shields.io/github/stars/novuhq/novu) | 2021-12-23 | [`f2ea61f7d7ac7e12db4c9e70767082841ed98b2b`](https://github.com/novuhq/novu/commit/f2ea61f7d7ac7e12db4c9e70767082841ed98b2b) |
| [Slidev](https://github.com/slidevjs/slidev) | ![](https://img.shields.io/github/stars/slidevjs/slidev) | 2021-04-12 | [`d6783323eb1ab1fc612577eb63579c8f7bc99c3a`](https://github.com/slidevjs/slidev/commit/d6783323eb1ab1fc612577eb63579c8f7bc99c3a) |
| [Turborepo](https://github.com/vercel/turborepo) | ![](https://img.shields.io/github/stars/vercel/turborepo) | 2022-03-02 | [`fd171519ec02a69c9afafc1bc5d9d1b481fba721`](https://github.com/vercel/turborepo/commit/fd171519ec02a69c9afafc1bc5d9d1b481fba721) |
| [Quasar Framework](https://github.com/quasarframework/quasar) | ![](https://img.shields.io/github/stars/quasarframework/quasar) | 2024-03-13 | [`7f8e550bb7b6ab639ce423d02008e7f5e61cbf55`](https://github.com/quasarframework/quasar/commit/7f8e550bb7b6ab639ce423d02008e7f5e61cbf55) |
| [Element Plus](https://github.com/element-plus/element-plus) | ![](https://img.shields.io/github/stars/element-plus/element-plus) | 2021-09-23 | [`f9e192535ff74d1443f1d9e0c5394fad10428629`](https://github.com/element-plus/element-plus/commit/f9e192535ff74d1443f1d9e0c5394fad10428629) |
| [NextAuth.js](https://github.com/nextauthjs/next-auth) | ![](https://img.shields.io/github/stars/nextauthjs/next-auth) | 2022-05-03 | [`4f29d39521451e859dbdb83179756b372e3dd7aa`](https://github.com/nextauthjs/next-auth/commit/4f29d39521451e859dbdb83179756b372e3dd7aa) |
| [Ember.js](https://github.com/emberjs/ember.js) | ![](https://img.shields.io/github/stars/emberjs/ember.js) | 2023-10-18 | [`b6b05da662497183434136fb0148e1dec544db04`](https://github.com/emberjs/ember.js/commit/b6b05da662497183434136fb0148e1dec544db04) |
| [Qwik](https://github.com/BuilderIO/qwik) | ![](https://img.shields.io/github/stars/BuilderIO/qwik) | 2022-11-14 | [`021b12f58cca657e0a008119bc711405513e1ee9`](https://github.com/BuilderIO/qwik/commit/021b12f58cca657e0a008119bc711405513e1ee9) |
| [VueUse](https://github.com/vueuse/vueuse) | ![](https://img.shields.io/github/stars/vueuse/vueuse) | 2021-09-25 | [`826351ba1d9c514e34426c85f3d69fb9875c7dd9`](https://github.com/vueuse/vueuse/commit/826351ba1d9c514e34426c85f3d69fb9875c7dd9) |
| [SvelteKit](https://github.com/sveltejs/kit) | ![](https://img.shields.io/github/stars/sveltejs/kit) | 2021-09-26 | [`b164420ab26fa04fd0fbe0ac05431f36a89ef193`](https://github.com/sveltejs/kit/commit/b164420ab26fa04fd0fbe0ac05431f36a89ef193) |
| [Verdaccio](https://github.com/verdaccio/verdaccio) | ![](https://img.shields.io/github/stars/verdaccio/verdaccio) | 2021-09-21 | [`9dbf73e955fcb70b0a623c5ab89649b95146c744`](https://github.com/verdaccio/verdaccio/commit/9dbf73e955fcb70b0a623c5ab89649b95146c744) |
| [Vercel](https://github.com/vercel/vercel) | ![](https://img.shields.io/github/stars/vercel/vercel) | 2023-01-12 | [`9c768b98b71cfc72e8638bf5172be88c39e8fa69`](https://github.com/vercel/vercel/commit/9c768b98b71cfc72e8638bf5172be88c39e8fa69) |
| [Vitest](https://github.com/vitest-dev/vitest) | ![](https://img.shields.io/github/stars/vitest-dev/vitest) | 2021-12-13 | [`d6ff0ccb819716713f5eab5c046861f4d8e4f988`](https://github.com/vitest-dev/vitest/commit/d6ff0ccb819716713f5eab5c046861f4d8e4f988) |
| [Cycle.js](https://github.com/cyclejs/cyclejs) | ![](https://img.shields.io/github/stars/cyclejs/cyclejs) | 2021-09-21 | [`f2187ab6688368edb904b649bd371a658f6a8637`](https://github.com/cyclejs/cyclejs/commit/f2187ab6688368edb904b649bd371a658f6a8637) |
| [Milkdown](https://github.com/Saul-Mirone/milkdown) | ![](https://img.shields.io/github/stars/Saul-Mirone/milkdown) | 2021-09-26 | [`4b2e1dd6125bc2198fd1b851c4f00eda70e9b913`](https://github.com/Saul-Mirone/milkdown/commit/4b2e1dd6125bc2198fd1b851c4f00eda70e9b913) |
| [Nhost](https://github.com/nhost/nhost) | ![](https://img.shields.io/github/stars/nhost/nhost) | 2022-02-07 | [`10a1799a1fef2f558f737de3bb6cadda2b50e58f`](https://github.com/nhost/nhost/commit/10a1799a1fef2f558f737de3bb6cadda2b50e58f) |
| [Logto](https://github.com/logto-io/logto) | ![](https://img.shields.io/github/stars/logto-io/logto) | 2021-07-29 | [`0b002e07850c8e6d09b35d22fab56d3e99d77043`](https://github.com/logto-io/logto/commit/0b002e07850c8e6d09b35d22fab56d3e99d77043) |
| [Rollup plugins](https://github.com/rollup/plugins) | ![](https://img.shields.io/github/stars/rollup/plugins) | 2021-09-21 | [`53fb18c0c2852598200c547a0b1d745d15b5b487`](https://github.com/rollup/plugins/commit/53fb18c0c2852598200c547a0b1d745d15b5b487) |
| [icestark](https://github.com/ice-lab/icestark) | ![](https://img.shields.io/github/stars/ice-lab/icestark) | 2021-12-16 | [`4862326a8de53d02f617e7b1986774fd7540fccd`](https://github.com/ice-lab/icestark/commit/4862326a8de53d02f617e7b1986774fd7540fccd) |
| [ByteMD](https://github.com/bytedance/bytemd) | ![](https://img.shields.io/github/stars/bytedance/bytemd) | 2021-02-18 | [`36ef25f1ea1cd0b08752df5f8c832302017bb7fb`](https://github.com/bytedance/bytemd/commit/36ef25f1ea1cd0b08752df5f8c832302017bb7fb) |
| [Stimulus Components](https://github.com/stimulus-components/stimulus-components) | ![](https://img.shields.io/github/stars/stimulus-components/stimulus-components) | 2024-10-26 | [`8e100d5b2c02ad5bf0b965822880a60f543f5ec3`](https://github.com/stimulus-components/stimulus-components/commit/8e100d5b2c02ad5bf0b965822880a60f543f5ec3) |
| [Serenity/JS](https://github.com/serenity-js/serenity-js) | ![](https://img.shields.io/github/stars/serenity-js/serenity-js) | 2025-01-01 | [`43dbe6f440d8dd81811da303e542381a17d06b4d`](https://github.com/serenity-js/serenity-js/commit/43dbe6f440d8dd81811da303e542381a17d06b4d) |
| [kysely](https://github.com/kysely-org/kysely) | ![](https://img.shields.io/github/stars/kysely-org/kysely) | 2025-07-29 | [`5ac19105ddb17af310c67e004c11fa3345454b66`](https://github.com/kysely-org/kysely/commit/5ac19105ddb17af310c67e004c11fa3345454b66) |

## Configuration

### linkWorkspacePackages

* Default: **false**
* Type: **true**, **false**, **deep**

If this is enabled, locally available packages are linked to `node_modules`
instead of being downloaded from the registry. This is very convenient in a
monorepo. If you need local packages to also be linked to subdependencies, you
can use the `deep` setting.

Else, packages are downloaded and installed from the registry. However,
workspace packages can still be linked by using the `workspace:` range protocol.

Packages are only linked if their versions satisfy the dependency ranges.

### injectWorkspacePackages

* Default: **false**
* Type: **Boolean**

Enables hard-linking of all local workspace dependencies instead of symlinking them. Alternatively, this can be achieved using [`dependenciesMeta[].injected`](package-json.md#dependenciesmetainjected), which allows to selectively enable hard-linking for specific dependencies.

:::note

Even if this setting is enabled, pnpm will prefer to deduplicate injected dependencies using symlinks—unless multiple dependency graphs are required due to mismatched peer dependencies. This behaviour is controlled by the `dedupeInjectedDeps` setting.

:::

### dedupeInjectedDeps

* Default: **true**
* Type: **Boolean**

When this setting is enabled, [dependencies that are injected](package-json.md#dependenciesmetainjected) will be symlinked from the workspace whenever possible. If the dependent project and the injected dependency reference the same peer dependencies, then it is not necessary to physically copy the injected dependency into the dependent's `node_modules`; a symlink is sufficient.

### syncInjectedDepsAfterScripts

Added in: v10.5.0

* Default: **undefined**
* Type: **String[]**

Injected workspace dependencies are collections of hardlinks, which don't add or remove the files when their sources change. This causes problems in packages that need to be built (such as in TypeScript projects).

This setting is a list of script names. When any of these scripts are executed in a workspace package, the injected dependencies inside `node_modules` will also be synchronized.

### preferWorkspacePackages

* Default: **false**
* Type: **Boolean**

If this is enabled, local packages from the workspace are preferred over
packages from the registry, even if there is a newer version of the package in
the registry.

This setting is only useful if the workspace doesn't use
`saveWorkspaceProtocol`.

### sharedWorkspaceLockfile

* Default: **true**
* Type: **Boolean**

If this is enabled, pnpm creates a single `pnpm-lock.yaml` file in the root of
the workspace. This also means that all dependencies of workspace packages will
be in a single `node_modules` (and get symlinked to their package `node_modules`
folder for Node's module resolution).

Advantages of this option:
* every dependency is a singleton
* faster installations in a monorepo
* fewer changes in code reviews as they are all in one file

:::note

Even though all the dependencies will be hard linked into the root
`node_modules`, packages will have access only to those dependencies
that are declared in their `package.json`, so pnpm's strictness is preserved.
This is a result of the aforementioned symbolic linking.

:::

### saveWorkspaceProtocol

* Default: **rolling**
* Type: **true**, **false**, **rolling**

This setting controls how dependencies that are linked from the workspace are added to `package.json`.

If `foo@1.0.0` is in the workspace and you run `pnpm add foo` in another project of the workspace, below is how `foo` will be added to the dependencies field. The `savePrefix` setting also influences how the spec is created.

| saveWorkspaceProtocol | savePrefix | spec |
|--|--|--|
| false | `''` | `1.0.0` |
| false | `'~'` | `~1.0.0` |
| false | `'^'` | `^1.0.0` |
| true | `''` | `workspace:1.0.0` |
| true | `'~'` | `workspace:~1.0.0` |
| true | `'^'` | `workspace:^1.0.0` |
| rolling | `''` | `workspace:*` |
| rolling | `'~'` | `workspace:~` |
| rolling | `'^'` | `workspace:^` |

### includeWorkspaceRoot

* Default: **false**
* Type: **Boolean**

When executing commands recursively in a workspace, execute them on the root workspace project as well.

### ignoreWorkspaceCycles

* Default: **false**
* Type: **Boolean**

When set to `true`, no workspace cycle warnings will be printed.

### disallowWorkspaceCycles

* Default: **false**
* Type: **Boolean**

When set to `true`, installation will fail if the workspace has cycles.

### failIfNoMatch

* Default: **false**
* Type: **Boolean**

When set to `true`, the CLI will exit with a non-zero code if no packages match the provided filters.

For example, the following command will exit with a non-zero code because `bad-pkg-name` is not present in the workspace:

```sh
pnpm --filter=bad-pkg-name test
```
