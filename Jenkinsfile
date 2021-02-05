node {
    stage ("git checkout"){ 
        checkout scm
    }

    stage ("build"){
        sh 'pip3 install -r requirements.txt'
        sh 'python3 test.py'
    }
    }
