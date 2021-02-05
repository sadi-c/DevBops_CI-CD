node {
    stage ("git checkout"){ 
        checkout scm
    }

    stage ("build"){
        sh 'python3 test.py'
    }
    }
