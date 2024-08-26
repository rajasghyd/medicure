## Certification Project – Medicure


### Project Overview

**Medicure** is a super specialty hospital based in New York, USA, providing world-class treatment and surgery, including Heart, Liver, Kidney transplants, and the first robotic surgery center. The chain is owned and managed by Global Health Limited.

Medicure aims to centrally manage all doctors' and patients' data across its hospitals in various cities. They have developed a microservice to offer these services. To reduce unnecessary maintenance costs and manual labor, they aim to automate their application build and deployment process using DevOps. They are open to using any one of the (AWS, Azure, GCP) cloud platforms as their primary cloud service provider.

### Goals

- Deliver product updates frequently to production with high quality and reliability.
- Accelerate software delivery speed and quality.
- Reduce feedback time between developers and testers.


### Current Challenges

- Building complex builds is difficult.
- Manual efforts to test various components/modules of the project.
- Incremental builds are difficult to manage, test, and deploy.
- Creation of infrastructure and configuration is very time-consuming.
- Continuous manual monitoring of the application is challenging.

### Solution Implementation

You already have the application setup in the source code repository.

#### Microservice Requirements

1. **Endpoints:**
   - **/registerDoctor** (HTTP Method: POST)  
     Request Body: JSON
   - **/updateDoctor/{doctorRegNo}** (HTTP Method: PUT)  
     Request Body: JSON
   - **/searchDoctor/{doctorName}** (HTTP Method: GET)  
     No Request Body
   - **/deleteDoctor/{doctorRegNo}** (HTTP Method: DELETE)  
     No Request Body

2. Push code into your GitHub Repository.
   

### Continuous Integration & Continuous Deployment Tools

- **Git**: For version control.
- **Maven**: For Building and Packaging Application.
- **Jenkins**: For continuous integration and deployment.
- **Docker**: For containerizing applications.
- **Ansible**: Configuration management tool.
- **Selenium**: For automating tests on the deployed web application.
- **Terraform**: For infrastructure creation.

### Business Challenge/Requirement

When a developer pushes the updated code to the GIT master branch:
1. The Jenkins pipeline should be triggered.
2. Code should be checked out, compiled, tested, packaged, and containerized.
3. Terraform should provision the test and prd environment. (2 separate ec2 instances)
4. Ansible should configure the provisioned machine and deploy the application to a test environment.
5. The Contact page should be tested using a test automation tool using Selenium.
6. Upon successful testing, Ansible should deploy the application to the prd environment.

This process should be automatic and triggered by a push to the GitHub master branch.

## Application source code is available at the following link
[GitHub-MedicureApp-Link](https://github.com/rajasghyd/medicare.git)

## How to run the app
- Build App : mvn clean package
- Run App : mvn spring-boot:run
- access Test Environment using the url : http://ipaddress:8085/
- access Prod Environment using the url : http://ipaddress:8086/

## How to submit the project the project : 

1. Create a document with detailed step by step tasks along with the screenshot and upload into respective assignment.
2. Please mention your github repository containing all the codes includeing application code, pipeline code, Dockerfile, Ansible scripts, Terraform scripts, kubernetes scripts etc..
