# C and C++ Playbook

Load for C, C++, native libraries, embedded code, CMake, Make, Meson, or header/source work.

## Detection

Relevant signals include `CMakeLists.txt`, `Makefile`, `configure.ac`, `meson.build`, `*.c`, `*.h`, `*.cpp`, `*.cc`, `*.cxx`, `*.hpp`, `*.hh`, compiler flags, native library bindings, or embedded build scripts.

## Commands

Prefer repo-defined build scripts first:

- CMake: `cmake --build <build-dir>` and the repo's configured test command.
- Make: `make` and `make test` when present.
- Meson: `meson test -C <build-dir>`.
- If no build is configured, compile only the touched translation unit when feasible.

## C Design Standards

- Treat each `.h` file as a public contract and each `.c` file as the private implementation owner.
- Preserve function signatures, struct layouts, exported symbols, and macro meanings unless the task explicitly changes the ABI/API.
- Use opaque structs for owned state when callers should not depend on internal fields.
- Make ownership and lifetime explicit in names, docs, or API shape.
- Return clear status/error values; do not hide failures in global state.
- Keep allocation, deallocation, file handles, sockets, and locks paired and testable.

## C++ Design Standards

- Prefer RAII for resources and avoid raw owning pointers when standard smart pointers or containers fit.
- Prefer value types and references over nullable ownership when possible.
- Keep templates and inheritance shallow unless they remove real duplication without hiding behavior.
- Use virtual interfaces only at real polymorphic boundaries.

## Pattern Guidance

- Use Adapter at C/native boundaries, OS APIs, vendor SDKs, and language bindings.
- Use Strategy with function pointers, callback tables, or small interface classes when runtime behavior varies.
- Use Factory only when construction policy is shared and non-trivial.
- Avoid global mutable state unless it is required by platform constraints and protected by a clear lifecycle.
