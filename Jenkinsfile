node {
    stage ("git checkout"){ 
        checkout scm
    }

    stage ("testing application"){
        sh 'pip3 install -r requirements.txt'
        sh 'python3 test.py'
    }

    stage ("building docker image"){ 
        // this builds the docker image and tags it with environment build number, it also save as a variable called customImage
    def customImage = docker.build("sadikac/blog-service:${env.BUILD_NUMBER}")
         
        
    }

    stage ("push to dockerhub"){
    docker.withRegistry('https://registry.hub.docker.com', 'sadikac') {


        /* Push the container to the custom Registry */
        customImage.push()
        customImage.push('latest')

        }       
    }
    }

