# ── Stage 1: Build ──────────────────────────────────────────
FROM maven:3.9-eclipse-temurin-21 AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -q
COPY src ./src
RUN mvn package -DskipTests -q

# ── Stage 2: Runtime ────────────────────────────────────────
FROM eclipse-temurin:21-jre-alpine
WORKDIR /app

RUN addgroup -S mardeprata && adduser -S mardeprata -G mardeprata
USER mardeprata

COPY --from=builder /app/target/mar-de-prata-app.jar app.jar

VOLUME /app/data

EXPOSE 8083
ENTRYPOINT ["java", "-jar", "app.jar", "--server.port=8083"]
