# Table of Contents

- [Noir Lang](#noir-lang)
- [Getting Started](#getting-started)
  - [Project Breakdown](#project-breakdown)
  - [Standalone Noir Installation](#standalone-noir-installation)
- [The Noir Language](#the-noir-language)
  **Concepts**
    **Data Types**
      - [Fields](#fields)
      - [Integers](#integers)
      - [Booleans](#booleans)
      - [Strings](#strings)
      - [Arrays](#arrays)
      - [Slices](#slices)
      - [Tuples](#tuples)
      - [Structs](#structs)
      - [References](#references)
      - [Function types](#function-types)
      - [Type Coercions](#type-coercions)
    - [Functions](#functions)
    - [Control Flow](#control-flow)
    - [Logical Operations](#logical-operations)
    - [Assert Function](#assert-function)
    - [Unconstrained Functions](#unconstrained-functions)
    - [Oracles](#oracles)
    - [Generics](#generics)
    - [Global Variables](#global-variables)
    - [Mutability](#mutability)
    - [Lambdas](#lambdas)
    - [Comments](#comments)
    - [Shadowing](#shadowing)
    - [Data Bus](#data-bus)
    - [Traits](#traits)
    - [Attributes](#attributes)
    - [Compile-time Code & Metaprogramming](#compile-time-code-metaprogramming)
  - [Standard Library](#standard-library)
    **Cryptographic Primitives**
      - [Ciphers](#ciphers)
      - [Hash methods](#hash-methods)
      - [Scalar multiplication](#scalar-multiplication)
      - [ECDSA Signature Verification](#ecdsa-signature-verification)
    - [Black Box Functions](#black-box-functions)
    - [Bn254 Field Library](#bn254-field-library)
    - [Containers](#containers)
      - [Bounded Vectors](#bounded-vectors)
      - [HashMap](#hashmap)
      - [Vectors](#vectors)
    - [fmtstr](#fmtstr)
    - [Is Unconstrained Function](#is-unconstrained-function)
    - [Logging](#logging)
    - [Memory Module](#memory-module)
    - [Metaprogramming](#metaprogramming)
      - [CtString](#ctstring)
      - [Expr](#expr)
      - [FunctionDefinition](#functiondefinition)
      - [Module](#module)
      - [UnaryOp and BinaryOp](#unaryop-and-binaryop)
      - [Quoted](#quoted)
      - [TypeDefinition](#typedefinition)
      - [TraitConstraint](#traitconstraint)
      - [TraitDefinition](#traitdefinition)
      - [TraitImpl](#traitimpl)
      - [Type](#type)
      - [TypedExpr](#typedexpr)
      - [UnresolvedType](#unresolvedtype)
    - [Option<T> Type](#option-t-type)
    - [Recursive Proofs](#recursive-proofs)
    - [Traits](#traits)
  - [Modules, Packages and Crates](#modules-packages-and-crates)
    - [Dependencies](#dependencies)
    - [Modules](#modules)
    - [Workspaces](#workspaces)
- [Explainers](#explainers)
  - [Oracles](#oracles)
- [Tutorials](#tutorials)
- [Reference](#reference)
  - [Debugger](#debugger)
    - [REPL Debugger](#repl-debugger)
    - [Known limitations](#known-limitations)
  - [Noir Codegen for TypeScript](#noir-codegen-for-typescript)
  - [NoirJS](#noirjs)
    **noir_js**
      - [classes](#classes)
      - [functions](#functions)
        - [Function: blake2s256()](#function-blake2s256)
        - [Function: ecdsa\_secp256k1\_verify()](#function-ecdsa-secp256k1-verify)
        - [Function: ecdsa\_secp256r1\_verify()](#function-ecdsa-secp256r1-verify)
        - [Function: xor()](#function-xor)
      - [type-aliases](#type-aliases)
        - [Type Alias: ForeignCallHandler()](#type-alias-foreigncallhandler)
        - [Type Alias: ForeignCallInput](#type-alias-foreigncallinput)
        - [Type Alias: ForeignCallOutput](#type-alias-foreigncalloutput)
        - [Type Alias: WitnessMap](#type-alias-witnessmap)
    - [noir_wasm](#noir-wasm)
      - [functions](#functions)
        - [Function: compile\_contract()](#function-compile-contract)
        - [Function: inflateDebugSymbols()](#function-inflatedebugsymbols)
- [Tooling](#tooling)
  - [Tests](#tests)
  - [Debugger](#debugger)
  - [Fuzzer](#fuzzer)
  - [Setting up shell completions](#setting-up-shell-completions)
  - [Profiler](#profiler)
  - [Dev Containers](#dev-containers)

---


# Noir Lang

Source: https://noir-lang.org/docs/

Version: v1.0.0-beta.17

On this page

![Noir Logo](/docs/img/logoDark.png)![Noir Logo](/docs/img/logo.png)

Noir is an open-source Domain-Specific Language for safe and seamless construction of privacy-preserving Zero-Knowledge programs, requiring no previous knowledge on the underlying mathematics or cryptography.

ZK programs are programs that can generate short proofs of statements without revealing all inputs to the statements. You can read more about Zero-Knowledge Proofs [here](https://dev.to/spalladino/a-beginners-intro-to-coding-zero-knowledge-proofs-c56).

## What's new about Noir?Noir works differently from most ZK languages by taking a two-pronged path. First, it compiles the program to an adaptable intermediate language known as ACIR. From there, depending on a given project's needs, ACIR can be further compiled into an arithmetic circuit for integration with the proving backend.

info

Noir is backend agnostic, which means it makes no assumptions on which proving backend powers the ZK proof. Being the language that powers [Aztec Contracts](https://docs.aztec.network/developers/contracts/main), it defaults to Aztec's Barretenberg proving backend.

However, the ACIR output can be transformed to be compatible with other PLONK-based backends, or into a [rank-1 constraint system](https://www.rareskills.io/post/rank-1-constraint-system) suitable for backends such as Arkwork's Marlin.

## Who is Noir for?Noir can be used both in complex cloud-based backends and in user's smartphones, requiring no knowledge on the underlying math or cryptography. From authorization systems that keep a password in the user's device, to complex on-chain verification of recursive proofs, Noir is designed to abstract away complexity without any significant overhead. Here are some examples of situations where Noir can be used:

* Aztec Contracts
* Solidity Verifiers
* Full-Stack Development

![Aztec word mark](/docs/img/aztec_word_mark_dark.svg)![Aztec word mark](/docs/img/aztec_word_mark_light.svg)

Aztec Contracts leverage Noir to allow for the storage and execution of private information. Writing an Aztec Contract is as easy as writing Noir, and Aztec developers can easily interact with the network storage and execution through the [Aztec.nr](https://docs.aztec.network/developers/contracts/main) library.

![Soliditry Verifier Example](/docs/assets/images/solidity_verifier_ex-e08a885fcda030790699aabd522e0fe5.png)

Noir can auto-generate Solidity verifier contracts that verify Noir proofs. This allows for non-interactive verification of proofs containing private information in an immutable system. This feature powers a multitude of use-case scenarios, from P2P chess tournaments, to [Aztec Layer-2 Blockchain](https://docs.aztec.network/)

Aztec Labs developed NoirJS, an easy interface to generate and verify Noir proofs in a Javascript environment. This allows for Noir to be used in webpages, mobile apps, games, and any other environment supporting JS execution in a standalone manner.

## LibrariesNoir is meant to be easy to extend by simply importing Noir libraries just like in Rust.
The [awesome-noir repo](https://github.com/noir-lang/awesome-noir#libraries) is a collection of libraries developed by the Noir community.
Writing a new library is easy and makes code be composable and easy to reuse. See the section on [dependencies](/docs/noir/modules_packages_crates/dependencies) for more information.

---


# Getting Started

Source: https://noir-lang.org/docs/getting_started/quick_start

Version: v1.0.0-beta.17

On this page

## InstallationThe easiest way to develop with Noir is using Nargo the CLI tool. It provides you the ability to start new projects, compile, execute and test Noir programs from the terminal.

You can use `noirup` the installation script to quickly install and update Nargo:

```
curl -L https://raw.githubusercontent.com/noir-lang/noirup/refs/heads/main/install | bash  
noirup
```

Once installed, you can [set up shell completions for the `nargo` command](/docs/tooling/shell_completions).

## NargoNargo provides the ability to initiate and execute Noir projects. Let's initialize the traditional `hello_world`:

```
nargo new hello_world
```

Two files will be created.

* `src/main.nr` contains a simple boilerplate circuit
* `Nargo.toml` contains environmental options, such as name, author, dependencies, and others.

Glancing at *main.nr* , we can see that inputs in Noir are private by default, but can be labeled public using the keyword `pub`. This means that we will *assert* that we know a value `x` which is different from `y` without revealing `x`:

```
fn main(x : Field, y : pub Field) {  
    assert(x != y);  
}
```

To learn more about private and public values, check the [Data Types](/docs/noir/concepts/data_types) section.

## Compiling and executingWe can now use `nargo` to generate a *Prover.toml* file, where our input values will be specified:

```
cd hello_world  
nargo check
```

Let's feed some valid values into this file:

```
x = "1"  
y = "2"
```

We're now ready to compile and execute our Noir program. By default the `nargo execute` command will do both, and generate the `witness` that we need to feed to our proving backend:

```
nargo execute
```

The witness corresponding to this execution will then be written to the file *./target/witness-name.gz*.

The command also automatically compiles your Noir program if it was not already / was edited, which you may notice the compiled artifacts being written to the file *./target/hello\_world.json*.

With circuit compiled and witness generated, we're ready to prove.

## Next Steps - Proving backendNoir is a high-level programming language for zero-knowledge proofs, which compiles your code into [ACIR](https://noir-lang.github.io/noir/docs/acir/circuit/index.html) and generates witnesses for further proof generations and verifications. In order to prove and verify your Noir programs, you'll need a proving backend.

Proving backends provide you multiple tools. The most common backend for Noir is [Barretenberg](https://barretenberg.aztec.network). It allows you to:

* Generate proofs and verify them
* Prove the verification of another proof (recursive aggregation)
* Generate a solidity contract that verifies your proof non-interactively
* Check and compare circuit size

Read [Barretenberg's Getting Started guide](https://barretenberg.aztec.network/docs/getting_started) to install and start using Noir with Barretenberg.

Visit [Awesome Noir](https://github.com/noir-lang/awesome-noir/?tab=readme-ov-file#proving-backends) for a comprehensive list of proving backends that work with Noir.

---


# Project Breakdown

Source: https://noir-lang.org/docs/getting_started/project_breakdown

Version: v1.0.0-beta.17

On this page

This section breaks down our hello world program from the previous section.

## Anatomy of a Nargo ProjectUpon creating a new project with `nargo new` and building the in/output files with `nargo check`
commands, you would get a minimal Nargo project of the following structure:

```
- src  
- Prover.toml  
- Nargo.toml
```

The source directory *src* holds the source code for your Noir program. By default only a *main.nr*
file will be generated within it.

## Prover.toml*Prover.toml* is used for specifying the input values for executing and proving the program. You can specify `toml` files with different names by using the `--prover-name` or `-p` flags, see the [Prover](#provertoml) section below. Optionally you may specify expected output values for prove-time checking as well.

## Nargo.toml*Nargo.toml* contains the environmental options of your project. It contains a "package" section and a "dependencies" section.

Example Nargo.toml:

```
[package]  
name = "noir_starter"  
type = "bin"  
authors = ["Alice"]  
compiler_version = "0.9.0"  
description = "Getting started with Noir"  
entry = "circuit/main.nr"  
license = "MIT"  
  
[dependencies]  
ecrecover = {tag = "v0.9.0", git = "https://github.com/colinnielsen/ecrecover-noir.git"}
```

Nargo.toml for a [workspace](/docs/noir/modules_packages_crates/workspaces) will look a bit different. For example:

```
[workspace]  
members = ["crates/a", "crates/b"]  
default-member = "crates/a"
```

## Package sectionThe package section defines a number of fields including:

* `name` (**required**) - the name of the package
* `type` (**required**) - can be "bin", "lib", or "contract" to specify whether its a binary, library or Aztec contract
* `authors` (optional) - authors of the project
* `compiler_version` - specifies the version of the compiler to use. This is enforced by the compiler and follow's [Rust's versioning](https://doc.rust-lang.org/cargo/reference/manifest.html#the-version-field), so a `compiler_version = 0.18.0` will enforce Nargo version 0.18.0, `compiler_version = ^0.18.0` will enforce anything above 0.18.0 but below 0.19.0, etc. For more information, see how [Rust handles these operators](https://docs.rs/semver/latest/semver/enum.Op.html)
* `compiler_unstable_features` (optional) - A list of unstable features required by this package to compile.
* `description` (optional)
* `entry` (optional) - a relative filepath to use as the entry point into your package (overrides the default of `src/lib.nr` or `src/main.nr`)
* `backend` (optional)
* `license` (optional)
* `expression_width` (optional) - Sets the default backend expression width. This field will override the default backend expression width specified by the Noir compiler (currently set to width 4).

## Dependencies sectionThis is where you will specify any dependencies for your project. See the [Dependencies page](/docs/noir/modules_packages_crates/dependencies) for more info.

`./proofs/` and `./contract/` directories will not be immediately visible until you create a proof or
verifier contract respectively.

## main.nrThe *main.nr* file contains a `main` method, this method is the entry point into your Noir program.

In our sample program, *main.nr* looks like this:

```
fn main(x : Field, y : Field) {  
    assert(x != y);  
}
```

The parameters `x` and `y` can be seen as the API for the program and must be supplied by the prover. Since neither `x` nor `y` is marked as public, the verifier does not supply any inputs, when verifying the proof.

The prover supplies the values for `x` and `y` in the *Prover.toml* file.

As for the program body, `assert` ensures that the condition to be satisfied (e.g. `x != y`) is constrained by the proof of the execution of said program (i.e. if the condition was not met, the verifier would reject the proof as an invalid proof).

## Prover.tomlThe *Prover.toml* file is a file which the prover uses to supply the inputs to the Noir program (both private and public).

In our hello world program the *Prover.toml* file looks like this:

```
x = "1"  
y = "2"
```

When the command `nargo execute` is executed, nargo will execute the Noir program using the inputs specified in `Prover.toml`, aborting if it finds that these do not satisfy the constraints defined by `main`. In this example, `x` and `y` must satisfy the inequality constraint `assert(x != y)`.

If an output name is specified such as `nargo execute foo`, the witness generated by this execution will be written to `./target/foo.gz`. This can then be used to generate a proof of the execution.

## Arrays of StructsThe following code shows how to pass an array of structs to a Noir program to generate a proof.

```
// main.nr  
struct Foo {  
    bar: Field,  
    baz: Field,  
}  
  
fn main(foos: [Foo; 3]) -> pub Field {  
    foos[2].bar + foos[2].baz  
}
```

Prover.toml:

```
[[foos]] # foos[0]  
bar = 0  
baz = 0  
  
[[foos]] # foos[1]  
bar = 0  
baz = 0  
  
[[foos]] # foos[2]  
bar = 1  
baz = 2
```

## Custom toml filesYou can specify a `toml` file with a different name to use for execution by using the `--prover-name` or `-p` flags.

This command looks for proof inputs in the default **Prover.toml** and generates the witness and saves it at `./target/foo.gz`:

```
nargo execute foo
```

This command looks for proof inputs in the custom **OtherProver.toml** and generates the witness and saves it at `./target/bar.gz`:

```
nargo execute -p OtherProver bar
```

Now that you understand the concepts, you'll probably want some editor feedback while you are writing more complex code.

---


# Standalone Noir Installation

Source: https://noir-lang.org/docs/getting_started/noir_installation

Version: v1.0.0-beta.17

On this page

Noirup is the endorsed method for installing Nargo, streamlining the process of fetching binaries or compiling from source. It supports a range of options to cater to your specific needs, from nightly builds and specific versions to compiling from various sources.

## Installing NoirupFirst, ensure you have `noirup` installed:

```
curl -L https://raw.githubusercontent.com/noir-lang/noirup/main/install | bash
```

## Fetching BinariesWith `noirup`, you can easily switch between different Nargo versions, including nightly builds:

* **Nightly Version**: Install the latest nightly build.

  ```
  noirup --version nightly
  ```
* **Specific Version**: Install a specific version of Nargo.

  ```
  noirup --version <version>
  ```

## Compiling from Source`noirup` also enables compiling Nargo from various sources:

* **From a Specific Branch**: Install from the latest commit on a branch.

  ```
  noirup --branch <branch-name>
  ```
* **From a Fork**: Install from the main branch of a fork.

  ```
  noirup --repo <username/repo>
  ```
* **From a Specific Branch in a Fork**: Install from a specific branch in a fork.

  ```
  noirup --repo <username/repo> --branch <branch-name>
  ```
* **From a Specific Pull Request**: Install from a specific PR.

  ```
  noirup --pr <pr-number>
  ```
* **From a Specific Commit**: Install from a specific commit.

  ```
  noirup -C <commit-hash>
  ```
* **From Local Source**: Compile and install from a local directory.

  ```
  noirup --path ./path/to/local/source
  ```

## Installation on WindowsThe default backend for Noir (Barretenberg) doesn't provide Windows binaries at this time. For that reason, Noir cannot be installed natively. However, it is available by using Windows Subsystem for Linux (WSL).

Step 1: Follow the instructions [here](https://learn.microsoft.com/en-us/windows/wsl/install) to install and run WSL.

step 2: Follow the [Noirup instructions](#installing-noirup).

## Setting up shell completionsOnce `nargo` is installed, you can [set up shell completions for it](/docs/tooling/shell_completions).

## Uninstalling NargoIf you installed Nargo with `noirup`, you can uninstall Nargo by removing the files in `~/.nargo`, `~/nargo`, and `~/noir_cache`. This ensures that all installed binaries, configurations, and cache related to Nargo are fully removed from your system.

```
rm -r ~/.nargo  
rm -r ~/nargo  
rm -r ~/noir_cache
```

---


# The Noir Language

Source: https://noir-lang.org/docs/noir/concepts/data_types

Version: v1.0.0-beta.17

On this page

Every value in Noir has a type, which determines which operations are valid for it.

All values in Noir are fundamentally composed of `Field` elements. For a more approachable
developing experience, abstractions are added on top to introduce different data types in Noir.

Noir has two category of data types: primitive types (e.g. `Field`, integers, `bool`) and compound
types that group primitive types (e.g. arrays, tuples, structs). Each value can either be private or
public.

## Private & Public TypesA **private value** is known only to the Prover, while a **public value** is known by both the
Prover and Verifier. Mark values as `private` when the value should only be known to the prover. All
primitive types (including individual fields of compound types) in Noir are private by default, and
can be marked public when certain values are intended to be revealed to the Verifier.

> **Note:** For public values defined in Noir programs paired with smart contract verifiers, once
> the proofs are verified on-chain the values can be considered known to everyone that has access to
> that blockchain.

Public data types are treated no differently to private types apart from the fact that their values
will be revealed in proofs generated. Simply changing the value of a public type will not change the
circuit (where the same goes for changing values of private types as well).

*Private values* are also referred to as *witnesses* sometimes.

> **Note:** The terms private and public when applied to a type (e.g. `pub Field`) have a different
> meaning than when applied to a function (e.g. `pub fn foo() {}`).
>
> The former is a visibility modifier for the Prover to interpret if a value should be made known to
> the Verifier, while the latter is a visibility modifier for the compiler to interpret if a
> function should be made accessible to external Noir programs like in other languages.

## pub ModifierAll data types in Noir are private by default. Types are explicitly declared as public using the
`pub` modifier:

```
fn main(x: u32, y: pub u32) -> pub u32 {  
    x + y  
}
```

In this example, `x` is **private** while `y` and `x + y` (the return value) are **public**. Note
that visibility is handled **per variable**, so it is perfectly valid to have one input that is
private and another that is public.

> **Note:** Public types can only be declared through parameters on `main`.

## Type AliasesA type alias is a new name for an existing type. Type aliases are declared with the keyword `type`:

```
type Id = u8;  
  
fn main() {  
    let id: Id = 1;  
    let zero: u8 = 0;  
    assert(zero + 1 == id);  
}
```

Type aliases can also be used with [generics](/docs/noir/concepts/generics):

```
type Id<Size> = Size;  
  
fn main() {  
    let id: Id<u32> = 1;  
    let zero: u32 = 0;  
    assert(zero + 1 == id);  
}
```

Type aliases can even refer to other aliases. An error will be issued if they form a cycle:

```
// Ok!  
type A = B;  
type B = Field;  
  
type Bad1 = Bad2;  
  
// error: Dependency cycle found  
type Bad2 = Bad1;  
//   ^^^^^^^^^^^ 'Bad2' recursively depends on itself: Bad2 -> Bad1 -> Bad2
```

By default, like functions, type aliases are private to the module they exist in. You can use `pub`
to make the type alias public or `pub(crate)` to make it public to just its crate:

```
// This type alias is now public  
pub type Id = u8;
```

## Numeric type aliasesType aliases can also be defined for numeric types, which can help cut down on longer type expressions.

```
type Double<let N: u32>: u32 = N * 2;  
  
// When used in an array position we need to use the turbofish operator to specify any  
// generics in a numeric type alias  
fn concat_self<let N: u32>(array: [u32; N]) -> [u32; Double::<N>] {  
    let mut result = [0; Double::<N>];  
    for i in 0..array.len() {  
        result[i] = array[i];  
        result[i + array.len()] = array[i];  
    }  
    result  
}  
  
struct Array<T, let N: u32> {  
    data: [T; N],  
}  
  
// When used within other type positions, however, we can refer to it without the `::`  
fn concat_self2<let N: u32>(array: Array<u32, N>) -> Array<u32, Double<N>> {  
    Array { data: concat_self(array.data) }  
}
```

## Wildcard TypeNoir can usually infer the type of the variable from the context, so specifying the type of a variable is only required when it cannot be inferred. However, specifying a complex type can be tedious, especially when it has multiple generic arguments. Often some of the generic types can be inferred from the context, and Noir only needs a hint to properly infer the other types. We can partially specify a variable's type by using `_` as a marker, indicating where we still want the compiler to infer the type.

```
let a: [_; 4] = foo(b);
```

---


# Fields

Source: https://noir-lang.org/docs/noir/concepts/data_types/fields

Version: v1.0.0-beta.17

On this page

The field type corresponds to the native field type of the proving backend.

The size of a Noir field depends on the elliptic curve's finite field for the proving backend adopted. For example, a field would be a 254-bit integer when paired with the default backend that spans the Grumpkin curve.

Fields support integer arithmetic:

```
fn main(x : Field, y : Field)  {  
    let z = x + y;  
}
```

`x`, `y` and `z` are all private fields in this example. Using the `let` keyword we defined a new private value `z` constrained to be equal to `x + y`.

If proving efficiency is of priority, fields should be used as a default for solving problems. Smaller integer types (e.g. `u64`) incur extra range constraints.

## MethodsAfter declaring a Field, you can use these common methods on it:

## to\_le\_bitsTransforms the field into an array of bits, Little Endian.

to\_le\_bits

```
pub fn to_le_bits<let N: u32>(self: Self) -> [u1; N] {
```

> [Source code: noir\_stdlib/src/field/mod.nr#L29-L31](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/field/mod.nr#L29-L31)

example:

to\_le\_bits\_example

```
fn test_to_le_bits() {  
        let field = 2;  
        let bits: [u1; 8] = field.to_le_bits();  
        assert_eq(bits, [0, 1, 0, 0, 0, 0, 0, 0]);  
    }
```

> [Source code: noir\_stdlib/src/field/mod.nr#L356-L362](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/field/mod.nr#L356-L362)

## to\_be\_bitsTransforms the field into an array of bits, Big Endian.

to\_be\_bits

```
pub fn to_be_bits<let N: u32>(self: Self) -> [u1; N] {
```

> [Source code: noir\_stdlib/src/field/mod.nr#L61-L63](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/field/mod.nr#L61-L63)

example:

to\_be\_bits\_example

```
fn test_to_be_bits() {  
        let field = 2;  
        let bits: [u1; 8] = field.to_be_bits();  
        assert_eq(bits, [0, 0, 0, 0, 0, 0, 1, 0]);  
    }
```

> [Source code: noir\_stdlib/src/field/mod.nr#L347-L353](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/field/mod.nr#L347-L353)

## to\_le\_bytesTransforms into an array of bytes, Little Endian

to\_le\_bytes

```
pub fn to_le_bytes<let N: u32>(self: Self) -> [u8; N] {
```

> [Source code: noir\_stdlib/src/field/mod.nr#L93-L95](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/field/mod.nr#L93-L95)

example:

to\_le\_bytes\_example

```
fn test_to_le_bytes() {  
        let field = 2;  
        let bytes: [u8; 8] = field.to_le_bytes();  
        assert_eq(bytes, [2, 0, 0, 0, 0, 0, 0, 0]);  
        assert_eq(Field::from_le_bytes::<8>(bytes), field);  
    }
```

> [Source code: noir\_stdlib/src/field/mod.nr#L375-L382](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/field/mod.nr#L375-L382)

## to\_be\_bytesTransforms into an array of bytes, Big Endian

to\_be\_bytes

```
pub fn to_be_bytes<let N: u32>(self: Self) -> [u8; N] {
```

> [Source code: noir\_stdlib/src/field/mod.nr#L130-L132](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/field/mod.nr#L130-L132)

example:

to\_be\_bytes\_example

```
fn test_to_be_bytes() {  
        let field = 2;  
        let bytes: [u8; 8] = field.to_be_bytes();  
        assert_eq(bytes, [0, 0, 0, 0, 0, 0, 0, 2]);  
        assert_eq(Field::from_be_bytes::<8>(bytes), field);  
    }
```

> [Source code: noir\_stdlib/src/field/mod.nr#L365-L372](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/field/mod.nr#L365-L372)

## pow\_32Returns the value to the power of the specified exponent

```
fn pow_32(self, exponent: Field) -> Field
```

example:

```
fn main() {  
    let field = 2  
    let pow = field.pow_32(4);  
    assert(pow == 16);  
}
```

## assert\_max\_bit\_sizeAdds a constraint to specify that the field can be represented with `bit_size` number of bits

assert\_max\_bit\_size

```
pub fn assert_max_bit_size<let BIT_SIZE: u32>(self) {
```

> [Source code: noir\_stdlib/src/field/mod.nr#L10-L12](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/field/mod.nr#L10-L12)

example:

```
fn main() {  
    let field = 2  
    field.assert_max_bit_size::<32>();  
}
```

## sgn0Parity of (prime) Field element, i.e. sgn0(x mod p) = 0 if x ∈ {0, ..., p-1} is even, otherwise sgn0(x mod p) = 1.

```
fn sgn0(self) -> u1
```

## ltReturns true if the field is less than the other field

```
pub fn lt(self, another: Field) -> bool
```

---


# Integers

Source: https://noir-lang.org/docs/noir/concepts/data_types/integers

Version: v1.0.0-beta.17

On this page

An integer type is a range constrained field type.
The Noir frontend supports both unsigned and signed integer types.
The allowed sizes are 1, 8, 16, 32, 64 and 128 bits. ([currently only unsigned integers for 128 bits](https://github.com/noir-lang/noir/issues/7591))

info

When an integer is defined in Noir without a specific type, it will default to `Field` unless another type is expected at its position.

The one exception is for loop indices which default to `u32` since comparisons on `Field`s are not possible.

You can add a type suffix such as `u32` or `Field` to the end of an integer literal to explicitly specify the type.

## Unsigned IntegersAn unsigned integer type is specified first with the letter `u` (indicating its unsigned nature) followed by its bit size (e.g. `8`):

```
fn main() {  
    let x: u8 = 1;  
    let y = 1_u8;  
    let z = x + y;  
    assert (z == 2);  
}
```

The bit size determines the maximum value the integer type can store. For example, a `u8` variable can store a value in the range of 0 to 255 (i.e. 28−1\\2^{8}-1\\28−1).

## Signed IntegersA signed integer type is specified first with the letter `i` (which stands for integer) followed by its bit size (e.g. `8`):

```
fn main() {  
    let x: i8 = -1;  
    let y = -1i8;  
    let z = x + y;  
    assert (z == -2);  
}
```

The bit size determines the maximum and minimum range of value the integer type can store. For example, an `i8` variable can store a value in the range of -128 to 127 (i.e. −27\\-2^{7}\\−27 to 27−1\\2^{7}-1\\27−1).

```
fn main(x: i16, y: i16) {  
    // modulo  
    let c = x % y;  
    let c = x % -13;  
}
```

Modulo operation is defined for negative integers thanks to integer division, so that the equality `x = (x/y)*y + (x%y)` holds.

## OverflowsComputations that exceed the type boundaries will result in overflow errors. This happens with both signed and unsigned integers. For example, attempting to prove:

```
fn main(x: u8, y: u8) -> pub u8 {  
    let z = x + y;  
    z  
}
```

With:

```
x = "255"  
y = "1"
```

Would result in:

```
$ nargo execute  
error: Assertion failed: 'attempt to add with overflow'  
┌─ ~/src/main.nr:9:13  
│  
│     let z = x + y;  
│             -----  
│  
= Call stack:  
  ...
```

A similar error would happen with signed integers:

```
fn main() -> i8 {  
    let x: i8 = -118;  
    let y = -11;  
    let z = x + y;  
    z  
}
```

Note that if a computation ends up being unused the compiler might remove it and it won't end up producing an overflow:

```
fn main() {  
    // "255 + 1" would overflow, but `z` is unused so no computation happens  
    let z: u8 = 255 + 1;  
}
```

## Wrapping methodsAlthough integer overflow is expected to error, some use-cases rely on wrapping. For these use-cases, the standard library provides `wrapping` variants of certain common operations via Wrapping traits in `std::ops`

```
fn wrapping_add(self, y: Self) -> Self;  
fn wrapping_sub(self, y: Self) -> Self;  
fn wrapping_mul(self, y: Self) -> Self;
```

Example of how it is used:

```
use std::ops::WrappingAdd  
fn main(x: u8, y: u8) -> pub u8 {  
    x.wrapping_add(y)  
}
```

---


# Booleans

Source: https://noir-lang.org/docs/noir/concepts/data_types/booleans

Version: v1.0.0-beta.17

The `bool` type in Noir has two possible values: `true` and `false`:

```
fn main() {  
    let t = true;  
    let f: bool = false;  
}
```

The boolean type is most commonly used in conditionals like `if` expressions and `assert`
statements. More about conditionals is covered in the [Control Flow](/docs/noir/concepts/control_flow) and
[Assert Function](/docs/noir/concepts/assert) sections.

---


# Strings

Source: https://noir-lang.org/docs/noir/concepts/data_types/strings

Version: v1.0.0-beta.17

On this page

The string type is a fixed length value defined with `str<N>`.

You can use strings in `assert()` functions or print them with
`println()`. See more about [Logging](/docs/noir/standard_library/logging).

```
fn main(message : pub str<11>, hex_as_string : str<4>) {  
    println(message);  
    assert(message == "hello world");  
    assert(hex_as_string == "0x41");  
}
```

You can convert a `str<N>` to a byte array by calling `as_bytes()`
or a vector by calling `as_bytes_vec()`.

```
fn main() {  
    let message = "hello world";  
    let message_bytes = message.as_bytes();  
    let mut message_vec = message.as_bytes_vec();  
    assert(message_bytes.len() == 11);  
    assert(message_bytes[0] == 104);  
    assert(message_bytes[0] == message_vec.get(0));  
}
```

## Escape charactersYou can use escape characters for your strings:

| Escape Sequence | Description |
| --- | --- |
| `\r` | Carriage Return |
| `\n` | Newline |
| `\t` | Tab |
| `\0` | Null Character |
| `\"` | Double Quote |
| `\\` | Backslash |

Example:

```
let s = "Hello \"world" // prints "Hello "world"  
let s = "hey \tyou"; // prints "hey   you"
```

## Raw stringsA raw string begins with the letter `r` and is optionally delimited by a number of hashes `#`.

Escape characters are *not* processed within raw strings. All contents are interpreted literally.

Example:

```
let s = r"Hello world";  
let s = r#"Simon says "hello world""#;  
  
// Any number of hashes may be used (>= 1) as long as the string also terminates with the same number of hashes  
let s = r##"One "#, Two "##, Three "##, Four "##, Five will end the string."##;
```

## Format stringsA format string begins with the letter `f` and allows inserting the value of local and global variables in it.

Example:

```
let four = 2 + 2;  
let s = f"Two plus two is: {four}";  
println(s);
```

The output of the above program is:

```
Two plus two is: 4
```

To insert the value of a local or global variable, put it inside `{...}` in the string.

If you need to write the `{` or `}` characters, use `{{` and `}}` respectively:

```
let four = 2 + 2;  
  
// Prints "This is not expanded: {four}"  
println(f"This is not expanded: {{four}}");
```

More complex expressions are not allowed inside `{...}`:

```
let s = f"Two plus two is: {2 + 2}" // Error: invalid format string
```

---


# Arrays

Source: https://noir-lang.org/docs/noir/concepts/data_types/arrays

Version: v1.0.0-beta.17

On this page

An array is one way of grouping together values into one compound type. Array types can be inferred
or explicitly specified via the syntax `[<Type>; <Size>]`:

```
fn main(x : u64, y : u64) {  
    let my_arr = [x, y];  
    let your_arr: [u64; 2] = [x, y];  
}
```

Here, both `my_arr` and `your_arr` are instantiated as an array containing two `Field` elements.

Array elements can be accessed using indexing:

```
fn main() {  
    let a = [1, 2, 3, 4, 5];  
  
    let first = a[0];  
    let second = a[1];  
}
```

All elements in an array must be of the same type (i.e. homogeneous). That is, an array cannot group
a `Field` value and a `u8` value together for example.

You can write mutable arrays, like:

```
fn main() {  
    let mut arr = [1, 2, 3, 4, 5];  
    assert(arr[0] == 1);  
  
    arr[0] = 42;  
    assert(arr[0] == 42);  
}
```

You can instantiate a new array of a fixed size with the same value repeated for each element. The following example instantiates an array of length 32 where each element is of type Field and has the value 0.

```
let array: [Field; 32] = [0; 32];
```

Like in Rust, arrays in Noir are a fixed size. However, if you wish to convert an array to a [slice](/docs/noir/concepts/data_types/slices), you can just call `as_slice` on your array:

```
let array: [Field; 32] = [0; 32];  
let sl = array.as_slice()
```

You can define multidimensional arrays:

```
let array : [[Field; 2]; 2];  
let element = array[0][0];
```

However, multidimensional slices are not supported. For example, the following code will error at compile time:

```
let slice : [[Field]] = &[];
```

## Dynamic IndexingUsing constant indices of arrays will often be more efficient at runtime in constrained code.
Indexing an array with non-constant indices (indices derived from the inputs to the program, or returned from unconstrained functions) is also
called "dynamic indexing" and incurs a slight runtime cost:

```
fn main(x: u32) {  
    let array = [1, 2, 3, 4];  
  
    // This is a constant index, after inlining the compiler sees that this  
    // will always be `array[2]`  
    let _a = array[double(1)];  
  
    // This is a non-constant index, there is no way to know which u32 value  
    // will be used as an index here  
    let _b = array[double(x)];  
}  
  
fn double(y: u32) -> u32 {  
    y * 2  
}
```

There is another restriction with dynamic indices: they cannot be used on arrays with
elements which contain a reference type:

```
fn main(x: u32) {  
    let array = [&mut 1, &mut 2, &mut 3, &mut 4];  
  
    // error! Only constant indices may be used here since `array` contains references internally!  
    let _c = array[x];  
}
```

## TypesYou can create arrays of primitive types or structs. There is not yet support for nested arrays
(arrays of arrays) or arrays of structs that contain arrays.

## MethodsFor convenience, the STD provides some ready-to-use, common methods for arrays.
Each of these functions are located within the generic impl `impl<T, N> [T; N] {`.
So anywhere `self` appears, it refers to the variable `self: [T; N]`.

## lenReturns the length of an array

```
fn len(self) -> Field
```

example

```
fn main() {  
    let array = [42, 42];  
    assert(array.len() == 2);  
}
```

## sortReturns a new sorted array. The original array remains untouched. Notice that this function will
only work for arrays of fields or integers, not for any arbitrary type. This is because the sorting
logic it uses internally is optimized specifically for these values. If you need a sort function to
sort any type, you should use the function `sort_via` described below.

```
fn sort(self) -> [T; N]
```

example

```
fn main() {  
    let arr = [42, 32];  
    let sorted = arr.sort();  
    assert(sorted == [32, 42]);  
}
```

## sort\_viaSorts the array with a custom comparison function. The ordering function must return true if the first argument should be sorted to be before the second argument or is equal to the second argument.

Using this method with an operator like `<` that does not return `true` for equal values will result in an assertion failure for arrays with equal elements.

```
fn sort_via(self, ordering: fn(T, T) -> bool) -> [T; N]
```

example

```
fn main() {  
    let arr = [42, 32]  
    let sorted_ascending = arr.sort_via(|a, b| a <= b);  
    assert(sorted_ascending == [32, 42]); // verifies  
  
    let sorted_descending = arr.sort_via(|a, b| a >= b);  
    assert(sorted_descending == [32, 42]); // does not verify  
}
```

## mapApplies a function to each element of the array, returning a new array containing the mapped elements.

```
fn map<U>(self, f: fn(T) -> U) -> [U; N]
```

example

```
let a = [1, 2, 3];  
let b = a.map(|a| a * 2); // b is now [2, 4, 6]
```

## mapiApplies a function to each element of the array, along with its index in the
array, returning a new array containing the mapped elements.

```
fn mapi<U, Env>(self, f: fn[Env](u32, T) -> U) -> [U; N]
```

example

```
let a = [1, 2, 3];  
let b = a.mapi(|i, a| i + a * 2); // b is now [2, 5, 8]
```

## for\_eachApplies a function to each element of the array.

```
fn for_each<Env>(self, f: fn[Env](T) -> ())
```

example

```
let a = [1, 2, 3];  
a.for_each(|x| {  
    println(f"{x}");  
});  
// prints:  
// 1  
// 2  
// 3
```

## for\_eachiApplies a function to each element of the array, along with its index in the
array.

```
fn for_eachi<Env>(self, f: fn[Env](u32, T) -> ())
```

example

```
let a = [1, 2, 3];  
a.for_eachi(|i, x| {  
    println(f"{i}, {x}");  
});  
// prints:  
// 0, 1  
// 1, 2  
// 2, 3
```

## foldApplies a function to each element of the array, returning the final accumulated value. The first
parameter is the initial value.

```
fn fold<U>(self, mut accumulator: U, f: fn(U, T) -> U) -> U
```

This is a left fold, so the given function will be applied to the accumulator and first element of
the array, then the second, and so on. For a given call the expected result would be equivalent to:

```
let a1 = [1];  
let a2 = [1, 2];  
let a3 = [1, 2, 3];  
  
let f = |a, b| a - b;  
a1.fold(10, f)  //=> f(10, 1)  
a2.fold(10, f)  //=> f(f(10, 1), 2)  
a3.fold(10, f)  //=> f(f(f(10, 1), 2), 3)
```

example:

```
fn main() {  
    let arr = [2, 2, 2, 2, 2];  
    let folded = arr.fold(0, |a, b| a + b);  
    assert(folded == 10);  
}
```

## reduceSame as fold, but uses the first element as the starting element.

Requires `self` to be non-empty.

```
fn reduce(self, f: fn(T, T) -> T) -> T
```

example:

```
fn main() {  
    let arr = [2, 2, 2, 2, 2];  
    let reduced = arr.reduce(|a, b| a + b);  
    assert(reduced == 10);  
}
```

## allReturns true if all the elements satisfy the given predicate

```
fn all(self, predicate: fn(T) -> bool) -> bool
```

example:

```
fn main() {  
    let arr = [2, 2, 2, 2, 2];  
    let all = arr.all(|a| a == 2);  
    assert(all);  
}
```

## anyReturns true if any of the elements satisfy the given predicate

```
fn any(self, predicate: fn(T) -> bool) -> bool
```

example:

```
fn main() {  
    let arr = [2, 2, 2, 2, 5];  
    let any = arr.any(|a| a == 5);  
    assert(any);  
}
```

## concatConcatenates this array with another array.

```
fn concat<let M: u32>(self, array2: [T; M]) -> [T; N + M]
```

```
fn main() {  
    let arr1 = [1, 2, 3, 4];  
    let arr2 = [6, 7, 8, 9, 10, 11];  
    let concatenated_arr = arr1.concat(arr2);  
    assert(concatenated_arr == [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]);  
}
```

## as\_str\_uncheckedConverts a byte array of type `[u8; N]` to a string. Note that this performs no UTF-8 validation -
the given array is interpreted as-is as a string.

```
impl<let N: u32> [u8; N] {  
    pub fn as_str_unchecked(self) -> str<N>  
}
```

example:

```
fn main() {  
    let hi = [104, 105].as_str_unchecked();  
    assert_eq(hi, "hi");  
}
```

---


# Slices

Source: https://noir-lang.org/docs/noir/concepts/data_types/slices

Version: v1.0.0-beta.17

On this page

Experimental Feature

This feature is experimental. The documentation may be incomplete or out of date, which means it could change in future versions, potentially causing unexpected behavior or not working as expected.

**Contributions Welcome:** If you notice any inaccuracies or potential improvements, please consider contributing. Visit our GitHub repository to make your contributions: [Contribute Here](https://github.com/noir-lang/noir).

A slice is a dynamically-sized view into a sequence of elements. They can be resized at runtime, but because they don't own the data, they cannot be returned from a circuit. You can treat slices as arrays without a constrained size.

```
fn main() -> pub u32 {  
    let mut slice: [Field] = &[0; 2];  
  
    let mut new_slice = slice.push_back(6);  
    new_slice.len()  
}
```

To write a slice literal, use a preceding ampersand as in: `&[0; 2]` or
`&[1, 2, 3]`.

It is important to note that slices are not references to arrays. In Noir,
`&[..]` is more similar to an immutable, growable vector.

View the corresponding test file [here](https://github.com/noir-lang/noir/blob/f387ec1475129732f72ba294877efdf6857135ac/crates/nargo_cli/tests/test_data_ssa_refactor/slices/src/main.nr).

## MethodsFor convenience, the STD provides some ready-to-use, common methods for slices:

## push\_backPushes a new element to the end of the slice, returning a new slice with a length one greater than the original unmodified slice.

```
fn push_back<T>(_self: [T], _elem: T) -> [T]
```

example:

```
fn main() -> pub Field {  
    let mut slice: [Field] = &[0; 2];  
  
    let mut new_slice = slice.push_back(6);  
    new_slice.len()  
}
```

View the corresponding test file [here](https://github.com/noir-lang/noir/blob/f387ec1475129732f72ba294877efdf6857135ac/crates/nargo_cli/tests/test_data_ssa_refactor/slices/src/main.nr).

## push\_frontReturns a new slice with the specified element inserted at index 0. The existing elements indexes are incremented by 1.

```
fn push_front(_self: Self, _elem: T) -> Self
```

Example:

```
let mut new_slice: [Field] = &[];  
new_slice = new_slice.push_front(20);  
assert(new_slice[0] == 20); // returns true
```

View the corresponding test file [here](https://github.com/noir-lang/noir/blob/f387ec1475129732f72ba294877efdf6857135ac/crates/nargo_cli/tests/test_data_ssa_refactor/slices/src/main.nr).

## pop\_frontReturns a tuple of two items, the first element of the slice and the rest of the slice.

```
fn pop_front(_self: Self) -> (T, Self)
```

Example:

```
let (first_elem, rest_of_slice) = slice.pop_front();
```

View the corresponding test file [here](https://github.com/noir-lang/noir/blob/f387ec1475129732f72ba294877efdf6857135ac/crates/nargo_cli/tests/test_data_ssa_refactor/slices/src/main.nr).

## pop\_backReturns a tuple of two items, the beginning of the slice with the last element omitted and the last element.

```
fn pop_back(_self: Self) -> (Self, T)
```

Example:

```
let (popped_slice, last_elem) = slice.pop_back();
```

View the corresponding test file [here](https://github.com/noir-lang/noir/blob/f387ec1475129732f72ba294877efdf6857135ac/crates/nargo_cli/tests/test_data_ssa_refactor/slices/src/main.nr).

## appendLoops over a slice and adds it to the end of another.

```
fn append(mut self, other: Self) -> Self
```

Example:

```
let append = &[1, 2].append(&[3, 4, 5]);
```

## insertInserts an element at a specified index and shifts all following elements by 1.

```
fn insert(_self: Self, _index: u32, _elem: T) -> Self
```

Example:

```
new_slice = rest_of_slice.insert(2, 100);  
assert(new_slice[2] == 100);
```

View the corresponding test file [here](https://github.com/noir-lang/noir/blob/f387ec1475129732f72ba294877efdf6857135ac/crates/nargo_cli/tests/test_data_ssa_refactor/slices/src/main.nr).

## removeRemove an element at a specified index, shifting all elements after it to the left, returning the altered slice and the removed element.

```
fn remove(_self: Self, _index: u32) -> (Self, T)
```

Example:

```
let (remove_slice, removed_elem) = slice.remove(3);
```

## lenReturns the length of a slice

```
fn len(self) -> Field
```

Example:

```
fn main() {  
    let slice = &[42, 42];  
    assert(slice.len() == 2);  
}
```

## as\_arrayConverts this slice into an array.

Make sure to specify the size of the resulting array.
Panics if the resulting array length is different than the slice's length.

```
fn as_array<let N: u32>(self) -> [T; N]
```

Example:

```
fn main() {  
    let slice = &[5, 6];  
  
    // Always specify the length of the resulting array!  
    let array: [Field; 2] = slice.as_array();  
  
    assert(array[0] == slice[0]);  
    assert(array[1] == slice[1]);  
}
```

## mapApplies a function to each element of the slice, returning a new slice containing the mapped elements.

```
fn map<U, Env>(self, f: fn[Env](T) -> U) -> [U]
```

example

```
let a = &[1, 2, 3];  
let b = a.map(|a| a * 2); // b is now &[2, 4, 6]
```

## mapiApplies a function to each element of the slice, along with its index in the
slice, returning a new slice containing the mapped elements.

```
fn mapi<U, Env>(self, f: fn[Env](u32, T) -> U) -> [U]
```

example

```
let a = &[1, 2, 3];  
let b = a.mapi(|i, a| i + a * 2); // b is now &[2, 5, 8]
```

## for\_eachApplies a function to each element of the slice.

```
fn for_each<Env>(self, f: fn[Env](T) -> ())
```

example

```
let a = &[1, 2, 3];  
a.for_each(|x| {  
    println(f"{x}");  
});  
// prints:  
// 1  
// 2  
// 3
```

## for\_eachiApplies a function to each element of the slice, along with its index in the
slice.

```
fn for_eachi<Env>(self, f: fn[Env](u32, T) -> ())
```

example

```
let a = &[1, 2, 3];  
a.for_eachi(|i, x| {  
    println(f"{i}, {x}");  
});  
// prints:  
// 0, 1  
// 1, 2  
// 2, 3
```

## foldApplies a function to each element of the slice, returning the final accumulated value. The first
parameter is the initial value.

```
fn fold<U, Env>(self, mut accumulator: U, f: fn[Env](U, T) -> U) -> U
```

This is a left fold, so the given function will be applied to the accumulator and first element of
the slice, then the second, and so on. For a given call the expected result would be equivalent to:

```
let a1 = &[1];  
let a2 = &[1, 2];  
let a3 = &[1, 2, 3];  
  
let f = |a, b| a - b;  
a1.fold(10, f)  //=> f(10, 1)  
a2.fold(10, f)  //=> f(f(10, 1), 2)  
a3.fold(10, f)  //=> f(f(f(10, 1), 2), 3)
```

example:

```
fn main() {  
    let slice = &[2, 2, 2, 2, 2];  
    let folded = slice.fold(0, |a, b| a + b);  
    assert(folded == 10);  
}
```

## reduceSame as fold, but uses the first element as the starting element.

```
fn reduce<Env>(self, f: fn[Env](T, T) -> T) -> T
```

example:

```
fn main() {  
    let slice = &[2, 2, 2, 2, 2];  
    let reduced = slice.reduce(|a, b| a + b);  
    assert(reduced == 10);  
}
```

## filterReturns a new slice containing only elements for which the given predicate returns true.

```
fn filter<Env>(self, f: fn[Env](T) -> bool) -> Self
```

example:

```
fn main() {  
    let slice = &[1, 2, 3, 4, 5];  
    let odds = slice.filter(|x| x % 2 == 1);  
    assert_eq(odds, &[1, 3, 5]);  
}
```

## joinFlatten each element in the slice into one value, separated by `separator`.

Note that although slices implement `Append`, `join` cannot be used on slice
elements since nested slices are prohibited.

```
fn join(self, separator: T) -> T where T: Append
```

example:

```
struct Accumulator {  
    total: Field,  
}  
  
// "Append" two accumulators by adding them  
impl Append for Accumulator {  
    fn empty() -> Self {  
        Self { total: 0 }  
    }  
  
    fn append(self, other: Self) -> Self {  
        Self { total: self.total + other.total }  
    }  
}  
  
fn main() {  
    let slice = &[1, 2, 3, 4, 5].map(|total| Accumulator { total });  
  
    let result = slice.join(Accumulator::empty());  
    assert_eq(result, Accumulator { total: 15 });  
  
    // We can use a non-empty separator to insert additional elements to sum:  
    let separator = Accumulator { total: 10 };  
    let result = slice.join(separator);  
    assert_eq(result, Accumulator { total: 55 });  
}
```

## allReturns true if all the elements satisfy the given predicate

```
fn all<Env>(self, predicate: fn[Env](T) -> bool) -> bool
```

example:

```
fn main() {  
    let slice = &[2, 2, 2, 2, 2];  
    let all = slice.all(|a| a == 2);  
    assert(all);  
}
```

## anyReturns true if any of the elements satisfy the given predicate

```
fn any<Env>(self, predicate: fn[Env](T) -> bool) -> bool
```

example:

```
fn main() {  
    let slice = &[2, 2, 2, 2, 5];  
    let any = slice.any(|a| a == 5);  
    assert(any);  
}
```

---


# Tuples

Source: https://noir-lang.org/docs/noir/concepts/data_types/tuples

Version: v1.0.0-beta.17

A tuple collects multiple values like an array, but with the added ability to collect values of
different types:

```
fn main() {  
    let tup: (u8, u64, Field) = (255, 500, 1000);  
}
```

One way to access tuple elements is via destructuring using pattern matching:

```
fn main() {  
    let tup = (1, 2);  
  
    let (one, two) = tup;  
  
    let three = one + two;  
}
```

Another way to access tuple elements is via direct member access, using a period (`.`) followed by
the index of the element we want to access. Index `0` corresponds to the first tuple element, `1` to
the second and so on:

```
fn main() {  
    let tup = (5, 6, 7, 8);  
  
    let five = tup.0;  
    let eight = tup.3;  
}
```

---


# Structs

Source: https://noir-lang.org/docs/noir/concepts/data_types/structs

Version: v1.0.0-beta.17

On this page

A struct also allows for grouping multiple values of different types. Unlike tuples, we can also
name each field.

> **Note:** The usage of *field* here refers to each element of the struct and is unrelated to the
> field type of Noir.

Defining a struct requires giving it a name and listing each field within as `<Key>: <Type>` pairs:

```
struct Animal {  
    hands: Field,  
    legs: Field,  
    eyes: u8,  
}
```

An instance of a struct can then be created with actual values in `<Key>: <Value>` pairs in any
order. Struct fields are accessible using their given names:

```
fn main() {  
    let legs = 4;  
  
    let dog = Animal {  
        eyes: 2,  
        hands: 0,  
        legs,  
    };  
  
    let zero = dog.hands;  
}
```

Structs can also be destructured in a pattern, binding each field to a new variable:

```
fn main() {  
    let Animal { hands, legs: feet, eyes } = get_octopus();  
  
    let ten = hands + feet + eyes as Field;  
}  
  
fn get_octopus() -> Animal {  
    let octopus = Animal {  
        hands: 0,  
        legs: 8,  
        eyes: 2,  
    };  
  
    octopus  
}
```

The new variables can be bound with names different from the original struct field names, as
showcased in the `legs --> feet` binding in the example above.

## VisibilityBy default, like functions, structs are private to the module they exist in. You can use `pub`
to make the struct public or `pub(crate)` to make it public to just its crate:

```
// This struct is now public  
pub struct Animal {  
    hands: Field,  
    legs: Field,  
    eyes: u8,  
}
```

The same applies to struct fields: by default they are private to the module they exist in,
but they can be made `pub` or `pub(crate)`:

```
// This struct is now public  
pub struct Animal {  
    hands: Field,           // private to its module  
    pub(crate) legs: Field, // accessible from the entire crate  
    pub eyes: u8,           // accessible from anywhere  
}
```

---


# References

Source: https://noir-lang.org/docs/noir/concepts/data_types/references

Version: v1.0.0-beta.17

Noir supports first-class references. References are a bit like pointers: they point to a specific address that can be followed to access the data stored at that address. You can use Rust-like syntax to use pointers in Noir: the `&` operator references the variable, the `*` operator dereferences it.

Example:

```
fn main() {  
    let mut x = 2;  
  
    // you can reference x as &mut and pass it to multiplyBy2  
    multiplyBy2(&mut x);  
}  
  
// you can access &mut here  
fn multiplyBy2(x: &mut Field) {  
    // and dereference it with *  
    *x = *x * 2;  
}
```

References do have limitations. Mutable references to array elements are not supported.

For example, the following code snippet:

```
fn foo(x: &mut u32) {  
    *x += 1;  
}  
fn main() {  
    let mut state: [u32; 4] = [1, 2, 3, 4];  
    foo(&mut state[0]);  
    assert_eq(state[0], 2); // expect:2 got:1  
}
```

Will error with the following:

```
error: Mutable references to array elements are currently unsupported  
  ┌─ src/main.nr:6:18  
  │  
6 │         foo(&mut state[0]);  
  │                  -------- Try storing the element in a fresh variable first  
  │
```

---


# Function types

Source: https://noir-lang.org/docs/noir/concepts/data_types/function_types

Version: v1.0.0-beta.17

Noir supports higher-order functions. The syntax for a function type is as follows:

```
fn(arg1_type, arg2_type, ...) -> return_type
```

Example:

```
fn assert_returns_100(f: fn() -> Field) { // f takes no args and returns a Field  
    assert(f() == 100);  
}  
  
fn main() {  
    assert_returns_100(|| 100); // ok  
    assert_returns_100(|| 150); // fails  
}
```

A function type also has an optional capture environment - this is necessary to support closures.
See [Lambdas](/docs/noir/concepts/lambdas) for more details.

---


# Type Coercions

Source: https://noir-lang.org/docs/noir/concepts/data_types/coercions

Version: v1.0.0-beta.17

When one type is required in Noir code but a different type is given, the compiler will typically issue
a type error. There are a few cases however where the compiler will instead automatically perform a
type coercion. These are typically limited to a few type pairs where converting from one to the other
will not sacrifice performance or correctness. Currently, Noir will will try to perform the following
type coercions:

| Actual Type | Expected Type |
| --- | --- |
| `[T; N]` | `[T]` |
| `fn(..) -> R` | `unconstrained fn(..) -> R` |
| `str<N>` | `CtString` |
| `fmtstr<N, T>` | `CtString` |
| `&mut T` | `&T` |

Note that:

* Conversions are only from the actual type to the expected type, never the other way around.
* Conversions are only performed on the outermost type, they're never performed within a nested type.
* `CtString` is a compile-time only type, so this conversion is only valid in [comptime code](/docs/noir/concepts/comptime).
* `&T` requires the experimental `-Zownership` flag to be enabled.

Examples:

```
fn requires_slice(_slice: [Field]) {}  
comptime fn requires_ct_string(_s: CtString) {}  
  
fn main() {  
    let array: [Field; 4] = [1, 2, 3, 4];  
  
    // Ok - array is converted to a slice  
    requires_slice(array);  
    // equivalent to:  
    requires_slice(array.as_slice());  
  
    // coerce a constrained function to an unconstrained one:  
    let f: unconstrained fn([Field]) = requires_slice;  
  
    comptime {  
        // Passing a str<6> where a CtString is expected  
        requires_ct_string("hello!")  
    }  
}
```

---


# Functions

Source: https://noir-lang.org/docs/noir/concepts/functions

Version: v1.0.0-beta.17

On this page

Functions in Noir follow the same semantics of Rust, though Noir does not support early returns.

To declare a function the `fn` keyword is used.

```
fn foo() {}
```

By default, functions are visible only within the package they are defined. To make them visible outside of that package (for example, as part of a [library](/docs/noir/modules_packages_crates/crates_and_packages#libraries)), you should mark them as `pub`:

```
pub fn foo() {}
```

You can also restrict the visibility of the function to only the crate it was defined in, by specifying `pub(crate)`:

```
pub(crate) fn foo() {}  //foo can only be called within its crate
```

All parameters in a function must have a type and all types are known at compile time. The parameter
is prepended with a colon and the parameter type. Multiple parameters are separated using a comma.

```
fn foo(x : Field, y : Field){}
```

You can use an underscore `_` as a parameter name when you don't need to use the parameter in the function body. This is useful when you need to satisfy a function signature but don't need to use all the parameters:

```
fn foo(_ : Field, y : Field) {  
    // Only using y parameter  
}
```

Alternatively, you can prefix a parameter name with an underscore (e.g. `_x`), which also indicates that the parameter is unused. This approach is often preferred as it preserves the parameter name for documentation purposes:

```
fn foo(_x : Field, y : Field) -> Field {  
    // Only using y parameter  
    y  
}
```

The return type of a function can be stated by using the `->` arrow notation. The function below
states that the foo function must return a `Field`. If the function returns no value, then the arrow
is omitted.

```
fn foo(x : Field, y : Field) -> Field {  
    x + y  
}
```

Note that a `return` keyword is unneeded in this case - the last expression in a function's body is
returned.

## Main functionIf you're writing a binary, the `main` function is the starting point of your program. You can pass all types of expressions to it, as long as they have a fixed size at compile time:

```
fn main(x : Field) // this is fine: passing a Field  
fn main(x : [Field; 2]) // this is also fine: passing a Field with known size at compile-time  
fn main(x : (Field, bool)) // 👌: passing a (Field, bool) tuple means size 2  
fn main(x : str<5>) // this is fine, as long as you pass a string of size 5  
  
fn main(x : Vec<Field>) // can't compile, has variable size  
fn main(x : [Field]) // can't compile, has variable size  
fn main(....// i think you got it by now
```

Keep in mind [tests](/docs/tooling/tests) don't differentiate between `main` and any other function. The following snippet passes tests, but won't compile or prove:

```
fn main(x : [Field]) {  
    assert(x[0] == 1);  
}  
  
#[test]  
fn test_one() {  
    main(&[1, 2]);  
}
```

```
$ nargo test  
[testing] Running 1 test functions  
[testing] Testing test_one... ok  
[testing] All tests passed  
  
$ nargo check  
The application panicked (crashed).  
Message:  Cannot have variable sized arrays as a parameter to main
```

## Call ExpressionsCalling a function in Noir is executed by using the function name and passing in the necessary
arguments.

Below we show how to call the `foo` function from the `main` function using a call expression:

```
fn main(x : Field, y : Field) {  
    let z = foo(x);  
}  
  
fn foo(x : Field) -> Field {  
    x + x  
}
```

## MethodsYou can define methods in Noir on any struct type in scope.

```
struct MyStruct {  
    foo: Field,  
    bar: Field,  
}  
  
impl MyStruct {  
    fn new(foo: Field) -> MyStruct {  
        MyStruct {  
            foo,  
            bar: 2,  
        }  
    }  
  
    fn sum(self) -> Field {  
        self.foo + self.bar  
    }  
}  
  
fn main() {  
    let s = MyStruct::new(40);  
    assert(s.sum() == 42);  
}
```

Methods are just syntactic sugar for functions, so if we wanted to we could also call `sum` as
follows:

```
assert(MyStruct::sum(s) == 42);
```

It is also possible to specialize which method is chosen depending on the [generic](/docs/noir/concepts/generics) type that is used. In this example, the `foo` function returns different values depending on its type:

```
struct Foo<T> {}  
  
impl Foo<u32> {  
    fn foo(self) -> Field { 1 }  
}  
  
impl Foo<u64> {  
    fn foo(self) -> Field { 2 }  
}  
  
fn main() {  
    let f1: Foo<u32> = Foo{};  
    let f2: Foo<u64> = Foo{};  
    assert(f1.foo() + f2.foo() == 3);  
}
```

Also note that impls with the same method name defined in them cannot overlap. For example, if we already have `foo` defined for `Foo<u32>` and `Foo<u64>` like we do above, we cannot also define `foo` in an `impl<T> Foo<T>` since it would be ambiguous which version of `foo` to choose.

```
// Including this impl in the same project as the above snippet would  
// cause an overlapping impls error  
impl<T> Foo<T> {  
    fn foo(self) -> Field { 3 }  
}
```

## LambdasLambdas are anonymous functions. They follow the syntax of Rust - `|arg1, arg2, ..., argN| return_expression`.

```
let add_50 = |val| val + 50;  
assert(add_50(100) == 150);
```

See [Lambdas](/docs/noir/concepts/lambdas) for more details.

## AttributesAttributes are metadata that can be applied to a function, using the following syntax: `#[attribute(value)]`.

See [Attributes](/docs/noir/concepts/attributes) for more details.

---


# Control Flow

Source: https://noir-lang.org/docs/noir/concepts/control_flow

Version: v1.0.0-beta.17

On this page

## If ExpressionsNoir supports `if-else` statements. The syntax is most similar to Rust's where it is not required
for the statement's conditional to be surrounded by parentheses.

```
let a = 0;  
let mut x: u32 = 0;  
  
if a == 0 {  
    if a != 0 {  
        x = 6;  
    } else {  
        x = 2;  
    }  
} else {  
    x = 5;  
    assert(x == 5);  
}  
assert(x == 2);
```

## For loops`for` loops allow you to repeat a block of code multiple times.

The following block of code between the braces is run 10 times.

```
for i in 0..10 {  
    // do something  
}
```

Alternatively, `start..=end` can be used for a range that is inclusive on both ends.

The index for loops is of type `u64`.

## Break and ContinueIn unconstrained code, `break` and `continue` are also allowed in `for` and `loop` loops. These are only allowed
in unconstrained code since normal constrained code requires that Noir knows exactly how many iterations
a loop may have. `break` and `continue` can be used like so:

```
for i in 0 .. 10 {  
    println("Iteration start")  
  
    if i == 2 {  
        continue;  
    }  
  
    if i == 5 {  
        break;  
    }  
  
    println(i);  
}  
println("Loop end")
```

When used, `break` will end the current loop early and jump to the statement after the for loop. In the example
above, the `break` will stop the loop and jump to the `println("Loop end")`.

`continue` will stop the current iteration of the loop, and jump to the start of the next iteration. In the example
above, `continue` will jump to `println("Iteration start")` when used. Note that the loop continues as normal after this.
The iteration variable `i` is still increased by one as normal when `continue` is used.

`break` and `continue` cannot currently be used to jump out of more than a single loop at a time.

## LoopsIn unconstrained code, `loop` is allowed for loops that end with a `break`.
A `loop` must contain at least one `break` statement that is reachable during execution.
This is only allowed in unconstrained code since normal constrained code requires that Noir knows exactly how many iterations
a loop may have.

```
let mut i = 10;  
loop {  
    println(i);  
    i -= 1;  
  
    if i == 0 {  
        break;  
    }  
}
```

## While loopsIn unconstrained code, `while` is allowed for loops that end when a given condition is met.
This is only allowed in unconstrained code since normal constrained code requires that Noir knows exactly how many iterations
a loop may have.

```
let mut i = 0  
while i < 10 {  
    println(i);  
    i += 2;  
}
```

---


# Logical Operations

Source: https://noir-lang.org/docs/noir/concepts/ops

Version: v1.0.0-beta.17

On this page

## Table of Supported Operations| Operation | Description | Requirements |
| --- | --- | --- |
| + | Adds two private input types together | Types must be private input |
| - | Subtracts two private input types together | Types must be private input |
| \* | Multiplies two private input types together | Types must be private input |
| / | Divides two private input types together | Types must be private input |
| % | Modulo operation | Types must be integer |
| ^ | XOR two private input types together | Types must be integer |
| & | AND two private input types together | Types must be integer |
| | | OR two private input types together | Types must be integer |
| << | Left shift an integer by another integer amount | Types must be integer |
| >> | Right shift an integer by another integer amount | Types must be integer |
| ! | Bitwise not of a value | Type must be integer or boolean |
| < | returns a bool if one value is less than the other | Upper bound must have a known bit size |
| <= | returns a bool if one value is less than or equal to the other | Upper bound must have a known bit size |
| > | returns a bool if one value is more than the other | Upper bound must have a known bit size |
| >= | returns a bool if one value is more than or equal to the other | Upper bound must have a known bit size |
| == | returns a bool if one value is equal to the other | Both types must not be constants |
| != | returns a bool if one value is not equal to the other | Both types must not be constants |

The modulo operator `%` will give an error when the right-hand side operand is zero, and will return `0` when the
right-hand side operand is `1`, or `-1`.

## Predicate Operators`<,<=, !=, == , >, >=` are known as predicate/comparison operations because they compare two values.
This differs from the operations such as `+` where the operands are used in *computation*.

## Bitwise Operations Example```
fn main(x: Field) {  
    let y = x as u32;  
    let z = y & y;  
}
```

`z` is implicitly constrained to be the result of `y & y`. The `&` operand is used to denote bitwise
`&`.

> `x & x` would not compile as `x` is a `Field` and not an integer type.

Bit shifts left: `<<`, or right: `>>` require the right hand side operand to be less that the bit size `s` of the operands type:
`x << y` or `x >> y` overflow if `x,y` are unsigned and `y >= s`
`x << y` or `x >> y` overflow if `x,y` are signed and `y >= s`

## Logical OperatorsNoir has no support for the logical operators `||` and `&&`. This is because encoding the
short-circuiting that these operators require can be inefficient for Noir's backend. Instead you can
use the bitwise operators `|` and `&` which operate identically for booleans, just without the
short-circuiting.

```
let my_val = 5;  
  
let mut flag = 1;  
if (my_val > 6) | (my_val == 0) {  
    flag = 0;  
}  
assert(flag == 1);  
  
if (my_val != 10) & (my_val < 50) {  
    flag = 0;  
}  
assert(flag == 0);
```

## Shorthand operatorsNoir shorthand operators for most of the above operators, namely `+=, -=, *=, /=, %=, &=, |=, ^=, <<=`, and `>>=`. These allow for more concise syntax. For example:

```
let mut i = 0;  
i = i + 1;
```

could be written as:

```
let mut i = 0;  
i += 1;
```

---


# Assert Function

Source: https://noir-lang.org/docs/noir/concepts/assert

Version: v1.0.0-beta.17

Noir includes a special `assert` function which will explicitly constrain the predicate/comparison
expression that follows to be true. If this expression is false at runtime, the program will fail to
be proven. As of v1.0.0-beta.2, assert statements are expressions and can be used in value contexts.

Example:

```
fn main(x : Field, y : Field) {  
    assert(x == y);  
}
```

> Assertions only work for predicate operations, such as `==`. If there's any ambiguity on the operation, the program will fail to compile. For example, it is unclear if `assert(x + y)` would check for `x + y == 0` or simply would return `true`.

You can optionally provide a message to be logged when the assertion fails:

```
assert(x == y, "x and y are not equal");
```

Aside string literals, the optional message can be a format string or any other type supported as input for Noir's [print](/docs/noir/standard_library/logging) functions. This feature lets you incorporate runtime variables into your failed assertion logs:

```
assert(x == y, f"Expected x == y, but got {x} == {y}");
```

Using a variable as an assertion message directly:

```
struct myStruct {  
  myField: Field  
}  
  
let s = myStruct { myField: y };  
assert(s.myField == x, s);
```

There is also a special `static_assert` function that behaves like `assert`,
but that runs at compile-time.

```
fn main(xs: [Field; 3]) {  
    let x = 2;  
    let y = 4;  
    static_assert(x + x == y, "expected 2 + 2 to equal 4");  
  
    // This passes since the length of `xs` is known at compile-time  
    static_assert(xs.len() == 3, "expected the input to have 3 elements");  
}
```

Like `assert`, the message can be a format string or any other type supported as input for Noir's [print](/docs/noir/standard_library/logging) functions.
This feature lets you incorporate runtime variables into your failed assertion logs:

```
static_assert(x + x == y, f"Expected 2 + 2 to equal 4 but got: {x} + {x} == {y}");
```

This function fails when passed a dynamic (run-time) argument:

```
fn main(x : Field, y : Field) {  
    // this fails because `x` is not known at compile-time  
    static_assert(x == 2, "expected x to be known at compile-time and equal to 2");  
  
    let mut example_slice = &[];  
    if y == 4 {  
        example_slice = example_slice.push_back(0);  
    }  
  
    // This fails because the length of `example_slice` is not known at  
    // compile-time  
    let error_message = "expected an empty slice, known at compile-time";  
    static_assert(example_slice.len() == 0, error_message);  
}
```

---


# Unconstrained Functions

Source: https://noir-lang.org/docs/noir/concepts/unconstrained

Version: v1.0.0-beta.17

On this page

Unconstrained functions are functions which do not constrain any of the included computation and allow for non-deterministic computation.

## Why?Zero-knowledge (ZK) domain-specific languages (DSL) enable developers to generate ZK proofs from their programs by compiling code down to the constraints of an NP complete language (such as R1CS or PLONKish languages). However, the hard bounds of a constraint system can be very limiting to the functionality of a ZK DSL.

Enabling a circuit language to perform unconstrained execution is a powerful tool. Said another way, unconstrained execution lets developers generate witnesses from code that does not generate any constraints. Being able to execute logic outside of a circuit is critical for both circuit performance and constructing proofs on information that is external to a circuit.

Fetching information from somewhere external to a circuit can also be used to enable developers to improve circuit efficiency.

A ZK DSL does not just prove computation, but proves that some computation was handled correctly. Thus, it is necessary that when we switch from performing some operation directly inside of a circuit to inside of an unconstrained environment that the appropriate constraints are still laid down elsewhere in the circuit.

## ExampleAn in depth example might help drive the point home. Let's look at how we can optimize a function to turn a `u64` into an array of `u8`s.

```
fn main(num: u64) -> pub [u8; 8] {  
    let mut out: [u8; 8] = [0; 8];  
    for i in 0..8 {  
        out[i] = (num >> (56 - (i * 8)) as u64 & 0xff) as u8;  
    }  
  
    out  
}
```

```
Total ACIR opcodes generated for language PLONKCSat { width: 3 }: 91  
Backend circuit size: 3619
```

A lot of the operations in this function are optimized away by the compiler (all the bit-shifts turn into divisions by constants). However we can save a bunch of gates by casting to u8 a bit earlier. This automatically truncates the bit-shifted value to fit in a u8 which allows us to remove the AND against 0xff. This saves us ~480 gates in total.

```
fn main(num: u72) -> pub [u8; 8] {  
    let mut out: [u8; 8] = [0; 8];  
    for i in 0..8 {  
        out[i] = (num >> (56 - (i * 8)) as u8;  
    }  
  
    out  
}
```

```
Total ACIR opcodes generated for language PLONKCSat { width: 3 }: 75  
Backend circuit size: 3143
```

Those are some nice savings already but we can do better. This code is all constrained so we're proving every step of calculating out using num, but we don't actually care about how we calculate this, just that it's correct. This is where brillig comes in.

It turns out that truncating a u72 into a u8 is hard to do inside a snark, each time we do as u8 we lay down 4 ACIR opcodes which get converted into multiple gates. It's actually much easier to calculate num from out than the other way around. All we need to do is multiply each element of out by a constant and add them all together, both relatively easy operations inside a snark.

We can then run `u72_to_u8` as unconstrained brillig code in order to calculate out, then use that result in our constrained function and assert that if we were to do the reverse calculation we'd get back num. This looks a little like the below:

```
fn main(num: u72) -> pub [u8; 8] {  
    // Safety: 'out' is properly constrained below in 'assert(num == reconstructed_num);'  
    let out = unsafe { u72_to_u8(num) };  
  
    let mut reconstructed_num: u72 = 0;  
    for i in 0..8 {  
        reconstructed_num += (out[i] as u72 << (56 - (8 * i)));  
    }  
    assert(num == reconstructed_num);  
    out  
}  
  
unconstrained fn u72_to_u8(num: u72) -> [u8; 8] {  
    let mut out: [u8; 8] = [0; 8];  
    for i in 0..8 {  
        out[i] = (num >> (56 - (i * 8))) as u8;  
    }  
    out  
}
```

```
Total ACIR opcodes generated for language PLONKCSat { width: 3 }: 78  
Backend circuit size: 2902
```

This ends up taking off another ~250 gates from our circuit! We've ended up with more ACIR opcodes than before but they're easier for the backend to prove (resulting in fewer gates).

Note that in order to invoke unconstrained functions we need to wrap them in an `unsafe` block,
to make it clear that the call is unconstrained.
Furthermore, a warning is emitted unless the `unsafe` block is commented with a `// Safety: ...` comment explaining why it is fine to call the unconstrained function. Note that either the `unsafe` block can be commented this way or the statement it exists in (like in the `let` example above).

Generally we want to use brillig whenever there's something that's easy to verify but hard to compute within the circuit. For example, if you wanted to calculate a square root of a number it'll be a much better idea to calculate this in brillig and then assert that if you square the result you get back your number.

## Break and ContinueIn addition to loops over runtime bounds, `break` and `continue` are also available in unconstrained code. See [break and continue](/docs/noir/concepts/control_flow#break-and-continue)

## Security checksTwo compilation security passes exist currently to ensure soundness of compiled code. Problems they catch are reported as "bugs" (as opposed to errors) in the compiler output. For example:

```
**bug**: Brillig function call isn't properly covered by a manual constraint
```

## Independent subgraph detectionThis pass examines the instruction flow graph to see if the final function would involve values that don't come from any provided inputs and don't result in the outputs. That would mean there are no constraints ensuring the required continuity.

This check is enabled by default and can be disabled by passing the `--skip-underconstrained-check` option to `nargo`.

## Brillig manual constraint coverageThe results of a Brillig function call must be constrained to ensure security, adhering to these rules: every resulting value (including every array element of a resulting array) has to be involved in a later constraint (i.e. assert, range check) against either one of the arguments of the call, or a constant. In this context, involvement means that a descendant value (e.g. a result of a chain of operations over the value) of a result has to be checked against a descendant value of an argument. For example:

```
unconstrained fn factor(v0: Field) -> [Field; 2] {  
    ...  
}  
  
fn main f0 (foo: Field) -> [Field; 2] {  
    let factored = unsafe { factor(foo) };  
    assert(factored[0] * factored[1] == foo);  
    return factored  
}
```

Here, the results of `factor` are two elements of the returned array. The value `factored[0] * factored[1]` is a descendant of both of them, so both are involved in a constraint against the argument value in the `assert`. Hence, the call to an unconstrained function is properly covered.

This pass checks if the constraint coverage of Brillig calls is sufficient in these terms.

The check is enabled by default and can be disabled by passing the `--skip-brillig-constraints-check` option to `nargo`.

## Lookback optionCertain false positives of this check can be avoided by providing the `--enable-brillig-constraints-check-lookback` option to `nargo`, which can be slower at compile-time but additionally ensures that descendants of call argument values coming from operations *preceding* the call itself would be followed. For example, consider this case:

```
unconstrained fn unconstrained_add(v0: Field, v1: Field) -> Field {  
    v0 + v1  
}  
  
fn main f0 (v0: Field, v1: Field) {  
    let foo = v0 + v1;  
    let bar = unsafe { unconstrained_add(v0, v1) };  
    assert(foo == bar);  
    return bar  
}
```

Normally, the addition operation over `v0` and `v1` happening before the call itself would prevent the call from being (correctly) considered properly constrained. With this option enabled, the false positive goes away at the cost of the check becoming somewhat less performant on large unrolled loops.

---


# Oracles

Source: https://noir-lang.org/docs/noir/concepts/oracles

Version: v1.0.0-beta.17

Experimental Feature

This feature is experimental. The documentation may be incomplete or out of date, which means it could change in future versions, potentially causing unexpected behavior or not working as expected.

**Contributions Welcome:** If you notice any inaccuracies or potential improvements, please consider contributing. Visit our GitHub repository to make your contributions: [Contribute Here](https://github.com/noir-lang/noir).

Noir has support for Oracles via RPC calls. This means Noir will make an RPC call and use the return value for proof generation.

Since Oracles are not resolved by Noir, they are [`unconstrained` functions](/docs/noir/concepts/unconstrained)

You can declare an Oracle through the `#[oracle(<name>)]` flag. Example:

```
#[oracle(get_number_sequence)]  
unconstrained fn get_number_sequence(_size: Field) -> [Field] {}
```

The timeout for when using an external RPC oracle resolver can be set with the `NARGO_FOREIGN_CALL_TIMEOUT` environment variable. This timeout is in units of milliseconds.

---


# Generics

Source: https://noir-lang.org/docs/noir/concepts/generics

Version: v1.0.0-beta.17

On this page

Generics allow you to use the same functions with multiple different concrete data types. You can
read more about the concept of generics in the Rust documentation
[here](https://doc.rust-lang.org/book/ch10-01-syntax.html).

Here is a trivial example showing the identity function that supports any type. In Rust, it is
common to refer to the most general type as `T`. We follow the same convention in Noir.

```
fn id<T>(x: T) -> T  {  
    x  
}
```

## Numeric GenericsIf we want to be generic over array lengths (which are type-level integers), we can use numeric
generics. Using these looks similar to using regular generics, but introducing them into scope
requires declaring them with `let MyGenericName: IntegerType`. This can be done anywhere a normal
generic is declared. Instead of types, these generics resolve to integers at compile-time.
Here's an example of a struct that is generic over the size of the array it contains internally:

```
struct BigInt<let N: u32> {  
    limbs: [u32; N],  
}  
  
impl<let N: u32> BigInt<N> {  
    // `N` is in scope of all methods in the impl  
    fn first(first: BigInt<N>, second: BigInt<N>) -> Self {  
        assert(first.limbs != second.limbs);  
        first  
    }  
  
    fn second(first: BigInt<N>, second: Self) -> Self {  
        assert(first.limbs != second.limbs);  
        second  
    }  
}
```

## In StructsGenerics are useful for specifying types in structs. For example, we can specify that a field in a
struct will be of a certain generic type. In this case `value` is of type `T`.

```
struct RepeatedValue<T> {  
    value: T,  
    count: u32,  
}  
  
impl<T> RepeatedValue<T> {  
    fn print(self) {  
        for _i in 0 .. self.count {  
            println(self.value);  
        }  
    }  
}  
  
fn main() {  
    let repeated = RepeatedValue { value: "Hello!", count: 2 };  
    repeated.print();  
}
```

The `print` function will print `Hello!` an arbitrary number of times, twice in this case.

## Calling functions on generic parametersSince a generic type `T` can represent any type, how can we call functions on the underlying type?
In other words, how can we go from "any type `T`" to "any type `T` that has certain methods available?"

This is what [traits](/docs/noir/concepts/traits) are for in Noir. Here's an example of a function generic over
any type `T` that implements the `Eq` trait for equality:

```
fn first_element_is_equal<T, let N: u32>(array1: [T; N], array2: [T; N]) -> bool   
    where T: Eq  
{  
    if (array1.len() == 0) | (array2.len() == 0) {  
        true  
    } else {  
        array1[0] == array2[0]  
    }  
}  
  
fn main() {  
    assert(first_element_is_equal([1, 2, 3], [1, 5, 6]));  
  
    // We can use first_element_is_equal for arrays of any type  
    // as long as we have an Eq impl for the types we pass in  
    let array = [MyStruct::new(), MyStruct::new()];  
    assert(first_element_is_equal(array, array));  
}  
  
struct MyStruct {  
    foo: Field  
}  
  
impl MyStruct {  
    fn new() -> Self {  
        MyStruct { foo: 0 }  
    }  
}  
  
impl Eq for MyStruct {  
    fn eq(self, other: MyStruct) -> bool {  
        self.foo == other.foo  
    }  
}
```

You can find more details on traits and trait implementations on the [traits page](/docs/noir/concepts/traits).

## Manually Specifying Generics with the Turbofish OperatorThere are times when the compiler cannot reasonably infer what type should be used for a generic, or when the developer themselves may want to manually distinguish generic type parameters. This is where the `::<>` turbofish operator comes into play.

The `::<>` operator can follow a variable or path and can be used to manually specify generic arguments within the angle brackets.
The name "turbofish" comes from that `::<>` looks like a little fish.

Examples:

```
fn main() {  
    let mut slice = [];  
    slice = slice.push_back(1);  
    slice = slice.push_back(2);  
    // Without turbofish a type annotation would be needed on the left hand side  
    let array = slice.as_array::<2>();  
}
```

```
trait MyTrait {  
    fn ten() -> Self;  
}  
  
impl MyTrait for Field {  
    fn ten() -> Self { 10 }  
}  
  
struct Foo<T> {  
    inner: T  
}  
          
impl<T> Foo<T> {  
    fn generic_method<U>(_self: Self) -> U where U: MyTrait {  
        U::ten()  
    }  
}  
          
fn example() {  
    let foo: Foo<Field> = Foo { inner: 1 };  
    // Using a type other than `Field` here (e.g. u32) would fail as   
    // there is no matching impl for `u32: MyTrait`.   
    //  
    // Substituting the `10` on the left hand side of this assert  
    // with `10 as u32` would fail with a type mismatch as we   
    // are expecting a `Field` from the right hand side.  
    assert(10 == foo.generic_method::<Field>());  
}
```

## Arithmetic GenericsIn addition to numeric generics, Noir also allows a limited form of arithmetic on generics.
When you have a numeric generic such as `N`, you can use the following operators on it in a
type position: `+`, `-`, `*`, `/`, and `%`.

Note that type checking arithmetic generics is a best effort guess from the compiler and there
are many cases of types that are equal that the compiler may not see as such. For example,
we know that `T * (N + M)` should be equal to `T*N + T*M` but the compiler does not currently
apply the distributive law and thus sees these as different types.

Even with this limitation though, the compiler can handle common cases decently well:

```
trait Serialize<let N: u32> {  
    fn serialize(self) -> [Field; N];  
}  
  
impl Serialize<1> for Field {  
    fn serialize(self) -> [Field; 1] {  
        [self]  
    }  
}  
  
impl<T, let N: u32, let M: u32> Serialize<N * M> for [T; N]  
    where T: Serialize<M> { .. }  
  
impl<T, U, let N: u32, let M: u32> Serialize<N + M> for (T, U)  
    where T: Serialize<N>, U: Serialize<M> { .. }  
  
fn main() {  
    let data = (1, [2, 3, 4]);  
    assert_eq(data.serialize().len(), 4);  
}
```

Note that if there is any over or underflow the types will fail to unify:

underflow-example

```
fn pop<let N: u32>(array: [Field; N]) -> [Field; N - 1] {  
    let mut result: [Field; N - 1] = std::mem::zeroed();  
    for i in 0..N - 1 {  
        result[i] = array[i];  
    }  
    result  
}  
  
fn main() {  
    // error: Could not determine array length `(0 - 1)`  
    pop([]);  
}
```

> [Source code: test\_programs/compile\_failure/arithmetic\_generics\_underflow/src/main.nr#L1-L14](https://github.com/noir-lang/noir/blob/master/test_programs/compile_failure/arithmetic_generics_underflow/src/main.nr#L1-L14)

This also applies if there is underflow in an intermediate calculation:

intermediate-underflow-example

```
fn main() {  
    // From main it looks like there's nothing sketchy going on  
    seems_fine([]);  
}  
  
// Since `seems_fine` says it can receive and return any length N  
fn seems_fine<let N: u32>(array: [Field; N]) -> [Field; N] {  
    // But inside `seems_fine` we pop from the array which  
    // requires the length to be greater than zero.  
  
    // error: Could not determine array length `(0 - 1)`  
    push_zero(pop(array))  
}  
  
fn pop<let N: u32>(array: [Field; N]) -> [Field; N - 1] {  
    let mut result: [Field; N - 1] = std::mem::zeroed();  
    for i in 0..N - 1 {  
        result[i] = array[i];  
    }  
    result  
}  
  
fn push_zero<let N: u32>(array: [Field; N]) -> [Field; N + 1] {  
    let mut result: [Field; N + 1] = std::mem::zeroed();  
    for i in 0..N {  
        result[i] = array[i];  
    }  
    // index N is already zeroed  
    result  
}
```

> [Source code: test\_programs/compile\_failure/arithmetic\_generics\_intermediate\_underflow/src/main.nr#L1-L32](https://github.com/noir-lang/noir/blob/master/test_programs/compile_failure/arithmetic_generics_intermediate_underflow/src/main.nr#L1-L32)

---


# Global Variables

Source: https://noir-lang.org/docs/noir/concepts/globals

Version: v1.0.0-beta.17

On this page

## GlobalsNoir supports global variables. The global's type must be specified by the user:

```
global N: Field = 5;  
  
global TUPLE: (Field, Field) = (3, 2);  
  
fn main() {  
    assert(N == 5);  
    assert(N == TUPLE.0 + TUPLE.1);  
}
```

info

Globals can be defined as any expression, so long as they don't depend on themselves - otherwise there would be a dependency cycle! For example:

```
global T: u32 = foo(T); // dependency error
```

If they are initialized to a literal integer, globals can be used to specify an array's length:

```
global N: u32 = 2;  
  
fn main(y : [Field; N]) {  
    assert(y[0] == y[1])  
}
```

A global from another module can be imported or referenced externally like any other name:

```
global N: Field = 20;  
  
fn main() {  
    assert(my_submodule::N != N);  
}  
  
mod my_submodule {  
    global N: Field = 10;  
}
```

When a global is used, Noir replaces the name with its definition on each occurrence.
This means globals defined using function calls will repeat the call each time they're used:

```
global RESULT: [Field; 100] = foo();  
  
fn foo() -> [Field; 100] { ... }
```

This is usually fine since Noir will generally optimize any function call that does not
refer to a program input into a constant. It should be kept in mind however, if the called
function performs side-effects like `println`, as these will still occur on each use.

## VisibilityBy default, like functions, globals are private to the module they exist in. You can use `pub`
to make the global public or `pub(crate)` to make it public to just its crate:

```
// This global is now public  
pub global N: u32 = 5;
```

---


# Mutability

Source: https://noir-lang.org/docs/noir/concepts/mutability

Version: v1.0.0-beta.17

On this page

Variables in noir can be declared mutable via the `mut` keyword. Mutable variables can be reassigned
to via an assignment expression.

```
let x = 2;  
x = 3; // error: x must be mutable to be assigned to  
  
let mut y = 3;  
let y = 4; // OK
```

The `mut` modifier can also apply to patterns:

```
let (a, mut b) = (1, 2);  
a = 11; // error: a must be mutable to be assigned to  
b = 12; // OK  
  
let mut (c, d) = (3, 4);  
c = 13; // OK  
d = 14; // OK  
  
// etc.  
let MyStruct { x: mut y } = MyStruct { x: a };  
// y is now in scope
```

Note that mutability in noir is local and everything is passed by value, so if a called function
mutates its parameters then the parent function will keep the old value of the parameters.

```
fn main() -> pub Field {  
    let x = 3;  
    helper(x);  
    x // x is still 3  
}  
  
fn helper(mut x: i32) {  
    x = 4;  
}
```

## Non-local mutabilityNon-local mutability can be achieved through the [mutable reference type `&mut T`](/docs/noir/concepts/data_types/references):

```
fn set_to_zero(x: &mut Field) {  
    *x = 0;  
}  
  
fn main() {  
    let mut y = 42;  
    set_to_zero(&mut y);  
    assert(*y == 0);  
}
```

When creating a mutable reference, the original variable being referred to (`y` in this
example) must also be mutable. Since mutable references are a reference type, they must
be explicitly dereferenced via `*` to retrieve the underlying value. Note that this yields
a copy of the value, so mutating this copy will not change the original value behind the
reference:

```
fn main() {  
    let mut x = 1;  
    let x_ref = &mut x;  
  
    let mut y = *x_ref;  
    let y_ref = &mut y;  
  
    x = 2;  
    *x_ref = 3;  
  
    y = 4;  
    *y_ref = 5;  
  
    assert(x == 3);  
    assert(*x_ref == 3);  
    assert(y == 5);  
    assert(*y_ref == 5);  
}
```

Note that types in Noir are actually deeply immutable so the copy that occurs when
dereferencing is only a conceptual copy - no additional constraints will occur.

Mutable references can also be stored within structs. Note that there is also
no lifetime parameter on these unlike rust. This is because the allocated memory
always lasts the entire program - as if it were an array of one element.

```
struct Foo {  
    x: &mut Field  
}  
  
impl Foo {  
    fn incr(mut self) {  
        *self.x += 1;  
    }  
}  
  
fn main() {  
    let foo = Foo { x: &mut 0 };  
    foo.incr();  
    assert(*foo.x == 1);  
}
```

In general, you should avoid non-local & shared mutability unless it is needed. Sticking
to only local mutability will improve readability and potentially improve compiler optimizations as well.

---


# Lambdas

Source: https://noir-lang.org/docs/noir/concepts/lambdas

Version: v1.0.0-beta.17

On this page

## IntroductionLambdas are anonymous functions. The syntax is `|arg1, arg2, ..., argN| return_expression`.

```
let add_50 = |val| val + 50;  
assert(add_50(100) == 150);
```

A block can be used as the body of a lambda, allowing you to declare local variables inside it:

```
let cool = || {  
  let x = 100;  
  let y = 100;  
  x + y  
}  
  
assert(cool() == 200);
```

## ClosuresInside the body of a lambda, you can use variables defined in the enclosing function. Such lambdas are called **closures**. In this example `x` is defined inside `main` and is accessed from within the lambda:

```
fn main() {  
  let x = 100;  
  let closure = || x + 150;  
  assert(closure() == 250);  
}
```

## Passing closures to higher-order functionsIt may catch you by surprise that the following code fails to compile:

```
fn foo(f: fn () -> Field) -> Field {  
 f()  
}  
  
fn main() {  
  let (x, y) = (50, 50);  
  assert(foo(|| x + y) == 100); // error :(  
}
```

The reason is that the closure's capture environment affects its type - we have a closure that captures two Fields and `foo`
expects a regular function as an argument - those are incompatible.

note

Variables contained within the `||` are the closure's parameters, and the expression that follows it is the closure's body. The capture environment is comprised of any variables used in the closure's body that are not parameters.

E.g. in |x| x + y, y would be a captured variable, but x would not be, since it is a parameter of the closure.

The syntax for the type of a closure is `fn[env](args) -> ret_type`, where `env` is the capture environment of the closure -
in this example that's `(Field, Field)`.

The best solution in our case is to make `foo` generic over the environment type of its parameter, so that it can be called
with closures with any environment, as well as with regular functions:

```
fn foo<Env>(f: fn[Env]() -> Field) -> Field {  
 f()  
}  
  
fn main() {  
  let (x, y) = (50, 50);  
  assert(foo(|| x + y) == 100); // compiles fine  
  assert(foo(|| 60) == 60);     // compiles fine  
}
```

---


# Comments

Source: https://noir-lang.org/docs/noir/concepts/comments

Version: v1.0.0-beta.17

A comment is a line in your codebase which the compiler ignores, however it can be read by
programmers.

Here is a single line comment:

```
// This is a comment and is ignored
```

`//` is used to tell the compiler to ignore the rest of the line.

Noir also supports multi-line block comments. Start a block comment with `/*` and end the block with `*/`.

Noir does not natively support doc comments. You may be able to use [Rust doc comments](https://doc.rust-lang.org/reference/comments.html) in your code to leverage some Rust documentation build tools with Noir code.

```
/*  
  This is a block comment describing a complex function.  
*/  
fn main(x : Field, y : pub Field) {  
    assert(x != y);  
}
```

---


# Shadowing

Source: https://noir-lang.org/docs/noir/concepts/shadowing

Version: v1.0.0-beta.17

On this page

Noir allows for inheriting variables' values and re-declaring them with the same name similar to Rust, known as shadowing.

For example, the following function is valid in Noir:

```
fn main() {  
    let x = 5;  
  
    {  
        let x = x * 2;  
        assert (x == 10);  
    }  
  
    assert (x == 5);  
}
```

In this example, a variable x is first defined with the value 5.

The local scope that follows shadows the original x, i.e. creates a local mutable x based on the value of the original x. It is given a value of 2 times the original x.

When we return to the main scope, x once again refers to just the original x, which stays at the value of 5.

## Temporal mutabilityOne way that shadowing is useful, in addition to ergonomics across scopes, is for temporarily mutating variables.

```
fn main() {  
    let age = 30;  
    // age = age + 5; // Would error as `age` is immutable by default.  
  
    let mut age = age + 5; // Temporarily mutates `age` with a new value.  
  
    let age = age; // Locks `age`'s mutability again.  
  
    assert (age == 35);  
}
```

---


# Data Bus

Source: https://noir-lang.org/docs/noir/concepts/data_bus

Version: v1.0.0-beta.17

On this page

Experimental Feature

This feature is experimental. The documentation may be incomplete or out of date, which means it could change in future versions, potentially causing unexpected behavior or not working as expected.

**Contributions Welcome:** If you notice any inaccuracies or potential improvements, please consider contributing. Visit our GitHub repository to make your contributions: [Contribute Here](https://github.com/noir-lang/noir).

The data bus is an optimization that the backend can use to make recursion more efficient.
In order to use it, you must define some inputs of the program entry points (usually the `main()`
function) with the `call_data` modifier, and the return values with the `return_data` modifier.
These modifiers are incompatible with `pub` and `mut` modifiers.

## Example```
fn main(mut x: u32, y: call_data u32, z: call_data [u32;4] ) -> return_data u32 {  
  let a = z[x];  
  a+y  
}
```

As a result, both call\_data and return\_data will be treated as private inputs and encapsulated into a read-only array each, for the backend to process.

---


# Traits

Source: https://noir-lang.org/docs/noir/concepts/traits

Version: v1.0.0-beta.17

On this page

## OverviewTraits in Noir are a useful abstraction similar to interfaces or protocols in other languages. Each trait defines
the interface of several methods contained within the trait. Types can then implement this trait by providing
implementations for these methods. For example in the program:

```
struct Rectangle {  
    width: Field,  
    height: Field,  
}  
  
impl Rectangle {  
    fn area(self) -> Field {  
        self.width * self.height  
    }  
}  
  
fn log_area(r: Rectangle) {  
    println(r.area());  
}
```

We have a function `log_area` to log the area of a `Rectangle`. Now how should we change the program if we want this
function to work on `Triangle`s as well?:

```
struct Triangle {  
    width: Field,  
    height: Field,  
}  
  
impl Triangle {  
    fn area(self) -> Field {  
        self.width * self.height / 2  
    }  
}
```

Making `log_area` generic over all types `T` would be invalid since not all types have an `area` method. Instead, we can
introduce a new `Area` trait and make `log_area` generic over all types `T` that implement `Area`:

```
trait Area {  
    fn area(self) -> Field;  
}  
  
fn log_area<T>(shape: T) where T: Area {  
    println(shape.area());  
}
```

We also need to explicitly implement `Area` for `Rectangle` and `Triangle`. We can do that by changing their existing
impls slightly. Note that the parameter types and return type of each of our `area` methods must match those defined
by the `Area` trait.

```
impl Area for Rectangle {  
    fn area(self) -> Field {  
        self.width * self.height  
    }  
}  
  
impl Area for Triangle {  
    fn area(self) -> Field {  
        self.width * self.height / 2  
    }  
}
```

Now we have a working program that is generic over any type of Shape that is used! Others can even use this program
as a library with their own types - such as `Circle` - as long as they also implement `Area` for these types.

## Where ClausesAs seen in `log_area` above, when we want to create a function or method that is generic over any type that implements
a trait, we can add a where clause to the generic function.

```
fn log_area<T>(shape: T) where T: Area {  
    println(shape.area());  
}
```

It is also possible to apply multiple trait constraints on the same variable at once by combining traits with the `+`
operator. Similarly, we can have multiple trait constraints by separating each with a comma:

```
fn foo<T, U>(elements: [T], thing: U) where  
    T: Default + Add + Eq,  
    U: Bar,  
{  
    let mut sum = T::default();  
  
    for element in elements {  
        sum += element;  
    }  
  
    if sum == T::default() {  
        thing.bar();  
    }  
}
```

## Trait boundsA shorter syntax for specifying trait bounds directly on generic types is available. For example, this code:

```
fn log_area<T>(shape: T) where T: Area {  
    println(shape.area());  
}
```

can also be written like this:

```
fn log_area<T: Area>(shape: T) {  
    println(shape.area());  
}
```

Both are equivalent. Using `where` is preferable when there are many trait bounds and it's clearer to have
them separate from the types the are applying bounds to.

## Invoking trait methodsAs seen in the previous section, the `area` method was invoked on a type `T` that had a where clause `T: Area`.

To invoke `area` on a type that directly implements the trait `Area`, the trait must be in scope (imported):

```
use geometry::Rectangle;  
  
fn main() {  
    let rectangle = Rectangle { width: 1, height: 2};  
    let area = rectangle.area(); // Error: the compiler doesn't know which `area` method this is  
}
```

The above program errors because there might be multiple traits with an `area` method, all implemented
by `Rectangle`, and it's not clear which one should be used.

To make the above program compile, the trait must be imported:

```
use geometry::Rectangle;  
use geometry::Area; // Bring the Area trait into scope  
  
fn main() {  
    let rectangle = Rectangle { width: 1, height: 2};  
    let area = rectangle.area(); // OK: will use `area` from `geometry::Area`  
}
```

An error will also be produced if multiple traits with an `area` method are in scope. If both traits
are needed in a file you can use the fully-qualified path to the trait:

```
use geometry::Rectangle;  
  
fn main() {  
    let rectangle = Rectangle { width: 1, height: 2};  
    let area = geometry::Area::area(rectangle);  
}
```

## As Trait SyntaxRarely to call a method it may not be sufficient to use the general method call syntax of `obj.method(args)`.
One case where this may happen is if there are two traits in scope which both define a method with the same name.
For example:

```
trait Foo  { fn bar(); }  
trait Foo2 { fn bar(); }  
  
fn example<T>()  
    where T: Foo + Foo2  
{  
    // How to call Foo::bar and Foo2::bar?  
}
```

In the above example we have both `Foo` and `Foo2` which define a `bar` method. The normal way to resolve
this would be to use the static method syntax `Foo::bar(object)` but there is no object in this case and
`Self` does not appear in the type signature of `bar` at all so we would not know which impl to choose.
For these situations there is the "as trait" syntax: `<Type as Trait>::method(object, args...)`

```
fn example<T>()  
    where T: Foo + Foo2  
{  
    <T as Foo>::bar();  
    <T as Foo2>::bar();  
}
```

## Generic ImplementationsYou can add generics to a trait implementation by adding the generic list after the `impl` keyword:

```
trait Second {  
    fn second(self) -> Field;  
}  
  
impl<T> Second for (T, Field) {  
    fn second(self) -> Field {  
        self.1  
    }  
}
```

You can also implement a trait for every type this way:

```
trait Debug {  
    fn debug(self);  
}  
  
impl<T> Debug for T {  
    fn debug(self) {  
        println(self);  
    }  
}  
  
fn main() {  
    1.debug();  
}
```

## Generic Trait Implementations With Where ClausesWhere clauses can be placed on trait implementations themselves to restrict generics in a similar way.
For example, while `impl<T> Foo for T` implements the trait `Foo` for every type, `impl<T> Foo for T where T: Bar`
will implement `Foo` only for types that also implement `Bar`. This is often used for implementing generic types.
For example, here is the implementation for array equality:

```
impl<T, let N: u32> Eq for [T; let N: u32] where T: Eq {  
    // Test if two arrays have the same elements.  
    // Because both arrays must have length N, we know their lengths already match.  
    fn eq(self, other: Self) -> bool {  
        let mut result = true;  
  
        for i in 0 .. self.len() {  
            // The T: Eq constraint is needed to call == on the array elements here  
            result &= self[i] == other[i];  
        }  
  
        result  
    }  
}
```

Where clauses can also be placed on struct implementations.
For example, here is a method utilizing a generic type that implements the equality trait.

```
struct Foo<T> {  
    a: u32,  
    b: T,  
}  
  
impl<T> Foo<T> where T: Eq {  
    fn eq(self, other: Self) -> bool {  
        (self.a == other.a) & self.b.eq(other.b)  
    }  
}
```

## Generic TraitsTraits themselves can also be generic by placing the generic arguments after the trait name. These generics are in
scope of every item within the trait.

```
trait Into<T> {  
    // Convert `self` to type `T`  
    fn into(self) -> T;  
}
```

When implementing generic traits the generic arguments of the trait must be specified. This is also true anytime
when referencing a generic trait (e.g. in a `where` clause).

```
struct MyStruct {  
    array: [Field; 2],  
}  
  
impl Into<[Field; 2]> for MyStruct {  
    fn into(self) -> [Field; 2] {  
        self.array  
    }  
}  
  
fn as_array<T>(x: T) -> [Field; 2]  
    where T: Into<[Field; 2]>  
{  
    x.into()  
}  
  
fn main() {  
    let array = [1, 2];  
    let my_struct = MyStruct { array };  
  
    assert_eq(as_array(my_struct), array);  
}
```

## Associated Types and ConstantsTraits also support associated types and constraints which can be thought of as additional generics that are referred to by name.

Here's an example of a trait with an associated type `Foo` and a constant `Bar`:

```
trait MyTrait {  
    type Foo;  
  
    let Bar: u32;  
}
```

Now when we're implementing `MyTrait` we also have to provide values for `Foo` and `Bar`:

```
impl MyTrait for Field {  
    type Foo = i32;  
  
    let Bar: u32 = 11;  
}
```

Since associated constants can also be used in a type position, its values are limited to only other
expression kinds allowed in numeric generics.

When writing a trait constraint, you can specify all associated types and constants explicitly if
you wish:

```
fn foo<T>(x: T) where T: MyTrait<Foo = i32, Bar = 11> {  
    ...  
}
```

Or you can also elide them since there should only be one `Foo` and `Bar` for a given implementation
of `MyTrait` for a type:

```
fn foo<T>(x: T) where T: MyTrait {  
    ...  
}
```

If you elide associated types, you can still refer to them via the type as trait syntax `<T as MyTrait>`:

```
fn foo<T>(x: T) where  
    T: MyTrait,  
    <T as MyTrait>::Foo: Default + Eq  
{  
    let foo_value: <T as MyTrait>::Foo = Default::default();  
    assert_eq(foo_value, foo_value);  
}
```

## Trait Methods With No `self`A trait can contain any number of methods, each of which have access to the `Self` type which represents each type
that eventually implements the trait. Similarly, the `self` variable is available as well but is not required to be used.
For example, we can define a trait to create a default value for a type. This trait will need to return the `Self` type
but doesn't need to take any parameters:

```
trait Default {  
    fn default() -> Self;  
}
```

Implementing this trait can be done similarly to any other trait:

```
impl Default for Field {  
    fn default() -> Field {  
        0  
    }  
}  
  
struct MyType {}  
  
impl Default for MyType {  
    fn default() -> Field {  
        MyType {}  
    }  
}
```

However, since there is no `self` parameter, we cannot call it via the method call syntax `object.method()`.
Instead, we'll need to refer to the function directly. This can be done either by referring to the
specific impl `MyType::default()` or referring to the trait itself `Default::default()`. In the later
case, type inference determines the impl that is selected.

```
let my_struct = MyStruct::default();  
  
let x: u64 = Default::default();  
let result = x + Default::default();
```

## Default Method ImplementationsA trait can also have default implementations of its methods by giving a body to the desired functions.
Note that this body must be valid for all types that may implement the trait. As a result, the only
valid operations on `self` will be operations valid for any type or other operations on the trait itself.

```
trait Numeric {  
    fn add(self, other: Self) -> Self;  
  
    // Default implementation of double is (self + self)  
    fn double(self) -> Self {  
        self.add(self)  
    }  
}
```

When implementing a trait with default functions, a type may choose to implement only the required functions:

```
impl Numeric for Field {  
    fn add(self, other: Field) -> Field {  
        self + other  
    }  
}
```

Or it may implement the optional methods as well:

```
impl Numeric for u32 {  
    fn add(self, other: u32) -> u32 {  
        self + other  
    }  
  
    fn double(self) -> u32 {  
        self * 2  
    }  
}
```

## Impl SpecializationWhen implementing traits for a generic type it is possible to implement the trait for only a certain combination
of generics. This can be either as an optimization or because those specific generics are required to implement the trait.

```
trait Sub {  
    fn sub(self, other: Self) -> Self;  
}  
  
struct NonZero<T> {  
    value: T,  
}  
  
impl Sub for NonZero<Field> {  
    fn sub(self, other: Self) -> Self {  
        let value = self.value - other.value;  
        assert(value != 0);  
        NonZero { value }  
    }  
}
```

## Overlapping ImplementationsOverlapping implementations are disallowed by Noir to ensure Noir's decision on which impl to select is never ambiguous.
This means if a trait `Foo` is already implemented
by a type `Bar<T>` for all `T`, then we cannot also have a separate impl for `Bar<Field>` (or any other
type argument). Similarly, if there is an impl for all `T` such as `impl<T> Debug for T`, we cannot create
any more impls to `Debug` for other types since it would be ambiguous which impl to choose for any given
method call.

```
trait Trait {}  
  
// Previous impl defined here  
impl<A, B> Trait for (A, B) {}  
  
// error: Impl for type `(Field, Field)` overlaps with existing impl  
impl Trait for (Field, Field) {}
```

## Trait CoherenceAnother restriction on trait implementations is coherence. This restriction ensures other crates cannot create
impls that may overlap with other impls, even if several unrelated crates are used as dependencies in the same
program.

The coherence restriction is: to implement a trait, either the trait itself or the object type must be declared
in the crate the impl is in.

In practice this often comes up when using types provided by libraries. If a library provides a type `Foo` that does
not implement a trait in the standard library such as `Default`, you may not `impl Default for Foo` in your own crate.
While restrictive, this prevents later issues or silent changes in the program if the `Foo` library later added its
own impl for `Default`. If you are a user of the `Foo` library in this scenario and need a trait not implemented by the
library your choices are to either submit a patch to the library or use the newtype pattern.

## The Newtype PatternThe newtype pattern gets around the coherence restriction by creating a new wrapper type around the library type
that we cannot create `impl`s for. Since the new wrapper type is defined in our current crate, we can create
impls for any trait we need on it.

```
struct Wrapper {  
    foo: some_library::Foo,  
}  
  
impl Default for Wrapper {  
    fn default() -> Wrapper {  
        Wrapper {  
            foo: some_library::Foo::new(),  
        }  
    }  
}
```

Since we have an impl for our own type, the behavior of this code will not change even if `some_library` is updated
to provide its own `impl Default for Foo`. The downside of this pattern is that it requires extra wrapping and
unwrapping of values when converting to and from the `Wrapper` and `Foo` types.

## Trait InheritanceSometimes, you might need one trait to use another trait’s functionality (like "inheritance" in some other languages). In this case, you can specify this relationship by listing any child traits after the parent trait's name and a colon. Now, whenever the parent trait is implemented it will require the child traits to be implemented as well. A parent trait is also called a "super trait."

```
trait Person {  
    fn name(self) -> String;  
}  
  
// Person is a supertrait of Student.  
// Implementing Student requires you to also impl Person.  
trait Student: Person {  
    fn university(self) -> String;  
}  
  
trait Programmer {  
    fn fav_language(self) -> String;  
}  
  
// CompSciStudent (computer science student) is a subtrait of both Programmer  
// and Student. Implementing CompSciStudent requires you to impl both supertraits.  
trait CompSciStudent: Programmer + Student {  
    fn git_username(self) -> String;  
}
```

## Trait AliasesSimilar to the proposed Rust feature for [trait aliases](https://github.com/rust-lang/rust/blob/4d215e2426d52ca8d1af166d5f6b5e172afbff67/src/doc/unstable-book/src/language-features/trait-alias.md),
Noir supports aliasing one or more traits and using those aliases wherever
traits would normally be used.

```
trait Foo {  
    fn foo(self) -> Self;  
}  
  
trait Bar {  
    fn bar(self) -> Self;  
}  
  
// Equivalent to:  
// trait Baz: Foo + Bar {}  
//  
// impl<T> Baz for T where T: Foo + Bar {}  
trait Baz = Foo + Bar;  
  
// We can use `Baz` to refer to `Foo + Bar`  
fn baz<T>(x: T) -> T where T: Baz {  
    x.foo().bar()  
}
```

## Generic Trait AliasesTrait aliases can also be generic by placing the generic arguments after the
trait name. These generics are in scope of every item within the trait alias.

```
trait Foo {  
    fn foo(self) -> Self;  
}  
  
trait Bar<T> {  
    fn bar(self) -> T;  
}  
  
// Equivalent to:  
// trait Baz<T>: Foo + Bar<T> {}  
//  
// impl<T, U> Baz<T> for U where U: Foo + Bar<T> {}  
trait Baz<T> = Foo + Bar<T>;
```

## Trait Alias Where ClausesTrait aliases support where clauses to add trait constraints to any of their
generic arguments, e.g. ensuring `T: Baz` for a trait alias `Qux<T>`.

```
trait Foo {  
    fn foo(self) -> Self;  
}  
  
trait Bar<T> {  
    fn bar(self) -> T;  
}  
  
trait Baz {  
    fn baz(self) -> bool;  
}  
  
// Equivalent to:  
// trait Qux<T>: Foo + Bar<T> where T: Baz {}  
//  
// impl<T, U> Qux<T> for U where  
//     U: Foo + Bar<T>,  
//     T: Baz,  
// {}  
trait Qux<T> = Foo + Bar<T> where T: Baz;
```

Note that while trait aliases support where clauses,
the equivalent traits can fail due to [#6467](https://github.com/noir-lang/noir/issues/6467)

## VisibilityBy default, like functions, traits and trait aliases are private to the module
they exist in. You can use `pub` to make the trait public or `pub(crate)` to make
it public to just its crate:

```
// This trait is now public  
pub trait Trait {}  
  
// This trait alias is now public  
pub trait Baz = Foo + Bar;
```

Trait methods have the same visibility as the trait they are in.

---


# Attributes

Source: https://noir-lang.org/docs/noir/concepts/attributes

Version: v1.0.0-beta.17

On this page

Attributes are metadata that can be applied to data types, functions, and some statements and expressions,
using the following syntax: `#[attribute(value)]`.

## `allow(dead_code)`When applied to a data type or function, the compiler won't produce a warning if the data type or function
ends up being unused.

Example:

```
#[allow(dead_code)]  
struct Unused {}
```

## `allow(unused_variables)`When applied on a `let` statement, the compiler won't produce a warning if the variable ends up being unused.

Example:

```
fn main() {  
    #[allow(unused_variables)]  
    let unused = 1;  
}
```

## `builtin`When applied to a function, indicates that the function is implemented by the compiler, for efficiency purposes.

## `deprecated`Marks a function as *deprecated*. Calling the function will generate a warning: `warning: use of deprecated function`

Example:

```
#[deprecated]  
fn slow_function() {}
```

The attribute takes an optional string which will be used as the deprecation message:
`#[deprecated("use some other function")]`

Example:

```
#[deprecated("use fast_function")]  
fn slow_function() {}  
  
fn fast_function() {}
```

## `field`Can be used on functions to enable conditional compilation of code depending on the field size.

The field attribute defines which field the function is compatible for. The function is conditionally compiled, under the condition that the field attribute matches the Noir native field.
The field can be defined implicitly, by using the name of the elliptic curve usually associated to it - for instance bn254, bls12\_381 - or explicitly by using the field (prime) order, in decimal or hexadecimal form.
As a result, it is possible to define multiple versions of a function with each version specialized for a different field attribute. This can be useful when a function requires different parameters depending on the underlying elliptic curve.

Example: we define the function `foo()` three times below. Once for the default Noir bn254 curve, once for the field F23\mathbb F\_{23}F23​, which will normally never be used by Noir, and once again for the bls12\_381 curve.

```
#[field(bn254)]  
fn foo() -> u32 {  
    1  
}  
  
#[field(23)]  
fn foo() -> u32 {  
    2  
}  
  
// This commented code would not compile as foo would be defined twice because it is the same field as bn254  
// #[field(21888242871839275222246405745257275088548364400416034343698204186575808495617)]  
// fn foo() -> u32 {  
//     2  
// }  
  
#[field(bls12_381)]  
fn foo() -> u32 {  
    3  
}
```

If the field name is not known to Noir, it will discard the function. Field names are case insensitive.

## `fuzz`Marks the functions for fuzzing. See [Fuzzer](/docs/tooling/fuzzer) for more details.

## `oracle`Mark a function as *oracle*; meaning it is an external unconstrained function, implemented in noir\_js. See [Unconstrained](/docs/noir/concepts/unconstrained) for more details.

## `test`Marks the function as a unit test. See [Tests](/docs/tooling/tests) for more details.

---


# Compile-time Code & Metaprogramming

Source: https://noir-lang.org/docs/noir/concepts/comptime

Version: v1.0.0-beta.17

On this page

## OverviewMetaprogramming in Noir is comprised of three parts:

1. `comptime` code
2. Quoting and unquoting
3. The metaprogramming API in `std::meta`

Each of these are explained in more detail in the next sections but the wide picture is that
`comptime` allows us to write code which runs at compile-time. In this `comptime` code we
can quote and unquote snippets of the program, manipulate them, and insert them in other
parts of the program. Comptime functions which do this are said to be macros. Additionally,
there's a compile-time API of built-in types and functions provided by the compiler which allows
for greater analysis and modification of programs.

---

## Comptime`comptime` is a new keyword in Noir which marks an item as executing or existing at compile-time. It can be used in several ways:

* `comptime fn` to define functions which execute exclusively during compile-time.
* `comptime global` to define a global variable which is evaluated at compile-time.
  + Unlike runtime globals, `comptime global`s can be mutable.
* `comptime { ... }` to execute a block of statements during compile-time.
* `comptime let` to define a variable whose value is evaluated at compile-time.
* `comptime for` to run a for loop at compile-time. Syntax sugar for `comptime { for .. }`.

## ScopingNote that while in a `comptime` context, any runtime variables *local to the current function* are never visible.

## EvaluatingEvaluation rules of `comptime` follows the normal unconstrained evaluation rules for other Noir code. There are a few things to note though:

* Certain built-in functions may not be available, although more may be added over time.
* Evaluation order of `comptime {}` blocks within global items is currently unspecified. For example, given the following two functions we can't guarantee
  which `println` will execute first. The ordering of the two printouts will be arbitrary, but should be stable across multiple compilations with the same `nargo` version as long as the program is also unchanged.

```
fn one() {  
    comptime { println("one"); }  
}  
  
fn two() {  
    comptime { println("two"); }  
}
```

* Since evaluation order is unspecified, care should be taken when using mutable globals so that they do not rely on a particular ordering.
  For example, using globals to generate unique ids should be fine but relying on certain ids always being produced (especially after edits to the program) should be avoided.
* Although the ordering of comptime code is usually unspecified, there are cases where it is:
  + Dependencies of a crate will always be evaluated before the dependent crate.
  + Any attributes on a function will be run before the function body is resolved. This is to allow the attribute to modify the function if necessary. Note that if the
    function itself was called at compile-time previously, it will already be resolved and cannot be modified. To prevent accidentally calling functions you wish to modify
    at compile-time, it may be helpful to sort your `comptime` annotation functions into a different submodule crate along with any dependencies they require.
  + Unlike raw `comptime {}` blocks, attributes on top-level items in the program do have a set evaluation order. Attributes within a module are evaluated top-down, and attributes
    in different modules are evaluated submodule-first. Sibling modules to the same parent module are evaluated in order of the module declarations (`mod foo; mod bar;`) in their
    parent module.

## LoweringWhen a `comptime` value is used in runtime code it must be lowered into a runtime value. This means replacing the expression with the literal that it evaluated to. For example, the code:

```
struct Foo { array: [Field; 2], len: u32 }  
  
fn main() {  
    println(comptime {  
        let mut foo = std::mem::zeroed::<Foo>();  
        foo.array[0] = 4;  
        foo.len = 1;  
        foo  
    });  
}
```

will be converted to the following after `comptime` expressions are evaluated:

```
struct Foo { array: [Field; 2], len: u32 }  
  
fn main() {  
    println(Foo { array: [4, 0], len: 1 });  
}
```

Not all types of values can be lowered. For example, references, `Type`s, and `TypeDefinition`s (among other types) cannot be lowered at all.

```
fn main() {  
    // There's nothing we could inline here to create a Type value at runtime  
    // let _ = get_type!();  
}  
  
comptime fn get_type() -> Type { ... }
```

Values of certain types may also change type when they are lowered. For example, a comptime format string will already be
formatted, and thus lowers into a runtime string instead:

```
fn main() {  
    let foo = comptime {  
        let i = 2;  
        f"i = {i}"  
    };  
    assert_eq(foo, "i = 2");  
}
```

---

## (Quasi) QuoteQuote")

Macros in Noir are `comptime` functions which return code as a value which is inserted into the call site when it is lowered there.
A code value in this case is of type `Quoted` and can be created by a `quote { ... }` expression.
More specifically, the code value `quote` creates is a token stream - a representation of source code as a series of words, numbers, string literals, or operators.
For example, the expression `quote { Hi "there reader"! }` would quote three tokens: the word "hi", the string "there reader", and an exclamation mark.
You'll note that snippets that would otherwise be invalid syntax can still be quoted.

When a `Quoted` value is used in runtime code, it is lowered into a `quote { ... }` expression. Since this expression is only valid
in compile-time code however, we'd get an error if we tried this. Instead, we can use macro insertion to insert each token into the
program at that point, and parse it as an expression. To do this, we have to add a `!` after the function name returning the `Quoted` value.
If the value was created locally and there is no function returning it, `std::meta::unquote!(_)` can be used instead.
Calling such a function at compile-time without `!` will just return the `Quoted` value to be further manipulated. For example:

quote-example

```
comptime fn quote_one() -> Quoted {  
        quote { 1 }  
    }  
  
    #[test]  
    fn returning_versus_macro_insertion() {  
        comptime {  
            // let _a: Quoted = quote { 1 };  
            let _a: Quoted = quote_one();  
  
            // let _b: Field = 1;  
            let _b: Field = quote_one!();  
  
            // Since integers default to fields, if we  
            // want a different type we have to explicitly cast  
            // let _c: i32 = 1 as i32;  
            let _c: i32 = quote_one!() as i32;  
        }  
    }
```

> [Source code: noir\_stdlib/src/meta/mod.nr#L131-L151](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/mod.nr#L131-L151)

For those familiar with quoting from other languages (primarily lisps), Noir's `quote` is actually a *quasiquote*.
This means we can escape the quoting by using the unquote operator to splice values in the middle of quoted code.

In addition to curly braces, you can also use square braces for the quote operator:

```
comptime {  
    let q1 = quote { 1 };  
    let q2 = quote [ 2 ];  
    assert_eq(q1, q2);  
  
    // Square braces can be used to quote mismatched curly braces if needed  
    let _ = quote[}];  
}
```

---

## UnquoteThe unquote operator `$` is usable within a `quote` expression.
It takes a variable as an argument, evaluates the variable, and splices the resulting value into the quoted token stream at that point. For example,

```
comptime {  
    let x = 1 + 2;  
    let y = quote { $x + 4 };  
}
```

The value of `y` above will be the token stream containing `3`, `+`, and `4`. We can also use this to combine `Quoted` values into larger token streams:

```
comptime {  
    let x = quote { 1 + 2 };  
    let y = quote { $x + 4 };  
}
```

The value of `y` above is now the token stream containing five tokens: `1 + 2 + 4`.

Note that to unquote something, a variable name *must* follow the `$` operator in a token stream.
If it is an expression (even a parenthesized one), it will do nothing. Most likely a parse error will be given when the macro is later unquoted.

Unquoting can also be avoided by escaping the `$` with a backslash:

```
comptime {  
    let x = quote { 1 + 2 };  
  
    // y contains the four tokens: `$x + 4`  
    let y = quote { \$x + 4 };  
}
```

## Combining TokensNote that `Quoted` is internally a series of separate tokens, and that all unquoting does is combine these token vectors.
This means that code which appears to append like a string actually appends like a vector internally:

```
comptime {  
    let x = 3;  
    let q = quote { foo$x }; // This is [foo, 3], not [foo3]  
  
    // Spaces are ignored in general, they're never part of a token  
    assert_eq(q, quote { foo   3 });  
}
```

If you do want string semantics, you can use format strings then convert back to a `Quoted` value with `.quoted_contents()`.
Note that formatting a quoted value with multiple tokens will always insert a space between each token. If this is
undesired, you'll need to only operate on quoted values containing a single token. To do this, you can iterate
over each token of a larger quoted value with `.tokens()`:

concatenate-example

```
comptime fn concatenate(q1: Quoted, q2: Quoted) -> Quoted {  
        assert(q1.tokens().len() <= 1);  
        assert(q2.tokens().len() <= 1);  
  
        f"{q1}{q2}".quoted_contents()  
    }  
  
    // The CtString type is also useful for a compile-time string of unbounded size  
    // so that you can append to it in a loop.  
    comptime fn double_spaced(q: Quoted) -> CtString {  
        let mut result = "".as_ctstring();  
  
        for token in q.tokens() {  
            if result != "".as_ctstring() {  
                result = result.append_str("  ");  
            }  
            result = result.append_fmtstr(f"{token}");  
        }  
  
        result  
    }  
  
    #[test]  
    fn concatenate_test() {  
        comptime {  
            let result = concatenate(quote {foo}, quote {bar});  
            assert_eq(result, quote {foobar});  
  
            let result = double_spaced(quote {foo bar 3}).as_quoted_str!();  
            assert_eq(result, "foo  bar  3");  
        }  
    }
```

> [Source code: noir\_stdlib/src/meta/mod.nr#L266-L299](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/mod.nr#L266-L299)

## $crateA common case when we have a library exporting macro code is that if you quote `foo::my_function()`, whether the
function can resolve will depend on the imports of where the macro code is used. It isn't enough to specify the
full path either. `crate::foo::my_function()` will not work in external crates and `my_crate_name::foo::my_function()`
will not work if the external crate renames the dependency `my_function` was defined in.

For cases like this there is `$crate` which when used in a quote will always resolve to the crate the quote is in.
So the library author can instead quote `$crate::foo::my_function()` and have it work in all cases as long as
`foo` and `my_function` are both publicly visible.

```
/// We want to access this function within the quoted code below  
/// and we want it to work in external crates.  
pub fn double(x: u64) -> u64 { x * 2 }  
  
comptime fn double_twice(code: Quoted) -> Quoted {  
    quote {  
        // `$crate` is a stand-in for the current crate  
        $crate::double($crate::double($code))  
    }  
}
```

---

## AttributesAttributes provide a way to run a `comptime` function on an item in the program.
When you use an attribute, the function with the same name will be called with that item as an argument:

```
#[my_struct_attribute]  
struct Foo {}  
  
comptime fn my_struct_attribute(s: TypeDefinition) {  
    println("Called my_struct_attribute!");  
}  
  
#[my_function_attribute]  
fn foo() {}  
  
comptime fn my_function_attribute(f: FunctionDefinition) {  
    println("Called my_function_attribute!");  
}
```

Anything returned from one of these functions will be inserted at top-level along with the original item.
Note that expressions are not valid at top-level so you'll get an error trying to return `3` or similar just as if you tried to write a program containing `3; struct Foo {}`.
You can insert other top-level items such as trait impls, structs, or functions this way though.
For example, this is the mechanism used to insert additional trait implementations into the program when deriving a trait impl from a struct:

derive-field-count-example

```
trait FieldCount {  
        fn field_count() -> u32;  
    }  
  
    #[derive_field_count]  
    struct Bar {  
        x: Field,  
        y: [Field; 2],  
    }  
  
    comptime fn derive_field_count(s: TypeDefinition) -> Quoted {  
        let typ = s.as_type();  
        let field_count = s.fields_as_written().len();  
        quote {  
            impl FieldCount for $typ {  
                fn field_count() -> u32 {  
                    $field_count  
                }  
            }  
        }  
    }
```

> [Source code: noir\_stdlib/src/meta/mod.nr#L153-L175](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/mod.nr#L153-L175)

## Calling annotations with additional argumentsArguments may optionally be given to attributes.
When this is done, these additional arguments are passed to the attribute function after the item argument.

annotation-arguments-example

```
#[assert_field_is_type(quote { i32 }.as_type())]  
    struct MyStruct {  
        my_field: i32,  
    }  
  
    comptime fn assert_field_is_type(s: TypeDefinition, typ: Type) {  
        // Assert the first field in `s` has type `typ`  
        let fields = s.fields([]);  
        assert_eq(fields[0].1, typ);  
    }
```

> [Source code: noir\_stdlib/src/meta/mod.nr#L177-L188](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/mod.nr#L177-L188)

We can also take any number of arguments by adding the `varargs` attribute:

annotation-varargs-example

```
#[assert_three_args(1, 2, 3)]  
    struct MyOtherStruct {  
        my_other_field: u32,  
    }  
  
    #[varargs]  
    comptime fn assert_three_args(_s: TypeDefinition, args: [Field]) {  
        assert_eq(args.len(), 3);  
    }
```

> [Source code: noir\_stdlib/src/meta/mod.nr#L190-L200](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/mod.nr#L190-L200)

## Attribute Evaluation OrderUnlike the evaluation order of stray `comptime {}` blocks within functions, attributes have a well-defined evaluation
order. Within a module, attributes are evaluated top to bottom. Between modules, attributes in child modules are evaluated
first. Attributes in sibling modules are resolved following the `mod foo; mod bar;` declaration order within their parent
modules.

```
mod foo; // attributes in foo are run first  
mod bar; // followed by attributes in bar  
  
// followed by any attributes in the parent module  
#[derive(Eq)]  
struct Baz {}
```

Note that because of this evaluation order, you may get an error trying to derive a trait for a struct whose fields
have not yet had the trait derived already:

```
// Error! `Bar` field of `Foo` does not (yet) implement Eq!  
#[derive(Eq)]  
struct Foo {  
    bar: Bar  
}  
  
#[derive(Eq)]  
struct Bar {}
```

In this case, the issue can be resolved by rearranging the structs.

---

## Comptime APIAlthough `comptime`, `quote`, and unquoting provide a flexible base for writing macros,
Noir's true metaprogramming ability comes from being able to interact with the compiler through a compile-time API.
This API can be accessed through built-in functions in `std::meta` as well as on methods of several `comptime` types.

The following is an incomplete list of some `comptime` types along with some useful methods on them. You can see more in the standard library [Metaprogramming section](/docs/noir/standard_library/meta).

* `Quoted`: A token stream
* `Type`: The type of a Noir type
  + `fn implements(self, constraint: TraitConstraint) -> bool`
    - Returns true if `self` implements the given trait constraint
* `Expr`: A syntactically valid expression. Can be used to recur on a program's parse tree to inspect how it is structured.
  + Methods:
    - `fn as_function_call(self) -> Option<(Expr, [Expr])>`
      * If this is a function call expression, return `(function, arguments)`
    - `fn as_block(self) -> Option<[Expr]>`
      * If this is a block, return each statement in the block
* `FunctionDefinition`: A function definition
  + Methods:
    - `fn parameters(self) -> [(Quoted, Type)]`
      * Returns a slice of `(name, type)` pairs for each parameter
* `TypeDefinition`: A struct or enum definition
  + Methods:
    - `fn as_type(self) -> Type`
      * Returns this `TypeDefinition` as a `Type`. Any generics are kept as-is
    - `fn generics(self) -> [Quoted]`
      * Return the name of each generic on this struct
    - `fn fields(self) -> [(Quoted, Type)]`
      * Return the name and type of each field
* `TraitConstraint`: A trait constraint such as `From<Field>`
* `TypedExpr`: A type-checked expression.
* `UnresolvedType`: A syntactic notation that refers to a Noir type that hasn't been resolved yet

There are many more functions available by exploring the `std::meta` module and its submodules.
Using these methods is the key to writing powerful metaprogramming libraries.

## `#[use_callers_scope]`Since certain functions such as `Quoted::as_type`, `Expression::as_type`, or `Quoted::as_trait_constraint` will attempt
to resolve their contents in a particular scope - it can be useful to change the scope they resolve in. By default
these functions will resolve in the current function's scope which is usually the attribute function they are called in.
If you're working on a library however, this may be a completely different module or crate to the item you're trying to
use the attribute on. If you want to be able to use `Quoted::as_type` to refer to types local to the caller's scope for
example, you can annotate your attribute function with `#[use_callers_scope]`. This will ensure your attribute, and any
closures it uses, can refer to anything in the caller's scope. `#[use_callers_scope]` also works recursively. So if both
your attribute function and a helper function it calls use it, then they can both refer to the same original caller.

---

## Example: DeriveUsing all of the above, we can write a `derive` macro that behaves similarly to Rust's but is not built into the language.
From the user's perspective it will look like this:

```
// Example usage  
#[derive(Default, Eq, Ord)]  
struct MyStruct { my_field: u32 }
```

To implement `derive` we'll have to create a `comptime` function that accepts
a variable amount of traits.

derive\_example

```
// These are needed for the unconstrained hashmap we're using to store derive functions  
use crate::collections::umap::UHashMap;  
use crate::hash::BuildHasherDefault;  
use crate::hash::poseidon2::Poseidon2Hasher;  
  
// A derive function is one that given a type definition can  
// create us a quoted trait impl from it.  
pub type DeriveFunction = fn(TypeDefinition) -> Quoted;  
  
// We'll keep a global HANDLERS map to keep track of the derive handler for each trait  
comptime mut global HANDLERS: UHashMap<TraitDefinition, DeriveFunction, BuildHasherDefault<Poseidon2Hasher>> =  
    UHashMap::default();  
  
// Given a type definition and a slice of traits to derive, create trait impls for each.  
// This function is as simple as iterating over the slice, checking if we have a trait  
// handler registered for the given trait, calling it, and appending the result.  
#[varargs]  
pub comptime fn derive(s: TypeDefinition, traits: [TraitDefinition]) -> Quoted {  
    let mut result = quote {};  
  
    for trait_to_derive in traits {  
        let handler = HANDLERS.get(trait_to_derive);  
        assert(handler.is_some(), f"No derive function registered for `{trait_to_derive}`");  
  
        let trait_impl = handler.unwrap()(s);  
        result = quote { $result $trait_impl };  
    }  
  
    result  
}
```

> [Source code: noir\_stdlib/src/meta/mod.nr#L33-L66](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/mod.nr#L33-L66)

Registering a derive function could be done as follows:

derive\_via

```
// To register a handler for a trait, just add it to our handlers map  
pub comptime fn derive_via(t: TraitDefinition, f: DeriveFunction) {  
    HANDLERS.insert(t, f);  
}
```

> [Source code: noir\_stdlib/src/meta/mod.nr#L68-L75](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/mod.nr#L68-L75)

big-derive-usage-example

```
// Finally, to register a handler we call the above function as an annotation  
    // with our handler function.  
    #[derive_via(derive_do_nothing)]  
    trait DoNothing {  
        fn do_nothing(self);  
    }  
  
    comptime fn derive_do_nothing(s: TypeDefinition) -> Quoted {  
        // This is simplified since we don't handle generics or where clauses!  
        // In a real example we'd likely also need to introduce each of  
        // `s.generics()` as well as a trait constraint for each generic  
        // to ensure they also implement the trait.  
        let typ = s.as_type();  
        quote {  
            impl DoNothing for $typ {  
                fn do_nothing(self) {  
                    // Traits can't tell us what to do  
                    println("something");  
                }  
            }  
        }  
    }  
  
    // Since `DoNothing` is a simple trait which:  
    // 1. Only has one method  
    // 2. Does not have any generics on the trait itself  
    // We can use `std::meta::make_trait_impl` to help us out.  
    // This helper function will generate our impl for us along with any  
    // necessary where clauses and still provides a flexible interface  
    // for us to work on each field on the struct.  
    comptime fn derive_do_nothing_alt(s: TypeDefinition) -> Quoted {  
        let trait_name = quote { DoNothing };  
        let method_signature = quote { fn do_nothing(self) };  
  
        // Call `do_nothing` recursively on each field in the struct  
        let for_each_field = |field_name| quote { self.$field_name.do_nothing(); };  
  
        // Some traits like Eq want to join each field expression with something like `&`.  
        // We don't need that here  
        let join_fields_with = quote {};  
  
        // The body function is a spot to insert any extra setup/teardown needed.  
        // We'll insert our println here. Since we recur on each field, we should see  
        // one println for the struct itself, followed by a println for every field (recursively).  
        let body = |body| quote {  
            println("something");  
            $body  
        };  
        crate::meta::make_trait_impl(  
            s,  
            trait_name,  
            method_signature,  
            for_each_field,  
            join_fields_with,  
            body,  
        )  
    }
```

> [Source code: noir\_stdlib/src/meta/mod.nr#L202-L260](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/mod.nr#L202-L260)

---


# Standard Library

Source: https://noir-lang.org/docs/noir/standard_library/cryptographic_primitives

Version: v1.0.0-beta.17

The Noir team is progressively adding new cryptographic primitives to the standard library. Reach out for news or if you would be interested in adding more of these calculations in Noir.

Some methods are available thanks to the Aztec backend, not being performed using Noir. When using other backends, these methods may or may not be supplied.

---


# Ciphers

Source: https://noir-lang.org/docs/noir/standard_library/cryptographic_primitives/ciphers

Version: v1.0.0-beta.17

On this page

## aes128Given a plaintext as an array of bytes, returns the corresponding aes128 ciphertext (CBC mode). Input padding is automatically performed using PKCS#7, so that the output length is `input.len() + (16 - input.len() % 16)`.

aes128

```
pub fn aes128_encrypt<let N: u32>(  
    input: [u8; N],  
    iv: [u8; 16],  
    key: [u8; 16],  
) -> [u8; N + 16 - N % 16] {}
```

> [Source code: noir\_stdlib/src/aes128.nr#L2-L8](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/aes128.nr#L2-L8)

```
fn main() {  
    let input: [u8; 4] = [0, 12, 3, 15]; // Random bytes, will be padded to 16 bytes.  
    let iv: [u8; 16] = [0; 16]; // Initialization vector  
    let key: [u8; 16] = [0; 16]; // AES key  
    let ciphertext = std::aes128::aes128_encrypt(input, iv, key); // In this case, the output length will be 16 bytes.  
}
```

This is a black box function. Read [this section](/docs/noir/standard_library/black_box_fns) to learn more about black box functions in Noir.

---


# Hash methods

Source: https://noir-lang.org/docs/noir/standard_library/cryptographic_primitives/hashes

Version: v1.0.0-beta.17

On this page

Many of the common hash methods have been moved outside of the Noir standard library and exist as independent libraries.
You can find the complete list of libraries in the [Hashes section](https://github.com/noir-lang/awesome-noir?tab=readme-ov-file#hashes)
of the awesome-noir repo, including:

* keccak256
* MiMC
* Poseidon
* RIPEMD160
* sha256
* sha512

## sha256 compressionPerforms a sha256 compression on an input and initial state, returning the resulting state.

warning

This is a different function than sha256. See [this library](https://github.com/noir-lang/sha256) for sha256 hashing.

sha256\_compression

```
pub fn sha256_compression(input: [u32; 16], state: [u32; 8]) -> [u32; 8] {}
```

> [Source code: noir\_stdlib/src/hash/mod.nr#L11-L13](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/hash/mod.nr#L11-L13)

This is a black box function. Read [this section](/docs/noir/standard_library/black_box_fns) to learn more about black box functions in Noir.

## blake2sGiven an array of bytes, returns an array with the Blake2 hash

blake2s

```
pub fn blake2s<let N: u32>(input: [u8; N]) -> [u8; 32]
```

> [Source code: noir\_stdlib/src/hash/mod.nr#L28-L30](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/hash/mod.nr#L28-L30)

example:

```
fn main() {  
    let x = [163, 117, 178, 149]; // some random bytes  
    let hash = std::hash::blake2s(x);  
}
```

This is a black box function. Read [this section](/docs/noir/standard_library/black_box_fns) to learn more about black box functions in Noir.

## blake3Given an array of bytes, returns an array with the Blake3 hash

blake3

```
pub fn blake3<let N: u32>(input: [u8; N]) -> [u8; 32]
```

> [Source code: noir\_stdlib/src/hash/mod.nr#L33-L35](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/hash/mod.nr#L33-L35)

example:

```
fn main() {  
    let x = [163, 117, 178, 149]; // some random bytes  
    let hash = std::hash::blake3(x);  
}
```

This is a black box function. Read [this section](/docs/noir/standard_library/black_box_fns) to learn more about black box functions in Noir.

## pedersen\_hashGiven an array of Fields, returns the Pedersen hash.

pedersen\_hash

```
pub fn pedersen_hash<let N: u32>(input: [Field; N]) -> Field
```

> [Source code: noir\_stdlib/src/hash/mod.nr#L71-L73](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/hash/mod.nr#L71-L73)

example:

pedersen-hash

```
fn main(x: Field, y: Field, expected_hash: Field) {  
    let hash = std::hash::pedersen_hash([x, y]);  
    assert_eq(hash, expected_hash);  
}
```

> [Source code: test\_programs/execution\_success/pedersen\_hash/src/main.nr#L1-L6](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/pedersen_hash/src/main.nr#L1-L6)

This is a black box function. Read [this section](/docs/noir/standard_library/black_box_fns) to learn more about black box functions in Noir.

## pedersen\_commitmentGiven an array of Fields, returns the Pedersen commitment.

pedersen\_commitment

```
pub fn pedersen_commitment<let N: u32>(input: [Field; N]) -> EmbeddedCurvePoint {
```

> [Source code: noir\_stdlib/src/hash/mod.nr#L51-L53](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/hash/mod.nr#L51-L53)

example:

pedersen-commitment

```
fn main(x: Field, y: Field, expected_commitment: std::embedded_curve_ops::EmbeddedCurvePoint) {  
    let commitment = std::hash::pedersen_commitment([x, y]);  
    assert_eq(commitment.x, expected_commitment.x);  
    assert_eq(commitment.y, expected_commitment.y);  
}
```

> [Source code: test\_programs/execution\_success/pedersen\_commitment/src/main.nr#L1-L7](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/pedersen_commitment/src/main.nr#L1-L7)

This is a black box function. Read [this section](/docs/noir/standard_library/black_box_fns) to learn more about black box functions in Noir.

## keccakf1600Given an initial `[u64; 25]` state, returns the state resulting from applying a keccakf1600 permutation (`[u64; 25]`).

keccakf1600

```
pub fn keccakf1600(input: [u64; 25]) -> [u64; 25] {}
```

> [Source code: noir\_stdlib/src/hash/mod.nr#L16-L18](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/hash/mod.nr#L16-L18)

This is a black box function. Read [this section](/docs/noir/standard_library/black_box_fns) to learn more about black box functions in Noir.

---


# Scalar multiplication

Source: https://noir-lang.org/docs/noir/standard_library/cryptographic_primitives/embedded_curve_ops

Version: v1.0.0-beta.17

On this page

The following functions perform operations over the embedded curve whose coordinates are defined by the configured noir field.
For the BN254 scalar field, this is BabyJubJub or Grumpkin.

note

Suffixes `_low` and `_high` denote low and high limbs of a scalar.

## embedded\_curve\_ops::multi\_scalar\_mulPerforms multi scalar multiplication over the embedded curve.
The function accepts arbitrary amount of point-scalar pairs on the input, it multiplies the individual pairs over
the curve and returns a sum of the resulting points.

Points represented as x and y coordinates [x1, y1, x2, y2, ...], scalars as low and high limbs [low1, high1, low2, high2, ...].

multi\_scalar\_mul

```
pub fn multi_scalar_mul<let N: u32>(  
    points: [EmbeddedCurvePoint; N],  
    scalars: [EmbeddedCurveScalar; N],  
) -> EmbeddedCurvePoint
```

> [Source code: noir\_stdlib/src/embedded\_curve\_ops.nr#L138-L143](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/embedded_curve_ops.nr#L138-L143)

example

```
fn main(point_x: Field, point_y: Field, scalar_low: Field, scalar_high: Field) {  
    let point = std::embedded_curve_ops::multi_scalar_mul([point_x, point_y], [scalar_low, scalar_high]);  
    println(point);  
}
```

## embedded\_curve\_ops::fixed\_base\_scalar\_mulPerforms fixed base scalar multiplication over the embedded curve (multiplies input scalar with a generator point).
The function accepts a single scalar on the input represented as 2 fields.

fixed\_base\_scalar\_mul

```
pub fn fixed_base_scalar_mul(scalar: EmbeddedCurveScalar) -> EmbeddedCurvePoint
```

> [Source code: noir\_stdlib/src/embedded\_curve\_ops.nr#L155-L157](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/embedded_curve_ops.nr#L155-L157)

example

```
fn main(scalar_low: Field, scalar_high: Field) {  
    let point = std::embedded_curve_ops::fixed_base_scalar_mul(scalar_low, scalar_high);  
    println(point);  
}
```

## embedded\_curve\_ops::embedded\_curve\_addAdds two points on the embedded curve.
This function takes two `EmbeddedCurvePoint` structures as parameters, representing points on the curve, and returns a new `EmbeddedCurvePoint` structure that represents their sum.

## Parameters:* `point1` (`EmbeddedCurvePoint`): The first point to add.
* `point2` (`EmbeddedCurvePoint`): The second point to add.

## Returns:* `EmbeddedCurvePoint`: The resulting point after the addition of `point1` and `point2`.

embedded\_curve\_add

```
pub fn embedded_curve_add(  
    point1: EmbeddedCurvePoint,  
    point2: EmbeddedCurvePoint,  
) -> EmbeddedCurvePoint {
```

> [Source code: noir\_stdlib/src/embedded\_curve\_ops.nr#L163-L168](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/embedded_curve_ops.nr#L163-L168)

example

```
fn main() {  
    let point1 = EmbeddedCurvePoint { x: 1, y: 2 };  
    let point2 = EmbeddedCurvePoint { x: 3, y: 4 };  
    let result = std::embedded_curve_ops::embedded_curve_add(point1, point2);  
    println!("Resulting Point: ({}, {})", result.x, result.y);  
}
```

This is a black box function. Read [this section](/docs/noir/standard_library/black_box_fns) to learn more about black box functions in Noir.

---


# ECDSA Signature Verification

Source: https://noir-lang.org/docs/noir/standard_library/cryptographic_primitives/ecdsa_sig_verification

Version: v1.0.0-beta.17

On this page

Noir supports ECDSA signatures verification over the secp256k1 and secp256r1 curves.

## ecdsa\_secp256k1::verify\_signatureVerifier for ECDSA Secp256k1 signatures.

ecdsa\_secp256k1

```
/// Verifies a ECDSA signature over the secp256k1 curve.  
/// - inputs:  
///     - x coordinate of public key as 32 bytes  
///     - y coordinate of public key as 32 bytes  
///     - the signature, as a 64 bytes array  
///       The signature internally will be represented as `(r, s)`,  
///       where `r` and `s` are fixed-sized big endian scalar values.  
///       As the `secp256k1` has a 256-bit modulus, we have a 64 byte signature  
///       while `r` and `s` will both be 32 bytes.  
///       We expect `s` to be normalized. This means given the curve's order,  
///       `s` should be less than or equal to `order / 2`.  
///       This is done to prevent malleability.  
///       For more context regarding malleability you can reference BIP 0062.  
///     - the hash of the message, as a vector of bytes  
/// - output: false for failure and true for success  
pub fn verify_signature(  
    public_key_x: [u8; 32],  
    public_key_y: [u8; 32],  
    signature: [u8; 64],  
    message_hash: [u8; 32],  
) -> bool
```

> [Source code: noir\_stdlib/src/ecdsa\_secp256k1.nr#L1-L23](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/ecdsa_secp256k1.nr#L1-L23)

example:

```
fn main(hashed_message : [u8;32], pub_key_x : [u8;32], pub_key_y : [u8;32], signature : [u8;64]) {  
     let valid_signature = std::ecdsa_secp256k1::verify_signature(pub_key_x, pub_key_y, signature, hashed_message);  
     assert(valid_signature);  
}
```

This is a black box function. Read [this section](/docs/noir/standard_library/black_box_fns) to learn more about black box functions in Noir.

## ecdsa\_secp256r1::verify\_signatureVerifier for ECDSA Secp256r1 signatures.
See ecdsa\_secp256r1::verify\_signature\_slice for a version that accepts slices directly.

ecdsa\_secp256r1

```
pub fn verify_signature(  
    public_key_x: [u8; 32],  
    public_key_y: [u8; 32],  
    signature: [u8; 64],  
    message_hash: [u8; 32],  
) -> bool
```

> [Source code: noir\_stdlib/src/ecdsa\_secp256r1.nr#L1-L8](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/ecdsa_secp256r1.nr#L1-L8)

example:

```
fn main(hashed_message : [u8;32], pub_key_x : [u8;32], pub_key_y : [u8;32], signature : [u8;64]) {  
     let valid_signature = std::ecdsa_secp256r1::verify_signature(pub_key_x, pub_key_y, signature, hashed_message);  
     assert(valid_signature);  
}
```

This is a black box function. Read [this section](/docs/noir/standard_library/black_box_fns) to learn more about black box functions in Noir.

---


# Black Box Functions

Source: https://noir-lang.org/docs/noir/standard_library/black_box_fns

Version: v1.0.0-beta.17

On this page

Black box functions are functions in Noir that rely on backends implementing support for specialized constraints. This makes certain zk-snark unfriendly computations cheaper than if they were implemented in Noir.

The ACVM spec defines a set of blackbox functions which backends will be expected to implement. This allows backends to use optimized implementations of these constraints if they have them, however they may also fallback to less efficient naive implementations if not.

## Function listHere is a list of the current black box functions:

* [AES128](/docs/noir/standard_library/cryptographic_primitives/ciphers#aes128)
* [SHA256](/docs/noir/standard_library/cryptographic_primitives/hashes#sha256)
* [Blake2s](/docs/noir/standard_library/cryptographic_primitives/hashes#blake2s)
* [Blake3](/docs/noir/standard_library/cryptographic_primitives/hashes#blake3)
* [Pedersen Hash](/docs/noir/standard_library/cryptographic_primitives/hashes#pedersen_hash)
* [Pedersen Commitment](/docs/noir/standard_library/cryptographic_primitives/hashes#pedersen_commitment)
* [ECDSA signature verification](/docs/noir/standard_library/cryptographic_primitives/ecdsa_sig_verification)
* [Embedded curve operations (MSM, addition, ...)](/docs/noir/standard_library/cryptographic_primitives/embedded_curve_ops)
* AND
* XOR
* RANGE
* [Keccakf1600](/docs/noir/standard_library/cryptographic_primitives/hashes#keccakf1600)
* [Recursive proof verification](/docs/noir/standard_library/recursion)

Most black box functions are included as part of the Noir standard library, however `AND`, `XOR` and `RANGE` are used as part of the Noir language syntax. For instance, using the bitwise operator `&` will invoke the `AND` black box function.

You can view the black box functions defined in the ACVM code [here](https://github.com/noir-lang/noir/blob/master/acvm-repo/acir/src/circuit/black_box_functions.rs).

---


# Bn254 Field Library

Source: https://noir-lang.org/docs/noir/standard_library/bn254

Version: v1.0.0-beta.17

On this page

Noir provides a module in standard library with some optimized functions for bn254 Fr in `std::field::bn254`.

## decompose```
fn decompose(x: Field) -> (Field, Field) {}
```

Decomposes a single field into two fields, low and high. The low field contains the lower 16 bytes of the input field and the high field contains the upper 16 bytes of the input field. Both field results are range checked to 128 bits.

## assert\_gt```
fn assert_gt(a: Field, b: Field) {}
```

Asserts that a > b. This will generate less constraints than using `assert(gt(a, b))`.

## assert\_lt```
fn assert_lt(a: Field, b: Field) {}
```

Asserts that a < b. This will generate less constraints than using `assert(lt(a, b))`.

## gt```
fn gt(a: Field, b: Field) -> bool  {}
```

Returns true if a > b.

## lt```
fn lt(a: Field, b: Field) -> bool  {}
```

Returns true if a < b.

---


# Containers

Source: https://noir-lang.org/docs/noir/standard_library/containers

Version: v1.0.0-beta.17

---


# Bounded Vectors

Source: https://noir-lang.org/docs/noir/standard_library/containers/boundedvec

Version: v1.0.0-beta.17

On this page

A `BoundedVec<T, MaxLen>` is a growable storage similar to a `Vec<T>` except that it
is bounded with a maximum possible length. Unlike `Vec`, `BoundedVec` is not implemented
via slices and thus is not subject to the same restrictions slices are (notably, nested
slices - and thus nested vectors as well - are disallowed).

Since a BoundedVec is backed by a normal array under the hood, growing the BoundedVec by
pushing an additional element is also more efficient - the length only needs to be increased
by one.

For these reasons `BoundedVec<T, N>` should generally be preferred over `Vec<T>` when there
is a reasonable maximum bound that can be placed on the vector.

Example:

```
let mut vector: BoundedVec<Field, 10> = BoundedVec::new();  
for i in 0..5 {  
    vector.push(i);  
}  
assert(vector.len() == 5);  
assert(vector.max_len() == 10);
```

## Methods## new```
pub fn new() -> Self
```

Creates a new, empty vector of length zero.

Since this container is backed by an array internally, it still needs an initial value
to give each element. To resolve this, each element is zeroed internally. This value
is guaranteed to be inaccessible unless `get_unchecked` is used.

Example:

```
let empty_vector: BoundedVec<Field, 10> = BoundedVec::new();  
assert(empty_vector.len() == 0);
```

Note that whenever calling `new` the maximum length of the vector should always be specified
via a type signature:

new\_example

```
fn good() -> BoundedVec<Field, 10> {  
    // Ok! MaxLen is specified with a type annotation  
    let v1: BoundedVec<Field, 3> = BoundedVec::new();  
    let v2 = BoundedVec::new();  
  
    // Ok! MaxLen is known from the type of `good`'s return value  
    v2  
}
```

> [Source code: test\_programs/noir\_test\_success/bounded\_vec/src/main.nr#L6-L15](https://github.com/noir-lang/noir/blob/master/test_programs/noir_test_success/bounded_vec/src/main.nr#L6-L15)

This defaulting of `MaxLen` (and numeric generics in general) to zero may change in future noir versions
but for now make sure to use type annotations when using bounded vectors. Otherwise, you will receive a constraint failure at runtime when the vec is pushed to.

## get```
pub fn get(self, index: u64) -> T {
```

Retrieves an element from the vector at the given index, starting from zero.

If the given index is equal to or greater than the length of the vector, this
will issue a constraint failure.

Example:

```
fn foo<N>(v: BoundedVec<u32, N>) {  
    let first = v.get(0);  
    let last = v.get(v.len() - 1);  
    assert(first != last);  
}
```

## get\_unchecked```
pub fn get_unchecked(self, index: u64) -> T {
```

Retrieves an element from the vector at the given index, starting from zero, without
performing a bounds check.

Since this function does not perform a bounds check on length before accessing the element,
it is unsafe! Use at your own risk!

Example:

get\_unchecked\_example

```
fn sum_of_first_three<let N: u32>(v: BoundedVec<u32, N>) -> u32 {  
    // Always ensure the length is larger than the largest  
    // index passed to get_unchecked  
    assert(v.len() > 2);  
    let first = v.get_unchecked(0);  
    let second = v.get_unchecked(1);  
    let third = v.get_unchecked(2);  
    first + second + third  
}
```

> [Source code: test\_programs/noir\_test\_success/bounded\_vec/src/main.nr#L42-L52](https://github.com/noir-lang/noir/blob/master/test_programs/noir_test_success/bounded_vec/src/main.nr#L42-L52)

## set```
pub fn set(&mut self: Self, index: u64, value: T) {
```

Writes an element to the vector at the given index, starting from zero.

If the given index is equal to or greater than the length of the vector, this will issue a constraint failure.

Example:

```
fn foo<N>(v: BoundedVec<u32, N>) {  
    let first = v.get(0);  
    assert(first != 42);  
    v.set(0, 42);  
    let new_first = v.get(0);  
    assert(new_first == 42);  
}
```

## set\_unchecked```
pub fn set_unchecked(&mut self: Self, index: u64, value: T) -> T {
```

Writes an element to the vector at the given index, starting from zero, without performing a bounds check.

Since this function does not perform a bounds check on length before accessing the element, it is unsafe! Use at your own risk!

Example:

set\_unchecked\_example

```
fn set_unchecked_example() {  
    let mut vec: BoundedVec<u32, 5> = BoundedVec::new();  
    vec.extend_from_array([1, 2]);  
  
    // Here we're safely writing within the valid range of `vec`  
    // `vec` now has the value [42, 2]  
    vec.set_unchecked(0, 42);  
  
    // We can then safely read this value back out of `vec`.  
    // Notice that we use the checked version of `get` which would prevent reading unsafe values.  
    assert_eq(vec.get(0), 42);  
  
    // We've now written past the end of `vec`.  
    // As this index is still within the maximum potential length of `v`,  
    // it won't cause a constraint failure.  
    vec.set_unchecked(2, 42);  
    println(vec);  
  
    // This will write past the end of the maximum potential length of `vec`,  
    // it will then trigger a constraint failure.  
    vec.set_unchecked(5, 42);  
    println(vec);  
}
```

> [Source code: test\_programs/noir\_test\_success/bounded\_vec/src/main.nr#L55-L79](https://github.com/noir-lang/noir/blob/master/test_programs/noir_test_success/bounded_vec/src/main.nr#L55-L79)

## push```
pub fn push(&mut self, elem: T) {
```

Pushes an element to the end of the vector. This increases the length
of the vector by one.

Panics if the new length of the vector will be greater than the max length.

Example:

bounded-vec-push-example

```
let mut v: BoundedVec<Field, 2> = BoundedVec::new();  
  
    v.push(1);  
    v.push(2);  
  
    // Panics with failed assertion "push out of bounds"  
    v.push(3);
```

> [Source code: test\_programs/noir\_test\_success/bounded\_vec/src/main.nr#L83-L91](https://github.com/noir-lang/noir/blob/master/test_programs/noir_test_success/bounded_vec/src/main.nr#L83-L91)

## pop```
pub fn pop(&mut self) -> T
```

Pops the element at the end of the vector. This will decrease the length
of the vector by one.

Panics if the vector is empty.

Example:

bounded-vec-pop-example

```
let mut v: BoundedVec<Field, 2> = BoundedVec::new();  
    v.push(1);  
    v.push(2);  
  
    let two = v.pop();  
    let one = v.pop();  
  
    assert(two == 2);  
    assert(one == 1);  
    // error: cannot pop from an empty vector  
    // let _ = v.pop();
```

> [Source code: test\_programs/noir\_test\_success/bounded\_vec/src/main.nr#L96-L108](https://github.com/noir-lang/noir/blob/master/test_programs/noir_test_success/bounded_vec/src/main.nr#L96-L108)

## len```
pub fn len(self) -> u64 {
```

Returns the current length of this vector

Example:

bounded-vec-len-example

```
let mut v: BoundedVec<Field, 4> = BoundedVec::new();  
    assert(v.len() == 0);  
  
    v.push(100);  
    assert(v.len() == 1);  
  
    v.push(200);  
    v.push(300);  
    v.push(400);  
    assert(v.len() == 4);  
  
    let _ = v.pop();  
    let _ = v.pop();  
    assert(v.len() == 2);
```

> [Source code: test\_programs/noir\_test\_success/bounded\_vec/src/main.nr#L113-L128](https://github.com/noir-lang/noir/blob/master/test_programs/noir_test_success/bounded_vec/src/main.nr#L113-L128)

## max\_len```
pub fn max_len(_self: BoundedVec<T, MaxLen>) -> u64 {
```

Returns the maximum length of this vector. This is always
equal to the `MaxLen` parameter this vector was initialized with.

Example:

bounded-vec-max-len-example

```
let mut v: BoundedVec<Field, 5> = BoundedVec::new();  
  
    assert(v.max_len() == 5);  
    v.push(10);  
    assert(v.max_len() == 5);
```

> [Source code: test\_programs/noir\_test\_success/bounded\_vec/src/main.nr#L133-L139](https://github.com/noir-lang/noir/blob/master/test_programs/noir_test_success/bounded_vec/src/main.nr#L133-L139)

## storage```
pub fn storage(self) -> [T; MaxLen] {
```

Returns the internal array within this vector.
Since arrays in Noir are immutable, mutating the returned storage array will not mutate
the storage held internally by this vector.

Note that uninitialized elements may be zeroed out!

Example:

bounded-vec-storage-example

```
let mut v: BoundedVec<Field, 5> = BoundedVec::new();  
  
    assert(v.storage() == [0, 0, 0, 0, 0]);  
  
    v.push(57);  
    assert(v.storage() == [57, 0, 0, 0, 0]);
```

> [Source code: test\_programs/noir\_test\_success/bounded\_vec/src/main.nr#L144-L151](https://github.com/noir-lang/noir/blob/master/test_programs/noir_test_success/bounded_vec/src/main.nr#L144-L151)

## extend\_from\_array```
pub fn extend_from_array<Len>(&mut self, array: [T; Len])
```

Pushes each element from the given array to this vector.

Panics if pushing each element would cause the length of this vector
to exceed the maximum length.

Example:

bounded-vec-extend-from-array-example

```
let mut vec: BoundedVec<Field, 3> = BoundedVec::new();  
    vec.extend_from_array([2, 4]);  
  
    assert(vec.len() == 2);  
    assert(vec.get(0) == 2);  
    assert(vec.get(1) == 4);
```

> [Source code: test\_programs/noir\_test\_success/bounded\_vec/src/main.nr#L156-L163](https://github.com/noir-lang/noir/blob/master/test_programs/noir_test_success/bounded_vec/src/main.nr#L156-L163)

## extend\_from\_bounded\_vec```
pub fn extend_from_bounded_vec<Len>(&mut self, vec: BoundedVec<T, Len>)
```

Pushes each element from the other vector to this vector. The length of
the other vector is left unchanged.

Panics if pushing each element would cause the length of this vector
to exceed the maximum length.

Example:

bounded-vec-extend-from-bounded-vec-example

```
let mut v1: BoundedVec<Field, 5> = BoundedVec::new();  
    let mut v2: BoundedVec<Field, 7> = BoundedVec::new();  
  
    v2.extend_from_array([1, 2, 3]);  
    v1.extend_from_bounded_vec(v2);  
  
    assert(v1.storage() == [1, 2, 3, 0, 0]);  
    assert(v2.storage() == [1, 2, 3, 0, 0, 0, 0]);
```

> [Source code: test\_programs/noir\_test\_success/bounded\_vec/src/main.nr#L168-L177](https://github.com/noir-lang/noir/blob/master/test_programs/noir_test_success/bounded_vec/src/main.nr#L168-L177)

## from\_array```
pub fn from_array<Len>(array: [T; Len]) -> Self
```

Creates a new vector, populating it with values derived from an array input.
The maximum length of the vector is determined based on the type signature.

Example:

```
let bounded_vec: BoundedVec<Field, 10> = BoundedVec::from_array([1, 2, 3])
```

## from\_parts```
pub fn from_parts(mut array: [T; MaxLen], len: u32) -> Self
```

Creates a new BoundedVec from the given array and length.
The given length must be less than or equal to the length of the array.

This function will zero out any elements at or past index `len` of `array`.
This incurs an extra runtime cost of O(MaxLen). If you are sure your array is
zeroed after that index, you can use `from_parts_unchecked` to remove the extra loop.

Example:

from-parts

```
let vec: BoundedVec<u32, 4> = BoundedVec::from_parts([1, 2, 3, 0], 3);  
            assert_eq(vec.len(), 3);  
  
            // Any elements past the given length are zeroed out, so these  
            // two BoundedVecs will be completely equal  
            let vec1: BoundedVec<u32, 4> = BoundedVec::from_parts([1, 2, 3, 1], 3);  
            let vec2: BoundedVec<u32, 4> = BoundedVec::from_parts([1, 2, 3, 2], 3);  
            assert_eq(vec1, vec2);
```

> [Source code: noir\_stdlib/src/collections/bounded\_vec.nr#L1123-L1132](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/bounded_vec.nr#L1123-L1132)

## from\_parts\_unchecked```
pub fn from_parts_unchecked(array: [T; MaxLen], len: u32) -> Self
```

Creates a new BoundedVec from the given array and length.
The given length must be less than or equal to the length of the array.

This function is unsafe because it expects all elements past the `len` index
of `array` to be zeroed, but does not check for this internally. Use `from_parts`
for a safe version of this function which does zero out any indices past the
given length. Invalidating this assumption can notably cause `BoundedVec::eq`
to give incorrect results since it will check even elements past `len`.

Example:

from-parts-unchecked

```
let vec: BoundedVec<u32, 4> = BoundedVec::from_parts_unchecked([1, 2, 3, 0], 3);  
            assert_eq(vec.len(), 3);  
  
            // invalid use!  
            let vec1: BoundedVec<u32, 4> = BoundedVec::from_parts_unchecked([1, 2, 3, 1], 3);  
            let vec2: BoundedVec<u32, 4> = BoundedVec::from_parts_unchecked([1, 2, 3, 2], 3);  
  
            // both vecs have length 3 so we'd expect them to be equal, but this  
            // fails because elements past the length are still checked in eq  
            assert(vec1 != vec2);
```

> [Source code: noir\_stdlib/src/collections/bounded\_vec.nr#L1137-L1148](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/bounded_vec.nr#L1137-L1148)

## map```
pub fn map<U, Env>(self, f: fn[Env](T) -> U) -> BoundedVec<U, MaxLen>
```

Creates a new vector of equal size by calling a closure on each element in this vector.

Example:

bounded-vec-map-example

```
let vec: BoundedVec<u32, 4> = BoundedVec::from_array([1, 2, 3, 4]);  
            let result = vec.map(|value| value * 2);
```

> [Source code: noir\_stdlib/src/collections/bounded\_vec.nr#L773-L776](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/bounded_vec.nr#L773-L776)

## mapi```
pub fn mapi<U, Env>(self, f: fn[Env](u32, T) -> U) -> BoundedVec<U, MaxLen>
```

Creates a new vector of equal size by calling a closure on each element in this
vector, along with its index in the vector.

Example:

bounded-vec-mapi-example

```
let vec: BoundedVec<u32, 4> = BoundedVec::from_array([1, 2, 3, 4]);  
            let result = vec.mapi(|i, value| i + value * 2);
```

> [Source code: noir\_stdlib/src/collections/bounded\_vec.nr#L834-L837](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/bounded_vec.nr#L834-L837)

## for\_each```
pub fn for_each<Env>(self, f: fn[Env](T) -> ())
```

Calls a closure on each element in this vector.

Example:

bounded-vec-for-each-example

```
let vec: BoundedVec<u32, 3> = BoundedVec::from_array([1, 2, 3]);  
            vec.for_each(|value| { *acc_ref += value; });
```

> [Source code: noir\_stdlib/src/collections/bounded\_vec.nr#L890-L893](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/bounded_vec.nr#L890-L893)

## for\_eachi```
pub fn for_eachi<Env>(self, f: fn[Env](u32, T) -> ())
```

Calls a closure on each element in this vector, along with its index in the vector.

Example:

bounded-vec-for-eachi-example

```
let vec: BoundedVec<u32, 3> = BoundedVec::from_array([1, 2, 3]);  
            vec.for_eachi(|i, value| { *acc_ref += i * value; });
```

> [Source code: noir\_stdlib/src/collections/bounded\_vec.nr#L962-L965](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/bounded_vec.nr#L962-L965)

## any```
pub fn any<Env>(self, predicate: fn[Env](T) -> bool) -> bool
```

Returns true if the given predicate returns true for any element
in this vector.

Example:

bounded-vec-any-example

```
let mut v: BoundedVec<u32, 3> = BoundedVec::new();  
    v.extend_from_array([2, 4, 6]);  
  
    let all_even = !v.any(|elem: u32| elem % 2 != 0);  
    assert(all_even);
```

> [Source code: test\_programs/noir\_test\_success/bounded\_vec/src/main.nr#L244-L250](https://github.com/noir-lang/noir/blob/master/test_programs/noir_test_success/bounded_vec/src/main.nr#L244-L250)

---


# HashMap

Source: https://noir-lang.org/docs/noir/standard_library/containers/hashmap

Version: v1.0.0-beta.17

On this page

`HashMap<Key, Value, MaxLen, Hasher>` is used to efficiently store and look up key-value pairs.

`HashMap` is a bounded type which can store anywhere from zero to `MaxLen` total elements.
Note that due to hash collisions, the actual maximum number of elements stored by any particular
hashmap is likely lower than `MaxLen`. This is true even with cryptographic hash functions since
every hash value will be performed modulo `MaxLen`.

Example:

```
// Create a mapping from Fields to u32s with a maximum length of 12  
// using a poseidon2 hasher  
use poseidon::poseidon2::Poseidon2Hasher;  
let mut map: HashMap<Field, u32, 12, BuildHasherDefault<Poseidon2Hasher>> = HashMap::default();  
  
map.insert(1, 2);  
map.insert(3, 4);  
  
let two = map.get(1).unwrap();
```

## Methods## defaultdefault

```
impl<K, V, let N: u32, B> Default for HashMap<K, V, N, B>  
where  
    B: BuildHasher + Default,  
{  
    /// Constructs an empty HashMap.  
    ///  
    /// Example:  
    ///  
    /// ```noir  
    /// let hashmap: HashMap<u8, u32, 10, BuildHasherDefault<Poseidon2Hasher>> = HashMap::default();  
    /// assert(hashmap.is_empty());  
    /// ```  
    fn default() -> Self {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L685-L699](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L685-L699)

Creates a fresh, empty HashMap.

When using this function, always make sure to specify the maximum size of the hash map.

This is the same `default` from the `Default` implementation given further below. It is
repeated here for convenience since it is the recommended way to create a hashmap.

Example:

default\_example

```
let hashmap: HashMap<u8, u32, 10, BuildHasherDefault<Poseidon2Hasher>> = HashMap::default();  
    assert(hashmap.is_empty());
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L232-L235](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L232-L235)

Because `HashMap` has so many generic arguments that are likely to be the same throughout
your program, it may be helpful to create a type alias:

type\_alias

```
type MyMap = HashMap<u8, u32, 10, BuildHasherDefault<Poseidon2Hasher>>;
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L226-L228](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L226-L228)

## with\_hasherwith\_hasher

```
pub fn with_hasher(_build_hasher: B) -> Self  
    where  
        B: BuildHasher,  
    {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L103-L108](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L103-L108)

Creates a hashmap with an existing `BuildHasher`. This can be used to ensure multiple
hashmaps are created with the same hasher instance.

Example:

with\_hasher\_example

```
let my_hasher: BuildHasherDefault<Poseidon2Hasher> = Default::default();  
    let hashmap: HashMap<u8, u32, 10, BuildHasherDefault<Poseidon2Hasher>> =  
        HashMap::with_hasher(my_hasher);  
    assert(hashmap.is_empty());
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L236-L241](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L236-L241)

## getget

```
pub fn get(self, key: K) -> Option<V>  
    where  
        K: Eq + Hash,  
        B: BuildHasher,  
    {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L471-L477](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L471-L477)

Retrieves a value from the hashmap, returning `Option::none()` if it was not found.

Example:

get\_example

```
fn get_example(map: HashMap<Field, Field, 5, BuildHasherDefault<Poseidon2Hasher>>) {  
    let x = map.get(12);  
  
    if x.is_some() {  
        assert(x.unwrap() == 42);  
    }  
}
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L321-L329](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L321-L329)

## insertinsert

```
pub fn insert(&mut self, key: K, value: V)  
    where  
        K: Eq + Hash,  
        B: BuildHasher,  
    {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L512-L518](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L512-L518)

Inserts a new key-value pair into the map. If the key was already in the map, its
previous value will be overridden with the newly provided one.

Example:

insert\_example

```
let mut map: HashMap<Field, Field, 5, BuildHasherDefault<Poseidon2Hasher>> = HashMap::default();  
    map.insert(12, 42);  
    assert(map.len() == 1);
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L242-L246](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L242-L246)

## removeremove

```
pub fn remove(&mut self, key: K)  
    where  
        K: Eq + Hash,  
        B: BuildHasher,  
    {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L567-L573](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L567-L573)

Removes the given key-value pair from the map. If the key was not already present
in the map, this does nothing.

Example:

remove\_example

```
map.remove(12);  
    assert(map.is_empty());  
  
    // If a key was not present in the map, remove does nothing  
    map.remove(12);  
    assert(map.is_empty());
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L249-L256](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L249-L256)

## is\_emptyis\_empty

```
pub fn is_empty(self) -> bool {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L166-L168](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L166-L168)

True if the length of the hash map is empty.

Example:

is\_empty\_example

```
assert(map.is_empty());  
  
    map.insert(1, 2);  
    assert(!map.is_empty());  
  
    map.remove(1);  
    assert(map.is_empty());
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L257-L265](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L257-L265)

## lenlen

```
pub fn len(self) -> u32 {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L430-L432](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L430-L432)

Returns the current length of this hash map.

Example:

len\_example

```
// This is equivalent to checking map.is_empty()  
    assert(map.len() == 0);  
  
    map.insert(1, 2);  
    map.insert(3, 4);  
    map.insert(5, 6);  
    assert(map.len() == 3);  
  
    // 3 was already present as a key in the hash map, so the length is unchanged  
    map.insert(3, 7);  
    assert(map.len() == 3);  
  
    map.remove(1);  
    assert(map.len() == 2);
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L266-L281](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L266-L281)

## capacitycapacity

```
pub fn capacity(_self: Self) -> u32 {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L452-L454](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L452-L454)

Returns the maximum capacity of this hashmap. This is always equal to the capacity
specified in the hashmap's type.

Unlike hashmaps in general purpose programming languages, hashmaps in Noir have a
static capacity that does not increase as the map grows larger. Thus, this capacity
is also the maximum possible element count that can be inserted into the hashmap.
Due to hash collisions (modulo the hashmap length), it is likely the actual maximum
element count will be lower than the full capacity.

Example:

capacity\_example

```
let empty_map: HashMap<Field, Field, 42, BuildHasherDefault<Poseidon2Hasher>> =  
        HashMap::default();  
    assert(empty_map.len() == 0);  
    assert(empty_map.capacity() == 42);
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L282-L287](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L282-L287)

## clearclear

```
pub fn clear(&mut self) {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L123-L125](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L123-L125)

Clears the hashmap, removing all key-value pairs from it.

Example:

clear\_example

```
assert(!map.is_empty());  
    map.clear();  
    assert(map.is_empty());
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L288-L292](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L288-L292)

## contains\_keycontains\_key

```
pub fn contains_key(self, key: K) -> bool  
    where  
        K: Hash + Eq,  
        B: BuildHasher,  
    {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L143-L149](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L143-L149)

True if the hashmap contains the given key. Unlike `get`, this will not also return
the value associated with the key.

Example:

contains\_key\_example

```
if map.contains_key(7) {  
        let value = map.get(7);  
        assert(value.is_some());  
    } else {  
        println("No value for key 7!");  
    }
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L293-L300](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L293-L300)

## entriesentries

```
pub fn entries(self) -> BoundedVec<(K, V), N> {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L190-L192](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L190-L192)

Returns a vector of each key-value pair present in the hashmap.

The length of the returned vector is always equal to the length of the hashmap.

Example:

entries\_example

```
let entries = map.entries();  
  
    // The length of a hashmap may not be compile-time known, so we  
    // need to loop over its capacity instead  
    for i in 0..map.capacity() {  
        if i < entries.len() {  
            let (key, value) = entries.get(i);  
            println(f"{key} -> {value}");  
        }  
    }
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L332-L343](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L332-L343)

## keyskeys

```
pub fn keys(self) -> BoundedVec<K, N> {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L229-L231](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L229-L231)

Returns a vector of each key present in the hashmap.

The length of the returned vector is always equal to the length of the hashmap.

Example:

keys\_example

```
let keys = map.keys();  
  
    for i in 0..keys.max_len() {  
        if i < keys.len() {  
            let key = keys.get_unchecked(i);  
            let value = map.get(key).unwrap_unchecked();  
            println(f"{key} -> {value}");  
        }  
    }
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L344-L354](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L344-L354)

## valuesvalues

```
pub fn values(self) -> BoundedVec<V, N> {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L266-L268](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L266-L268)

Returns a vector of each value present in the hashmap.

The length of the returned vector is always equal to the length of the hashmap.

Example:

values\_example

```
let values = map.values();  
  
    for i in 0..values.max_len() {  
        if i < values.len() {  
            let value = values.get_unchecked(i);  
            println(f"Found value {value}");  
        }  
    }
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L355-L364](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L355-L364)

## iter\_mutiter\_mut

```
pub fn iter_mut(&mut self, f: fn(K, V) -> (K, V))  
    where  
        K: Eq + Hash,  
        B: BuildHasher,  
    {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L303-L309](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L303-L309)

Iterates through each key-value pair of the HashMap, setting each key-value pair to the
result returned from the given function.

Note that since keys can be mutated, the HashMap needs to be rebuilt as it is iterated
through. If this is not desired, use `iter_values_mut` if only values need to be mutated,
or `entries` if neither keys nor values need to be mutated.

The iteration order is left unspecified. As a result, if two keys are mutated to become
equal, which of the two values that will be present for the key in the resulting map is also unspecified.

Example:

iter\_mut\_example

```
// Add 1 to each key in the map, and double the value associated with that key.  
    map.iter_mut(|k, v| (k + 1, v * 2));
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L368-L371](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L368-L371)

## iter\_keys\_mutiter\_keys\_mut

```
pub fn iter_keys_mut(&mut self, f: fn(K) -> K)  
    where  
        K: Eq + Hash,  
        B: BuildHasher,  
    {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L341-L347](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L341-L347)

Iterates through the HashMap, mutating each key to the result returned from
the given function.

Note that since keys can be mutated, the HashMap needs to be rebuilt as it is iterated
through. If only iteration is desired and the keys are not intended to be mutated,
prefer using `entries` instead.

The iteration order is left unspecified. As a result, if two keys are mutated to become
equal, which of the two values that will be present for the key in the resulting map is also unspecified.

Example:

iter\_keys\_mut\_example

```
// Double each key, leaving the value associated with that key untouched  
    map.iter_keys_mut(|k| k * 2);
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L372-L375](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L372-L375)

## iter\_values\_mutiter\_values\_mut

```
pub fn iter_values_mut(&mut self, f: fn(V) -> V) {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L373-L375](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L373-L375)

Iterates through the HashMap, applying the given function to each value and mutating the
value to equal the result. This function is more efficient than `iter_mut` and `iter_keys_mut`
because the keys are untouched and the underlying hashmap thus does not need to be reordered.

Example:

iter\_values\_mut\_example

```
// Halve each value  
    map.iter_values_mut(|v| v / 2);
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L376-L379](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L376-L379)

## retainretain

```
pub fn retain(&mut self, f: fn(K, V) -> bool) {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L394-L396](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L394-L396)

Retains only the key-value pairs for which the given function returns true.
Any key-value pairs for which the function returns false will be removed from the map.

Example:

retain\_example

```
map.retain(|k, v| (k != 0) & (v != 0));
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L304-L306](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L304-L306)

## Trait Implementations## defaultdefault

```
impl<K, V, let N: u32, B> Default for HashMap<K, V, N, B>  
where  
    B: BuildHasher + Default,  
{  
    /// Constructs an empty HashMap.  
    ///  
    /// Example:  
    ///  
    /// ```noir  
    /// let hashmap: HashMap<u8, u32, 10, BuildHasherDefault<Poseidon2Hasher>> = HashMap::default();  
    /// assert(hashmap.is_empty());  
    /// ```  
    fn default() -> Self {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L685-L699](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L685-L699)

Constructs an empty HashMap.

Example:

default\_example

```
let hashmap: HashMap<u8, u32, 10, BuildHasherDefault<Poseidon2Hasher>> = HashMap::default();  
    assert(hashmap.is_empty());
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L232-L235](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L232-L235)

## eqeq

```
impl<K, V, let N: u32, B> Eq for HashMap<K, V, N, B>  
where  
    K: Eq + Hash,  
    V: Eq,  
    B: BuildHasher,  
{  
    /// Checks if two HashMaps are equal.  
    ///  
    /// Example:  
    ///  
    /// ```noir  
    /// let mut map1: HashMap<Field, u64, 4, BuildHasherDefault<Poseidon2Hasher>> = HashMap::default();  
    /// let mut map2: HashMap<Field, u64, 4, BuildHasherDefault<Poseidon2Hasher>> = HashMap::default();  
    ///  
    /// map1.insert(1, 2);  
    /// map1.insert(3, 4);  
    ///  
    /// map2.insert(3, 4);  
    /// map2.insert(1, 2);  
    ///  
    /// assert(map1 == map2);  
    /// ```  
    fn eq(self, other: HashMap<K, V, N, B>) -> bool {
```

> [Source code: noir\_stdlib/src/collections/map.nr#L634-L658](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/collections/map.nr#L634-L658)

Checks if two HashMaps are equal.

Example:

eq\_example

```
let mut map1: HashMap<Field, u64, 4, BuildHasherDefault<Poseidon2Hasher>> = HashMap::default();  
    let mut map2: HashMap<Field, u64, 4, BuildHasherDefault<Poseidon2Hasher>> = HashMap::default();  
  
    map1.insert(1, 2);  
    map1.insert(3, 4);  
  
    map2.insert(3, 4);  
    map2.insert(1, 2);  
  
    assert(map1 == map2);
```

> [Source code: test\_programs/execution\_success/hashmap/src/main.nr#L307-L318](https://github.com/noir-lang/noir/blob/master/test_programs/execution_success/hashmap/src/main.nr#L307-L318)

---


# Vectors

Source: https://noir-lang.org/docs/noir/standard_library/containers/vec

Version: v1.0.0-beta.17

On this page

Experimental Feature

This feature is experimental. The documentation may be incomplete or out of date, which means it could change in future versions, potentially causing unexpected behavior or not working as expected.

**Contributions Welcome:** If you notice any inaccuracies or potential improvements, please consider contributing. Visit our GitHub repository to make your contributions: [Contribute Here](https://github.com/noir-lang/noir).

A vector is a collection type similar to Rust's `Vec<T>` type. In Noir, it is a convenient way to use slices as mutable arrays.

Example:

```
let mut vector: Vec<Field> = Vec::new();  
for i in 0..5 {  
    vector.push(i);  
}  
assert(vector.len() == 5);
```

## Methods## newCreates a new, empty vector.

```
pub fn new() -> Self
```

Example:

```
let empty_vector: Vec<Field> = Vec::new();  
assert(empty_vector.len() == 0);
```

## from\_sliceCreates a vector containing each element from a given slice. Mutations to the resulting vector will not affect the original slice.

```
pub fn from_slice(slice: [T]) -> Self
```

Example:

```
let slice: [Field] = &[1, 2, 3];  
let vector_from_slice = Vec::from_slice(slice);  
assert(vector_from_slice.len() == 3);
```

## lenReturns the number of elements in the vector.

```
pub fn len(self) -> Field
```

Example:

```
let empty_vector: Vec<Field> = Vec::new();  
assert(empty_vector.len() == 0);
```

## getRetrieves an element from the vector at a given index. Panics if the index points beyond the vector's end.

```
pub fn get(self, index: u32) -> T
```

Example:

```
let vector: Vec<Field> = Vec::from_slice(&[10, 20, 30]);  
assert(vector.get(1) == 20);
```

## set```
pub fn set(&mut self: Self, index: u32, value: T)
```

Writes an element to the vector at the given index, starting from zero.

Panics if the index points beyond the vector's end.

Example:

```
let vector: Vec<Field> = Vec::from_slice(&[10, 20, 30]);  
assert(vector.get(1) == 20);  
vector.set(1, 42);  
assert(vector.get(1) == 42);
```

## pushAdds a new element to the vector's end, returning a new vector with a length one greater than the original unmodified vector.

```
pub fn push(&mut self, elem: T)
```

Example:

```
let mut vector: Vec<Field> = Vec::new();  
vector.push(10);  
assert(vector.len() == 1);
```

## popRemoves an element from the vector's end, returning a new vector with a length one less than the original vector, along with the removed element. Panics if the vector's length is zero.

```
pub fn pop(&mut self) -> T
```

Example:

```
let mut vector = Vec::from_slice(&[10, 20]);  
let popped_elem = vector.pop();  
assert(popped_elem == 20);  
assert(vector.len() == 1);
```

## insertInserts an element at a specified index, shifting subsequent elements to the right.

```
pub fn insert(&mut self, index: u32, elem: T)
```

Example:

```
let mut vector = Vec::from_slice(&[10, 30]);  
vector.insert(1, 20);  
assert(vector.get(1) == 20);
```

## removeRemoves an element at a specified index, shifting subsequent elements to the left, and returns the removed element.

```
pub fn remove(&mut self, index: Field) -> T
```

Example:

```
let mut vector = Vec::from_slice(&[10, 20, 30]);  
let removed_elem = vector.remove(1);  
assert(removed_elem == 20);  
assert(vector.len() == 2);
```

---


# fmtstr

Source: https://noir-lang.org/docs/noir/standard_library/fmtstr

Version: v1.0.0-beta.17

On this page

`fmtstr<N, T>` is the type resulting from using format string (`f"..."`).

## Methods## quoted\_contentsquoted\_contents

```
pub comptime fn quoted_contents(self) -> Quoted {}
```

> [Source code: noir\_stdlib/src/meta/format\_string.nr#L6-L8](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/format_string.nr#L6-L8)

Returns the format string contents (that is, without the leading and trailing double quotes) as a `Quoted` value.

## as\_quoted\_stras\_quoted\_str

```
pub comptime fn as_quoted_str(self) -> Quoted {
```

> [Source code: noir\_stdlib/src/meta/format\_string.nr#L11-L13](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/format_string.nr#L11-L13)

Returns the format string contents (with the leading and trailing double quotes) as a `Quoted` string literal (not a format string literal).

Example:

as\_quoted\_str\_test

```
comptime {  
        let x = 1;  
        let f: str<_> = f"x = {x}".as_quoted_str!();  
        assert_eq(f, "x = 0x01");  
    }
```

> [Source code: test\_programs/compile\_success\_empty/comptime\_fmt\_strings/src/main.nr#L19-L25](https://github.com/noir-lang/noir/blob/master/test_programs/compile_success_empty/comptime_fmt_strings/src/main.nr#L19-L25)

---


# Is Unconstrained Function

Source: https://noir-lang.org/docs/noir/standard_library/is_unconstrained

Version: v1.0.0-beta.17

It's very common for functions in circuits to take unconstrained hints of an expensive computation and then verify it. This is done by running the hint in an unconstrained context and then verifying the result in a constrained context.

When a function is marked as unconstrained, any subsequent functions that it calls will also be run in an unconstrained context. However, if we are implementing a library function, other users might call it within an unconstrained context or a constrained one. Generally, in an unconstrained context we prefer just computing the result instead of taking a hint of it and verifying it, since that'd mean doing the same computation twice:

```
fn my_expensive_computation(){  
  ...  
}  
  
unconstrained fn my_expensive_computation_hint(){  
  my_expensive_computation()  
}  
  
pub fn external_interface(){  
  my_expensive_computation_hint();  
  // verify my_expensive_computation: If external_interface is called from unconstrained, this is redundant  
  ...  
}
```

In order to improve the performance in an unconstrained context you can use the function at `std::runtime::is_unconstrained() -> bool`:

```
use dep::std::runtime::is_unconstrained;  
  
fn my_expensive_computation(){  
  ...  
}  
  
unconstrained fn my_expensive_computation_hint(){  
  my_expensive_computation()  
}  
  
pub fn external_interface(){  
  if is_unconstrained() {  
    my_expensive_computation();  
  } else {  
    my_expensive_computation_hint();  
    // verify my_expensive_computation  
    ...  
  }  
}
```

The is\_unconstrained result is resolved at compile time, so in unconstrained contexts the compiler removes the else branch, and in constrained contexts the compiler removes the if branch, reducing the amount of compute necessary to run external\_interface.

Note that using `is_unconstrained` in a `comptime` context will also return `true`:

```
fn main() {  
    comptime {  
        assert(is_unconstrained());  
    }  
}
```

---


# Logging

Source: https://noir-lang.org/docs/noir/standard_library/logging

Version: v1.0.0-beta.17

The standard library provides two familiar statements you can use: `println` and `print`. Despite being a limited implementation of rust's `println!` and `print!` macros, these constructs can be useful for debugging.

You can print the output of both statements in your Noir code by using the `nargo execute` command or the `--show-output` flag when using `nargo test` (provided there are print statements in your tests).

It is recommended to use `nargo execute` if you want to debug failing constraints with `println` or `print` statements. This is due to every input in a test being a constant rather than a witness, so we issue an error during compilation while we only print during execution (which comes after compilation). Neither `println`, nor `print` are callable for failed constraints caught at compile time.

Both `print` and `println` are generic functions which can work on integers, fields, strings, and even structs or expressions. Note however, that slices are currently unsupported. For example:

```
struct Person {  
    age: u32,  
    height: u32,  
}  
  
fn main(age: u32, height: u32) {  
    let person = Person {  
        age: age,  
        height: height,  
    };  
    println(person);  
    println(age + height);  
    println("Hello world!");  
}
```

You can print different types in the same statement (including strings) with a type called `fmtstr`. It can be specified in the same way as a normal string, just prepended with an "f" character:

```
  let fmt_str = f"i: {i}, j: {j}";  
  println(fmt_str);  
  
  let s = myStruct { y: x, x: y };  
  println(s);  
  
  println(f"i: {i}, s: {s}");  
  
  println(x);  
  println([x, y]);  
  
  let foo = fooStruct { my_struct: s, foo: 15 };  
  println(f"s: {s}, foo: {foo}");  
  
  println(15);       // prints 0x0f, implicit Field  
  println(-1 as u8); // prints 255  
  println(-1 as i8); // prints -1
```

Examples shown above are interchangeable between the two `print` statements:

```
let person = Person { age : age, height : height };  
  
println(person);  
print(person);  
  
println("Hello world!"); // Prints with a newline at the end of the input  
print("Hello world!");   // Prints the input and keeps cursor on the same line
```

---


# Memory Module

Source: https://noir-lang.org/docs/noir/standard_library/mem

Version: v1.0.0-beta.17

```
fn zeroed<T>() -> T
```

Returns a zeroed value of any type.
This function is generally unsafe to use as the zeroed bit pattern is not guaranteed to be valid for all types.
It can however, be useful in cases when the value is guaranteed not to be used such as in a BoundedVec library implementing a growable vector, up to a certain length, backed by an array.
The array can be initialized with zeroed values which are guaranteed to be inaccessible until the vector is pushed to.
Similarly, enumerations in noir can be implemented using this method by providing zeroed values for the unused variants.

This function currently supports the following types:

* Field
* Bool
* Uint
* Array
* Slice
* String
* Tuple
* Functions

Using it on other types could result in unexpected behavior.

# `std::mem::checked_transmute`

```
fn checked_transmute<T, U>(value: T) -> U
```

Transmutes a value of one type into the same value but with a new type `U`.

This function is safe to use since both types are asserted to be equal later during compilation after the concrete values for generic types become known.
This function is useful for cases where the compiler may fail a type check that is expected to pass where
a user knows the two types to be equal. For example, when using arithmetic generics there are cases the compiler
does not see as equal, such as `[Field; N*(A + B)]` and `[Field; N*A + N*B]`, which users may know to be equal.
In these cases, `checked_transmute` can be used to cast the value to the desired type while also preserving safety
by checking this equality once `N`, `A`, `B` are fully resolved.

Note that since this safety check is performed after type checking rather than during, no error is issued if the function
containing `checked_transmute` is never called.

# `std::mem::array_refcount`

```
fn array_refcount<T, let N: u32>(array: [T; N]) -> u32 {}
```

Returns the internal reference count of an array value in unconstrained code.

Arrays only have reference count in unconstrained code - using this anywhere
else will return zero.

This function is mostly intended for debugging compiler optimizations but can also be used
to find where array copies may be happening in unconstrained code by placing it before array
mutations.

# `std::mem::slice_refcount`

```
fn slice_refcount<T>(slice: [T]) -> u32 {}
```

Returns the internal reference count of a slice value in unconstrained code.

Slices only have reference count in unconstrained code - using this anywhere
else will return zero.

This function is mostly intended for debugging compiler optimizations but can also be used
to find where slice copies may be happening in unconstrained code by placing it before slice
mutations.

---


# Metaprogramming

Source: https://noir-lang.org/docs/noir/standard_library/meta

Version: v1.0.0-beta.17

On this page

`std::meta` is the entry point for Noir's metaprogramming API. This consists of `comptime` functions
and types used for inspecting and modifying Noir programs.

## Functions## type\_oftype\_of

```
pub comptime fn type_of<T>(x: T) -> Type {}
```

> [Source code: noir\_stdlib/src/meta/mod.nr#L29-L31](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/mod.nr#L29-L31)

Returns the type of a variable at compile-time.

Example:

```
comptime {  
    let x: i32 = 1;  
    let x_type: Type = std::meta::type_of(x);  
  
    assert_eq(x_type, quote { i32 }.as_type());  
}
```

## unquoteunquote

```
pub comptime fn unquote(code: Quoted) -> Quoted {
```

> [Source code: noir\_stdlib/src/meta/mod.nr#L21-L23](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/mod.nr#L21-L23)

Unquotes the passed-in token stream where this function was called.

Example:

```
comptime {  
    let code = quote { 1 + 2 };  
  
    // let x = 1 + 2;  
    let x = unquote!(code);  
}
```

## derivederive

```
#[varargs]  
pub comptime fn derive(s: TypeDefinition, traits: [TraitDefinition]) -> Quoted {
```

> [Source code: noir\_stdlib/src/meta/mod.nr#L50-L53](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/mod.nr#L50-L53)

Attribute placed on type definitions.

Creates a trait impl for each trait passed in as an argument.
To do this, the trait must have a derive handler registered
with `derive_via` beforehand. The traits in the stdlib that
can be derived this way are `Eq`, `Ord`, `Default`, and `Hash`.

Example:

```
#[derive(Eq, Default)]  
struct Foo<T> {  
    x: i32,  
    y: T,  
}  
  
fn main() {  
    let foo1 = Foo::default();  
    let foo2 = Foo { x: 0, y: &[0] };  
    assert_eq(foo1, foo2);  
}
```

## derive\_viaderive\_via\_signature

```
pub comptime fn derive_via(t: TraitDefinition, f: DeriveFunction) {
```

> [Source code: noir\_stdlib/src/meta/mod.nr#L70-L72](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/mod.nr#L70-L72)

Attribute placed on trait definitions.

Registers a function to create impls for the given trait
when the trait is used in a `derive` call. Users may use
this to register their own functions to enable their traits
to be derived by `derive`.

Because this function requires a function as an argument which
should produce a trait impl for any given type definition, users may find
it helpful to use a function like `std::meta::make_trait_impl` to
help creating these impls.

Example:

```
#[derive_via(derive_do_nothing)]  
trait DoNothing {  
    fn do_nothing(self);  
}  
  
comptime fn derive_do_nothing(s: TypeDefinition) -> Quoted {  
    let typ = s.as_type();  
    quote {  
        impl DoNothing for $typ {  
            fn do_nothing(self) {  
                println("Nothing");  
            }  
        }  
    }  
}
```

As another example, `derive_eq` in the stdlib is used to derive the `Eq`
trait for any type definition. It makes use of `make_trait_impl` to do this:

derive\_eq

```
comptime fn derive_eq(s: TypeDefinition) -> Quoted {  
    let signature = quote { fn eq(_self: Self, _other: Self) -> bool };  
    let for_each_field = |name| quote { (_self.$name == _other.$name) };  
    let body = |fields| {  
        if s.fields_as_written().len() == 0 {  
            quote { true }  
        } else {  
            fields  
        }  
    };  
    crate::meta::make_trait_impl(  
        s,  
        quote { $crate::cmp::Eq },  
        signature,  
        for_each_field,  
        quote { & },  
        body,  
    )  
}
```

> [Source code: noir\_stdlib/src/cmp.nr#L10-L30](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/cmp.nr#L10-L30)

## make\_trait\_implmake\_trait\_impl

```
pub comptime fn make_trait_impl<Env1, Env2>(  
    s: TypeDefinition,  
    trait_name: Quoted,  
    function_signature: Quoted,  
    for_each_field: fn[Env1](Quoted) -> Quoted,  
    join_fields_with: Quoted,  
    body: fn[Env2](Quoted) -> Quoted,  
) -> Quoted {
```

> [Source code: noir\_stdlib/src/meta/mod.nr#L89-L98](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/mod.nr#L89-L98)

A helper function to more easily create trait impls while deriving traits.

Note that this function only works for traits which:

1. Have only one method
2. Have no generics on the trait itself.

* E.g. Using this on a trait such as `trait Foo<T> { ... }` will result in the
  generated impl incorrectly missing the `T` generic.

If your trait fits these criteria then `make_trait_impl` is likely the easiest
way to write your derive handler. The arguments are as follows:

* `s`: The type definition to make the impl for
* `trait_name`: The name of the trait to derive. E.g. `quote { Eq }`.
* `function_signature`: The signature of the trait method to derive. E.g. `fn eq(self, other: Self) -> bool`.
* `for_each_field`: An operation to be performed on each field. E.g. `|name| quote { (self.$name == other.$name) }`.
* `join_fields_with`: A separator to join each result of `for_each_field` with.
  E.g. `quote { & }`. You can also use an empty `quote {}` for no separator.
* `body`: The result of the field operations is passed into this function for any final processing.
  This is the place to insert any setup/teardown code the trait requires. If the trait doesn't require
  any such code, you can return the body as-is: `|body| body`.

Example deriving `Hash`:

derive\_hash

```
comptime fn derive_hash(s: TypeDefinition) -> Quoted {  
    let name = quote { $crate::hash::Hash };  
    let signature = quote { fn hash<H>(_self: Self, _state: &mut H) where H: $crate::hash::Hasher };  
    let for_each_field = |name| quote { _self.$name.hash(_state); };  
    crate::meta::make_trait_impl(  
        s,  
        name,  
        signature,  
        for_each_field,  
        quote {},  
        |fields| fields,  
    )  
}
```

> [Source code: noir\_stdlib/src/hash/mod.nr#L156-L170](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/hash/mod.nr#L156-L170)

Example deriving `Ord`:

derive\_ord

```
comptime fn derive_ord(s: TypeDefinition) -> Quoted {  
    let name = quote { $crate::cmp::Ord };  
    let signature = quote { fn cmp(_self: Self, _other: Self) -> $crate::cmp::Ordering };  
    let for_each_field = |name| quote {  
        if result == $crate::cmp::Ordering::equal() {  
            result = _self.$name.cmp(_other.$name);  
        }  
    };  
    let body = |fields| quote {  
        let mut result = $crate::cmp::Ordering::equal();  
        $fields  
        result  
    };  
    crate::meta::make_trait_impl(s, name, signature, for_each_field, quote {}, body)  
}
```

> [Source code: noir\_stdlib/src/cmp.nr#L223-L239](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/cmp.nr#L223-L239)

---


# CtString

Source: https://noir-lang.org/docs/noir/standard_library/meta/ctstring

Version: v1.0.0-beta.17

On this page

`std::meta::ctstring` contains methods on the built-in `CtString` type which is
a compile-time, dynamically-sized string type. Compared to `str<N>` and `fmtstr<N, T>`,
`CtString` is useful because its size does not need to be specified in its type. This
can be used for formatting items at compile-time or general string handling in `comptime`
code.

Since `fmtstr`s can be converted into `CtString`s, you can make use of their formatting
abilities in CtStrings by formatting in `fmtstr`s then converting the result to a CtString
afterward.

## Traits## AsCtStringas-ctstring

```
pub trait AsCtString {  
    comptime fn as_ctstring(self) -> CtString;  
}
```

> [Source code: noir\_stdlib/src/meta/ctstring.nr#L44-L48](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/ctstring.nr#L44-L48)

Converts an object into a compile-time string.

Implementations:

```
impl<let N: u32> AsCtString for str<N> { ... }  
impl<let N: u32, T> AsCtString for fmtstr<N, T> { ... }
```

## Methods## newnew

```
pub comptime fn new() -> Self {
```

> [Source code: noir\_stdlib/src/meta/ctstring.nr#L4-L6](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/ctstring.nr#L4-L6)

Creates an empty `CtString`.

## append\_strappend\_str

```
pub comptime fn append_str<let N: u32>(self, s: str<N>) -> Self {
```

> [Source code: noir\_stdlib/src/meta/ctstring.nr#L12-L14](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/ctstring.nr#L12-L14)

Returns a new CtString with the given str appended onto the end.

## append\_fmtstrappend\_fmtstr

```
pub comptime fn append_fmtstr<let N: u32, T>(self, s: fmtstr<N, T>) -> Self {
```

> [Source code: noir\_stdlib/src/meta/ctstring.nr#L18-L20](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/ctstring.nr#L18-L20)

Returns a new CtString with the given fmtstr appended onto the end.

## as\_quoted\_stras\_quoted\_str

```
pub comptime fn as_quoted_str(self) -> Quoted {
```

> [Source code: noir\_stdlib/src/meta/ctstring.nr#L27-L29](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/ctstring.nr#L27-L29)

Returns a quoted string literal from this string's contents.

There is no direct conversion from a `CtString` to a `str<N>` since
the size would not be known. To get around this, this function can
be used in combination with macro insertion (`!`) to insert this string
literal at this function's call site.

Example:

as\_quoted\_str\_example

```
let my_ctstring = "foo bar".as_ctstring();  
            let my_str: str<7> = my_ctstring.as_quoted_str!();  
  
            assert_eq(crate::meta::type_of(my_str), quote { str<7> }.as_type());
```

> [Source code: noir\_stdlib/src/meta/ctstring.nr#L95-L100](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/ctstring.nr#L95-L100)

## Trait Implementations```
impl Eq for CtString  
impl Hash for CtString  
impl Append for CtString
```

---


# Expr

Source: https://noir-lang.org/docs/noir/standard_library/meta/expr

Version: v1.0.0-beta.17

On this page

`std::meta::expr` contains methods on the built-in `Expr` type for quoted, syntactically valid expressions.

## Methods## as\_arrayas\_array

```
pub comptime fn as_array(self) -> Option<[Expr]> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L10-L12](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L10-L12)

If this expression is an array, this returns a slice of each element in the array.

## as\_assertas\_assert

```
pub comptime fn as_assert(self) -> Option<(Expr, Option<Expr>)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L16-L18](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L16-L18)

If this expression is an assert, this returns the assert expression and the optional message.

## as\_assert\_eqas\_assert\_eq

```
pub comptime fn as_assert_eq(self) -> Option<(Expr, Expr, Option<Expr>)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L23-L25](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L23-L25)

If this expression is an assert\_eq, this returns the left-hand-side and right-hand-side
expressions, together with the optional message.

## as\_assignas\_assign

```
pub comptime fn as_assign(self) -> Option<(Expr, Expr)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L30-L32](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L30-L32)

If this expression is an assignment, this returns a tuple with the left hand side
and right hand side in order.

## as\_binary\_opas\_binary\_op

```
pub comptime fn as_binary_op(self) -> Option<(Expr, BinaryOp, Expr)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L37-L39](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L37-L39)

If this expression is a binary operator operation `<lhs> <op> <rhs>`,
return the left-hand side, operator, and the right-hand side of the operation.

## as\_blockas\_block

```
pub comptime fn as_block(self) -> Option<[Expr]> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L44-L46](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L44-L46)

If this expression is a block `{ stmt1; stmt2; ...; stmtN }`, return
a slice containing each statement.

## as\_boolas\_bool

```
pub comptime fn as_bool(self) -> Option<bool> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L50-L52](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L50-L52)

If this expression is a boolean literal, return that literal.

## as\_castas\_cast

```
#[builtin(expr_as_cast)]  
    pub comptime fn as_cast(self) -> Option<(Expr, UnresolvedType)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L56-L59](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L56-L59)

If this expression is a cast expression (`expr as type`), returns the casted
expression and the type to cast to.

## as\_comptimeas\_comptime

```
pub comptime fn as_comptime(self) -> Option<[Expr]> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L64-L66](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L64-L66)

If this expression is a `comptime { stmt1; stmt2; ...; stmtN }` block,
return each statement in the block.

## as\_constructoras\_constructor

```
pub comptime fn as_constructor(self) -> Option<(UnresolvedType, [(Quoted, Expr)])> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L71-L73](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L71-L73)

If this expression is a constructor `Type { field1: expr1, ..., fieldN: exprN }`,
return the type and the fields.

## as\_foras\_for

```
pub comptime fn as_for(self) -> Option<(Quoted, Expr, Expr)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L78-L80](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L78-L80)

If this expression is a for statement over a single expression, return the identifier,
the expression and the for loop body.

## as\_for\_rangeas\_for

```
pub comptime fn as_for(self) -> Option<(Quoted, Expr, Expr)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L78-L80](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L78-L80)

If this expression is a for statement over a range, return the identifier,
the range start, the range end and the for loop body.

## as\_function\_callas\_function\_call

```
pub comptime fn as_function_call(self) -> Option<(Expr, [Expr])> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L92-L94](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L92-L94)

If this expression is a function call `foo(arg1, ..., argN)`, return
the function and a slice of each argument.

## as\_ifas\_if

```
pub comptime fn as_if(self) -> Option<(Expr, Expr, Option<Expr>)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L100-L102](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L100-L102)

If this expression is an `if condition { then_branch } else { else_branch }`,
return the condition, then branch, and else branch. If there is no else branch,
`None` is returned for that branch instead.

## as\_indexas\_index

```
pub comptime fn as_index(self) -> Option<(Expr, Expr)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L107-L109](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L107-L109)

If this expression is an index into an array `array[index]`, return the
array and the index.

## as\_integeras\_integer

```
pub comptime fn as_integer(self) -> Option<(Field, bool)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L114-L116](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L114-L116)

If this expression is an integer literal, return the integer as a field
as well as whether the integer is negative (true) or not (false).

## as\_lambdaas\_lambda

```
pub comptime fn as_lambda(  
        self,  
    ) -> Option<([(Expr, Option<UnresolvedType>)], Option<UnresolvedType>, Expr)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L120-L124](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L120-L124)

If this expression is a lambda, returns the parameters, return type and body.

## as\_letas\_let

```
pub comptime fn as_let(self) -> Option<(Expr, Option<UnresolvedType>, Expr)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L129-L131](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L129-L131)

If this expression is a let statement, returns the let pattern as an `Expr`,
the optional type annotation, and the assigned expression.

## as\_member\_accessas\_member\_access

```
pub comptime fn as_member_access(self) -> Option<(Expr, Quoted)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L136-L138](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L136-L138)

If this expression is a member access `foo.bar`, return the struct/tuple
expression and the field. The field will be represented as a quoted value.

## as\_method\_callas\_method\_call

```
pub comptime fn as_method_call(self) -> Option<(Expr, Quoted, [UnresolvedType], [Expr])> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L143-L145](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L143-L145)

If this expression is a method call `foo.bar::<generic1, ..., genericM>(arg1, ..., argN)`, return
the receiver, method name, a slice of each generic argument, and a slice of each argument.

## as\_repeated\_element\_arrayas\_repeated\_element\_array

```
pub comptime fn as_repeated_element_array(self) -> Option<(Expr, Expr)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L150-L152](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L150-L152)

If this expression is a repeated element array `[elem; length]`, return
the repeated element and the length expressions.

## as\_repeated\_element\_sliceas\_repeated\_element\_slice

```
pub comptime fn as_repeated_element_slice(self) -> Option<(Expr, Expr)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L157-L159](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L157-L159)

If this expression is a repeated element slice `[elem; length]`, return
the repeated element and the length expressions.

## as\_sliceas\_slice

```
pub comptime fn as_slice(self) -> Option<[Expr]> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L164-L166](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L164-L166)

If this expression is a slice literal `&[elem1, ..., elemN]`,
return each element of the slice.

## as\_tupleas\_tuple

```
pub comptime fn as_tuple(self) -> Option<[Expr]> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L171-L173](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L171-L173)

If this expression is a tuple `(field1, ..., fieldN)`,
return each element of the tuple.

## as\_unary\_opas\_unary\_op

```
pub comptime fn as_unary_op(self) -> Option<(UnaryOp, Expr)> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L178-L180](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L178-L180)

If this expression is a unary operation `<op> <rhs>`,
return the unary operator as well as the right-hand side expression.

## as\_unsafeas\_unsafe

```
pub comptime fn as_unsafe(self) -> Option<[Expr]> {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L185-L187](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L185-L187)

If this expression is an `unsafe { stmt1; ...; stmtN }` block,
return each statement inside in a slice.

## has\_semicolonhas\_semicolon

```
pub comptime fn has_semicolon(self) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L206-L208](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L206-L208)

`true` if this expression is trailed by a semicolon. E.g.

```
comptime {  
    let expr1 = quote { 1 + 2 }.as_expr().unwrap();  
    let expr2 = quote { 1 + 2; }.as_expr().unwrap();  
  
    assert(expr1.as_binary_op().is_some());  
    assert(expr2.as_binary_op().is_some());  
  
    assert(!expr1.has_semicolon());  
    assert(expr2.has_semicolon());  
}
```

## is\_breakis\_break

```
pub comptime fn is_break(self) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L212-L214](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L212-L214)

`true` if this expression is `break`.

## is\_continueis\_continue

```
pub comptime fn is_continue(self) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L218-L220](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L218-L220)

`true` if this expression is `continue`.

## modifymodify

```
pub comptime fn modify<Env>(self, f: fn[Env](Expr) -> Option<Expr>) -> Expr {
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L229-L231](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L229-L231)

Applies a mapping function to this expression and to all of its sub-expressions.
`f` will be applied to each sub-expression first, then applied to the expression itself.

This happens recursively for every expression within `self`.

For example, calling `modify` on `(&[1], &[2, 3])` with an `f` that returns `Option::some`
for expressions that are integers, doubling them, would return `(&[2], &[4, 6])`.

## quotedquoted

```
pub comptime fn quoted(self) -> Quoted {
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L266-L268](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L266-L268)

Returns this expression as a `Quoted` value. It's the same as `quote { $self }`.

## resolveresolve

```
pub comptime fn resolve(self, in_function: Option<FunctionDefinition>) -> TypedExpr {}
```

> [Source code: noir\_stdlib/src/meta/expr.nr#L282-L284](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/expr.nr#L282-L284)

Resolves and type-checks this expression and returns the result as a `TypedExpr`.

The `in_function` argument specifies where the expression is resolved:

* If it's `none`, the expression is resolved in the function where `resolve` was called
* If it's `some`, the expression is resolved in the given function

If any names used by this expression are not in scope or if there are any type errors,
this will give compiler errors as if the expression was written directly into
the current `comptime` function.

---


# FunctionDefinition

Source: https://noir-lang.org/docs/noir/standard_library/meta/function_def

Version: v1.0.0-beta.17

On this page

`std::meta::function_def` contains methods on the built-in `FunctionDefinition` type representing
a function definition in the source program.

## Methods## add\_attributeadd\_attribute

```
pub comptime fn add_attribute<let N: u32>(self, attribute: str<N>) {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L3-L5](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L3-L5)

Adds an attribute to the function. This is only valid
on functions in the current crate which have not yet been resolved.
This means any functions called at compile-time are invalid targets for this method.

## as\_typed\_expras\_typed\_expr

```
pub comptime fn as_typed_expr(self) -> TypedExpr {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L8-L10](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L8-L10)

Returns this function as a `TypedExpr`, which can be unquoted. For example:

```
let typed_expr = some_function.as_typed_expr();  
let _ = quote { $typed_expr(1, 2, 3); };
```

## bodybody

```
pub comptime fn body(self) -> Expr {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L13-L15](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L13-L15)

Returns the body of the function as an expression. This is only valid
on functions in the current crate which have not yet been resolved.
This means any functions called at compile-time are invalid targets for this method.

## has\_named\_attributehas\_named\_attribute

```
pub comptime fn has_named_attribute<let N: u32>(self, name: str<N>) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L18-L20](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L18-L20)

Returns true if this function has a custom attribute with the given name.

## is\_unconstrainedis\_unconstrained

```
pub comptime fn is_unconstrained(self) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L23-L25](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L23-L25)

Returns true if this function is unconstrained.

## modulemodule

```
pub comptime fn module(self) -> Module {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L28-L30](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L28-L30)

Returns the module where the function is defined.

## namename

```
pub comptime fn name(self) -> Quoted {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L33-L35](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L33-L35)

Returns the name of the function.

## parametersparameters

```
pub comptime fn parameters(self) -> [(Quoted, Type)] {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L38-L40](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L38-L40)

Returns each parameter of the function as a tuple of (parameter pattern, parameter type).

## return\_typereturn\_type

```
pub comptime fn return_type(self) -> Type {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L43-L45](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L43-L45)

The return type of the function.

## set\_bodyset\_body

```
pub comptime fn set_body(self, body: Expr) {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L48-L50](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L48-L50)

Mutate the function body to a new expression. This is only valid
on functions in the current crate which have not yet been resolved.
This means any functions called at compile-time are invalid targets for this method.

## set\_parametersset\_parameters

```
pub comptime fn set_parameters(self, parameters: [(Quoted, Type)]) {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L53-L55](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L53-L55)

Mutates the function's parameters to a new set of parameters. This is only valid
on functions in the current crate which have not yet been resolved.
This means any functions called at compile-time are invalid targets for this method.

Expects a slice of (parameter pattern, parameter type) for each parameter. Requires
each parameter pattern to be a syntactically valid parameter.

## set\_return\_typeset\_return\_type

```
pub comptime fn set_return_type(self, return_type: Type) {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L58-L60](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L58-L60)

Mutates the function's return type to a new type. This is only valid
on functions in the current crate which have not yet been resolved.
This means any functions called at compile-time are invalid targets for this method.

## set\_return\_publicset\_return\_public

```
pub comptime fn set_return_public(self, public: bool) {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L63-L65](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L63-L65)

Mutates the function's return visibility to public (if `true` is given) or private (if `false` is given).
This is only valid on functions in the current crate which have not yet been resolved.
This means any functions called at compile-time are invalid targets for this method.

## set\_unconstrainedset\_unconstrained

```
pub comptime fn set_unconstrained(self, value: bool) {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L71-L73](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L71-L73)

Mutates the function to be unconstrained (if `true` is given) or not (if `false` is given).
This is only valid on functions in the current crate which have not yet been resolved.
This means any functions called at compile-time are invalid targets for this method.

## visibilityvisibility

```
pub comptime fn visibility(self) -> Quoted {}
```

> [Source code: noir\_stdlib/src/meta/function\_def.nr#L76-L78](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/function_def.nr#L76-L78)

Returns the function's visibility as a `Quoted` value, which will be one of:

* `quote { }`: the function is private
* `quote { pub }`: the function is `pub`
* `quote { pub(crate) }`: the function is `pub(crate)`

## Trait Implementations```
impl Eq for FunctionDefinition  
impl Hash for FunctionDefinition
```

Note that each function is assigned a unique ID internally and this is what is used for
equality and hashing. So even functions with identical signatures and bodies may not
be equal in this sense if they were originally different items in the source program.

---


# Module

Source: https://noir-lang.org/docs/noir/standard_library/meta/module

Version: v1.0.0-beta.17

On this page

`std::meta::module` contains methods on the built-in `Module` type which represents a module in the source program.
Note that this type represents a module generally, it isn't limited to only `mod my_submodule { ... }`
declarations in the source program.

## Methods## add\_itemadd\_item

```
pub comptime fn add_item(self, item: Quoted) {}
```

> [Source code: noir\_stdlib/src/meta/module.nr#L5-L7](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/module.nr#L5-L7)

Adds a top-level item (a function, a struct, a global, etc.) to the module.
Adding multiple items in one go is also valid if the `Quoted` value has multiple items in it.
Note that the items are type-checked as if they are inside the module they are being added to.

## child\_moduleschild\_modules

```
pub comptime fn child_modules(self) -> [Module] {}
```

> [Source code: noir\_stdlib/src/meta/module.nr#L30-L32](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/module.nr#L30-L32)

Returns all the child modules of the current module.

child\_modules\_example

```
mod my_module {  
    pub mod child1 {}  
    pub mod child2 {}  
    pub mod child3 {  
        pub mod nested_child {}  
    }  
}  
  
#[test]  
fn child_modules_test() {  
    comptime {  
        let my_module = quote [my_module].as_module().unwrap();  
        let children = my_module.child_modules().map(Module::name);  
  
        // The order children are returned in is left unspecified.  
        assert_eq(children, &[quote [child1], quote [child2], quote [child3]]);  
    }  
}
```

> [Source code: test\_programs/compile\_success\_empty/comptime\_module/src/main.nr#L150-L169](https://github.com/noir-lang/noir/blob/master/test_programs/compile_success_empty/comptime_module/src/main.nr#L150-L169)

## functionsfunctions

```
pub comptime fn functions(self) -> [FunctionDefinition] {}
```

> [Source code: noir\_stdlib/src/meta/module.nr#L20-L22](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/module.nr#L20-L22)

Returns each function defined in the module.

## has\_named\_attributehas\_named\_attribute

```
pub comptime fn has_named_attribute<let N: u32>(self, name: str<N>) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/module.nr#L10-L12](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/module.nr#L10-L12)

Returns true if this module has a custom attribute with the given name.

## is\_contractis\_contract

```
pub comptime fn is_contract(self) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/module.nr#L15-L17](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/module.nr#L15-L17)

`true` if this module is a contract module (was declared via `contract foo { ... }`).

## namename

```
pub comptime fn name(self) -> Quoted {}
```

> [Source code: noir\_stdlib/src/meta/module.nr#L35-L37](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/module.nr#L35-L37)

Returns the name of the module.
The top-level module in each crate has no name and is thus empty.

## parentparent

```
pub comptime fn parent(self) -> Option<Module> {}
```

> [Source code: noir\_stdlib/src/meta/module.nr#L40-L42](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/module.nr#L40-L42)

Returns the parent module of the given module, if any.

parent\_example

```
mod module1 {  
    pub mod module2 {}  
}  
  
#[test]  
fn parent_test() {  
    comptime {  
        let my_module2 = quote [module1::module2].as_module().unwrap();  
        assert_eq(my_module2.name(), quote [module2]);  
  
        let my_module1 = my_module2.parent().unwrap();  
        assert_eq(my_module1.name(), quote [module1]);  
  
        // The top-level module in each crate has no name  
        let top_level_module = my_module1.parent().unwrap();  
        assert_eq(top_level_module.name(), quote []);  
    }  
}
```

> [Source code: test\_programs/compile\_success\_empty/comptime\_module/src/main.nr#L129-L148](https://github.com/noir-lang/noir/blob/master/test_programs/compile_success_empty/comptime_module/src/main.nr#L129-L148)

## structsstructs

```
pub comptime fn structs(self) -> [TypeDefinition] {}
```

> [Source code: noir\_stdlib/src/meta/module.nr#L25-L27](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/module.nr#L25-L27)

Returns each struct defined in the module.

## Trait Implementations```
impl Eq for Module  
impl Hash for Module
```

Note that each module is assigned a unique ID internally and this is what is used for
equality and hashing. So even modules with identical names and contents may not
be equal in this sense if they were originally different items in the source program.

---


# UnaryOp and BinaryOp

Source: https://noir-lang.org/docs/noir/standard_library/meta/op

Version: v1.0.0-beta.17

On this page

`std::meta::op` contains the `UnaryOp` and `BinaryOp` types as well as methods on them.
These types are used to represent a unary or binary operator respectively in Noir source code.

## Types## UnaryOpRepresents a unary operator. One of `-`, `!`, `&mut`, or `*`.

## Methods## is\_minusis\_minus

```
pub fn is_minus(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L26-L28](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L26-L28)

Returns `true` if this operator is `-`.

## is\_notis\_not

```
pub fn is_not(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L32-L34](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L32-L34)

`true` if this operator is `!`

## is\_mutable\_referenceis\_mutable\_reference

```
pub fn is_mutable_reference(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L38-L40](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L38-L40)

`true` if this operator is `&mut`

## is\_dereferenceis\_dereference

```
pub fn is_dereference(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L44-L46](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L44-L46)

`true` if this operator is `*`

## quotedunary\_quoted

```
pub comptime fn quoted(self) -> Quoted {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L50-L52](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L50-L52)

Returns this operator as a `Quoted` value.

## Trait Implementations```
impl Eq for UnaryOp  
impl Hash for UnaryOp
```

## BinaryOpRepresents a binary operator. One of `+`, `-`, `*`, `/`, `%`, `==`, `!=`, `<`, `<=`, `>`, `>=`, `&`, `|`, `^`, `>>`, or `<<`.

## Methods## is\_addis\_add

```
pub fn is_add(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L88-L90](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L88-L90)

`true` if this operator is `+`

## is\_subtractis\_subtract

```
pub fn is_subtract(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L94-L96](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L94-L96)

`true` if this operator is `-`

## is\_multiplyis\_multiply

```
pub fn is_multiply(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L100-L102](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L100-L102)

`true` if this operator is `*`

## is\_divideis\_divide

```
pub fn is_divide(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L106-L108](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L106-L108)

`true` if this operator is `/`

## is\_modulois\_modulo

```
pub fn is_modulo(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L178-L180](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L178-L180)

`true` if this operator is `%`

## is\_equalis\_equal

```
pub fn is_equal(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L112-L114](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L112-L114)

`true` if this operator is `==`

## is\_not\_equalis\_not\_equal

```
pub fn is_not_equal(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L118-L120](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L118-L120)

`true` if this operator is `!=`

## is\_less\_thanis\_less\_than

```
pub fn is_less_than(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L124-L126](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L124-L126)

`true` if this operator is `<`

## is\_less\_than\_or\_equalis\_less\_than\_or\_equal

```
pub fn is_less_than_or_equal(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L130-L132](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L130-L132)

`true` if this operator is `<=`

## is\_greater\_thanis\_greater\_than

```
pub fn is_greater_than(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L136-L138](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L136-L138)

`true` if this operator is `>`

## is\_greater\_than\_or\_equalis\_greater\_than\_or\_equal

```
pub fn is_greater_than_or_equal(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L142-L144](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L142-L144)

`true` if this operator is `>=`

## is\_andis\_and

```
pub fn is_and(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L148-L150](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L148-L150)

`true` if this operator is `&`

## is\_oris\_or

```
pub fn is_or(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L154-L156](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L154-L156)

`true` if this operator is `|`

## is\_shift\_rightis\_shift\_right

```
pub fn is_shift_right(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L166-L168](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L166-L168)

`true` if this operator is `>>`

## is\_shift\_leftis\_shift\_left

```
pub fn is_shift_left(self) -> bool {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L172-L174](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L172-L174)

`true` if this operator is `<<`

## quotedbinary\_quoted

```
pub comptime fn quoted(self) -> Quoted {
```

> [Source code: noir\_stdlib/src/meta/op.nr#L184-L186](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/op.nr#L184-L186)

Returns this operator as a `Quoted` value.

## Trait Implementations```
impl Eq for BinaryOp  
impl Hash for BinaryOp
```

---


# Quoted

Source: https://noir-lang.org/docs/noir/standard_library/meta/quoted

Version: v1.0.0-beta.17

On this page

`std::meta::quoted` contains methods on the built-in `Quoted` type which represents
quoted token streams and is the result of the `quote { ... }` expression.

## Methods## as\_expras\_expr

```
pub comptime fn as_expr(self) -> Option<Expr> {}
```

> [Source code: noir\_stdlib/src/meta/quoted.nr#L6-L8](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/quoted.nr#L6-L8)

Parses the quoted token stream as an expression. Returns `Option::none()` if
the expression failed to parse.

Example:

as\_expr\_example

```
#[test]  
    fn test_expr_as_function_call() {  
        comptime {  
            let expr = quote { foo(42) }.as_expr().unwrap();  
            let (_function, args) = expr.as_function_call().unwrap();  
            assert_eq(args.len(), 1);  
            assert_eq(args[0].as_integer().unwrap(), (42, false));  
        }  
    }
```

> [Source code: test\_programs/noir\_test\_success/comptime\_expr/src/main.nr#L336-L346](https://github.com/noir-lang/noir/blob/master/test_programs/noir_test_success/comptime_expr/src/main.nr#L336-L346)

## as\_moduleas\_module

```
pub comptime fn as_module(self) -> Option<Module> {}
```

> [Source code: noir\_stdlib/src/meta/quoted.nr#L11-L13](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/quoted.nr#L11-L13)

Interprets this token stream as a module path leading to the name of a module.
Returns `Option::none()` if the module isn't found or this token stream cannot be parsed as a path.

Example:

as\_module\_example

```
mod baz {  
    pub mod qux {}  
}  
  
#[test]  
fn as_module_test() {  
    comptime {  
        let my_mod = quote { baz::qux }.as_module().unwrap();  
        assert_eq(my_mod.name(), quote { qux });  
    }  
}
```

> [Source code: test\_programs/compile\_success\_empty/comptime\_module/src/main.nr#L115-L127](https://github.com/noir-lang/noir/blob/master/test_programs/compile_success_empty/comptime_module/src/main.nr#L115-L127)

## as\_trait\_constraintas\_trait\_constraint

```
pub comptime fn as_trait_constraint(self) -> TraitConstraint {}
```

> [Source code: noir\_stdlib/src/meta/quoted.nr#L16-L18](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/quoted.nr#L16-L18)

Interprets this token stream as a trait constraint (without an object type).
Note that this function panics instead of returning `Option::none()` if the token
stream does not parse and resolve to a valid trait constraint.

Example:

implements\_example

```
pub fn function_with_where<T>(_x: T)  
where  
    T: SomeTrait<i32>,  
{  
    comptime {  
        let t = quote { T }.as_type();  
        let some_trait_i32 = quote { SomeTrait<i32> }.as_trait_constraint();  
        assert(t.implements(some_trait_i32));  
  
        assert(t.get_trait_impl(some_trait_i32).is_none());  
    }  
}
```

> [Source code: test\_programs/compile\_success\_empty/comptime\_type/src/main.nr#L160-L173](https://github.com/noir-lang/noir/blob/master/test_programs/compile_success_empty/comptime_type/src/main.nr#L160-L173)

## as\_typeas\_type

```
pub comptime fn as_type(self) -> Type {}
```

> [Source code: noir\_stdlib/src/meta/quoted.nr#L21-L23](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/quoted.nr#L21-L23)

Interprets this token stream as a resolved type. Panics if the token
stream doesn't parse to a type or if the type isn't a valid type in scope.

implements\_example

```
pub fn function_with_where<T>(_x: T)  
where  
    T: SomeTrait<i32>,  
{  
    comptime {  
        let t = quote { T }.as_type();  
        let some_trait_i32 = quote { SomeTrait<i32> }.as_trait_constraint();  
        assert(t.implements(some_trait_i32));  
  
        assert(t.get_trait_impl(some_trait_i32).is_none());  
    }  
}
```

> [Source code: test\_programs/compile\_success\_empty/comptime\_type/src/main.nr#L160-L173](https://github.com/noir-lang/noir/blob/master/test_programs/compile_success_empty/comptime_type/src/main.nr#L160-L173)

## tokenstokens

```
pub comptime fn tokens(self) -> [Quoted] {}
```

> [Source code: noir\_stdlib/src/meta/quoted.nr#L26-L28](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/quoted.nr#L26-L28)

Returns a slice of the individual tokens that form this token stream.

## Trait Implementations```
impl Eq for Quoted  
impl Hash for Quoted
```

---


# TypeDefinition

Source: https://noir-lang.org/docs/noir/standard_library/meta/struct_def

Version: v1.0.0-beta.17

On this page

`std::meta::type_def` contains methods on the built-in `TypeDefinition` type.
This type corresponds to `struct Name { field1: Type1, ... }` and `enum Name { Variant1(Fields1), ... }` items in the source program.

## Methods## add\_attributeadd\_attribute

```
pub comptime fn add_attribute<let N: u32>(self, attribute: str<N>) {}
```

> [Source code: noir\_stdlib/src/meta/type\_def.nr#L5-L7](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/type_def.nr#L5-L7)

Adds an attribute to the data type.

## add\_genericadd\_generic

```
pub comptime fn add_generic<let N: u32>(self, generic_name: str<N>) -> Type {}
```

> [Source code: noir\_stdlib/src/meta/type\_def.nr#L10-L12](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/type_def.nr#L10-L12)

Adds an generic to the type. Returns the new generic type.
Errors if the given generic name isn't a single identifier or if
the type already has a generic with the same name.

This method should be used carefully, if there is existing code referring
to the type it may be checked before this function is called and
see the type with the original number of generics. This method should
thus be preferred to use on code generated from other macros and types
that are not used in function signatures.

Example:

add-generic-example

```
comptime fn add_generic(s: TypeDefinition) {  
        assert_eq(s.generics().len(), 0);  
        let new_generic = s.add_generic("T");  
  
        let generics = s.generics();  
        assert_eq(generics.len(), 1);  
        let (typ, numeric) = generics[0];  
        assert_eq(typ, new_generic);  
        assert(numeric.is_none());  
    }
```

> [Source code: test\_programs/compile\_success\_empty/comptime\_struct\_definition/src/main.nr#L46-L57](https://github.com/noir-lang/noir/blob/master/test_programs/compile_success_empty/comptime_struct_definition/src/main.nr#L46-L57)

## as\_typeas\_type

```
pub comptime fn as_type(self) -> Type {}
```

> [Source code: noir\_stdlib/src/meta/type\_def.nr#L17-L19](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/type_def.nr#L17-L19)

Returns this type definition as a type in the source program. If this definition has
any generics, the generics are also included as-is.

## as\_type\_with\_genericsas\_type\_with\_generics

```
pub comptime fn as_type_with_generics(self, generics: [Type]) -> Option<Type> {}
```

> [Source code: noir\_stdlib/src/meta/type\_def.nr#L28-L30](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/type_def.nr#L28-L30)

Returns a type from this type definition using the given generic arguments. Returns `Option::none()`
if an incorrect amount of generic arguments are given for this type.

## genericsgenerics

```
pub comptime fn generics(self) -> [(Type, Option<Type>)] {}
```

> [Source code: noir\_stdlib/src/meta/type\_def.nr#L40-L42](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/type_def.nr#L40-L42)

Returns each generic on this type definition. Each generic is represented as a tuple containing the type,
and an optional containing the numeric type if it's a numeric generic.

Example:

```
#[example]  
struct Foo<T, U, let K: u32> {  
    bar: [T; K],  
    baz: Baz<U, U>,  
}  
  
comptime fn example(foo: TypeDefinition) {  
    assert_eq(foo.generics().len(), 3);  
  
    // Fails because `T` isn't in scope  
    // let t = quote { T }.as_type();  
    // assert_eq(foo.generics()[0].0, t);  
    assert(foo.generics()[0].1.is_none());  
  
    // Last generic is numeric, so we have the numeric type available to us  
    assert(foo.generics()[2].1.is_some());  
}
```

## fieldsfields

```
pub comptime fn fields(self, generic_args: [Type]) -> [(Quoted, Type, Quoted)] {}
```

> [Source code: noir\_stdlib/src/meta/type\_def.nr#L48-L50](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/type_def.nr#L48-L50)

Returns (name, type, visibility) tuples of each field in this struct type.
Any generic types used in each field type is automatically substituted with the
provided generic arguments.

## fields\_as\_writtenfields\_as\_written

```
pub comptime fn fields_as_written(self) -> [(Quoted, Type, Quoted)] {}
```

> [Source code: noir\_stdlib/src/meta/type\_def.nr#L57-L59](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/type_def.nr#L57-L59)

Returns (name, type, visibility) tuples of each field in this struct type. Each type is as-is
with any generic arguments unchanged. Unless the field types are not needed,
users should generally prefer to use `TypeDefinition::fields` over this
function if possible.

## has\_named\_attributehas\_named\_attribute

```
pub comptime fn has_named_attribute<let N: u32>(self, name: str<N>) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/type\_def.nr#L33-L35](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/type_def.nr#L33-L35)

Returns true if this type has a custom attribute with the given name.

## modulemodule

```
pub comptime fn module(self) -> Module {}
```

> [Source code: noir\_stdlib/src/meta/type\_def.nr#L62-L64](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/type_def.nr#L62-L64)

Returns the module where the type is defined.

## namename

```
pub comptime fn name(self) -> Quoted {}
```

> [Source code: noir\_stdlib/src/meta/type\_def.nr#L67-L69](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/type_def.nr#L67-L69)

Returns the name of this type

Note that the returned quoted value will be just the type name, it will
not be the full path to the type definition, nor will it include any generics.

## set\_fieldsset\_fields

```
pub comptime fn set_fields(self, new_fields: [(Quoted, Type, Quoted)]) {}
```

> [Source code: noir\_stdlib/src/meta/type\_def.nr#L76-L78](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/type_def.nr#L76-L78)

Sets the fields of this struct to the given fields list where each element
is a pair of the field's name and the field's type. Expects each field name
to be a single identifier. Note that this will override any previous fields
on this struct. If those should be preserved, use `.fields()` to retrieve the
current fields on the struct type and append the new fields from there.

Example:

```
// Change this struct to:  
// struct Foo {  
//     pub a: u32,  
//     b: i8,  
// }  
#[mangle_fields]  
struct Foo { x: Field }  
  
comptime fn mangle_fields(s: TypeDefinition) {  
    s.set_fields(&[  
        (quote { a }, quote { u32 }.as_type(), quote { pub }),  
        (quote { b }, quote { i8 }.as_type(), quote {}),  
    ]);  
}
```

## Trait Implementations```
impl Eq for TypeDefinition  
impl Hash for TypeDefinition
```

Note that each type definition is assigned a unique ID internally and this is what is used for
equality and hashing. So even type definitions with identical generics and fields may not
be equal in this sense if they were originally different items in the source program.

---


# TraitConstraint

Source: https://noir-lang.org/docs/noir/standard_library/meta/trait_constraint

Version: v1.0.0-beta.17

On this page

`std::meta::trait_constraint` contains methods on the built-in `TraitConstraint` type which represents
a trait constraint that can be used to search for a trait implementation. This is similar
syntactically to just the trait itself, but can also contain generic arguments. E.g. `Eq`, `Default`,
`BuildHasher<Poseidon2Hasher>`.

This type currently has no public methods but it can be used alongside `Type` in `implements` or `get_trait_impl`.

## Trait Implementations```
impl Eq for TraitConstraint  
impl Hash for TraitConstraint
```

---


# TraitDefinition

Source: https://noir-lang.org/docs/noir/standard_library/meta/trait_def

Version: v1.0.0-beta.17

On this page

`std::meta::trait_def` contains methods on the built-in `TraitDefinition` type. This type
represents trait definitions such as `trait Foo { .. }` at the top-level of a program.

## Methods## as\_trait\_constraintas\_trait\_constraint

```
pub comptime fn as_trait_constraint(_self: Self) -> TraitConstraint {}
```

> [Source code: noir\_stdlib/src/meta/trait\_def.nr#L6-L8](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/trait_def.nr#L6-L8)

Converts this trait into a trait constraint. If there are any generics on this
trait, they will be kept as-is without instantiating or replacing them.

## Trait Implementations```
impl Eq for TraitDefinition  
impl Hash for TraitDefinition
```

---


# TraitImpl

Source: https://noir-lang.org/docs/noir/standard_library/meta/trait_impl

Version: v1.0.0-beta.17

On this page

`std::meta::trait_impl` contains methods on the built-in `TraitImpl` type which represents a trait
implementation such as `impl Foo for Bar { ... }`.

## Methods## trait\_generic\_argstrait\_generic\_args

```
pub comptime fn trait_generic_args(self) -> [Type] {}
```

> [Source code: noir\_stdlib/src/meta/trait\_impl.nr#L3-L5](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/trait_impl.nr#L3-L5)

Returns any generic arguments on the trait of this trait implementation, if any.

```
impl Foo<i32, Field> for Bar { ... }  
  
comptime {  
    let bar_type = quote { Bar }.as_type();  
    let foo = quote { Foo<i32, Field> }.as_trait_constraint();  
  
    let my_impl: TraitImpl = bar_type.get_trait_impl(foo).unwrap();  
  
    let generics = my_impl.trait_generic_args();  
    assert_eq(generics.len(), 2);  
  
    assert_eq(generics[0].0, quote { i32 }.as_type());  
    assert(generics[0].1.is_none());  
    assert_eq(generics[1].0, quote { Field }.as_type());  
    assert(generics[1].1.is_none());  
}
```

## methodsmethods

```
pub comptime fn methods(self) -> [FunctionDefinition] {}
```

> [Source code: noir\_stdlib/src/meta/trait\_impl.nr#L8-L10](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/trait_impl.nr#L8-L10)

Returns each method in this trait impl.

Example:

```
comptime {  
    let i32_type = quote { i32 }.as_type();  
    let eq = quote { Eq }.as_trait_constraint();  
  
    let impl_eq_for_i32: TraitImpl = i32_type.get_trait_impl(eq).unwrap();  
    let methods = impl_eq_for_i32.methods();  
  
    assert_eq(methods.len(), 1);  
    assert_eq(methods[0].name(), quote { eq });  
}
```

---


# Type

Source: https://noir-lang.org/docs/noir/standard_library/meta/typ

Version: v1.0.0-beta.17

On this page

`std::meta::typ` contains methods on the built-in `Type` type used for representing
a type in the source program.

## Functionsfresh\_type\_variable

```
pub comptime fn fresh_type_variable() -> Type {}
```

> [Source code: noir\_stdlib/src/meta/typ.nr#L57-L59](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typ.nr#L57-L59)

Creates and returns an unbound type variable. This is a special kind of type internal
to type checking which will type check with any other type. When it is type checked
against another type it will also be set to that type. For example, if `a` is a type
variable and we have the type equality `(a, i32) = (u8, i32)`, the compiler will set
`a` equal to `u8`.

Unbound type variables will often be rendered as `_` while printing them. Bound type
variables will appear as the type they are bound to.

This can be used in conjunction with functions which internally perform type checks
such as `Type::implements` or `Type::get_trait_impl` to potentially grab some of the types used.

Note that calling `Type::implements` or `Type::get_trait_impl` on a type variable will always
fail.

Example:

serialize-setup

```
trait Serialize<let N: u32> {}  
  
impl Serialize<1> for Field {}  
  
impl<T, let N: u32, let M: u32> Serialize<N * M> for [T; N]  
where  
    T: Serialize<M>,  
{}  
  
impl<T, U, let N: u32, let M: u32> Serialize<N + M> for (T, U)  
where  
    T: Serialize<N>,  
    U: Serialize<M>,  
{}
```

> [Source code: test\_programs/compile\_success\_empty/comptime\_type/src/main.nr#L14-L29](https://github.com/noir-lang/noir/blob/master/test_programs/compile_success_empty/comptime_type/src/main.nr#L14-L29)

fresh-type-variable-example

```
let typevar1 = std::meta::typ::fresh_type_variable();  
        let constraint = quote { Serialize<$typevar1> }.as_trait_constraint();  
        let field_type = quote { Field }.as_type();  
  
        // Search for a trait impl (binding typevar1 to 1 when the impl is found):  
        assert(field_type.implements(constraint));  
  
        // typevar1 should be bound to the "1" generic now:  
        assert_eq(typevar1.as_constant().unwrap(), 1);  
  
        // If we want to do the same with a different type, we need to  
        // create a new type variable now that `typevar1` is bound  
        let typevar2 = std::meta::typ::fresh_type_variable();  
        let constraint = quote { Serialize<$typevar2> }.as_trait_constraint();  
        let array_type = quote { [(Field, Field); 5] }.as_type();  
        assert(array_type.implements(constraint));  
  
        // Now typevar2 should be bound to the serialized pair size 2 times the array length 5  
        assert_eq(typevar2.as_constant().unwrap(), 10);
```

> [Source code: test\_programs/compile\_success\_empty/comptime\_type/src/main.nr#L129-L149](https://github.com/noir-lang/noir/blob/master/test_programs/compile_success_empty/comptime_type/src/main.nr#L129-L149)

## Methods## as\_arrayas\_array

```
pub comptime fn as_array(self) -> Option<(Type, Type)> {}
```

> [Source code: noir\_stdlib/src/meta/typ.nr#L76-L78](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typ.nr#L76-L78)

If this type is an array, return a pair of (element type, size type).

Example:

```
comptime {  
    let array_type = quote { [Field; 3] }.as_type();  
    let (field_type, three_type) = array_type.as_array().unwrap();  
  
    assert(field_type.is_field());  
    assert_eq(three_type.as_constant().unwrap(), 3);  
}
```

## as\_constantas\_constant

```
pub comptime fn as_constant(self) -> Option<u32> {}
```

> [Source code: noir\_stdlib/src/meta/typ.nr#L83-L85](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typ.nr#L83-L85)

If this type is a constant integer (such as the `3` in the array type `[Field; 3]`),
return the numeric constant.

## as\_integeras\_integer

```
pub comptime fn as_integer(self) -> Option<(bool, u8)> {}
```

> [Source code: noir\_stdlib/src/meta/typ.nr#L90-L92](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typ.nr#L90-L92)

If this is an integer type, return a boolean which is `true`
if the type is signed, as well as the number of bits of this integer type.

## as\_mutable\_referenceas\_mutable\_reference

```
pub comptime fn as_mutable_reference(self) -> Option<Type> {}
```

> [Source code: noir\_stdlib/src/meta/typ.nr#L96-L98](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typ.nr#L96-L98)

If this is a mutable reference type `&mut T`, returns the mutable type `T`.

## as\_sliceas\_slice

```
pub comptime fn as_slice(self) -> Option<Type> {}
```

> [Source code: noir\_stdlib/src/meta/typ.nr#L102-L104](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typ.nr#L102-L104)

If this is a slice type, return the element type of the slice.

## as\_stras\_str

```
pub comptime fn as_str(self) -> Option<Type> {}
```

> [Source code: noir\_stdlib/src/meta/typ.nr#L108-L110](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typ.nr#L108-L110)

If this is a `str<N>` type, returns the length `N` as a type.

## as\_data\_typeas\_data\_type

```
pub comptime fn as_data_type(self) -> Option<(TypeDefinition, [Type])> {}
```

> [Source code: noir\_stdlib/src/meta/typ.nr#L119-L121](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typ.nr#L119-L121)

If this is a struct type, returns the struct in addition to
any generic arguments on this type.

## as\_tupleas\_tuple

```
pub comptime fn as_tuple(self) -> Option<[Type]> {}
```

> [Source code: noir\_stdlib/src/meta/typ.nr#L125-L127](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typ.nr#L125-L127)

If this is a tuple type, returns each element type of the tuple.

## get\_trait\_implget\_trait\_impl

```
pub comptime fn get_trait_impl(self, constraint: TraitConstraint) -> Option<TraitImpl> {}
```

> [Source code: noir\_stdlib/src/meta/typ.nr#L148-L150](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typ.nr#L148-L150)

Retrieves the trait implementation that implements the given
trait constraint for this type. If the trait constraint is not
found, `None` is returned. Note that since the concrete trait implementation
for a trait constraint specified in a `where` clause is unknown,
this function will return `None` in these cases. If you only want to know
whether a type implements a trait, use `implements` instead.

Example:

```
comptime {  
    let field_type = quote { Field }.as_type();  
    let default = quote { Default }.as_trait_constraint();  
  
    let the_impl: TraitImpl = field_type.get_trait_impl(default).unwrap();  
    assert(the_impl.methods().len(), 1);  
}
```

## implementsimplements

```
pub comptime fn implements(self, constraint: TraitConstraint) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/typ.nr#L171-L173](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typ.nr#L171-L173)

`true` if this type implements the given trait. Note that unlike
`get_trait_impl` this will also return true for any `where` constraints
in scope.

Example:

```
fn foo<T>() where T: Default {  
    comptime {  
        let field_type = quote { Field }.as_type();  
        let default = quote { Default }.as_trait_constraint();  
        assert(field_type.implements(default));  
  
        let t = quote { T }.as_type();  
        assert(t.implements(default));  
    }  
}
```

## is\_boolis\_bool

```
pub comptime fn is_bool(self) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/typ.nr#L177-L179](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typ.nr#L177-L179)

`true` if this type is `bool`.

## is\_fieldis\_field

```
pub comptime fn is_field(self) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/typ.nr#L183-L185](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typ.nr#L183-L185)

`true` if this type is `Field`.

## is\_unitis\_unit

```
pub comptime fn is_unit(self) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/typ.nr#L189-L191](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typ.nr#L189-L191)

`true` if this type is the unit `()` type.

## Trait Implementations```
impl Eq for Type  
impl Hash for Type
```

Note that this is syntactic equality, this is not the same as whether two types will type check
to be the same type. Unless type inference or generics are being used however, users should not
typically have to worry about this distinction unless `std::meta::typ::fresh_type_variable` is used.

---


# TypedExpr

Source: https://noir-lang.org/docs/noir/standard_library/meta/typed_expr

Version: v1.0.0-beta.17

On this page

`std::meta::typed_expr` contains methods on the built-in `TypedExpr` type for resolved and type-checked expressions.

## Methods## get\_typeas\_function\_definition

```
pub comptime fn as_function_definition(self) -> Option<FunctionDefinition> {}
```

> [Source code: noir\_stdlib/src/meta/typed\_expr.nr#L7-L9](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typed_expr.nr#L7-L9)

If this expression refers to a function definitions, returns it. Otherwise returns `Option::none()`.

## get\_typeget\_type

```
pub comptime fn get_type(self) -> Option<Type> {}
```

> [Source code: noir\_stdlib/src/meta/typed\_expr.nr#L13-L15](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/typed_expr.nr#L13-L15)

Returns the type of the expression, or `Option::none()` if there were errors when the expression was previously resolved.

---


# UnresolvedType

Source: https://noir-lang.org/docs/noir/standard_library/meta/unresolved_type

Version: v1.0.0-beta.17

On this page

`std::meta::unresolved_type` contains methods on the built-in `UnresolvedType` type for the syntax of types.

## Methods## as\_mutable\_referenceas\_mutable\_reference

```
pub comptime fn as_mutable_reference(self) -> Option<UnresolvedType> {}
```

> [Source code: noir\_stdlib/src/meta/unresolved\_type.nr#L8-L10](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/unresolved_type.nr#L8-L10)

If this is a mutable reference type `&mut T`, returns the mutable type `T`.

## as\_sliceas\_slice

```
pub comptime fn as_slice(self) -> Option<UnresolvedType> {}
```

> [Source code: noir\_stdlib/src/meta/unresolved\_type.nr#L14-L16](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/unresolved_type.nr#L14-L16)

If this is a slice `&[T]`, returns the element type `T`.

## is\_boolis\_bool

```
pub comptime fn is_bool(self) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/unresolved\_type.nr#L20-L22](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/unresolved_type.nr#L20-L22)

Returns `true` if this type is `bool`.

## is\_fieldis\_field

```
pub comptime fn is_field(self) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/unresolved\_type.nr#L26-L28](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/unresolved_type.nr#L26-L28)

Returns true if this type refers to the Field type.

## is\_unitis\_unit

```
pub comptime fn is_unit(self) -> bool {}
```

> [Source code: noir\_stdlib/src/meta/unresolved\_type.nr#L32-L34](https://github.com/noir-lang/noir/blob/master/noir_stdlib/src/meta/unresolved_type.nr#L32-L34)

Returns true if this type is the unit `()` type.

---


# Option<T> Type

Source: https://noir-lang.org/docs/noir/standard_library/options

Version: v1.0.0-beta.17

On this page

The `Option<T>` type is a way to express that a value might be present (`Some(T))` or absent (`None`). It's a safer way to handle potential absence of values, compared to using nulls in many other languages.

```
struct Option<T> {  
    None,  
    Some(T),  
}
```

The `Option` type, already imported into your Noir program, can be used directly:

```
fn main() {  
    let none = Option::none();  
    let some = Option::some(3);  
}
```

See [this test](https://github.com/noir-lang/noir/blob/5cbfb9c4a06c8865c98ff2b594464b037d821a5c/crates/nargo_cli/tests/test_data/option/src/main.nr) for a more comprehensive set of examples of each of the methods described below.

## Methods## noneConstructs a none value.

## someConstructs a some wrapper around a given value.

## is\_noneReturns true if the Option is None.

## is\_someReturns true of the Option is Some.

## unwrapAsserts `self.is_some()` and returns the wrapped value.

## unwrap\_uncheckedReturns the inner value without asserting `self.is_some()`. This method can be useful within an if condition when we already know that `option.is_some()`. If the option is None, there is no guarantee what value will be returned, only that it will be of type T for an `Option<T>`.

## unwrap\_orReturns the wrapped value if `self.is_some()`. Otherwise, returns the given default value.

## unwrap\_or\_elseReturns the wrapped value if `self.is_some()`. Otherwise, calls the given function to return a default value.

## expectAsserts `self.is_some()` with a provided custom message and returns the contained `Some` value. The custom message is expected to be a format string.

## mapIf self is `Some(x)`, this returns `Some(f(x))`. Otherwise, this returns `None`.

## map\_orIf self is `Some(x)`, this returns `f(x)`. Otherwise, this returns the given default value.

## map\_or\_elseIf self is `Some(x)`, this returns `f(x)`. Otherwise, this returns `default()`.

## andReturns None if self is None. Otherwise, this returns `other`.

## and\_thenIf self is None, this returns None. Otherwise, this calls the given function with the Some value contained within self, and returns the result of that call. In some languages this function is called `flat_map` or `bind`.

## orIf self is Some, return self. Otherwise, return `other`.

## or\_elseIf self is Some, return self. Otherwise, return `default()`.

## xorIf only one of the two Options is Some, return that option. Otherwise, if both options are Some or both are None, None is returned.

## filterReturns `Some(x)` if self is `Some(x)` and `predicate(x)` is true. Otherwise, this returns `None`.

## flattenFlattens an `Option<Option<T>>` into a `Option<T>`. This returns `None` if the outer Option is None. Otherwise, this returns the inner Option.

---


# Recursive Proofs

Source: https://noir-lang.org/docs/noir/standard_library/recursion

Version: v1.0.0-beta.17

On this page

Noir supports recursively verifying proofs, meaning you verify the proof of a Noir program in another Noir program. This enables creating proofs of arbitrary size by doing step-wise verification of smaller components of a large proof.

Noir cannot check internally whether a recursive proof is valid or not as this can only be checked by the proving backend. This means that witness execution can still succeed in the case where an invalid proof is used, however an invalid proof is expected to cause the proving backend to fail to generate a valid proof.

In order to verify recursive proofs from Barretenberg, it's recommended to use the [bb\_proof\_verification](https://github.com/AztecProtocol/aztec-packages/tree/next/barretenberg/noir/bb_proof_verification) library which is published by the Barretenberg team.

## Verifying Recursive Proofs```
#[foreign(recursive_aggregation)]  
pub fn verify_proof(verification_key: [Field], proof: [Field], public_inputs: [Field], key_hash: Field) {}
```

This is a black box function. Read [this section](/docs/noir/standard_library/black_box_fns) to learn more about black box functions in Noir.

Read [the explainer on recursion](https://barretenberg.aztec.network/docs/explainers/recursive_aggregation) to know more about this function and the [guide on how to use it.](https://barretenberg.aztec.network/docs/how_to_guides/recursive_aggregation)

You can see a full example of recursive proofs in [this example recursion demo repo](https://github.com/noir-lang/noir-examples/tree/master/recursion).

---


# Modules, Packages and Crates

Source: https://noir-lang.org/docs/noir/modules_packages_crates/crates_and_packages

Version: v1.0.0-beta.17

On this page

## CratesA crate is the smallest amount of code that the Noir compiler considers at a time.
Crates can contain modules, and the modules may be defined in other files that get compiled with the crate, as we’ll see in the coming sections.

## Crate TypesA Noir crate can come in several forms: binaries, libraries or contracts.

## Binaries*Binary crates* are programs which you can compile to an ACIR circuit which you can then create proofs against. Each must have a function called `main` that defines the ACIR circuit which is to be proved.

## Libraries*Library crates* don't have a `main` function and they don't compile down to ACIR. Instead they define functionality intended to be shared with multiple projects, and eventually included in a binary crate.

## ContractsContract crates are similar to binary crates in that they compile to ACIR which you can create proofs against. They are different in that they do not have a single `main` function, but are a collection of functions to be deployed to the [Aztec network](https://aztec.network). You can learn more about the technical details of Aztec in the [monorepo](https://github.com/AztecProtocol/aztec-packages) or contract [examples](https://github.com/AztecProtocol/aztec-packages/tree/master/noir-projects/noir-contracts/contracts).

## Crate RootEvery crate has a root, which is the source file that the compiler starts, this is also known as the root module. The Noir compiler does not enforce any conditions on the name of the file which is the crate root, however if you are compiling via Nargo the crate root must be called `lib.nr` or `main.nr` for library or binary crates respectively.

## PackagesA Nargo *package* is a collection of one or more crates that provides a set of functionality. A package must include a Nargo.toml file.

A package *must* contain either a library or a binary crate, but not both.

## Differences from Cargo PackagesOne notable difference between Rust's Cargo and Noir's Nargo is that while Cargo allows a package to contain an unlimited number of binary crates and a single library crate, Nargo currently only allows a package to contain a single crate.

In future this restriction may be lifted to allow a Nargo package to contain both a binary and library crate or multiple binary crates.

---


# Dependencies

Source: https://noir-lang.org/docs/noir/modules_packages_crates/dependencies

Version: v1.0.0-beta.17

On this page

Nargo allows you to upload packages to GitHub and use them as dependencies.

## Specifying a dependencySpecifying a dependency requires a `tag` to a specific commit and a `git` url to the url containing the package.

note

Without a `tag` , there would be no versioning and dependencies would change each time you compile your project.

For example, to add the [bignum library](https://github.com/noir-lang/noir-bignum) to your project, add it to *Nargo.toml*:

```
# Nargo.toml  
  
[dependencies]  
bignum = { tag = "v0.8.0", git = "https://github.com/noir-lang/noir-bignum" }
```

If the module is in a subdirectory, you can define a subdirectory in your git repository, for example:

```
# Nargo.toml  
  
[dependencies]  
blob = {tag ="v1.2.1", git = "https://github.com/AztecProtocol/aztec-packages", directory = "noir-projects/noir-protocol-circuits/crates/blob"}
```

info

Currently, there are no requirements applied on the contents of `tag`. Requirements based on semver 2.0 guidelines could be introduced in the future.

## Specifying a local dependencyYou can also specify dependencies that are local to your machine.

For example, this file structure has a library and binary crate

```
├── binary_crate  
│   ├── Nargo.toml  
│   └── src  
│       └── main.nr  
└── lib_a  
    ├── Nargo.toml  
    └── src  
        └── lib.nr
```

Inside of the binary crate, you can specify:

```
# Nargo.toml  
  
[dependencies]  
lib_a = { path = "../lib_a" }
```

## Importing dependenciesYou can import a dependency to a Noir file using the following syntax. For example, to import the
ecrecover-noir library and local lib\_a referenced above:

```
use ecrecover;  
use lib_a;
```

You can also import only the specific parts of dependency that you want to use, like so:

```
use std::hash::blake3;  
use std::scalar_mul::fixed_base_embedded_curve;
```

Lastly, You can import multiple items in the same line by enclosing them in curly braces:

```
use std::hash::{blake2s, blake3};
```

We don't have a way to consume libraries from inside a [workspace](/docs/noir/modules_packages_crates/workspaces) as external dependencies right now.

Inside a workspace, these are consumed as `{ path = "../to_lib" }` dependencies in *Nargo.toml*.

## Dependencies of DependenciesNote that when you import a dependency, you also get access to all of the dependencies of that package.

For example, the [phy\_vector](https://github.com/resurgencelabs/phy_vector) library imports an [fraction](https://github.com/resurgencelabs/fraction) library. If you're importing the phy\_vector library, then you can access the functions in fractions library like so:

```
use phy_vector;  
  
fn main(x : u32, y : pub u32) {  
  //...  
  let f = phy_vector::fraction::toFraction(true, 2, 1);  
  //...  
}
```

## Available LibrariesNoir does not currently have an official package manager. You can find a list of available Noir libraries in the [awesome-noir repo here](https://github.com/noir-lang/awesome-noir#libraries).

Some libraries that are available today include:

* [Standard Library](https://github.com/noir-lang/noir/tree/master/noir_stdlib) - the Noir Standard Library
* [Ethereum Storage Proof Verification](https://github.com/aragonzkresearch/noir-trie-proofs) - a library that contains the primitives necessary for RLP decoding (in the form of look-up table construction) and Ethereum state and storage proof verification (or verification of any trie proof involving 32-byte long keys)
* [BigInt](https://github.com/shuklaayush/noir-bigint) - a library that provides a custom BigUint56 data type, allowing for computations on large unsigned integers
* [ECrecover](https://github.com/colinnielsen/ecrecover-noir/tree/main) - a library to verify an ECDSA signature and return the source Ethereum address
* [Sparse Merkle Tree Verifier](https://github.com/vocdoni/smtverifier-noir/tree/main) - a library for verification of sparse Merkle trees
* [Signed Int](https://github.com/resurgencelabs/signed_int) - a library for accessing a custom Signed Integer data type, allowing access to negative numbers on Noir
* [Fraction](https://github.com/resurgencelabs/fraction) - a library for accessing fractional number data type in Noir, allowing results that aren't whole numbers

---


# Modules

Source: https://noir-lang.org/docs/noir/modules_packages_crates/modules

Version: v1.0.0-beta.17

On this page

Noir's module system follows the same convention as the *newer* version of Rust's module system.

## Purpose of ModulesModules are used to organize files. Without modules all of your code would need to live in a single
file. In Noir, the compiler does not automatically scan all of your files to detect modules. This
must be done explicitly by the developer.

## Examples## Importing a module in the crate rootFilename : `src/main.nr`

```
mod foo;  
  
fn main() {  
    foo::hello_world();  
}
```

Filename : `src/foo.nr`

```
fn from_foo() {}
```

In the above snippet, the crate root is the `src/main.nr` file. The compiler sees the module
declaration `mod foo` which prompts it to look for a foo.nr file.

Visually this module hierarchy looks like the following :

```
crate  
 ├── main  
 │  
 └── foo  
      └── from_foo
```

The module filename may also be the name of the module as a directory with the contents in a
file named `mod.nr` within that directory. The above example can alternatively be expressed like this:

Filename : `src/main.nr`

```
mod foo;  
  
fn main() {  
    foo::hello_world();  
}
```

Filename : `src/foo/mod.nr`

```
fn from_foo() {}
```

Note that it's an error to have both files `src/foo.nr` and `src/foo/mod.nr` in the filesystem.

## Importing a module throughout the treeAll modules are accessible from the `crate::` namespace.

```
crate  
 ├── bar  
 ├── foo  
 └── main
```

In the above snippet, if `bar` would like to use functions in `foo`, it can do so by `use crate::foo::function_name`.

## Sub-modulesFilename : `src/main.nr`

```
mod foo;  
  
fn main() {  
    foo::from_foo();  
}
```

Filename : `src/foo.nr`

```
mod bar;  
fn from_foo() {}
```

Filename : `src/foo/bar.nr`

```
fn from_bar() {}
```

In the above snippet, we have added an extra module to the module tree; `bar`. `bar` is a submodule
of `foo` hence we declare bar in `foo.nr` with `mod bar`. Since `foo` is not the crate root, the
compiler looks for the file associated with the `bar` module in `src/foo/bar.nr`

Visually the module hierarchy looks as follows:

```
crate  
 ├── main  
 │  
 └── foo  
      ├── from_foo  
      └── bar  
           └── from_bar
```

Similar to importing a module in the crate root, modules can be placed in a `mod.nr` file, like this:

Filename : `src/main.nr`

```
mod foo;  
  
fn main() {  
    foo::from_foo();  
}
```

Filename : `src/foo/mod.nr`

```
mod bar;  
fn from_foo() {}
```

Filename : `src/foo/bar/mod.nr`

```
fn from_bar() {}
```

## Referencing a parent moduleGiven a submodule, you can refer to its parent module using the `super` keyword.

Filename : `src/main.nr`

```
mod foo;  
  
fn main() {  
    foo::from_foo();  
}
```

Filename : `src/foo.nr`

```
mod bar;  
  
fn from_foo() {}
```

Filename : `src/foo/bar.nr`

```
// Same as foo::from_foo  
use super::from_foo;   
  
fn from_bar() {  
    from_foo();        // invokes super::from_foo(), which is foo::from_foo()  
    super::from_foo(); // also invokes foo::from_foo()  
}
```

## `use` visibility`use` declarations are private to the containing module, by default. However, like functions,
they can be marked as `pub` or `pub(crate)`. Such a use declaration serves to *re-export* a name.
A public `use` declaration can therefore redirect some public name to a different target definition:
even a definition with a private canonical path, inside a different module.

An example of re-exporting:

```
mod some_module {  
    pub use foo::{bar, baz};  
    mod foo {  
        pub fn bar() {}  
        pub fn baz() {}  
    }  
}  
  
fn main() {  
    some_module::bar();  
    some_module::baz();  
}
```

In this example, the module `some_module` re-exports two public names defined in `foo`.

## VisibilityBy default, like functions, modules are private to the module (or crate) they exist in. You can use `pub`
to make the module public or `pub(crate)` to make it public to just its crate:

```
// This module is now public and can be seen by other crates.  
pub mod foo;
```

---


# Workspaces

Source: https://noir-lang.org/docs/noir/modules_packages_crates/workspaces

Version: v1.0.0-beta.17

Workspaces are a feature of nargo that allow you to manage multiple related Noir packages in a single repository. A workspace is essentially a group of related projects that share common build output directories and configurations.

Each Noir project (with its own Nargo.toml file) can be thought of as a package. Each package is expected to contain exactly one "named circuit", being the "name" defined in Nargo.toml with the program logic defined in `./src/main.nr`.

For a project with the following structure:

```
├── crates  
│   ├── a  
│   │   ├── Nargo.toml  
│   │   └── Prover.toml  
│   │   └── src  
│   │       └── main.nr  
│   └── b  
│       ├── Nargo.toml  
│       └── Prover.toml  
│       └── src  
│           └── main.nr  
│  
└── Nargo.toml
```

You can define a workspace in Nargo.toml like so:

```
[workspace]  
members = ["crates/a", "crates/b"]  
default-member = "crates/a"
```

`members` indicates which packages are included in the workspace. As such, all member packages of a workspace will be processed when the `--workspace` flag is used with various commands or if a `default-member` is not specified. The `--package` option can be used to limit
the scope of some commands to a specific member of the workspace; otherwise these commands run on the package nearest on the path to the
current directory where `nargo` was invoked.

`default-member` indicates which package various commands process by default.

Libraries can be defined in a workspace. Inside a workspace, these are consumed as `{ path = "../to_lib" }` dependencies in Nargo.toml.

Inside a workspace, these are consumed as `{ path = "../to_lib" }` dependencies in Nargo.toml.

Please note that nesting regular packages is not supported: certain commands work on the workspace level and will use the topmost Nargo.toml file they can find on the path; unless this is a workspace configuration with `members`, the command might run on some unintended package.

---


# Explainers

Source: https://noir-lang.org/docs/explainers/explainer-writing-noir

Version: v1.0.0-beta.17

On this page

This article intends to set you up with key concepts essential for writing more viable applications that use zero knowledge proofs, namely around efficient circuits.

## Context - 'Efficient' is subjectiveWhen writing a web application for a performant computer with high-speed internet connection, writing efficient code sometimes is seen as an afterthought only if needed. Large multiplications running at the innermost of nested loops may not even be on a dev's radar.
When writing firmware for a battery-powered microcontroller, you think of cpu cycles as rations to keep within a product's power budget.

> Code is written to create applications that perform specific tasks within specific constraints

And these constraints differ depending on where the compiled code is execute.

## The Ethereum Virtual Machine (EVM)")

In scenarios where extremely low gas costs are required for an Ethereum application to be viable/competitive, Ethereum smart contract developers get into what is colloquially known as: "*gas golfing*". Finding the lowest execution cost of their compiled code (EVM bytecode) to achieve a specific task.

The equivalent optimization task when writing zk circuits is affectionately referred to as "*gate golfing*", finding the lowest gate representation of the compiled Noir code.

## Coding for circuits - a paradigm shiftIn zero knowledge cryptography, code is compiled to "circuits" consisting of arithmetic gates, and gate count is the significant cost. Depending on the proving system this is linearly proportionate to proof size and proving time, so from a product point of view this should be kept as low as possible.

Whilst writing efficient code for web apps and Solidity have some differences, writing efficient circuits have a different set of considerations. It is a bit of a paradigm shift, like writing code for GPUs for the first time...

For example, drawing a circle at (0, 0) of radius `r`:

* For a single CPU thread,

```
for theta in 0..2*pi {  
  let x = r * cos(theta);  
  let y = r * sin(theta);  
  draw(x, y);  
} // note: would do 0 - pi/2 and draw +ve/-ve x and y.
```

* For GPUs (simultaneous parallel calls with x, y across image),

```
if (x^2 + y^2 = r^2) {  
  draw(x, y);  
}
```

([Related](https://www.youtube.com/watch?v=-P28LKWTzrI))

Whilst this CPU -> GPU does not translate to circuits exactly, it is intended to exemplify the difference in intuition when coding for different machine capabilities/constraints.

## Context TakeawayFor those coming from a primarily web app background, this article will explain what you need to consider when writing circuits. Furthermore, for those experienced writing efficient machine code, prepare to shift what you think is efficient 😬

## Translating from RustPrograms written in anything from pseudo code to C, can be translated into Noir. A Rust program written for execution can be readily ported to Noir thanks to the similarities in syntax.

note

Many valuable functions and algorithms have been written in more established languages (C/C++), and converted to modern ones (like Rust).

Fortunately for Noir developers, when needing a particular function a Rust implementation can be readily compiled into Noir with some key changes. While the compiler does a decent amount of optimizations, it won't be able to change code that has been optimized for clock-cycles into code optimized for arithmetic gates.

A few things to do when converting Rust code to Noir:

* `println!` is not a macro, use `println` function (same for `assert_eq`)
* No early `return` in function. Use constrain via assertion instead
* No passing by reference. Remove `&` operator to pass by value (copy)
* No boolean operators (`&&`, `||`). Use bitwise operators (`&`, `|`) with boolean values
* No type `usize`. Use types `u8`, `u32`, `u64`, ...
* `main` return must be public, `pub`
* No `const`, use `global`
* Noir's LSP is your friend, so error message should be informative enough to resolve syntax issues.

## Writing efficient Noir for performant productsThe following points help refine our understanding over time.

note

A Noir program makes a statement that can be verified.

It compiles to a structure that represents the calculation, and can assert results within the calculation at any stage (via the `constrain` keyword).

A Noir program compiles to an Abstract Circuit Intermediate Representation which is:

* Conceptually a tree structure
* Leaves (inputs) are the `Field` type
* Nodes contain arithmetic operations to combine them (gates)
* The root is the final result (return value)

tip

The command `nargo info` shows the programs circuit size, and is useful to compare the value of changes made.
You can dig deeper and use the `--print-acir` param to take a closer look at individual ACIR opcodes, and the proving backend to see its gate count (eg for barretenberg, the `bb` binary has a `gates` option).

## Numerical typesAs mentioned earlier Noir has many familiar integer types (eg `i8`, `u64`). Ideally after bringing a program into Noir, proving/verifying of its execution just works where needed: client/server side, on an evm, or on the Aztec network.

A program optimized for execution may leverage the binary representations of integers, reducing the number of clock cycles, and thus time of execution.
The cryptography in a proving backend makes use of a `Field` type, and leveraging this lower level type correctly can reduce gate count, and thus proof size and proving time.

In some instances simply replacing the integer type with a `Field` could save on some range checks (and hence gates).
Note: when casting a `Field` to an integer type, the value is converted based on the integer binary representation. Eg a Field variable with a value of 260 `as u8` becomes 4

## `Field`s for efficiency`Field` types have their own underlying representation that is efficient for cryptography, which is different to binary representations efficient for CPUs. So, mathematically speaking, things like bitwise operations do not directly translate to fields. That said, the same outcome can be achieved if wanting to use the Field type as a number with lower overhead.

For instance shift (`<<`) and or (`|`) work seamlessly with integer types (bit-packing `u8`'s into a `u16`):

```
  high as u16 << 8 | low as u16
```

More efficiently with `Field` types, the equivalent is:

```
  low.assert_max_bit_size::<8>(); // ensure Field values could be represented as 8 bit numbers  
  high.assert_max_bit_size::<8>();  
  (high * 2.pow_32(8) + low)
```

(Note, the power of two can instead be a constant (256) or global evaluated at compile time)

The first snippet is good for compatibility when using existing code, converting to the latter can help optimize frequently used functions.

tip

Where possible, use the `Field` type for values. Writing code with smaller value types and bit-packing strategies will result in MORE gates

## Use Arithmetic over non-arithmetic operationsSince circuits are made of arithmetic gates, the cost of arithmetic operations tends to be one gate. Whereas for procedural code, they represent several clock cycles.

Inversely, non-arithmetic operators are achieved with multiple gates, vs 1 clock cycle for procedural code.

| (cost\op) | arithmetic (`*`, `+`) | bit-wise ops (eg `<`, `|`, `>>`) |
| --- | --- | --- |
| **cycles** | 10+ | 1 |
| **gates** | 1 | 10+ |

Bit-wise operations (e.g. bit shifts `<<` and `>>`), albeit commonly used in general programming and especially for clock cycle optimizations, are on the contrary expensive in gates when performed within circuits.

Translate away from bit shifts when writing constrained functions for the best performance.

On the flip side, feel free to use bit shifts in unconstrained functions and tests if necessary, as they are executed outside of circuits and does not induce performance hits.

## Use static over dynamic valuesAnother general theme that manifests in different ways is that static reads are represented with less gates than dynamic ones.

Reading from read-only memory (ROM) adds less gates than random-access memory (RAM), 2 vs ~3.25 due to the additional bounds checks. Arrays of fixed length (albeit used at a lower capacity), will generate less gates than dynamic storage.

Related to this, if an index used to access an array is not known at compile time (ie unknown until run time), then ROM will be converted to RAM, expanding the gate count.

tip

Use arrays and indices that are known at compile time where possible.
Using `assert_constant(i);` before an index, `i`, is used in an array will give a compile error if `i` is NOT known at compile time.

## Reduce what is inside loops and conditional logicPutting less logic inside an `if` (`else`, etc) paths, or inside a loop, translates to less gates required to represent the program. The compiler should mostly take care of this.

A loop duplicates the gates for each iteration of the loop, or put another way, "unrolls" the loop. Any calculations/calls that are unchanged in the loop should be calculated once before, and the result used in the loop.

An `if` statement is "flattened" and gates created for each path even if execution uses only one path. Furthermore, there are additional operations required for each path. Sometimes this can have a multiplying effect on the operations in the `if` and `else` etc.

tip

Only have essential computation inside conditional logic and loops, and calculate anything else once (before, or after, depending).

## Leverage unconstrained executionConstrained verification can leverage unconstrained execution, this is especially useful for operations that are represented by many gates.
Use an [unconstrained function](/docs/noir/concepts/unconstrained) to perform gate-heavy calculations, then verify and constrain the result.

Eg division generates more gates than multiplication, so calculating the quotient in an unconstrained function then constraining the product for the quotient and divisor (+ any remainder) equals the dividend will be more efficient.

Use  `if is_unconstrained() { /`, to conditionally execute code if being called in an unconstrained vs constrained way.

## AdvancedUnless you're well into the depth of gate optimization, this advanced section can be ignored.

## Combine arithmetic operationsA Noir program can be honed further by combining arithmetic operators in a way that makes the most of each constraint of the backend proving system. This is in scenarios where the backend might not be doing this perfectly.

Eg Barretenberg backend (current default for Noir) is a width-4 PLONKish constraint system
w1∗w2∗qm+w1∗q1+w2∗q2+w3∗q3+w4∗q4+qc=0w\_1\*w\_2\*q\_m + w\_1\*q\_1 + w\_2\*q\_2 + w\_3\*q\_3 + w\_4\*q\_4 + q\_c = 0w1​∗w2​∗qm​+w1​∗q1​+w2​∗q2​+w3​∗q3​+w4​∗q4​+qc​=0

Here we see there is one occurrence of witness 1 and 2 (w1w\_1w1​, w2w\_2w2​) being multiplied together, with addition to witnesses 1-4 (w1w\_1w1​ .. w4w\_4w4​) multiplied by 4 corresponding circuit constants (q1q\_1q1​ .. q4q\_4q4​) (plus a final circuit constant, qcq\_cqc​).

Use `nargo info --print-acir`, to inspect the ACIR opcodes (and the proving system for gates), and it may present opportunities to amend the order of operations and reduce the number of constraints.

## Variable as witness vs expressionIf you've come this far and really know what you're doing at the equation level, a temporary lever (that will become unnecessary/useless over time) is: `std::as_witness`. This informs the compiler to save a variable as a witness not an expression.

The compiler will mostly be correct and optimal, but this may help some near term edge cases that are yet to optimize.
Note: When used incorrectly it will create **less** efficient circuits (higher gate count).

## References* Guillaume's ["`Crypdoku`" talk](https://www.youtube.com/watch?v=MrQyzuogxgg) (Jun'23)
* [Idiomatic Noir](https://www.vlayer.xyz/blog/idiomatic-noir-part-1-collections) blog post

---


# Tutorials

Source: https://noir-lang.org/docs/tutorials/noirjs_app

Version: v1.0.0-beta.17

On this page

NoirJS is a Typescript package meant to work both in a browser and a server environment.

In this tutorial, we will combine NoirJS with Aztec's Barretenberg backend to build a simple web app. From here, you should get an idea on how to proceed with your own Noir projects!

You can find the complete app code for this guide [here](https://github.com/noir-lang/tiny-noirjs-app).

## DependenciesBefore we start, we want to make sure we have Node installed. If you don't have it already you can install it [here](https://nodejs.org/en/download), we recommend using [Yarn](https://yarnpkg.com/getting-started/install) as our package manager for this tutorial.

We'll also need version 1.0.0-beta.15 nargo installed, see the Noir [installation guide](/docs/getting_started/noir_installation) for details.

Let's go barebones. Doing the bare minimum is not only simple, but also allows you to easily adapt it to almost any frontend framework.

Barebones means we can immediately start with the dependencies even on an empty folder 😈:

```
yarn add @noir-lang/noir_js@1.0.0-beta.15 @aztec/bb.js@3.0.0-nightly.20251104 buffer vite vite-plugin-node-polyfills@0.17.0
```

Wait, what are these dependencies?

* `noir_js` is the main Noir package. It will execute our program, and generate the witness that will be sent to the backend.
* `bb.js` is the Typescript interface for Aztec's Barretenberg proving backend. It also uses the `wasm` version in order to run on the browser.

info

In this guide, we will install versions pinned to 1.0.0-beta.15. These work with Barretenberg version 3.0.0-nightly.20251104, so we are using that one version too. Feel free to try with older or later versions, though!

## Setting up our Noir programZK is a powerful technology. An app that reveals computational correctness but doesn't reveal some of its inputs is almost unbelievable, yet Noir makes it as easy as a single line of code.

tip

It's not just you. We also enjoy syntax highlighting. [Check out the Language Server](/docs/tooling/language_server)

All you need is a `main.nr` and a `Nargo.toml` file. You can follow the [noirup](/docs/getting_started/noir_installation) installation and just run `noirup -v 1.0.0-beta.15`, or just create them by hand:

```
mkdir -p circuit/src  
touch circuit/src/main.nr circuit/Nargo.toml
```

To make our program interesting, let's give it a real use-case scenario: Bob wants to prove he is older than 18, without disclosing his age. Open `main.nr` and write:

age\_check

```
fn main(age: u8) {  
    assert(age > 18);  
}
```

> [Source code: examples/browser/src/main.nr#L1-L5](https://github.com/noir-lang/noir/blob/master/examples/browser/src/main.nr#L1-L5)

This program accepts a private input called age, and simply proves this number is higher than 18. But to run this code, we need to give the compiler a `Nargo.toml` with at least a name and a type:

```
[package]  
name = "circuit"  
type = "bin"
```

This is all that we need to get started with Noir.

![my heart is ready for you, noir.js](/docs/assets/images/titanic-d2704a425a86db29828739ded4d92dd4.jpeg)

## Compile compile compileFinally we're up for something cool. But before we can execute a Noir program, we need to compile it into ACIR: an abstract representation.

This can be done by cd-ing into our circuit directory and running the `nargo compile` command.

```
cd circuit  
  
nargo compile
```

This will write the compiled circuit into the `target` directory, which we'll then load into our JS later on.

## Setting up our appRemember when apps only had one `html` and one `js` file? Well, that's enough for Noir webapps. Let's create them in the project root:

```
touch index.html index.js
```

And add something useful to our HTML file:

index

```
<!DOCTYPE html>  
<head>  
  <style>  
    .outer {  
        display: flex;  
        justify-content: space-between;  
        width: 100%;  
    }  
    .inner {  
        width: 45%;  
        border: 1px solid black;  
        padding: 10px;  
        word-wrap: break-word;  
    }  
  </style>  
</head>  
<body>  
  <script type="module" src="/index.js"></script>  
  <h1>Noir app</h1>  
  <div class="input-area">  
    <input id="age" type="number" placeholder="Enter age" />  
    <button id="submit">Submit Age</button>  
  </div>  
  <div class="outer">  
    <div id="logs" class="inner"><h2>Logs</h2></div>  
    <div id="results" class="inner"><h2>Proof</h2></div>  
  </div>  
</body>  
</html>
```

> [Source code: examples/browser/index.html#L1-L31](https://github.com/noir-lang/noir/blob/master/examples/browser/index.html#L1-L31)

It *could* be a beautiful UI... Depending on which universe you live in. In any case, we're using some scary CSS to make two boxes that will show cool things on the screen.

As for the JS, real madmen could just `console.log` everything, but let's say we want to see things happening (the true initial purpose of JS... right?). Here's some boilerplate for that. Just paste it in `index.js`:

```
const show = (id, content) => {  
  const container = document.getElementById(id);  
  container.appendChild(document.createTextNode(content));  
  container.appendChild(document.createElement('br'));  
};  
  
document.getElementById('submit').addEventListener('click', async () => {  
  try {  
    // code will go in here  
  }  catch {  
    show('logs', 'Oh 💔');  
  }  
});
```

info

At this point in the tutorial, your folder structure should look like this:

```
.  
├── circuit  
│   ├── Nargo.toml  
│   ├── src  
│   │   └── main.nr  
│   └── target  
│       └── circuit.json  
├── index.html  
├── index.js  
├── package.json  
├── etc...
```

## Some more JSWe're starting with the good stuff now. We want to execute our circuit to get the witness, and then feed that witness to Barretenberg. Luckily, both packages are quite easy to work with. Let's import them at the top of the file and initialize the WASM modules:

imports

```
import { UltraHonkBackend } from '@aztec/bb.js';  
import { Noir } from '@noir-lang/noir_js';  
import initNoirC from '@noir-lang/noirc_abi';  
import initACVM from '@noir-lang/acvm_js';  
import acvm from '@noir-lang/acvm_js/web/acvm_js_bg.wasm?url';  
import noirc from '@noir-lang/noirc_abi/web/noirc_abi_wasm_bg.wasm?url';  
import circuit from './circuit/target/circuit.json';  
// Initialize WASM modules  
await Promise.all([initACVM(fetch(acvm)), initNoirC(fetch(noirc))]);
```

> [Source code: examples/browser/index.js#L1-L11](https://github.com/noir-lang/noir/blob/master/examples/browser/index.js#L1-L11)

And instantiate them inside our try-catch block:

init

```
const noir = new Noir(circuit);  
    const backend = new UltraHonkBackend(circuit.bytecode);
```

> [Source code: examples/browser/index.js#L23-L26](https://github.com/noir-lang/noir/blob/master/examples/browser/index.js#L23-L26)

## Executing and provingNow for the app itself. We're capturing whatever is in the input when people press the submit button. Inside our `try` block, let's just grab that input and get its value. Noir will gladly execute it, and give us a witness:

execute

```
const age = document.getElementById('age').value;  
    show('logs', 'Generating witness... ⏳');  
    const { witness } = await noir.execute({ age });  
    show('logs', 'Generated witness... ✅');
```

> [Source code: examples/browser/index.js#L27-L32](https://github.com/noir-lang/noir/blob/master/examples/browser/index.js#L27-L32)

note

For the remainder of the tutorial, everything will be happening inside the `try` block

Now we're ready to prove stuff! Let's feed some inputs to our circuit and calculate the proof:

prove

```
show('logs', 'Generating proof... ⏳');  
    const proof = await backend.generateProof(witness);  
    show('logs', 'Generated proof... ✅');  
    show('results', proof.proof);
```

> [Source code: examples/browser/index.js#L33-L38](https://github.com/noir-lang/noir/blob/master/examples/browser/index.js#L33-L38)

Our program is technically **done** . You're probably eager to see stuff happening! To serve this in a convenient way, we can use a bundler like `vite` by creating a `vite.config.js` file:

```
touch vite.config.js
```

Noir needs to load two WASM modules, but Vite doesn't include them by default in the bundle. We need to add the configuration below to `vite.config.js` to make it work.
We also need to target ESNext since `bb.js` uses top-level await, which isn't supported in some browsers.

config

```
import { defineConfig } from 'vite';  
import { nodePolyfills } from 'vite-plugin-node-polyfills';  
  
export default defineConfig({  
  plugins: [nodePolyfills()],  
  optimizeDeps: {  
    exclude: ['@aztec/bb.js'],  
  },  
  resolve: {  
    alias: {  
      pino: 'pino/browser.js',  
    },  
  },  
});
```

> [Source code: examples/browser/vite.config.js#L1-L16](https://github.com/noir-lang/noir/blob/master/examples/browser/vite.config.js#L1-L16)

This should be enough for vite. We don't even need to install it, just run:

```
yarn vite dev
```

If it doesn't open a browser for you, just visit `localhost:5173`. You should now see the worst UI ever, with an ugly input.

![Noir Webapp UI](/docs/assets/images/webapp1-d6f2b2258acb7f8a416c4fb4264b3697.png)

Now, our circuit requires a private input `fn main(age: u8)`, and fails if it is less than 18. Let's see if it works. Submit any number above 18 (as long as it fits in 8 bits) and you should get a valid proof. Otherwise the proof won't even generate correctly.

By the way, if you're human, you shouldn't be able to understand anything on the "proof" box. That's OK. We like you, human ❤️.

## VerifyingTime to celebrate, yes! But we shouldn't trust machines so blindly. Let's add these lines to see our proof being verified:

verify

```
show('logs', 'Verifying proof... ⌛');  
    const isValid = await backend.verifyProof(proof);  
    show('logs', `Proof is ${isValid ? 'valid' : 'invalid'}... ✅`);
```

> [Source code: examples/browser/index.js#L40-L44](https://github.com/noir-lang/noir/blob/master/examples/browser/index.js#L40-L44)

You have successfully generated a client-side Noir web app!

![coded app without math knowledge](/docs/assets/images/flextape-c09f3e7e99be36195b640a90e68aa7da.jpeg)

## Next stepsAt this point, you have a working ZK app that works on the browser. Actually, it works on a mobile phone too!

If you want to continue learning by doing, here are some challenges for you:

* Install [nargo](https://noir-lang.org/docs/getting_started/noir_installation) and write [Noir tests](/docs/tooling/tests)
* Change the circuit to accept a [public input](/docs/noir/concepts/data_types#private--public-types) as the cutoff age. It could be different depending on the purpose, for example!
* Enjoy Noir's Rust-like syntax and write a struct `Country` that implements a trait `MinAge` with a method `get_min_age`. Then, make a struct `Person` have an `u8` as its age and a country of type `Country`. You can pass a `person` in JS just like a JSON object `person: { age, country: { min_age: 18 }}`

The world is your stage, just have fun with ZK! You can see how noirjs is used in some common frameworks in the [awesome-noir repo](https://github.com/noir-lang/awesome-noir?tab=readme-ov-file#boilerplates).

---


# Reference

Source: https://noir-lang.org/docs/reference/nargo_commands

Version: v1.0.0-beta.17

On this page

This document contains the help content for the `nargo` command-line program.

**Command Overview:**

* [`nargo`↴](#nargo)
* [`nargo check`↴](#nargo-check)
* [`nargo fmt`↴](#nargo-fmt)
* [`nargo compile`↴](#nargo-compile)
* [`nargo new`↴](#nargo-new)
* [`nargo init`↴](#nargo-init)
* [`nargo execute`↴](#nargo-execute)
* [`nargo export`↴](#nargo-export)
* [`nargo debug`↴](#nargo-debug)
* [`nargo test`↴](#nargo-test)
* [`nargo fuzz`↴](#nargo-fuzz)
* [`nargo info`↴](#nargo-info)
* [`nargo lsp`↴](#nargo-lsp)
* [`nargo expand`↴](#nargo-expand)
* [`nargo doc`↴](#nargo-doc)
* [`nargo generate-completion-script`↴](#nargo-generate-completion-script)

## `nargo`Noir's package manager

**Usage:** `nargo <COMMAND>`

## **Subcommands:*** `check` — Check a local package and all of its dependencies for errors
* `fmt` — Format the Noir files in a workspace
* `compile` — Compile the program and its secret execution trace into ACIR format
* `new` — Create a Noir project in a new directory
* `init` — Create a Noir project in the current directory
* `execute` — Executes a circuit to calculate its return value
* `export` — Exports functions marked with #[export] attribute
* `debug` — Executes a circuit in debug mode
* `test` — Run the tests for this program
* `fuzz` — Run the fuzzing harnesses for this program
* `info` — Provides detailed information on each of a program's function (represented by a single circuit)
* `lsp` — Starts the Noir LSP server
* `expand` — Show the result of macro expansion
* `doc` — Builds documentation for the specified package or workspace
* `generate-completion-script` — Generates a shell completion script for your favorite shell

## **Options:**## `nargo check`Check a local package and all of its dependencies for errors

**Usage:** `nargo check [OPTIONS]`

## **Options:*** `--package <PACKAGE>` — The name of the package to run the command on. By default run on the first one found moving up along the ancestors of the current directory
* `--workspace` — Run on all packages in the workspace

  Possible values: `true`, `false`
* `--overwrite` — Force overwrite of existing files

  Possible values: `true`, `false`
* `--force` — Force a full recompilation

  Possible values: `true`, `false`
* `--print-acir` — Display the ACIR for compiled circuit, including the Brillig bytecode

  Possible values: `true`, `false`
* `--deny-warnings` — Treat all warnings as errors

  Possible values: `true`, `false`
* `--silence-warnings` — Suppress warnings

  Possible values: `true`, `false`
* `--debug-comptime-in-file <DEBUG_COMPTIME_IN_FILE>` — Enable printing results of comptime evaluation: provide a path suffix for the module to debug, e.g. "package\_name/src/main.nr"
* `--skip-underconstrained-check` — Flag to turn off the compiler check for under constrained values. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--skip-brillig-constraints-check` — Flag to turn off the compiler check for missing Brillig call constraints. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--count-array-copies` — Count the number of arrays that are copied in an unconstrained context for performance debugging

  Possible values: `true`, `false`
* `--enable-brillig-constraints-check-lookback` — Flag to turn on the lookback feature of the Brillig call constraints check, allowing tracking argument values before the call happens preventing certain rare false positives (leads to a slowdown on large rollout functions)

  Possible values: `true`, `false`
* `--inliner-aggressiveness <INLINER_AGGRESSIVENESS>` — Setting to decide on an inlining strategy for Brillig functions. A more aggressive inliner should generate larger programs but more optimized A less aggressive inliner should generate smaller programs

  Default value: `9223372036854775807`
* `--pedantic-solving` — Use pedantic ACVM solving, i.e. double-check some black-box function assumptions when solving. This is disabled by default

  Default value: `false`

  Possible values: `true`, `false`
* `-Z`, `--unstable-features <UNSTABLE_FEATURES>` — Unstable features to enable for this current build.

If non-empty, it disables unstable features required in crate manifests.

* `--no-unstable-features` — Disable any unstable features required in crate manifests

  Possible values: `true`, `false`

## `nargo fmt`Format the Noir files in a workspace

**Usage:** `nargo fmt [OPTIONS]`

## **Options:*** `--check` — Run noirfmt in check mode

  Possible values: `true`, `false`
* `--package <PACKAGE>` — The name of the package to run the command on. By default run on the first one found moving up along the ancestors of the current directory
* `--workspace` — Run on all packages in the workspace

  Possible values: `true`, `false`

## `nargo compile`Compile the program and its secret execution trace into ACIR format

**Usage:** `nargo compile [OPTIONS]`

## **Options:*** `--package <PACKAGE>` — The name of the package to run the command on. By default run on the first one found moving up along the ancestors of the current directory
* `--workspace` — Run on all packages in the workspace

  Possible values: `true`, `false`
* `--force` — Force a full recompilation

  Possible values: `true`, `false`
* `--print-acir` — Display the ACIR for compiled circuit, including the Brillig bytecode

  Possible values: `true`, `false`
* `--deny-warnings` — Treat all warnings as errors

  Possible values: `true`, `false`
* `--silence-warnings` — Suppress warnings

  Possible values: `true`, `false`
* `--debug-comptime-in-file <DEBUG_COMPTIME_IN_FILE>` — Enable printing results of comptime evaluation: provide a path suffix for the module to debug, e.g. "package\_name/src/main.nr"
* `--skip-underconstrained-check` — Flag to turn off the compiler check for under constrained values. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--skip-brillig-constraints-check` — Flag to turn off the compiler check for missing Brillig call constraints. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--count-array-copies` — Count the number of arrays that are copied in an unconstrained context for performance debugging

  Possible values: `true`, `false`
* `--enable-brillig-constraints-check-lookback` — Flag to turn on the lookback feature of the Brillig call constraints check, allowing tracking argument values before the call happens preventing certain rare false positives (leads to a slowdown on large rollout functions)

  Possible values: `true`, `false`
* `--inliner-aggressiveness <INLINER_AGGRESSIVENESS>` — Setting to decide on an inlining strategy for Brillig functions. A more aggressive inliner should generate larger programs but more optimized A less aggressive inliner should generate smaller programs

  Default value: `9223372036854775807`
* `--pedantic-solving` — Use pedantic ACVM solving, i.e. double-check some black-box function assumptions when solving. This is disabled by default

  Default value: `false`

  Possible values: `true`, `false`
* `-Z`, `--unstable-features <UNSTABLE_FEATURES>` — Unstable features to enable for this current build.

If non-empty, it disables unstable features required in crate manifests.

* `--no-unstable-features` — Disable any unstable features required in crate manifests

  Possible values: `true`, `false`

## `nargo new`Create a Noir project in a new directory

**Usage:** `nargo new [OPTIONS] <PATH>`

## **Arguments:*** `<PATH>` — The path to save the new project

## **Options:*** `--name <NAME>` — Name of the package [default: package directory name]
* `--lib` — Use a library template

  Possible values: `true`, `false`
* `--bin` — Use a binary template [default]

  Possible values: `true`, `false`
* `--contract` — Use a contract template

  Possible values: `true`, `false`

## `nargo init`Create a Noir project in the current directory

**Usage:** `nargo init [OPTIONS]`

## **Options:*** `--name <NAME>` — Name of the package [default: current directory name]
* `--lib` — Use a library template

  Possible values: `true`, `false`
* `--bin` — Use a binary template [default]

  Possible values: `true`, `false`
* `--contract` — Use a contract template

  Possible values: `true`, `false`

## `nargo execute`Executes a circuit to calculate its return value

**Usage:** `nargo execute [OPTIONS] [WITNESS_NAME]`

## **Arguments:*** `<WITNESS_NAME>` — Write the execution witness to named file

Defaults to the name of the package being executed.

## **Options:*** `-p`, `--prover-name <PROVER_NAME>` — The name of the toml file which contains the inputs for the prover

  Default value: `Prover`
* `--package <PACKAGE>` — The name of the package to run the command on. By default run on the first one found moving up along the ancestors of the current directory
* `--workspace` — Run on all packages in the workspace

  Possible values: `true`, `false`
* `--force` — Force a full recompilation

  Possible values: `true`, `false`
* `--print-acir` — Display the ACIR for compiled circuit, including the Brillig bytecode

  Possible values: `true`, `false`
* `--deny-warnings` — Treat all warnings as errors

  Possible values: `true`, `false`
* `--silence-warnings` — Suppress warnings

  Possible values: `true`, `false`
* `--debug-comptime-in-file <DEBUG_COMPTIME_IN_FILE>` — Enable printing results of comptime evaluation: provide a path suffix for the module to debug, e.g. "package\_name/src/main.nr"
* `--skip-underconstrained-check` — Flag to turn off the compiler check for under constrained values. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--skip-brillig-constraints-check` — Flag to turn off the compiler check for missing Brillig call constraints. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--count-array-copies` — Count the number of arrays that are copied in an unconstrained context for performance debugging

  Possible values: `true`, `false`
* `--enable-brillig-constraints-check-lookback` — Flag to turn on the lookback feature of the Brillig call constraints check, allowing tracking argument values before the call happens preventing certain rare false positives (leads to a slowdown on large rollout functions)

  Possible values: `true`, `false`
* `--inliner-aggressiveness <INLINER_AGGRESSIVENESS>` — Setting to decide on an inlining strategy for Brillig functions. A more aggressive inliner should generate larger programs but more optimized A less aggressive inliner should generate smaller programs

  Default value: `9223372036854775807`
* `--pedantic-solving` — Use pedantic ACVM solving, i.e. double-check some black-box function assumptions when solving. This is disabled by default

  Default value: `false`

  Possible values: `true`, `false`
* `-Z`, `--unstable-features <UNSTABLE_FEATURES>` — Unstable features to enable for this current build.

If non-empty, it disables unstable features required in crate manifests.

* `--no-unstable-features` — Disable any unstable features required in crate manifests

  Possible values: `true`, `false`
* `--oracle-resolver <ORACLE_RESOLVER>` — JSON RPC url to solve oracle calls
* `--oracle-file <ORACLE_FILE>` — Path to the oracle transcript

## `nargo export`Exports functions marked with #[export] attribute

**Usage:** `nargo export [OPTIONS]`

## **Options:*** `--package <PACKAGE>` — The name of the package to run the command on. By default run on the first one found moving up along the ancestors of the current directory
* `--workspace` — Run on all packages in the workspace

  Possible values: `true`, `false`
* `--force` — Force a full recompilation

  Possible values: `true`, `false`
* `--print-acir` — Display the ACIR for compiled circuit, including the Brillig bytecode

  Possible values: `true`, `false`
* `--deny-warnings` — Treat all warnings as errors

  Possible values: `true`, `false`
* `--silence-warnings` — Suppress warnings

  Possible values: `true`, `false`
* `--debug-comptime-in-file <DEBUG_COMPTIME_IN_FILE>` — Enable printing results of comptime evaluation: provide a path suffix for the module to debug, e.g. "package\_name/src/main.nr"
* `--skip-underconstrained-check` — Flag to turn off the compiler check for under constrained values. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--skip-brillig-constraints-check` — Flag to turn off the compiler check for missing Brillig call constraints. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--count-array-copies` — Count the number of arrays that are copied in an unconstrained context for performance debugging

  Possible values: `true`, `false`
* `--enable-brillig-constraints-check-lookback` — Flag to turn on the lookback feature of the Brillig call constraints check, allowing tracking argument values before the call happens preventing certain rare false positives (leads to a slowdown on large rollout functions)

  Possible values: `true`, `false`
* `--inliner-aggressiveness <INLINER_AGGRESSIVENESS>` — Setting to decide on an inlining strategy for Brillig functions. A more aggressive inliner should generate larger programs but more optimized A less aggressive inliner should generate smaller programs

  Default value: `9223372036854775807`
* `--pedantic-solving` — Use pedantic ACVM solving, i.e. double-check some black-box function assumptions when solving. This is disabled by default

  Default value: `false`

  Possible values: `true`, `false`
* `-Z`, `--unstable-features <UNSTABLE_FEATURES>` — Unstable features to enable for this current build.

If non-empty, it disables unstable features required in crate manifests.

* `--no-unstable-features` — Disable any unstable features required in crate manifests

  Possible values: `true`, `false`

## `nargo debug`Executes a circuit in debug mode

**Usage:** `nargo debug [OPTIONS] [WITNESS_NAME]`

## **Arguments:*** `<WITNESS_NAME>` — Write the execution witness to named file

## **Options:*** `-p`, `--prover-name <PROVER_NAME>` — The name of the toml file which contains the inputs for the prover

  Default value: `Prover`
* `--package <PACKAGE>` — The name of the package to execute
* `--force` — Force a full recompilation

  Possible values: `true`, `false`
* `--print-acir` — Display the ACIR for compiled circuit, including the Brillig bytecode

  Possible values: `true`, `false`
* `--deny-warnings` — Treat all warnings as errors

  Possible values: `true`, `false`
* `--silence-warnings` — Suppress warnings

  Possible values: `true`, `false`
* `--debug-comptime-in-file <DEBUG_COMPTIME_IN_FILE>` — Enable printing results of comptime evaluation: provide a path suffix for the module to debug, e.g. "package\_name/src/main.nr"
* `--skip-underconstrained-check` — Flag to turn off the compiler check for under constrained values. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--skip-brillig-constraints-check` — Flag to turn off the compiler check for missing Brillig call constraints. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--count-array-copies` — Count the number of arrays that are copied in an unconstrained context for performance debugging

  Possible values: `true`, `false`
* `--enable-brillig-constraints-check-lookback` — Flag to turn on the lookback feature of the Brillig call constraints check, allowing tracking argument values before the call happens preventing certain rare false positives (leads to a slowdown on large rollout functions)

  Possible values: `true`, `false`
* `--inliner-aggressiveness <INLINER_AGGRESSIVENESS>` — Setting to decide on an inlining strategy for Brillig functions. A more aggressive inliner should generate larger programs but more optimized A less aggressive inliner should generate smaller programs

  Default value: `9223372036854775807`
* `--pedantic-solving` — Use pedantic ACVM solving, i.e. double-check some black-box function assumptions when solving. This is disabled by default

  Default value: `false`

  Possible values: `true`, `false`
* `-Z`, `--unstable-features <UNSTABLE_FEATURES>` — Unstable features to enable for this current build.

If non-empty, it disables unstable features required in crate manifests.

* `--no-unstable-features` — Disable any unstable features required in crate manifests

  Possible values: `true`, `false`
* `--acir-mode` — Force ACIR output (disabling instrumentation)

  Possible values: `true`, `false`
* `--skip-instrumentation <SKIP_INSTRUMENTATION>` — Disable vars debug instrumentation (enabled by default)

  Possible values: `true`, `false`
* `--test-name <TEST_NAME>` — Name (or substring) of the test function to debug
* `--oracle-resolver <ORACLE_RESOLVER>` — JSON RPC url to solve oracle calls

## `nargo test`Run the tests for this program

**Usage:** `nargo test [OPTIONS] [TEST_NAMES]...`

## **Arguments:*** `<TEST_NAMES>` — If given, only tests with names containing this string will be run

## **Options:*** `--show-output` — Display output of `println` statements

  Possible values: `true`, `false`
* `--exact` — Only run tests that match exactly

  Possible values: `true`, `false`
* `--list-tests` — Print all matching test names, without running them

  Possible values: `true`, `false`
* `--no-run` — Only compile the tests, without running them

  Possible values: `true`, `false`
* `--package <PACKAGE>` — The name of the package to run the command on. By default run on the first one found moving up along the ancestors of the current directory
* `--workspace` — Run on all packages in the workspace

  Possible values: `true`, `false`
* `--force` — Force a full recompilation

  Possible values: `true`, `false`
* `--print-acir` — Display the ACIR for compiled circuit, including the Brillig bytecode

  Possible values: `true`, `false`
* `--deny-warnings` — Treat all warnings as errors

  Possible values: `true`, `false`
* `--silence-warnings` — Suppress warnings

  Possible values: `true`, `false`
* `--debug-comptime-in-file <DEBUG_COMPTIME_IN_FILE>` — Enable printing results of comptime evaluation: provide a path suffix for the module to debug, e.g. "package\_name/src/main.nr"
* `--skip-underconstrained-check` — Flag to turn off the compiler check for under constrained values. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--skip-brillig-constraints-check` — Flag to turn off the compiler check for missing Brillig call constraints. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--count-array-copies` — Count the number of arrays that are copied in an unconstrained context for performance debugging

  Possible values: `true`, `false`
* `--enable-brillig-constraints-check-lookback` — Flag to turn on the lookback feature of the Brillig call constraints check, allowing tracking argument values before the call happens preventing certain rare false positives (leads to a slowdown on large rollout functions)

  Possible values: `true`, `false`
* `--inliner-aggressiveness <INLINER_AGGRESSIVENESS>` — Setting to decide on an inlining strategy for Brillig functions. A more aggressive inliner should generate larger programs but more optimized A less aggressive inliner should generate smaller programs

  Default value: `9223372036854775807`
* `--pedantic-solving` — Use pedantic ACVM solving, i.e. double-check some black-box function assumptions when solving. This is disabled by default

  Default value: `false`

  Possible values: `true`, `false`
* `-Z`, `--unstable-features <UNSTABLE_FEATURES>` — Unstable features to enable for this current build.

If non-empty, it disables unstable features required in crate manifests.

* `--no-unstable-features` — Disable any unstable features required in crate manifests

  Possible values: `true`, `false`
* `--oracle-resolver <ORACLE_RESOLVER>` — JSON RPC url to solve oracle calls
* `--test-threads <TEST_THREADS>` — Number of threads used for running tests in parallel

  Default value: `4`
* `--format <FORMAT>` — Configure formatting of output

  Possible values:

  + `pretty`:
    Print verbose output
  + `terse`:
    Display one character per test
  + `json`:
    Output a JSON Lines document
* `-q`, `--quiet` — Display one character per test instead of one line

  Possible values: `true`, `false`
* `--no-fuzz` — Do not run fuzz tests (tests that have arguments)

  Possible values: `true`, `false`
* `--only-fuzz` — Only run fuzz tests (tests that have arguments)

  Possible values: `true`, `false`
* `--corpus-dir <CORPUS_DIR>` — If given, load/store fuzzer corpus from this folder
* `--minimized-corpus-dir <MINIMIZED_CORPUS_DIR>` — If given, perform corpus minimization instead of fuzzing and store results in the given folder
* `--fuzzing-failure-dir <FUZZING_FAILURE_DIR>` — If given, store the failing input in the given folder
* `--fuzz-timeout <FUZZ_TIMEOUT>` — Maximum time in seconds to spend fuzzing (default: 1 seconds)

  Default value: `1`
* `--fuzz-max-executions <FUZZ_MAX_EXECUTIONS>` — Maximum number of executions to run for each fuzz test (default: 100000)

  Default value: `100000`
* `--fuzz-show-progress` — Show progress of fuzzing (default: false)

  Possible values: `true`, `false`

## `nargo fuzz`Run the fuzzing harnesses for this program

**Usage:** `nargo fuzz [OPTIONS] [FUZZING_HARNESS_NAME]`

## **Arguments:*** `<FUZZING_HARNESS_NAME>` — If given, only the fuzzing harnesses with names containing this string will be run

## **Options:*** `--corpus-dir <CORPUS_DIR>` — If given, load/store fuzzer corpus from this folder
* `--minimized-corpus-dir <MINIMIZED_CORPUS_DIR>` — If given, perform corpus minimization instead of fuzzing and store results in the given folder
* `--fuzzing-failure-dir <FUZZING_FAILURE_DIR>` — If given, store the failing input in the given folder
* `--list-all` — List all available harnesses that match the name

  Possible values: `true`, `false`
* `--show-output` — Display output of `println` statements

  Possible values: `true`, `false`
* `--num-threads <NUM_THREADS>` — The number of threads to use for fuzzing

  Default value: `1`
* `--exact` — Only run harnesses that match exactly

  Possible values: `true`, `false`
* `--package <PACKAGE>` — The name of the package to run the command on. By default run on the first one found moving up along the ancestors of the current directory
* `--workspace` — Run on all packages in the workspace

  Possible values: `true`, `false`
* `--force` — Force a full recompilation

  Possible values: `true`, `false`
* `--print-acir` — Display the ACIR for compiled circuit, including the Brillig bytecode

  Possible values: `true`, `false`
* `--deny-warnings` — Treat all warnings as errors

  Possible values: `true`, `false`
* `--silence-warnings` — Suppress warnings

  Possible values: `true`, `false`
* `--debug-comptime-in-file <DEBUG_COMPTIME_IN_FILE>` — Enable printing results of comptime evaluation: provide a path suffix for the module to debug, e.g. "package\_name/src/main.nr"
* `--skip-underconstrained-check` — Flag to turn off the compiler check for under constrained values. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--skip-brillig-constraints-check` — Flag to turn off the compiler check for missing Brillig call constraints. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--count-array-copies` — Count the number of arrays that are copied in an unconstrained context for performance debugging

  Possible values: `true`, `false`
* `--enable-brillig-constraints-check-lookback` — Flag to turn on the lookback feature of the Brillig call constraints check, allowing tracking argument values before the call happens preventing certain rare false positives (leads to a slowdown on large rollout functions)

  Possible values: `true`, `false`
* `--inliner-aggressiveness <INLINER_AGGRESSIVENESS>` — Setting to decide on an inlining strategy for Brillig functions. A more aggressive inliner should generate larger programs but more optimized A less aggressive inliner should generate smaller programs

  Default value: `9223372036854775807`
* `--pedantic-solving` — Use pedantic ACVM solving, i.e. double-check some black-box function assumptions when solving. This is disabled by default

  Default value: `false`

  Possible values: `true`, `false`
* `-Z`, `--unstable-features <UNSTABLE_FEATURES>` — Unstable features to enable for this current build.

If non-empty, it disables unstable features required in crate manifests.

* `--no-unstable-features` — Disable any unstable features required in crate manifests

  Possible values: `true`, `false`
* `--oracle-resolver <ORACLE_RESOLVER>` — JSON RPC url to solve oracle calls
* `--timeout <TIMEOUT>` — Maximum time in seconds to spend fuzzing (default: no timeout)

  Default value: `0`
* `--max-executions <MAX_EXECUTIONS>` — Maximum number of executions of ACIR and Brillig per harness (default: no limit)

  Default value: `0`

## `nargo info`Provides detailed information on each of a program's function (represented by a single circuit)

Current information provided per circuit: 1. The number of ACIR opcodes 2. Counts the final number gates in the circuit used by a backend

**Usage:** `nargo info [OPTIONS]`

## **Options:*** `--package <PACKAGE>` — The name of the package to run the command on. By default run on the first one found moving up along the ancestors of the current directory
* `--workspace` — Run on all packages in the workspace

  Possible values: `true`, `false`
* `--profile-execution`

  Possible values: `true`, `false`
* `-p`, `--prover-name <PROVER_NAME>` — The name of the toml file which contains the inputs for the prover

  Default value: `Prover`
* `--force` — Force a full recompilation

  Possible values: `true`, `false`
* `--print-acir` — Display the ACIR for compiled circuit, including the Brillig bytecode

  Possible values: `true`, `false`
* `--deny-warnings` — Treat all warnings as errors

  Possible values: `true`, `false`
* `--silence-warnings` — Suppress warnings

  Possible values: `true`, `false`
* `--debug-comptime-in-file <DEBUG_COMPTIME_IN_FILE>` — Enable printing results of comptime evaluation: provide a path suffix for the module to debug, e.g. "package\_name/src/main.nr"
* `--skip-underconstrained-check` — Flag to turn off the compiler check for under constrained values. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--skip-brillig-constraints-check` — Flag to turn off the compiler check for missing Brillig call constraints. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--count-array-copies` — Count the number of arrays that are copied in an unconstrained context for performance debugging

  Possible values: `true`, `false`
* `--enable-brillig-constraints-check-lookback` — Flag to turn on the lookback feature of the Brillig call constraints check, allowing tracking argument values before the call happens preventing certain rare false positives (leads to a slowdown on large rollout functions)

  Possible values: `true`, `false`
* `--inliner-aggressiveness <INLINER_AGGRESSIVENESS>` — Setting to decide on an inlining strategy for Brillig functions. A more aggressive inliner should generate larger programs but more optimized A less aggressive inliner should generate smaller programs

  Default value: `9223372036854775807`
* `--pedantic-solving` — Use pedantic ACVM solving, i.e. double-check some black-box function assumptions when solving. This is disabled by default

  Default value: `false`

  Possible values: `true`, `false`
* `-Z`, `--unstable-features <UNSTABLE_FEATURES>` — Unstable features to enable for this current build.

If non-empty, it disables unstable features required in crate manifests.

* `--no-unstable-features` — Disable any unstable features required in crate manifests

  Possible values: `true`, `false`

## `nargo lsp`Starts the Noir LSP server

Starts an LSP server which allows IDEs such as VS Code to display diagnostics in Noir source.

VS Code Noir Language Support: <https://marketplace.visualstudio.com/items?itemName=noir-lang.vscode-noir>

**Usage:** `nargo lsp`

## `nargo expand`Show the result of macro expansion

**Usage:** `nargo expand [OPTIONS]`

## **Options:*** `--package <PACKAGE>` — The name of the package to run the command on. By default run on the first one found moving up along the ancestors of the current directory
* `--workspace` — Run on all packages in the workspace

  Possible values: `true`, `false`
* `--force` — Force a full recompilation

  Possible values: `true`, `false`
* `--print-acir` — Display the ACIR for compiled circuit, including the Brillig bytecode

  Possible values: `true`, `false`
* `--deny-warnings` — Treat all warnings as errors

  Possible values: `true`, `false`
* `--silence-warnings` — Suppress warnings

  Possible values: `true`, `false`
* `--debug-comptime-in-file <DEBUG_COMPTIME_IN_FILE>` — Enable printing results of comptime evaluation: provide a path suffix for the module to debug, e.g. "package\_name/src/main.nr"
* `--skip-underconstrained-check` — Flag to turn off the compiler check for under constrained values. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--skip-brillig-constraints-check` — Flag to turn off the compiler check for missing Brillig call constraints. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--count-array-copies` — Count the number of arrays that are copied in an unconstrained context for performance debugging

  Possible values: `true`, `false`
* `--enable-brillig-constraints-check-lookback` — Flag to turn on the lookback feature of the Brillig call constraints check, allowing tracking argument values before the call happens preventing certain rare false positives (leads to a slowdown on large rollout functions)

  Possible values: `true`, `false`
* `--inliner-aggressiveness <INLINER_AGGRESSIVENESS>` — Setting to decide on an inlining strategy for Brillig functions. A more aggressive inliner should generate larger programs but more optimized A less aggressive inliner should generate smaller programs

  Default value: `9223372036854775807`
* `--pedantic-solving` — Use pedantic ACVM solving, i.e. double-check some black-box function assumptions when solving. This is disabled by default

  Default value: `false`

  Possible values: `true`, `false`
* `-Z`, `--unstable-features <UNSTABLE_FEATURES>` — Unstable features to enable for this current build.

If non-empty, it disables unstable features required in crate manifests.

* `--no-unstable-features` — Disable any unstable features required in crate manifests

  Possible values: `true`, `false`

## `nargo doc`Builds documentation for the specified package or workspace.

Note: this command is in development and functionality may change greatly with no warning.

**Usage:** `nargo doc [OPTIONS]`

## **Options:*** `--package <PACKAGE>` — The name of the package to run the command on. By default run on the first one found moving up along the ancestors of the current directory
* `--workspace` — Run on all packages in the workspace

  Possible values: `true`, `false`
* `--force` — Force a full recompilation

  Possible values: `true`, `false`
* `--print-acir` — Display the ACIR for compiled circuit, including the Brillig bytecode

  Possible values: `true`, `false`
* `--deny-warnings` — Treat all warnings as errors

  Possible values: `true`, `false`
* `--silence-warnings` — Suppress warnings

  Possible values: `true`, `false`
* `--debug-comptime-in-file <DEBUG_COMPTIME_IN_FILE>` — Enable printing results of comptime evaluation: provide a path suffix for the module to debug, e.g. "package\_name/src/main.nr"
* `--skip-underconstrained-check` — Flag to turn off the compiler check for under constrained values. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--skip-brillig-constraints-check` — Flag to turn off the compiler check for missing Brillig call constraints. Warning: This can improve compilation speed but can also lead to correctness errors. This check should always be run on production code

  Possible values: `true`, `false`
* `--count-array-copies` — Count the number of arrays that are copied in an unconstrained context for performance debugging

  Possible values: `true`, `false`
* `--enable-brillig-constraints-check-lookback` — Flag to turn on the lookback feature of the Brillig call constraints check, allowing tracking argument values before the call happens preventing certain rare false positives (leads to a slowdown on large rollout functions)

  Possible values: `true`, `false`
* `--inliner-aggressiveness <INLINER_AGGRESSIVENESS>` — Setting to decide on an inlining strategy for Brillig functions. A more aggressive inliner should generate larger programs but more optimized A less aggressive inliner should generate smaller programs

  Default value: `9223372036854775807`
* `--pedantic-solving` — Use pedantic ACVM solving, i.e. double-check some black-box function assumptions when solving. This is disabled by default

  Default value: `false`

  Possible values: `true`, `false`
* `-Z`, `--unstable-features <UNSTABLE_FEATURES>` — Unstable features to enable for this current build.

If non-empty, it disables unstable features required in crate manifests.

* `--no-unstable-features` — Disable any unstable features required in crate manifests

  Possible values: `true`, `false`

## `nargo generate-completion-script`Generates a shell completion script for your favorite shell

**Usage:** `nargo generate-completion-script <SHELL>`

## **Arguments:*** `<SHELL>` — The shell to generate completions for. One of: bash, elvish, fish, powershell, zsh

---

*This document was generated automatically by
[`clap-markdown`](https://crates.io/crates/clap-markdown).*

---


# Debugger

Source: https://noir-lang.org/docs/reference/debugger/debugger_vscode

Version: v1.0.0-beta.17

On this page

Experimental Feature

This feature is experimental. The documentation may be incomplete or out of date, which means it could change in future versions, potentially causing unexpected behavior or not working as expected.

**Contributions Welcome:** If you notice any inaccuracies or potential improvements, please consider contributing. Visit our GitHub repository to make your contributions: [Contribute Here](https://github.com/noir-lang/noir).

The Noir debugger enabled by the vscode-noir extension ships with default settings such that the most common scenario should run without any additional configuration steps.

These defaults can nevertheless be overridden by defining a launch configuration file. This page provides a reference for the properties you can override via a launch configuration file, as well as documenting the Nargo `dap` command, which is a dependency of the VS Code Noir debugger.

## Creating and editing launch configuration filesTo create a launch configuration file from VS Code, open the *debug pane*, and click on *create a launch.json file*.

![Creating a launch configuration file](/docs/assets/images/ref1-create-launch-c0d86e35c4eaaa744bdbf385aeddcecf.png)

A `launch.json` file will be created, populated with basic defaults.

## Noir Debugger launch.json properties## projectFolder*String, optional.*

Absolute path to the Nargo project to debug. By default, it is dynamically determined by looking for the nearest `Nargo.toml` file to the active file at the moment of launching the debugger.

## proverName*String, optional.*

Name of the prover input to use. Defaults to `Prover`, which looks for a file named `Prover.toml` at the `projectFolder`.

## generateAcir*Boolean, optional.*

If true, generate ACIR opcodes instead of unconstrained opcodes which will be closer to release binaries but less convenient for debugging. Defaults to `false`.

## skipInstrumentation*Boolean, optional.*

Skips variables debugging instrumentation of code, making debugging less convenient but the resulting binary smaller and closer to production. Defaults to `false`.

note

Skipping instrumentation causes the debugger to be unable to inspect local variables.

## testName*String, optional.*

Test name (or substring) of the test function to debug. The name is not required to match exactly, as long as it's non-ambiguous.
For the debugger to run, only one test function should match the name lookup.

ie: if there are two test functions `test_simple_assert` and `test_increment`, setting `--test-name test_` will fail with `'test_' matches with more than one test function`. Instead, setting `--test_name test_simple` is not ambiguous, so the debugger will start debugging the `test_simple_assert` test function.

note

When provided, the debugger will debug the matching function instead of the package `main` function.

## oracleResolver*String, optional.*

JSON RPC URL to solve oracle calls.

note

When the debugger is run using the `Debug test` codelens, this option is set from the `TXE_TARGET` environment variable value.

## `nargo dap [OPTIONS]`When run without any option flags, it starts the Nargo Debug Adapter Protocol server, which acts as the debugging backend for the VS Code Noir Debugger.

All option flags are related to preflight checks. The Debug Adapter Protocol specifies how errors are to be informed from a running DAP server, but it doesn't specify mechanisms to communicate server initialization errors between the DAP server and its client IDE.

Thus `nargo dap` ships with a *preflight check* mode. If flag `--preflight-check` and the rest of the `--preflight-*` flags are provided, Nargo will run the same initialization routine except it will not start the DAP server.

`vscode-noir` will then run `nargo dap` in preflight check mode first before a debugging session starts. If the preflight check ends in error, vscode-noir will present stderr and stdout output from this process through its own Output pane in VS Code. This makes it possible for users to diagnose what pieces of configuration might be wrong or missing in case of initialization errors.

If the preflight check succeeds, `vscode-noir` proceeds to start the DAP server normally but running `nargo dap` without any additional flags.

## Options| Option | Description |
| --- | --- |
| `--preflight-check` | If present, dap runs in preflight check mode. |
| `--preflight-project-folder <PREFLIGHT_PROJECT_FOLDER>` | Absolute path to the project to debug for preflight check. |
| `--preflight-prover-name <PREFLIGHT_PROVER_NAME>` | Name of prover file to use for preflight check |
| `--preflight-generate-acir` | Optional. If present, compile in ACIR mode while running preflight check. |
| `--preflight-skip-instrumentation` | Optional. If present, compile without introducing debug instrumentation while running preflight check. |
| `-h, --help` | Print help. |

---


# REPL Debugger

Source: https://noir-lang.org/docs/reference/debugger/debugger_repl

Version: v1.0.0-beta.17

On this page

Experimental Feature

This feature is experimental. The documentation may be incomplete or out of date, which means it could change in future versions, potentially causing unexpected behavior or not working as expected.

**Contributions Welcome:** If you notice any inaccuracies or potential improvements, please consider contributing. Visit our GitHub repository to make your contributions: [Contribute Here](https://github.com/noir-lang/noir).

## Running the REPL debugger`nargo debug [OPTIONS] [WITNESS_NAME]`

Runs the Noir REPL debugger. If a `WITNESS_NAME` is provided the debugger writes the resulting execution witness to a `WITNESS_NAME` file.

## Options| Option | Description |
| --- | --- |
| `-p, --prover-name <PROVER_NAME>` | The name of the toml file which contains the inputs for the prover [default: Prover] |
| `--package <PACKAGE>` | The name of the package to debug |
| `--print-acir` | Display the ACIR for compiled circuit |
| `--test-name <TEST_NAME>` | The name (or substring) of the test function to debug |
| `--oracle-resolver <RESOLVER_URL>` | JSON RPC url to solve oracle calls |
| `-h, --help` | Print help |

None of these options are required.

note

Since the debugger starts by compiling the target package, all Noir compiler options are also available.

note

If the `--test-name` option is provided the debugger will debug the matching function instead of the package `main` function.
This argument must only match one function. If the given name matches with more than one test function the debugger will not start.

note

For debugging aztec-contract tests that interact with the TXE ([see further details here](https://docs.aztec.network/developers/guides/smart_contracts/testing)), a JSON RPC server URL must be provided by setting the `--oracle-resolver` option

## REPL commandsOnce the debugger is running, it accepts the following commands.

## `help` (h)Displays the menu of available commands.

```
> help  
Available commands:  
  
  opcodes                          display ACIR opcodes  
  into                             step into to the next opcode  
  next                             step until a new source location is reached  
  out                              step until a new source location is reached  
                                   and the current stack frame is finished  
  break LOCATION:OpcodeLocation    add a breakpoint at an opcode location  
  break line:i64                   add a breakpoint at an opcode associated to the given source code line  
  over                             step until a new source location is reached  
                                   without diving into function calls  
  restart                          restart the debugging session  
  delete LOCATION:OpcodeLocation   delete breakpoint at an opcode location  
  witness                          show witness map  
  witness index:u32                display a single witness from the witness map  
  witness index:u32 value:String   update a witness with the given value  
  memset index:usize value:String  update a memory cell with the given  
                                   value  
  continue                         continue execution until the end of the  
                                   program  
  vars                             show variable values available at this point  
                                   in execution  
  stacktrace                       display the current stack trace  
  memory                           show memory (valid when executing unconstrained code)                                 value  
  step                             step to the next ACIR opcode  
  
Other commands:  
  
  help  Show this help message  
  quit  Quit repl
```

## Stepping through programs## `next` (n)Step until the next Noir source code location. While other commands, such as [`into`](#into-i) and [`step`](#step-s), allow for finer grained control of the program's execution at the opcode level, `next` is source code centric. For example:

```
3    ...  
4    fn main(x: u32) {  
5        assert(entry_point(x) == 2);  
6        swap_entry_point(x, x + 1);  
7 ->     assert(deep_entry_point(x) == 4);  
8        multiple_values_entry_point(x);  
9    }
```

Using `next` here would cause the debugger to jump to the definition of `deep_entry_point` (if available).

If you want to step over `deep_entry_point` and go straight to line 8, use [the `over` command](#over) instead.

## `over`Step until the next source code location, without diving into function calls. For example:

```
3    ...  
4    fn main(x: u32) {  
5        assert(entry_point(x) == 2);  
6        swap_entry_point(x, x + 1);  
7 ->     assert(deep_entry_point(x) == 4);  
8        multiple_values_entry_point(x);  
9    }
```

Using `over` here would cause the debugger to execute until line 8 (`multiple_values_entry_point(x);`).

If you want to step into `deep_entry_point` instead, use [the `next` command](#next-n).

## `out`Step until the end of the current function call. For example:

```
  3    ...  
  4    fn main(x: u32) {  
  5        assert(entry_point(x) == 2);  
  6        swap_entry_point(x, x + 1);  
  7 ->     assert(deep_entry_point(x) == 4);  
  8        multiple_values_entry_point(x);  
  9    }  
 10  
 11    unconstrained fn returns_multiple_values(x: u32) -> (u32, u32, u32, u32) {  
 12    ...  
 ...  
 55  
 56    unconstrained fn deep_entry_point(x: u32) -> u32 {  
 57 ->     level_1(x + 1)  
 58    }
```

Running `out` here will resume execution until line 8.

## `step` (s)Skips to the next ACIR code. A compiled Noir program is a sequence of ACIR opcodes. However, an unconstrained VM opcode denotes the start of an unconstrained code block, to be executed by the unconstrained VM. For example (redacted for brevity):

```
0  BLACKBOX::RANGE [(_0, num_bits: 32)] [ ]  
1 ->  BRILLIG inputs=[Single(Expression { mul_terms: [], linear_combinations: [(1, Witness(0))], q_c: 0 })] outputs=[Simple(Witness(1))]  
	1.0  |   Mov { destination: RegisterIndex(2), source: RegisterIndex(0) }  
	1.1  |   Const { destination: RegisterIndex(0), value: Value { inner: 0 } }  
	1.2  |   Const { destination: RegisterIndex(1), value: Value { inner: 0 } }  
	1.3  |   Mov { destination: RegisterIndex(2), source: RegisterIndex(2) }  
	1.4  |   Call { location: 7 }  
	...  
	1.43 |   Return  
2    EXPR [ (1, _1) -2 ]
```

The `->` here shows the debugger paused at an ACIR opcode: `BRILLIG`, at index 1, which denotes an unconstrained code block is about to start.

Using the `step` command at this point would result in the debugger stopping at ACIR opcode 2, `EXPR`, skipping unconstrained computation steps.

Use [the `into` command](#into-i) instead if you want to follow unconstrained computation step by step.

## `into` (i)Steps into the next opcode. A compiled Noir program is a sequence of ACIR opcodes. However, a BRILLIG opcode denotes the start of an unconstrained code block, to be executed by the unconstrained VM. For example (redacted for brevity):

```
0  BLACKBOX::RANGE [(_0, num_bits: 32)] [ ]  
1 ->  BRILLIG inputs=[Single(Expression { mul_terms: [], linear_combinations: [(1, Witness(0))], q_c: 0 })] outputs=[Simple(Witness(1))]  
	1.0  |   Mov { destination: RegisterIndex(2), source: RegisterIndex(0) }  
	1.1  |   Const { destination: RegisterIndex(0), value: Value { inner: 0 } }  
	1.2  |   Const { destination: RegisterIndex(1), value: Value { inner: 0 } }  
	1.3  |   Mov { destination: RegisterIndex(2), source: RegisterIndex(2) }  
	1.4  |   Call { location: 7 }  
	...  
	1.43 |   Return  
2    EXPR [ (1, _1) -2 ]
```

The `->` here shows the debugger paused at an ACIR opcode: `BRILLIG`, at index 1, which denotes an unconstrained code block is about to start.

Using the `into` command at this point would result in the debugger stopping at opcode 1.0, `Mov ...`, allowing the debugger user to follow unconstrained computation step by step.

Use [the `step` command](#step-s) instead if you want to skip to the next ACIR code directly.

## `continue` (c)Continues execution until the next breakpoint, or the end of the program.

## `restart` (res)Interrupts execution, and restarts a new debugging session from scratch.

## `opcodes` (o)Display the program's ACIR opcode sequence. For example:

```
0  BLACKBOX::RANGE [(_0, num_bits: 32)] [ ]  
1 ->  BRILLIG inputs=[Single(Expression { mul_terms: [], linear_combinations: [(1, Witness(0))], q_c: 0 })] outputs=[Simple(Witness(1))]  
	1.0  |   Mov { destination: RegisterIndex(2), source: RegisterIndex(0) }  
	1.1  |   Const { destination: RegisterIndex(0), value: Value { inner: 0 } }  
	1.2  |   Const { destination: RegisterIndex(1), value: Value { inner: 0 } }  
	1.3  |   Mov { destination: RegisterIndex(2), source: RegisterIndex(2) }  
	1.4  |   Call { location: 7 }  
	...  
	1.43 |   Return  
2     EXPR [ (1, _1) -2 ]
```

## Breakpoints## `break [Opcode]` (or shorthand `b [Opcode]`)Sets a breakpoint on the specified opcode index. To get a list of the program opcode numbers, see [the `opcode` command](#opcodes-o). For example:

```
0  BLACKBOX::RANGE [(_0, num_bits: 32)] [ ]  
1 ->  BRILLIG inputs=[Single(Expression { mul_terms: [], linear_combinations: [(1, Witness(0))], q_c: 0 })] outputs=[Simple(Witness(1))]  
	1.0  |   Mov { destination: RegisterIndex(2), source: RegisterIndex(0) }  
	1.1  |   Const { destination: RegisterIndex(0), value: Value { inner: 0 } }  
	1.2  |   Const { destination: RegisterIndex(1), value: Value { inner: 0 } }  
	1.3  |   Mov { destination: RegisterIndex(2), source: RegisterIndex(2) }  
	1.4  |   Call { location: 7 }  
	...  
	1.43 |   Return  
2    EXPR [ (1, _1) -2 ]
```

In this example, issuing a `break 1.2` command adds break on opcode 1.2, as denoted by the `*` character:

```
0  BLACKBOX::RANGE [(_0, num_bits: 32)] [ ]  
1 ->  BRILLIG inputs=[Single(Expression { mul_terms: [], linear_combinations: [(1, Witness(0))], q_c: 0 })] outputs=[Simple(Witness(1))]  
	1.0  |   Mov { destination: RegisterIndex(2), source: RegisterIndex(0) }  
	1.1  |   Const { destination: RegisterIndex(0), value: Value { inner: 0 } }  
	1.2  | * Const { destination: RegisterIndex(1), value: Value { inner: 0 } }  
	1.3  |   Mov { destination: RegisterIndex(2), source: RegisterIndex(2) }  
	1.4  |   Call { location: 7 }  
	...  
	1.43 |   Return  
2    EXPR [ (1, _1) -2 ]
```

Running [the `continue` command](#continue-c) at this point would cause the debugger to execute the program until opcode 1.2.

## `break [line]` (or shorthand `b [line]`)Similar to `break [opcode]`, but instead of selecting the opcode by index selects the opcode location by matching the source code location

## `delete [Opcode]` (or shorthand `d [Opcode]`)Deletes a breakpoint at an opcode location. Usage is analogous to [the `break` command](#).

## Variable inspection## varsShow variable values available at this point in execution.

note

The ability to inspect variable values from the debugger depends on compilation to be run in a special debug instrumentation mode. This instrumentation weaves variable tracing code with the original source code.

So variable value inspection comes at the expense of making the resulting ACIR bytecode bigger and harder to understand and optimize.

If you find this compromise unacceptable, you can run the debugger with the flag `--skip-debug-instrumentation`. This will compile your circuit without any additional debug information, so the resulting ACIR bytecode will be identical to the one produced by standard Noir compilation. However, if you opt for this, the `vars` command will not be available while debugging.

## Stacktrace## `stacktrace`Displays the current stack trace.

## Witness map## `witness` (w)Show witness map. For example:

```
_0 = 0  
_1 = 2  
_2 = 1
```

## `witness [Witness Index]`Display a single witness from the witness map. For example:

```
> witness 1  
_1 = 2
```

## `witness [Witness Index] [New value]`Overwrite the given index with a new value. For example:

```
> witness 1 3  
_1 = 3
```

## Unconstrained VM memory## `memory`Show unconstrained VM memory state. For example:

```
> memory  
At opcode 1.13: Store { destination_pointer: RegisterIndex(0), source: RegisterIndex(3) }  
...  
> registers  
0 = 0  
1 = 10  
2 = 0  
3 = 1  
4 = 1  
5 = 2³²  
6 = 1  
> into  
At opcode 1.14: Const { destination: RegisterIndex(5), value: Value { inner: 1 } }  
...  
> memory  
0 = 1  
>
```

In the example above: we start with clean memory, then step through a `Store` opcode which stores the value of register 3 (1) into the memory address stored in register 0 (0). Thus now `memory` shows memory address 0 contains value 1.

note

This command is only functional while the debugger is executing unconstrained code.

## `memset [Memory address] [New value]`Update a memory cell with the given value. For example:

```
> memory  
0 = 1  
> memset 0 2  
> memory  
0 = 2  
> memset 1 4  
> memory  
0 = 2  
1 = 4  
>
```

note

This command is only functional while the debugger is executing unconstrained code.

---


# Known limitations

Source: https://noir-lang.org/docs/reference/debugger/debugger_known_limitations

Version: v1.0.0-beta.17

On this page

Experimental Feature

This feature is experimental. The documentation may be incomplete or out of date, which means it could change in future versions, potentially causing unexpected behavior or not working as expected.

**Contributions Welcome:** If you notice any inaccuracies or potential improvements, please consider contributing. Visit our GitHub repository to make your contributions: [Contribute Here](https://github.com/noir-lang/noir).

There are currently some limits to what the debugger can observe.

## Mutable referencesThe debugger is currently blind to any state mutated via a mutable reference. For example, in:

```
let mut x = 1;  
let y = &mut x;  
*y = 2;
```

The update on `x` will not be observed by the debugger. That means, when running `vars` from the debugger REPL, or inspecting the *local variables* pane in the VS Code debugger, `x` will appear with value 1 despite having executed `*y = 2;`.

## Variables of type function or mutable references are opaqueWhen inspecting variables, any variable of type `Function` or `MutableReference` will render its value as `<<function>>` or `<<mutable ref>>`.

## Debugger instrumentation affects resulting ACIRIn order to make the state of local variables observable, the debugger compiles Noir circuits interleaving foreign calls that track any mutations to them. While this works (except in the cases described above) and doesn't introduce any behavior changes, it does as a side effect produce bigger bytecode. In particular, when running the command `opcodes` on the REPL debugger, you will notice Unconstrained VM blocks that look like this:

```
...  
5    BRILLIG inputs=[Single(Expression { mul_terms: [], linear_combinations: [], q_c: 2 }), Single(Expression { mul_terms: [], linear_combinations: [(1, Witness(2))], q_c: 0 })]  
       |       outputs=[]  
  5.0  |   Mov { destination: RegisterIndex(2), source: RegisterIndex(0) }  
  5.1  |   Mov { destination: RegisterIndex(3), source: RegisterIndex(1) }  
  5.2  |   Const { destination: RegisterIndex(0), value: Value { inner: 0 } }  
  5.3  |   Const { destination: RegisterIndex(1), value: Value { inner: 0 } }  
  5.4  |   Mov { destination: RegisterIndex(2), source: RegisterIndex(2) }  
  5.5  |   Mov { destination: RegisterIndex(3), source: RegisterIndex(3) }  
  5.6  |   Call { location: 8 }  
  5.7  |   Stop  
  5.8  |   ForeignCall { function: "__debug_var_assign", destinations: [], inputs: [RegisterIndex(RegisterIndex(2)), RegisterIndex(RegisterIndex(3))] }  
...
```

If you are interested in debugging/inspecting compiled ACIR without these synthetic changes, you can invoke the REPL debugger with the `--skip-instrumentation` flag or launch the VS Code debugger with the `skipConfiguration` property set to true in its launch configuration. You can find more details about those in the [Debugger REPL reference](/docs/reference/debugger/debugger_repl) and the [VS Code Debugger reference](/docs/reference/debugger/debugger_vscode).

note

Skipping debugger instrumentation means you won't be able to inspect values of local variables.

---


# Noir Codegen for TypeScript

Source: https://noir-lang.org/docs/reference/noir_codegen

Version: v1.0.0-beta.17

On this page

When using TypeScript, it is extra work to interpret Noir program outputs in a type-safe way. Third party libraries may exist for popular Noir programs, but they are either hard to find or unmaintained.

Now you can generate TypeScript bindings for your Noir programs in two steps:

1. Exporting Noir functions using `nargo export`
2. Using the TypeScript module `noir_codegen` to generate TypeScript binding

**Note:** you can only export functions from a Noir *library* (not binary or contract program types).

## Installation## Your TypeScript projectIf you don't already have a TypeScript project you can add the module with `yarn` (or `npm`), then initialize it:

```
yarn add typescript -D  
npx tsc --init
```

## Add TypeScript module - `noir_codegen`The following command will add the module to your project's devDependencies:

```
yarn add @noir-lang/noir_codegen -D
```

## Nargo libraryMake sure you have Nargo, v0.25.0 or greater, installed. If you don't, follow the [installation guide](/docs/getting_started/noir_installation).

If you're in a new project, make a `circuits` folder and create a new Noir library:

```
mkdir circuits && cd circuits  
nargo new --lib myNoirLib
```

## Usage## Export ABI of specified functionsFirst go to the `.nr` files in your Noir library, and add the `#[export]` macro to each function that you want to use in TypeScript.

```
#[export]  
fn your_function(...
```

From your Noir library (where `Nargo.toml` is), run the following command:

```
nargo export
```

You will now have an `export` directory with a .json file per exported function.

You can also specify the directory of Noir programs using `--program-dir`, for example:

```
nargo export --program-dir=./circuits/myNoirLib
```

## Generate TypeScript bindings from exported functionsTo use the `noir-codegen` package we added to the TypeScript project:

```
yarn noir-codegen ./export/your_function.json
```

This creates an `exports` directory with an `index.ts` file containing all exported functions.

**Note:** adding `--out-dir` allows you to specify an output dir for your TypeScript bindings to go. Eg:

```
yarn noir-codegen ./export/*.json --out-dir ./path/to/output/dir
```

## Example .nr function to .ts outputConsider a Noir library with this function:

```
#[export]  
fn not_equal(x: Field, y: Field) -> bool {  
    x != y  
}
```

After the export and codegen steps, you should have an `index.ts` like:

```
export type Field = string;  
  
  
export const is_equal_circuit: CompiledCircuit =   
{"abi":{"parameters":[{"name":"x","type":{"kind":"field"},"visibility":"private"},{"name":"y","type":{"kind":"field"},"visibility":"private"}],"return_type":{"abi_type":{"kind":"boolean"},"visibility":"private"}},"bytecode":"H4sIAAAAAAAA/7WUMQ7DIAxFQ0Krrr2JjSGYLVcpKrn/CaqqDQN12WK+hPBgmWd/wEyHbF1SS923uhOs3pfoChI+wKXMAXzIKyNj4PB0TFTYc0w5RUjoqeAeEu1wqK0F54RGkWvW44LPzExnlkbMEs4JNZmN8PxS42uHv82T8a3Jeyn2Ks+VLPcO558HmyLMCDOXAXXtpPt4R/Rt9T36ss6dS9HGPx/eG17nGegKBQAA"};  
  
export async function is_equal(x: Field, y: Field, foreignCallHandler?: ForeignCallHandler): Promise<boolean> {  
  const program = new Noir(is_equal_circuit);  
  const args: InputMap = { x, y };  
  const { returnValue } = await program.execute(args, foreignCallHandler);  
  return returnValue as boolean;  
}
```

Now the `is_equal()` function and relevant types are readily available for use in TypeScript.

---


# NoirJS

Source: https://noir-lang.org/docs/reference/NoirJS/noir_js

Version: v1.0.0-beta.17

On this page

## Classes| Class | Description |
| --- | --- |
| [Noir](/docs/reference/NoirJS/noir_js/classes/Noir) | - |

## Type Aliases| Type Alias | Description |
| --- | --- |
| [ErrorWithPayload](/docs/reference/NoirJS/noir_js/type-aliases/ErrorWithPayload) | - |
| [ForeignCallHandler](/docs/reference/NoirJS/noir_js/type-aliases/ForeignCallHandler) | A callback which performs an foreign call and returns the response. |
| [ForeignCallInput](/docs/reference/NoirJS/noir_js/type-aliases/ForeignCallInput) | - |
| [ForeignCallOutput](/docs/reference/NoirJS/noir_js/type-aliases/ForeignCallOutput) | - |
| [WitnessMap](/docs/reference/NoirJS/noir_js/type-aliases/WitnessMap) | - |

## Variables## InputMap```
InputMap: any;
```

## Functions| Function | Description |
| --- | --- |
| [and](/docs/reference/NoirJS/noir_js/functions/and) | Performs a bitwise AND operation between `lhs` and `rhs` |
| [blake2s256](/docs/reference/NoirJS/noir_js/functions/blake2s256) | Calculates the Blake2s256 hash of the input bytes |
| [ecdsa\_secp256k1\_verify](/docs/reference/NoirJS/noir_js/functions/ecdsa_secp256k1_verify) | Verifies a ECDSA signature over the secp256k1 curve. |
| [ecdsa\_secp256r1\_verify](/docs/reference/NoirJS/noir_js/functions/ecdsa_secp256r1_verify) | Verifies a ECDSA signature over the secp256r1 curve. |
| [xor](/docs/reference/NoirJS/noir_js/functions/xor) | Performs a bitwise XOR operation between `lhs` and `rhs` |

## References## CompiledCircuitRenames and re-exports [InputMap](#inputmap)

---


# classes

Source: https://noir-lang.org/docs/reference/NoirJS/noir_js/classes/Noir

Version: v1.0.0-beta.17

On this page

## Constructors## Constructor```
new Noir(circuit): Noir;
```

## Parameters| Parameter | Type |
| --- | --- |
| `circuit` | `CompiledCircuit` |

## Returns`Noir`

## Methods## execute()")

```
execute(inputs, foreignCallHandler?): Promise<{  
  returnValue: InputValue;  
  witness: Uint8Array;  
}>;
```

## Parameters| Parameter | Type |
| --- | --- |
| `inputs` | `InputMap` |
| `foreignCallHandler?` | [`ForeignCallHandler`](/docs/reference/NoirJS/noir_js/type-aliases/ForeignCallHandler) |

## Returns`Promise`<{
`returnValue`: `InputValue`;
`witness`: `Uint8Array`;
}>

## DescriptionAllows to execute a circuit to get its witness and return value.

## Example```
async execute(inputs)
```

---


# functions

Source: https://noir-lang.org/docs/reference/NoirJS/noir_js/functions/and

Version: v1.0.0-beta.17

On this page

```
function and(lhs, rhs): string;
```

Performs a bitwise AND operation between `lhs` and `rhs`

## Parameters| Parameter | Type |
| --- | --- |
| `lhs` | `string` |
| `rhs` | `string` |

## Returns`string`

---


# Function: blake2s256()

Source: https://noir-lang.org/docs/reference/NoirJS/noir_js/functions/blake2s256

Version: v1.0.0-beta.17

On this page

```
function blake2s256(inputs): Uint8Array;
```

Calculates the Blake2s256 hash of the input bytes

## Parameters| Parameter | Type |
| --- | --- |
| `inputs` | `Uint8Array` |

## Returns`Uint8Array`

---


# Function: ecdsa\_secp256k1\_verify()

Source: https://noir-lang.org/docs/reference/NoirJS/noir_js/functions/ecdsa_secp256k1_verify

Version: v1.0.0-beta.17

On this page

```
function ecdsa_secp256k1_verify(  
   hashed_msg,   
   public_key_x_bytes,   
   public_key_y_bytes,   
   signature): boolean;
```

Verifies a ECDSA signature over the secp256k1 curve.

## Parameters| Parameter | Type |
| --- | --- |
| `hashed_msg` | `Uint8Array` |
| `public_key_x_bytes` | `Uint8Array` |
| `public_key_y_bytes` | `Uint8Array` |
| `signature` | `Uint8Array` |

## Returns`boolean`

---


# Function: ecdsa\_secp256r1\_verify()

Source: https://noir-lang.org/docs/reference/NoirJS/noir_js/functions/ecdsa_secp256r1_verify

Version: v1.0.0-beta.17

On this page

```
function ecdsa_secp256r1_verify(  
   hashed_msg,   
   public_key_x_bytes,   
   public_key_y_bytes,   
   signature): boolean;
```

Verifies a ECDSA signature over the secp256r1 curve.

## Parameters| Parameter | Type |
| --- | --- |
| `hashed_msg` | `Uint8Array` |
| `public_key_x_bytes` | `Uint8Array` |
| `public_key_y_bytes` | `Uint8Array` |
| `signature` | `Uint8Array` |

## Returns`boolean`

---


# Function: xor()

Source: https://noir-lang.org/docs/reference/NoirJS/noir_js/functions/xor

Version: v1.0.0-beta.17

On this page

```
function xor(lhs, rhs): string;
```

Performs a bitwise XOR operation between `lhs` and `rhs`

## Parameters| Parameter | Type |
| --- | --- |
| `lhs` | `string` |
| `rhs` | `string` |

## Returns`string`

---


# type-aliases

Source: https://noir-lang.org/docs/reference/NoirJS/noir_js/type-aliases/ErrorWithPayload

Version: v1.0.0-beta.17

On this page

```
type ErrorWithPayload = ExecutionError & object;
```

## Type Declaration| Name | Type |
| --- | --- |
| `decodedAssertionPayload?` | `any` |
| `noirCallStack?` | `string`[] |

---


# Type Alias: ForeignCallHandler()

Source: https://noir-lang.org/docs/reference/NoirJS/noir_js/type-aliases/ForeignCallHandler

Version: v1.0.0-beta.17

On this page

```
type ForeignCallHandler = (name, inputs) => Promise<ForeignCallOutput[]>;
```

A callback which performs an foreign call and returns the response.

## Parameters| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The identifier for the type of foreign call being performed. |
| `inputs` | [`ForeignCallInput`](/docs/reference/NoirJS/noir_js/type-aliases/ForeignCallInput)[] | An array of hex encoded inputs to the foreign call. |

## Returns`Promise`<[`ForeignCallOutput`](/docs/reference/NoirJS/noir_js/type-aliases/ForeignCallOutput)[]>

outputs - An array of hex encoded outputs containing the results of the foreign call.

---


# Type Alias: ForeignCallInput

Source: https://noir-lang.org/docs/reference/NoirJS/noir_js/type-aliases/ForeignCallInput

Version: v1.0.0-beta.17

```
type ForeignCallInput = string[];
```

---


# Type Alias: ForeignCallOutput

Source: https://noir-lang.org/docs/reference/NoirJS/noir_js/type-aliases/ForeignCallOutput

Version: v1.0.0-beta.17

```
type ForeignCallOutput = string | string[];
```

---


# Type Alias: WitnessMap

Source: https://noir-lang.org/docs/reference/NoirJS/noir_js/type-aliases/WitnessMap

Version: v1.0.0-beta.17

```
type WitnessMap = Map<number, string>;
```

---


# noir_wasm

Source: https://noir-lang.org/docs/reference/NoirJS/noir_wasm

Version: v1.0.0-beta.17

On this page

## Interfaces## ContractCompilationArtifactsThe compilation artifacts of a given contract.

## Properties| Property | Type | Description |
| --- | --- | --- |
| `contract` | `ContractArtifact` | The compiled contract. |
| `warnings` | `unknown`[] | Compilation warnings. |

---

## ProgramCompilationArtifactsThe compilation artifacts of a given program.

## Properties| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | not part of the compilation output, injected later |
| `program` | `ProgramArtifact` | The compiled contract. |
| `warnings` | `unknown`[] | Compilation warnings. |

## Variables## createFileManager()")

```
const createFileManager: (dataDir) => FileManager = createNodejsFileManager;
```

Creates a new FileManager instance based on fs in node and memfs in the browser (via webpack alias)

## Parameters| Parameter | Type | Description |
| --- | --- | --- |
| `dataDir` | `string` | root of the file system |

## Returns`FileManager`

## Functions| Function | Description |
| --- | --- |
| [compile](/docs/reference/NoirJS/noir_wasm/functions/compile) | Compiles a Noir project |
| [compile\_contract](/docs/reference/NoirJS/noir_wasm/functions/compile_contract) | Compiles a Noir project |
| [inflateDebugSymbols](/docs/reference/NoirJS/noir_wasm/functions/inflateDebugSymbols) | Decompresses and decodes the debug symbols |

## References## compile\_programRenames and re-exports [compile](/docs/reference/NoirJS/noir_wasm/functions/compile)

---


# Function: compile\_contract()

Source: https://noir-lang.org/docs/reference/NoirJS/noir_wasm/functions/compile_contract

Version: v1.0.0-beta.17

On this page

```
function compile_contract(  
   fileManager,   
   projectPath?,   
   logFn?,   
debugLogFn?): Promise<ContractCompilationArtifacts>;
```

Compiles a Noir project

## Parameters| Parameter | Type | Description |
| --- | --- | --- |
| `fileManager` | `FileManager` | The file manager to use |
| `projectPath?` | `string` | The path to the project inside the file manager. Defaults to the root of the file manager |
| `logFn?` | `LogFn` | A logging function. If not provided, console.log will be used |
| `debugLogFn?` | `LogFn` | A debug logging function. If not provided, logFn will be used |

## Returns`Promise`<[`ContractCompilationArtifacts`](/docs/reference/NoirJS/noir_wasm#contractcompilationartifacts)>

## Example```
// Node.js  
  
import { compile_contract, createFileManager } from '@noir-lang/noir_wasm';  
  
const fm = createFileManager(myProjectPath);  
const myCompiledCode = await compile_contract(fm);
```

```
// Browser  
  
import { compile_contract, createFileManager } from '@noir-lang/noir_wasm';  
  
const fm = createFileManager('/');  
for (const path of files) {  
  await fm.writeFile(path, await getFileAsStream(path));  
}  
const myCompiledCode = await compile_contract(fm);
```

---


# Function: inflateDebugSymbols()

Source: https://noir-lang.org/docs/reference/NoirJS/noir_wasm/functions/inflateDebugSymbols

Version: v1.0.0-beta.17

On this page

```
function inflateDebugSymbols(debugSymbols): any;
```

Decompresses and decodes the debug symbols

## Parameters| Parameter | Type | Description |
| --- | --- | --- |
| `debugSymbols` | `string` | The base64 encoded debug symbols |

## Returns`any`

---


# Tooling

Source: https://noir-lang.org/docs/tooling/language_server

Version: v1.0.0-beta.17

On this page

This section helps you install and configure the Noir Language Server.

The Language Server Protocol (LSP) has two components, the [Server](#language-server) and the [Client](#language-client). Below we describe each in the context of Noir.

## Language ServerThe Server component is provided by the Nargo command line tool that you installed at the beginning of this guide.
As long as Nargo is installed and you've used it to run other commands in this guide, it should be good to go!

If you'd like to verify that the `nargo lsp` command is available, you can run `nargo --help` and look for `lsp` in the list of commands. If you see it, you're using a version of Noir with LSP support.

## Language ClientThe Client component is usually an editor plugin that launches the Server. It communicates LSP messages between the editor and the Server. For example, when you save a file, the Client will alert the Server, so it can try to compile the project and report any errors.

Currently, Noir provides a Language Client for Visual Studio Code via the [vscode-noir](https://github.com/noir-lang/vscode-noir) extension. You can install it via the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=noir-lang.vscode-noir).

> **Note:** Noir's Language Server Protocol support currently assumes users' VSCode workspace root to be the same as users' Noir project root (i.e. where Nargo.toml lies).
>
> If LSP features seem to be missing / malfunctioning, make sure you are opening your Noir project directly (instead of as a sub-folder) in your VSCode instance.

When your language server is running correctly and the VSCode plugin is installed, you should see handy codelens buttons for compilation, measuring circuit size, execution, and tests:

![Compile and Execute](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKQAAAAWCAIAAADB1aBoAAAAA3NCSVQICAjb4U/gAAAIC0lEQVRoge2Z/VNT6RXHT+CSXHKDcUkIJRqBNGZZwEUNJhgXLOHFl904G5SOWds61K52HLvO2h/27+hMu0ud2bG+raxSWaWCAqsFTFA0vJlEiNnwHkwIMcHc3Bt5DP2BLEWIGoTabcnnp3tzz3Oe85xvnvOcO5fxboYYoqwMYv7bAUR5e0TFXkFExV5BRMVeQUTFXkH85MUWFR78JF/AAMCke47+emNCZKNWK7X75Ow3m3FVZumvjn127LhWIYjAGpPsPFS67s1mettgSx2f/H7BB1ukKXw2hvzuoc7GmrtjaFkiC+E06dqC7ull8YVLig+UZvMxn91Qf1Y3Gt5oXW6+6HHtl+cGl5ib9NLjmiw8dDPtMXz71+axJTlcCDs9k+8wD/kjtQ+/oIxc6Xi3ZWLqdaN58vK98qmuhkv1Nu80JzElETzLqjQABJzW/uXyRVub/s7lH1zTceFlSgNg7ASO1+ZAALDUpTyfaD91Xu9EALA8f9Z5rN6gUGDfL1lsaZ5mt9xl7WrV3XuF5HiGcivb8t1p/SACAPA4bZ6Q0+TNpUXKtMRYIB29+ustfR4ExMa9+wWDFiJrsygBvLbWBiOeV7hZtCqWHL5Xd00/NgU8ZcUulsmetClDwIFJm/5GbZcDgajkUCFde6bVOTfopM2lJcq01bFBj+X29Uaj+41kEZUcktOGJ2kyqYAAz/D92tr7ZFph2S9EGHPN736f23fjb439eKqiuHiTaHXMc8+Y8dYNnS3ixIZAc2RmZ5X/Rua68s2tMQQCZUVZkuHMlR5/vFBRvGuTiBNDOUyt15utntkFSngsRDkNtWcNCerDuY7zVe1eAGCklh5SeS9fnMjdK/sZHys7tgH90HS63oqI9G3qgg3JxLRv7EFTvX6QXhDMy0sViy9RaCQbXVZDq64jnOQM4Trh8/66wfmZxlJVHymx9qqTD1yQJP+4TKNwn9KNAzD4GVLLpao/1cRKd2s15Ykd3138cw0Sbtdqt2V0VD+gAWIE74kffvv1lxMgUGj37dxqf1HjWf8FHymx++dOPvBxN+4r3ykf+0Y/EVnq5xEnykm3Vp2udEFK/n6NKttc1XXrAs49vv5RZY0JAeAZxeqMQMOZryx+PHW7Rr2bPFfd5XmjqQAA/Ka62+srimSmqkdpRZm+2xd7/IBLCsuyAw1nvrI8E+Tv/7gk237JOJWq2qNkdV482ekGLifGBxCmUyGtjU3rRKrA1VO6cQAAbo56R7qj7nTVEKSqfqlWPa6ss81X5nUNGosvUWoOflqxRyHlxb34KBYn4kiSXDBEmCkOmu4ZXQgAjXcY+glJxkyng8bNHWMBAL/N5kTuR51DFMCUvX/ERySsmhlKD/d0TyAA5OwwjBCS9HfChZQilULfPaMHAZow9TgSfy6KsGtbCPWDoceFANDjvmGS4M7zEyeWikhju8U/DUAN3u10CDKk3EV4j+XJK058/sWJz7848QeNBAMA0nhTT29Ql++WT91vNE4CxIkz00JTIEfHwydCsQiDlExx0HSn00lPI9rj8UdUtoj09Wtc3W1DFAA1aLRS68RrFhpF1oSwBBKlRiJz9hqade0270xpek4HEJMgANwveozHmdSEP1S+EElS8QQHgAQAkgqEfg0iOkDNXE9NAzBmLoNBikQ/jvMFmDgrTCwYm8PkijVHMn9cwKSdGdEiFjJF+ejZMrvwWMVxIsZH+kJ3NOkLsggWI/ID+PlE+6nTuhdr02SPYSRfk2a7avKEpmAKFPuPy2aeYjCGszDgzElghBAEgQm3Hzm6DQAAYjAYYGELuo7IO07kd47YRxzef2fHMfSYo5AIsWH7XKeIop/FE2wGeKcBACOIeGo2Ya8hhkkQoRAxgsN65giECRBR9DN3++WwFX55oWkyyOFyAGZ0SeDEUBO+pbVaWPLWbWsdvY+FeXLBgM6JaJp8Zn94/mzX0zlG6b45CQQAQME5T2NZOBO8oZvZwkySFD1w5y9X+15VByJ5z0b+4Y6bFysrqxu7RudWbbLX0IOy1OpcMS8ew+JwbrKAGwdg77YEs/Ky+RgAlrRZlk5aLZHqgolksiQMAE/ZIlvrs/Y/CWdkN1tiM/NyBDgAMHBeMh8PZ7UMTNnMA0S2XMrFAOJTFTlCp8Wy2AYNY8zWLQCGQFaUQ96trWtonXzvQ0USBlM28yA3Z2smNw4AMDZPwI0DGOmzxWblvc/HADA2nxsP8NRDctekxAMAcN/NWTtTyabJQIDDC62e7O9zCGX56QkYAGAJAkG4o+3VOxv5R8132lq6hheezAAAaLjx0rX84q27D3xAYID8bvM/q+u9fnvLP1pUJXsPb+cA5extqbk7HmFmgt7+EaLw0FEBByYt+vo2Z9hthAZbrrapijS/zedgwYDb1lJ73bWw8wwHLlFptiThzALtNvKs7vX2tPX7y9yiHdrDambQM2yqrVtcdxbLk1d8JgeA0Hu2UbRjU0B/4QEJYG6+m6UtkT+6oLc2XeYW7dB+uosZg0iXuflqo9dva7nWXlq0/2gBC6hR3ZUqw3hHS2+Z6sCRXL+fdA4MuCQAAOAyGmzqgiNHC4Zunqnp7a6tw0sLPzmuZgLyjXY3VTufzt/ljLDfs/cc+6PQab7T1mIcJpf7xfml8JQV5eyblU2Dy+BrtVJbjK5Uty92Iy4eTLLzoNj8dcPQf3ympRN+Z9+pqXSPvj2Zo7wdwovtHA1ft6P8TxO+jEf5v+Qn/9UryvIRFXsF8S9Y1Xd0ujyQIgAAAABJRU5ErkJggg==)
![Run test](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEEAAAAPCAIAAAA0xzUOAAAAA3NCSVQICAjb4U/gAAADeklEQVRIid1W/U9bVRh+7rjSjitrY5tOQFmKHWsmCKx8GBhUuqRGY9WyROc2ncsSSZYlS/QfcYkm6C8EP5LFoVtYLAntIANv+Uob2ErXkWvpWj7s7Ud6B/e2yAH8YTgY9AOJiZvPT+d+PO/7Puc857yHOqIvwzOOff91Af8C6H9K0JovW1+VA8CKGFuYGr014EvsKbOy8eynzRpq6yviu3nFxpGc1ALtUXXYG5Q2Hjc16GvLI5PTsZWcEVZjY51dLE/v1+iMVvMJIfizW8pJ2omE84cvnaCgqjv/oZr9tnearO+SqaxsaKBvpdNQ/rr17fooNzHEju9GCUiS93mDb5xQKCj8+Yrls9rwj1fHBADUIfMFk/BL52icqT55SjNzj6k4VnRAtha94/jVzi0+GWUd5O8BAIDRNllaKg8y60sLdx29zgcpyEvrLa01xUwe1paCv/X0pepPGl5U022XKsnvjq5ejmzzkkyta7DqqqOca4h151IiU1dUlGLBHskyf5Raf1R249pXwZRS/85ZY+0UNzCfJaSiyvKmNmzruhrEIdMHFtMfHbbIa001cH1/xSPRBSolBFGyO0pfNi33dLKRDVa6/SBT6xqtOgPPudh0SvJUdec/rwMoEpvqvTbgJ9l2FYl4x4JJAAnOHzbrlDTmM/ud0R4uiU7eCCYBPPBwybayEoSiwmrN4cqykNsvxKIAQG2nZc4u0zxS4nPdZsf8wuZkr8bGO7vYeJHx3HsMEXO5ThSXN0ZrAJX9CGEYhi42tl9sAgDsoxGQ0SvTfd12Q6Pxowut4bsD/U6/sIOWPSiR+Nn52bCQxi1kYXw4/HGz4eA0GwZZ2/IlTybPx85Mu4AoJlOBka977j+5VAn/qM3vOlDe8r7FFP/mug/bWkKm/kCkkLv/p46ObvvEnJj+F8nLelB1/FgBgMWEqCgp2g8AiiNVL+XvRQEgztwPFxuatYU0ALpQoykEnlNrVHIAZJGPi6uggXVxefl5lVr+mLZzHYg05x0ZHpwIZSh9C3j30Own5uPaO30z7kFfm+lMe60kiXwgENXtTYQwedMmN7eevmzJB1mam3R087EXqt86pVfmEZJ6GHD23UsBKY/Lb2lpv9gS7P/uui8J6vFd491LXxTz3pHhQU9IzN1mniZsatCUMPG5Z6z6R9j0Ep/J9089/g93vr8AzRSBA8PSv2UAAAAASUVORK5CYII=)

You should also see your tests in the `testing` panel:

![Testing panel](/docs/assets/images/codelens_testing_panel-67748b868389348391d10d5113fb186a.png)

## Configuration* **Noir: Enable LSP** - If checked, the extension will launch the Language Server via `nargo lsp` and communicate with it.
* **Noir: Nargo Flags** - Additional flags may be specified if you require them to be added when the extension calls `nargo lsp`.
* **Noir: Nargo Path** - An absolute path to a Nargo binary with the `lsp` command. This may be useful if Nargo is not within the `PATH` of your editor.
* **Noir > Trace: Server** - Setting this to `"messages"` or `"verbose"` will log LSP messages between the Client and Server. Useful for debugging.

---


# Tests

Source: https://noir-lang.org/docs/tooling/tests

Version: v1.0.0-beta.17

On this page

You can test your Noir programs using Noir circuits.

Nargo will automatically compile and run any functions which have the decorator `#[test]` on them if
you run `nargo test`.

For example if you have a program like:

```
fn add(x: u64, y: u64) -> u64 {  
    x + y  
}  
#[test]  
fn test_add() {  
    assert(add(2,2) == 4);  
    assert(add(0,1) == 1);  
    assert(add(1,0) == 1);  
}
```

Running `nargo test` will test that the `test_add` function can be executed while satisfying all
the constraints which allows you to test that add returns the expected values. Test functions can't
have any arguments currently.

## Test failYou can write tests that are expected to fail by using the decorator `#[test(should_fail)]`. For example:

```
fn add(x: u64, y: u64) -> u64 {  
    x + y  
}  
#[test(should_fail)]  
fn test_add() {  
    assert(add(2,2) == 5);  
}
```

You can be more specific and make it fail with a specific reason by using `should_fail_with = "<the reason for failure>"`:

```
fn main(african_swallow_avg_speed: u64) {  
    assert(african_swallow_avg_speed == 65, "What is the airspeed velocity of an unladen swallow");  
}  
  
#[test]  
fn test_king_arthur() {  
    main(65);  
}  
  
#[test(should_fail_with = "What is the airspeed velocity of an unladen swallow")]  
fn test_bridgekeeper() {  
    main(32);  
}
```

The string given to `should_fail_with` doesn't need to exactly match the failure reason, it just needs to be a substring of it:

```
fn main(african_swallow_avg_speed: u64) {  
    assert(african_swallow_avg_speed == 65, "What is the airspeed velocity of an unladen swallow");  
}  
  
#[test]  
fn test_king_arthur() {  
    main(65);  
}  
  
#[test(should_fail_with = "airspeed velocity")]  
fn test_bridgekeeper() {  
    main(32);  
}
```

## Fuzz testsYou can write fuzzing harnesses that will run on `nargo test` by using the decorator `#[test]` with a function that has arguments. For example:

```
#[test]  
fn test_basic(a: Field, b: Field) {  
    assert(a + b == b + a);  
}
```

The test above is not expected to fail. By default, the fuzzer will run for 1 second and use 100000 executions (whichever comes first). All available threads will be used for each fuzz test.
The fuzz tests also work with `#[test(should_fail)]`, `#[test(should_fail_with = "<the reason for failure>")]` and `#[test(only_fail_with = "<the reason for failure>")]`. For example:

```
#[test(should_fail)]  
fn test_should_fail(a: [bool; 32]) {  
    let mut or_sum= false;  
    for i in 0..32 {  
        or_sum=or_sum|(a[i]==((i&1)as bool));  
    }  
    assert(!or_sum);  
}
```

or

```
#[test(should_fail_with = "This is the message that will be checked for")]  
fn test_should_fail_with(a: [bool; 32]) {  
    let mut or_sum= false;  
    for i in 0..32 {  
        or_sum=or_sum|(a[i]==((i&1)as bool));  
    }  
    assert(or_sum);  
    assert(false, "This is the message that will be checked for");  
}
```

```
#[test(only_fail_with = "This is the message that will be checked for")]  
fn test_add(a: u64, b: u64) {  
    assert((a+b-15)!=(a-b+30), "This is the message that will be checked for");  
}
```

The underlying fuzzing mechanism is described in the [Fuzzer](/docs/tooling/fuzzer) documentation.

There are some fuzzing-specific options that can be used with `nargo test`:
--no-fuzz
Do not run fuzz tests (tests that have arguments)

```
  --only-fuzz  
      Only run fuzz tests (tests that have arguments)  
  
  --corpus-dir <CORPUS_DIR>  
      If given, load/store fuzzer corpus from this folder  
  
  --minimized-corpus-dir <MINIMIZED_CORPUS_DIR>  
      If given, perform corpus minimization instead of fuzzing and store results in the given folder  
  
  --fuzzing-failure-dir <FUZZING_FAILURE_DIR>  
      If given, store the failing input in the given folder  
  
  --fuzz-timeout <FUZZ_TIMEOUT>  
      Maximum time in seconds to spend fuzzing (default: 1 second)  
  
      [default: 1]  
  
  --fuzz-max-executions <FUZZ_MAX_EXECUTIONS>  
      Maximum number of executions to run for each fuzz test (default: 100000)  
  
      [default: 100000]  
  
  --fuzz-show-progress  
      Show progress of fuzzing (default: false)
```

By default, the fuzzing corpus is saved in a temporary directory, but this can be changed. This allows you to resume fuzzing from the same corpus if the process is interrupted, if you want to run continuous fuzzing on your corpus, or if you want to use previous failures for regression testing.

---


# Fuzzer

Source: https://noir-lang.org/docs/tooling/fuzzer

Version: v1.0.0-beta.17

On this page

The Noir Fuzzer is a tool that allows you to fuzz your Noir programs. It is a type of testing tool that automatically generates and mutates test inputs to find bugs in programs. This fuzzer in particular, can automatically generate test cases for Noir programs with very little effort from the program writer.

## Key Features* Uses coverage-guided fuzzing (tracks which parts of the program are executed)
* Maintains a corpus of test cases that provide good coverage
* Uses mutation-based fuzzing (modifies existing inputs to create new test cases and can use crossover)
* Can detect discrepancies between ACIR and Brillig execution modes
* Can explore failing programs and detect only specific failure conditions
* Includes performance metrics and pretty printing of progress
* Supports corpus minimization (finding a smaller set of inputs that maintain coverage), although for now only the lazy approach is implemented
* Can be used with an oracle to perform differential fuzzing against a known good implementation in another language

## UsageA simple example of a fuzzing harness is the following:

```
#[fuzz]  
fn fuzz_add(a: Field, b: Field) {  
    assert(a != (b+3));  
}
```

Given a noir program, with a fuzzing harness, the fuzzer can be run with the following command:

```
nargo fuzz [FUZZING_HARNESS_NAME]
```

If [FUZZING\_HARNESS\_NAME] is given, only the fuzzing harnesses with names containing this string will be run.

An example of the output of the fuzzer is shown below:

![Basic fuzzer example](/docs/assets/images/basic-fuzzer-example-6d074454a3d76de463c067fe59713890.png)

By default, the fuzzer will save the corpus for a particular harness in the `corpus/<package_name>/<harness_name>` directory, but this can be changed by specifying the `--corpus-dir <DIR>` option, which will save the corpus in `<DIR>/<package_name>/<harness_name>`.

The fuzzer will output metrics about the fuzzing process, when new coverage is discovered (starting with `NEW`) or if some time has passed since the last output (`LOOP`). The time since the last output is doubled every `LOOP`, unless new coverage is discovered. Then it is reset to the initial interval of 1 second.

The output is streamed to the console, and shows key metrics like:

* `CNT` - Number of test cases executed
* `CRPS` - Number of active test cases in the corpus
* `AB_NEW` - Number of test cases added to the corpus with ACIR/Brillig hybrid execution
* `B_NEW` - Number of test cases added to the corpus with Brillig
* `RMVD` - Number of test cases removed from the corpus, because other test cases have been found that have the same coverage
* `A_TIME` - Time spent fuzzing with ACIR (cumulative from all threads)
* `B_TIME` - Time spent fuzzing with Brillig (cumulative from all threads)
* `M_TIME` - Time spend mutating test cases (cumulative from all threads)
* `RND_SIZE` - Number of mutated test cases in the last round (round is until new coverage is discovered or 100ms has passed)
* `RND_EX_TIME` - How much time was spent executing the test cases in the last round (in a single thread)
* `UPD_TIME` - Time spent updating the corpus (in a single thread)

If the timeout is not specified, the fuzzer will run until it finds a failing test case. By default the failing test case is saved in the `Prover-failing-<package_name>-<harness_name>.toml` file. So that it can be easily used with nargo execute by renaming it to `Prover.toml` and renaming the harness to `main`.

Additional fuzzing-specific options include:

```
  --corpus-dir <CORPUS_DIR>  
      If given, load/store fuzzer corpus from this folder  
  --minimized-corpus-dir <MINIMIZED_CORPUS_DIR>  
      If given, perform corpus minimization instead of fuzzing and store results in the given folder  
  --fuzzing-failure-dir <FUZZING_FAILURE_DIR>  
      If given, store the failing input in the given folder  
  --list-all  
      List all available harnesses that match the name (doesn't perform any fuzzing)  
  --num-threads <NUM_THREADS>  
      The number of threads to use for fuzzing [default: 1]  
  --exact  
      Only run harnesses that match exactly  
  --timeout <TIMEOUT>  
      Maximum time in seconds to spend fuzzing per harness (default: no timeout)  
  --max-executions <MAX_EXECUTIONS>  
      Maximum number of executions of ACIR and Brillig per harness (default: no limit)
```

`--show-output` and `--oracle-resolver` can be used in the same way as with regular execution and testing.
It is recommended to use `--skip-underconstrained-check` to increase compilation speed.

## Fuzzing more complex programs## Using `should_fail` and `should_fail_with`The fuzzer can be used to fuzz programs that are expected to fail. To do this, you can use the `should_fail` and `should_fail_with` attributes.

The following example will fuzz the program with the `should_fail` attribute, and will only consider a test case as a failure if the program passes:

```
#[fuzz(should_fail)]  
fn fuzz_should_fail(a: [bool; 32]) {  
    let mut or_sum= false;  
    for i in 0..32 {  
        or_sum=or_sum|(a[i]==((i&1)as bool));  
    }  
    assert(!or_sum);  
}
```

The `should_fail_with` expects that the program will fail with a specific error message. The following example will fuzz the program with the `should_fail_with` attribute, and will only consider a test case as a failure if the program passes or fails with the message different from "This is the message that will be checked for":

```
#[fuzz(should_fail_with = "This is the message that will be checked for")]  
fn fuzz_should_fail_with(a: [bool; 32]) {  
    let mut or_sum= false;  
    for i in 0..32 {  
        or_sum=or_sum|(a[i]==((i&1)as bool));  
    }  
    assert(or_sum);  
    assert(false, "This is the message that will be checked for");  
}
```

## Using `only_fail_with`A lot of the time, the program will already have many expected assertions that would lead to a failing test case, for example:

```
#[fuzz]  
fn fuzz_add(a: u64, b: u64) {  
    assert((a+b-15)!=(a-b+30));  
}
```

Using integer arithmetic will often automatically lead to overflows and underflows, which will lead to a failing test case. If we want to check that a specific property is broken, rather than detect all failures, we can specify an "only\_fail\_with" attribute to the fuzzing harness, which will only mark a testcase as failing if the assertion contains a specific message:

```
#[fuzz(only_fail_with = "This is the message that will be checked for")]  
fn fuzz_add(a: u64, b: u64) {  
    assert((a+b-15)!=(a-b+30), "This is the message that will be checked for");  
}
```

N.B. You can't find a failing testcase for this specific example, as the assertion is always true.

Let's change the assertion in the example above to:

```
#[fuzz(only_fail_with = "This is the message that will be checked for")]  
fn fuzz_add(a: u64, b: u64) {  
    assert((a+b-16)!=(a-b+30), "This is the message that will be checked for");  
}
```

Now, when we run the fuzzer, we'll see the following output:

![Fuzzing failure output showing the failing test case and its inputs](/docs/assets/images/only-fail-with-example-0a9c4e2d143303d836bdf493d519238d.png)

## Using an oracleYou can use an oracle to perform differential fuzzing against a known good implementation in another language. To do this you need to specify an oracle in the code, and run the fuzzer with the `--oracle-resolver <ORACLE_RESOLVER_URL>` option.

For this example, we'll use the following noir program:

```
#[oracle(check_addition)]  
unconstrained fn check_addition(a: u32, b: u32, c: u32) -> bool {}  
unconstrained fn check_addition_wrapper(a: u32, b: u32, c: u32) -> bool {  
    check_addition(a, b, c)  
}  
  
#[fuzz(only_fail_with = "addition incorrect")]  
fn main(a: u32, b: u32) {  
    let c = a + b + ((b - a == 49)  as u32);  
    // Safety: this is for fuzzing purposes only  
    assert(unsafe { check_addition_wrapper(a, b, c) }, "addition incorrect");  
}
```

You can create a simple python server to resolve the oracle (you'll have to install `werkzeug` and `jsonrpc` through your chosen package manager):

```
from werkzeug.serving import run_simple  
from werkzeug.wrappers import Response, Request  
  
from jsonrpc import JSONRPCResponseManager, dispatcher  
  
@dispatcher.add_method  
def resolve_foreign_call(arg):  
    assert arg["function"]=="check_addition"  
    a=int(arg["inputs"][0],16)  
    b=int(arg["inputs"][1],16)  
    c=int(arg["inputs"][2],16)  
    success=(a+b==c)  
    result=dict()  
    result['values']=["1" if success else "0"]  
    return result  
  
  
@Request.application  
def application(request):  
    response = JSONRPCResponseManager.handle(  
        request.data, dispatcher)  
    return Response(response.json, mimetype='application/json')  
  
if __name__ == '__main__':  
    run_simple('localhost', 40000, application)
```

You need to run this server before running the fuzzer.

Now if you run the fuzzer, you can see the following output:

![Fuzzing failure output showing oracle-checked failure](/docs/assets/images/oracle-fuzzing-68876d95731ad48138f7ba9510838b48.png)

---


# Setting up shell completions

Source: https://noir-lang.org/docs/tooling/shell_completions

Version: v1.0.0-beta.17

On this page

The `nargo` binary provides a command to generate shell completions:

```
nargo generate-completion-script [shell]
```

where `shell` must be one of `bash`, `elvish`, `fish`, `powershell`, and `zsh`.

Below we explain how to install them in some popular shells.

## Installing Zsh CompletionsIf you have `oh-my-zsh` installed, you might already have a directory of automatically loading completion scripts — `.oh-my-zsh/completions`.
If not, first create it:

```
mkdir -p ~/.oh-my-zsh/completions
```

Then copy the completion script to that directory:

```
nargo generate-completion-script zsh > ~/.oh-my-zsh/completions/_nargo
```

Without `oh-my-zsh`, you’ll need to add a path for completion scripts to your function path, and turn on completion script auto-loading.
First, add these lines to `~/.zshrc`:

```
fpath=(~/.zsh/completions $fpath)  
autoload -U compinit  
compinit
```

Next, create a directory at `~/.zsh/completions`:

```
mkdir -p ~/.zsh/completions
```

Then copy the completion script to that directory:

```
nargo generate-completion-script zsh > ~/.zsh/completions/_nargo
```

## Installing Bash CompletionsIf you have [bash-completion](https://github.com/scop/bash-completion) installed, you can just copy the completion script to the `/usr/local/etc/bash_completion.d` directory:

```
nargo generate-completion-script bash > /usr/local/etc/bash_completion.d/nargo
```

Without `bash-completion`, you’ll need to source the completion script directly.
First create a directory such as `~/.bash_completions/`:

```
mkdir ~/.bash_completions/
```

Copy the completion script to that directory:

```
nargo generate-completion-script bash > ~/.bash_completions/nargo.bash
```

Then add the following line to `~/.bash_profile` or `~/.bashrc`:

```
source ~/.bash_completions/nargo.bash
```

## Installing Fish CompletionsCopy the completion script to any path listed in the environment variable `$fish_completion_path`. For example, a typical location is `~/.config/fish/completions/nargo.fish`:

```
nargo generate-completion-script fish > ~/.config/fish/completions/nargo.fish
```

---


# Profiler

Source: https://noir-lang.org/docs/tooling/profiler

Version: v1.0.0-beta.17

On this page

The profiler is a sampling profiler designed to analyze and visualize Noir programs. It assists developers to identify bottlenecks by mapping execution data back to the original source code.

## InstallationThe profiler is automatically installed with Nargo starting noirup v0.1.4.

Check if the profiler is already installed by running `noir-profiler --version`. If the profiler is not found, update noirup and install the profiler by [reinstalling both noirup and Nargo](/docs/getting_started/quick_start#noir).

## Usage## Profiling ACIR opcodesThe profiler provides the ability to flamegraph a Noir program's ACIR opcodes footprint. This is useful for *approximately* identifying bottlenecks in constrained execution and proving of Noir programs.

note

"*Approximately*" as:

* Execution speeds depend on the constrained execution trace compiled from ACIR opcodes
* Proving speeds depend on the how the proving backend of choice interprets the ACIR opcodes

## Create a demonstrative projectLet's start by creating a simple Noir program that aims to zero out an array past some dynamic index.

Run `nargo new program` to create a new project named *program*, then copy in the following as source code:

```
fn main(ptr: pub u32, mut array: [u32; 32]) -> pub [u32; 32] {  
    for i in 0..32 {  
        if i > ptr {  
            array[i] = 0;  
        }  
    }  
    array  
}
```

Change into the project directory and compile the program using `nargo compile`. We are now ready to try out the profiler.

## FlamegraphingLet's take a granular look at our program's ACIR opcode footprint using the profiler, running:

```
noir-profiler opcodes --artifact-path ./target/program.json --output ./target/
```

The command generates a flamegraph in your *target* folder that maps the number of ACIR opcodes to their corresponding locations in your program's source code.

Opening the flamegraph in a web browser will provide a more interactive experience, allowing you to click into different regions of the graph and examine them.

Flamegraph of the demonstrative project generated with Nargo v1.0.0-beta.2:

![ACIR Flamegraph Unoptimized](/docs/assets/images/acir-flamegraph-unoptimized-546afbec080a85b8a07de754c3e2e263.png)

The demonstrative project consists of 387 ACIR opcodes in total. From the flamegraph, we can see that the majority come from the write to `array[i]`.

With insight into our program's bottleneck, let's optimize it.

## Visualizing optimizationsWe can improve our program's performance using [unconstrained functions](/docs/noir/concepts/unconstrained).

Let's replace expensive array writes with array gets with the new code below:

```
fn main(ptr: pub u32, array: [u32; 32]) -> pub [u32; 32] {  
    // Safety: Sets all elements after `ptr` in `array` to zero.  
    let zeroed_array = unsafe { zero_out_array(ptr, array) };  
    for i in 0..32 {  
        if i > ptr {  
            assert_eq(zeroed_array[i], 0);  
        } else {  
            assert_eq(zeroed_array[i], array[i]);  
        }  
    }  
    zeroed_array  
}  
  
unconstrained fn zero_out_array(ptr: u32, mut array: [u32; 32]) -> [u32; 32] {  
    for i in 0..32 {  
        if i > ptr {  
            array[i] = 0;  
        }  
    }  
    array  
}
```

Instead of writing our array in a fully constrained context, we first write our array inside an unconstrained function. Then, we assert every value in the array returned from the unconstrained function in a constrained context.

This brings the ACIR opcodes count of our program down to a total of 284 opcodes:

![ACIR Flamegraph Optimized](/docs/assets/images/acir-flamegraph-optimized-ba11bb17cfc7666ada23ca2d4f3aee0b.png)

## SearchingThe `i > ptr` region in the above image is highlighted purple as we were searching for it.

Click "Search" in the top right corner of the flamegraph to start a search (e.g. i > ptr).

Check "Matched" in the bottom right corner to learn the percentage out of total opcodes associated with the search (e.g. 43.3%).

tip

If you try searching for `memory::op` before and after the optimization, you will find that the search will no longer have matches after the optimization.

This comes from the optimization removing the use of a dynamic array (i.e. an array with a dynamic index, that is its values rely on witness inputs). After the optimization, the program reads from two arrays with known constant indices, replacing the original memory operations with simple arithmetic operations.

## Profiling proving backend gatesThe profiler further provides the ability to flamegraph a Noir program's proving backend gates footprint. This is useful for fully identifying proving bottlenecks of Noir programs.

This feature depends on the proving backend you are using and whether it supports the profiler with a gate profiling API. We will use [Barretenberg](https://github.com/AztecProtocol/aztec-packages/tree/master/barretenberg) as an example here. Follow the [quick start guide](/docs/getting_started/quick_start#proving-backend) to install it if you have not already.

## FlamegraphingLet's take a granular look at our program's proving backend gates footprint using the profiler, running:

```
noir-profiler gates --artifact-path ./target/program.json --backend-path bb --output ./target -- --include_gates_per_opcode
```

The `--backend-path` flag takes in the path to your proving backend binary.

The above command assumes you have Barretenberg (bb) installed and that its path is saved in your PATH. If that is not the case, you can pass in the absolute path to your proving backend binary instead.

Flamegraph of the optimized demonstrative project generated with bb v0.76.4:

![Gates Flamegraph Optimized](/docs/assets/images/gates-flamegraph-optimized-17ab2888d7480ddf5e82b9944be2c829.png)

The demonstrative project consists of 3,062 proving backend gates in total.

note

If you try searching for `i > ptr` in the source code, you will notice that this call stack is only contributing 3.8% of the total proving backend gates, versus the 43.3% ACIR opcodes it contributes.

This illustrates that number of ACIR opcodes are at best approximations of proving performances, where actual proving performances depend on how the proving backend interprets and translates ACIR opcodes into proving gates.

## Understanding bottlenecksProfiling your program with different parameters is good way to understand your program's bottlenecks as it scales.

From the flamegraph above, you will notice that `blackbox::range` contributes the majority of the backend gates. This comes from how Barretenberg UltraHonk uses lookup tables for its range gates under the hood, which comes with a considerable but fixed setup cost in terms of proving gates.

If our array is larger, range gates would become a much smaller percentage of our total circuit. See this flamegraph for the same optimized program but with an array of size 2,048 (versus originally 32) in comparison:

![Gates Flamegraph Optimized 2048](/docs/assets/images/gates-flamegraph-optimized-2048-dd97d0996d6cd357e24fd386c2c47c6e.png)

Where `blackbox::range` contributes a considerably smaller portion of the total proving gates.

Every proving backend interprets ACIR opcodes differently, so it is important to profile proving backend gates to get the full picture of proving performance.

As additional reference, this is the flamegraph of the pre-optimization demonstrative project at array size 32:

![Gates Flamegraph Unoptimized](/docs/assets/images/gates-flamegraph-unoptimized-acf36aa9b749d4f0766d4e2a09689d60.png)

And at array size 2,048:

![Gates Flamegraph Unoptimized 2048](/docs/assets/images/gates-flamegraph-unoptimized-2048-ac68b8f6840d1fe864f4cdb6ee00bc18.png)

## Profiling execution traces (unconstrained)")

The profiler also provides the ability to flamegraph a Noir program's execution trace. This is useful for identifying execution bottlenecks of Noir programs.

The profiler supports profiling fully unconstrained Noir programs at this moment.

## Updating the demonstrative projectLet's turn our demonstrative program into an unconstrained program by adding an `unconstrained` modifier to the main function:

```
unconstrained fn main(...){...}
```

Since we are profiling the execution trace, we will also need to provide a set of inputs to execute the program with.

Run `nargo check` to generate a *Prover.toml* file, which you can fill it in with:

```
ptr = 1  
array = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

## FlamegraphingLet's take a granular look at our program's unconstrained execution trace footprint using the profiler, running:

```
noir-profiler execution-opcodes --artifact-path ./target/program.json --prover-toml-path Prover.toml --output ./target
```

This is similar to the `opcodes` command, except it additionally takes in the *Prover.toml* file to profile execution with a specific set of inputs.

Flamegraph of the demonstrative project generated with Nargo v1.0.0-beta.2:
![Brillig Trace &quot;Optimized&quot;](/docs/assets/images/brillig-trace-opt-32-089b0dbe8f328deac4f3bc71bc952d7d.png)

Note that unconstrained Noir functions compile down to Brillig opcodes, which is what the counts in this flamegraph stand for, rather than constrained ACIR opcodes like in the previous section.

## Balancing proving and execution optimizationsRewriting constrained operations with unconstrained operations like what we did in [the optimization section](#visualizing-optimizations) helps remove ACIR opcodes (hence shorter proving times), but would introduce more Brillig opcodes (hence longer execution times).

For example, we can find a 13.9% match `new_array` in the flamegraph above.

In contrast, if we profile the pre-optimization demonstrative project:
![Brillig Trace Initial Program](/docs/assets/images/brillig-trace-initial-32-8f9a440c570b9454b996d375a9385b63.png)

You will notice that it does not contain `new_array` and executes a smaller total of 1,582 Brillig opcodes (versus 2,125 Brillig opcodes post-optimization).

As new unconstrained functions were added, it is reasonable that the program would consist of more Brillig opcodes. That said, the tradeoff is often easily justifiable by the fact that proving speeds are more commonly the major bottleneck of Noir programs versus execution speeds.

This is however good to keep in mind in case you start noticing execution speeds being the bottleneck of your program, or if you are simply looking to optimize your program's execution speeds.

---


# Dev Containers

Source: https://noir-lang.org/docs/tooling/devcontainer

Version: v1.0.0-beta.17

On this page

This guide explains how to use Dev Containers for Noir development, enabling consistent development environments across different machines and cloud-based development through GitHub Codespaces.

## What are Dev Containers?Dev Containers provide a full-featured development environment inside a Docker container. They ensure all developers work with the same tools, dependencies, and configurations, eliminating "works on my machine" issues.

For Noir development, Dev Containers offer:

* Pre-installed Noir toolchain (nargo, noirup)
* Pre-installed Barretenberg backend (bb, bbup)
* Consistent development experience across platforms
* Quick onboarding for new contributors

## Using Dev Containers Locally## Prerequisites* [Docker](https://www.docker.com/products/docker-desktop/) installed and running
* [Visual Studio Code](https://code.visualstudio.com/) or similar (ex. Cursor, Roo, etc)
* [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) or similar

## Setting up a Noir Dev Container1. Create a `.devcontainer/devcontainer.json` file in your project root. This will add the [devcontainer feature](https://github.com/AztecProtocol/devcontainer-feature) built by Aztec Labs, and the Noir extension.

```
{  
  "name": "Noir Development",  
  "image": "mcr.microsoft.com/devcontainers/base:ubuntu",  
  "features": {  
    "ghcr.io/aztecprotocol/devcontainer-features/noir:1": {},  
    "ghcr.io/aztecprotocol/devcontainer-features/barretenberg:1": {}  
  },  
  "customizations": {  
    "vscode": {  
      "extensions": [  
        "noir-lang.vscode-noir"  
      ]  
    }  
  }  
}
```

2. Open your project in your IDE
3. When prompted, click "Reopen in Container" or use the Command Palette (`Ctrl/Cmd + Shift + P`) and select "Dev Containers: Reopen in Container"
4. The IDE will build the container and set up your development environment with Noir and Barretenberg pre-installed

## Using GitHub CodespacesGitHub Codespaces provides cloud-hosted Dev Container environments, allowing you to develop Noir projects directly in your browser or in VS Code.

## Quick Start with CodespacesThe easiest way to get started is using the [Tiny Noir Codespace](https://github.com/aztecprotocol/tiny-noir-codespace) template:

1. Visit the [repository](https://github.com/aztecprotocol/tiny-noir-codespace)
2. Click the "Code" button and select "Create codespace on main"
3. GitHub will create a cloud-based development environment with Noir pre-configured

## Adding Codespaces to Your ProjectTo enable Codespaces for your own Noir project, use the same `.devcontainer/devcontainer.json` configuration shown above. When contributors visit your repository, they can create a Codespace with all necessary tools pre-installed.

## Available Devcontainer FeaturesThe [AztecProtocol devcontainer features](https://github.com/AztecProtocol/devcontainer-feature) provide:

## Noir Feature* Installs `nargo` CLI for compiling and testing Noir programs
* Installs `noirup` for managing Noir versions
* Automatically configures the latest stable version

## Barretenberg Feature* Installs `bb` CLI for proving and verification
* Installs `bbup` for managing Barretenberg versions
* Provides backend support for Noir programs

## Configuration OptionsYou can customize the Dev Container setup by modifying the features in `devcontainer.json`:

```
{  
  "features": {  
    "ghcr.io/aztecprotocol/devcontainer-features/noir:1": {  
      // Feature-specific options (if available)  
    },  
    "ghcr.io/aztecprotocol/devcontainer-features/barretenberg:1": {  
      // Feature-specific options (if available)  
    }  
  }  
}
```

## Tips for Development1. **Free Tier**: GitHub Codespaces offers up to 60 hours free per month for personal accounts
2. **Performance**: For resource-intensive operations like proving, local Dev Containers may perform better than Codespaces
3. **Persistence**: Changes made in a Dev Container are preserved in the container. Use version control to save your work
4. **Extensions**: The Noir VS Code extension is automatically installed, providing syntax highlighting, LSP support, and debugging capabilities

## Next Steps* Set up a Dev Container for your Noir project
* Explore the [Noir VS Code extension](/docs/tooling/language_server) features
* Learn about [debugging Noir programs](/docs/tooling/debugger) in your containerized environment

---
