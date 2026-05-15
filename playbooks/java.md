# Java Playbook

Load for Java, JVM, Spring, Maven, Gradle, or JUnit work.

## Detection

Relevant signals include `pom.xml`, `build.gradle`, `settings.gradle`, `gradlew`, `mvnw`, `src/main/java`, `src/test/java`, `*.java`, Spring annotations, JUnit, Mockito, or Testcontainers.

## Commands

Prefer wrapper scripts:

- Maven: `./mvnw test`, `./mvnw verify`, or `mvn test` if no wrapper exists.
- Gradle: `./gradlew test`, `./gradlew build`, or `gradle test` if no wrapper exists.

On Windows, use `mvnw.cmd` or `gradlew.bat` when needed.

## Java Standards

- Keep domain logic separate from framework annotations where practical.
- Prefer constructor injection over field injection.
- Use immutable value objects for stable domain data.
- Keep DTOs, entities, and domain models distinct when their responsibilities differ.
- Avoid leaking persistence concerns into controllers or UI/API layers.

## Java OOP and Design

- Keep classes small, cohesive, and named for their domain role.
- Depend on interfaces at external, persistence, provider, and integration boundaries.
- Prefer composition and constructor injection over inheritance and static global helpers.
- Use records for immutable data carriers when the supported Java version allows it.
- Use sealed types or enums for closed state sets when they make invalid states harder to represent.
- Use Strategy, Factory, Adapter, or Repository/Gateway patterns when they protect a real boundary or remove repeated branching.

## Spring / Service Architecture

- Controller: HTTP shape and validation.
- Service/application layer: use cases and transaction boundaries.
- Repository/gateway: persistence or external services.
- Domain: rules and invariants.

## Testing

- Unit tests: JUnit + Mockito/Fakes for service/domain logic.
- Integration tests: Spring test slices or Testcontainers for real boundaries.
- Avoid full application context tests unless the integration value is clear.
- Assert behavior and observable outputs, not implementation details.

