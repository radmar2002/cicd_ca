# Guestbook App - Continuous Delivery using Docker and Ansible Source Code

This folder contains all of the source code and repositories for the CI/CD exercise

## Objectives
* Demonstrate your knowledge and proficiency with Software Development Life Cycle best practices and tooling
* Describe the processes you undertake to have the project running in a stable, secure, and scalable manner in the Cloud.

## The Process Steps:
1. Creating the Guestbook Application
	* [DONE] Guestbook Sample Application 
	* [ ] Unit and Integration Tests
	* [ ] Acceptance Tests
2. Unit/Integration Testing using Docker
	* [ ] Test Stage
	* [ ] Docker Images
	* [ ] Docker and Docker Compose Building Blocks
3. Building Artifacts using Docker
	* [ ] Build Stage
	* [ ] Test Stage Consistency
	* [ ] Creating Built Distributions
4. Creating Releases using Docker
	* [DONE] Release Stage
	* [ ] Release Image
	* [ ] Release Environment
5. Continuous Delivery Automation
	* [ ] Make Build System
	* [ ] GitHub Repos
	* [ ] Docker Hub Repos
6. Continuous Delivery using Jenkins
	* [ ] Jenkins
	* [ ] GitHub and Docker Hub Integration
	* [ ] Running Jenkins in AWS
7. Continuous Deployment using Ansible
	* [ ] Ansible Deployment Playbook
	* [ ] Infrastructure as Code
	* [ ] End-to-End Continuous Delivery
8. Improve the Workflow
	* [ ] Production Ready	
	* [ ] Error and Failure Handling
	* [ ] Tag Publish	


## Notes on stable, secure, and scalable concepts

#### Stable -Practices for Operational Stability
* Develop Loosely Coupled Services
* Release Small Changes
* Monitor the System
* Infrastructure as Code
* Automated Testing
* Deployment Automation

#### Secure 
* Achieve Tool Integration - The only way for security checks to work seamlessly in Continuous Integration/Deployment (CI/CD) pipelines is for security tools to be integrated with DevOps software such as Jenkins and Ansible. API endpoints can provide the means for achieving this integration, and these popular DevOps tools should be integrated with security frameworks like Selenium if APIs are available.
* Automate Security Tests
* Secure the Software Supply Chain

#### Scalable
* As the system grows (in data volume, traffic volume, or complexity), there should be reasonable ways of dealing with that growth.






## System Requirements

- Linux
- Docker >= 17.03.1-ce
- Docker Compose >= 1.18.0
- Docker Machine >= 0.16
- Git
- AWS CLI