node {
    stage ("git checkout"){ 
        checkout scm
    }

    stage ("testing application"){
        sh 'pip3 install -r requirements.txt'
        sh 'python3 test.py'
    }

    stage ("building docker image and pushing to dockerhub"){
    def customImage = docker.build("sadikac/blog-service:${env.BUILD_NUMBER}")
         
        
    }
    }
