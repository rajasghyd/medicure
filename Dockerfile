FROM openjdk:11
EXPOSE 8082
ARG JAR_FILE=/target/*.jar
COPY ${JAR_FILE} app.jar
RUN echo "Creation of your docker image is in progress, please hold on for a moment"
ENTRYPOINT ["java", "-jar", "app.jar"]
MAINTAINER "rajasghyd@gmail.com"
