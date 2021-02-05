# Setting up CI/CD pipeline using Jenkins

> 1. Making sure you have a Jenkins server running in your public subnet.From the command line of your server running in the public subnet do the following commands:
* sudo yum install git -y
* sudo yum install python3 -y
* sudo amazon-linux-extras install docker -y
* sudo yum install docker
* sudo service docker start
* sudo systemctl enable docker
* sudo usermod -a -G docker jenkins

> 2. Access your Jenkins server from the web using the public IP at port 8080. From there install the follwing plugins for Jenkins server to do so go to manage Jenkins then manage plugins 
* Docker Commons Plugin
* Docker Pipeline
* Docker plugin
* docker-build-step
* CloudBees Docker Build and Publish plugin
* SSH Agent


