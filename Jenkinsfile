node {
    stage ("git checkout"){ 
        checkout scm
    }

    stage ("testing application"){
        sh 'pip3 install -r requirements.txt'
        sh 'python3 test.py'
    }

    

    stage ("push to dockerhub"){
    docker.withRegistry('https://registry.hub.docker.com', 'sadikac') {
    def customImage = docker.build("sadikac/blog-service:${env.BUILD_NUMBER}")


        /* Push the container to the custom Registry */
        customImage.push()
        customImage.push('latest')

        }       
    }
    stage  ("deploy to ec2"){
    def docker_rm = 'docker rm -f devbops_blog'
    def docker_run = 'docker run -p 8080:80 -d --name devbops_blog sadikac/blog-service'
    

       sshagent(credentials: ['SadikaPrivate']) {
           sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.53 ${docker_rm}"
           sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.53 ${docker_run}"
    

    }
    }
    }

