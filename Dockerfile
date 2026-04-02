# ── Stage 1: Build ──────────────────────────────────────────
FROM maven:3.9-eclipse-temurin-17 AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -q
COPY src ./src
RUN mvn package -DskipTests -q

# ── Stage 2: Runtime ────────────────────────────────────────
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app

# Utilizador não-root
RUN addgroup -S fiosmj && adduser -S fiosmj -G fiosmj
USER fiosmj

COPY --from=builder /app/target/*.jar app.jar

# Volume para DB + uploads
VOLUME /app/data

EXPOSE 8081
ENTRYPOINT ["java", "-jar", "app.jar", \
  "--spring.datasource.url=jdbc:sqlite:/app/data/fiosmj.db", \
  "--spring.web.resources.static-locations=classpath:/static/,file:/app/data/uploads/"]
