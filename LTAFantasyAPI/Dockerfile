# Usando a imagem oficial do OpenJDK como base
FROM eclipse-temurin:17-jdk-alpine

# Definindo o diretório de trabalho no container
WORKDIR /app

# Copiando o arquivo mvnw (Maven Wrapper)
COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .

# Garantindo que o mvnw tenha permissões de execução
RUN chmod +x mvnw

# Instalando as dependências usando o Maven
RUN ./mvnw dependency:go-offline

# Copiando o código fonte da aplicação para o container
COPY src ./src

# Empacotando a aplicação com o Maven (ignora testes)
RUN ./mvnw package -DskipTests

# Expondo a porta 8080, onde a API irá rodar
EXPOSE 8080

# Comando para rodar a aplicação no container
CMD ["java", "-jar", "target/LTAFantasyAPI-0.0.1-SNAPSHOT.jar"]
