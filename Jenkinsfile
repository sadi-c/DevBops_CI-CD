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
    }

