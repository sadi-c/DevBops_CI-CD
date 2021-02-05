node {
    stage ("git checkout"){ 
        checkout scm
    }

    stage ("build"){
        sh 'python3 Test.py'
    }
    }
