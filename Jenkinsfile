pipeline {
    agent any
    options { skipDefaultCheckout(true) }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build') {
            steps { sh 'python3 -m py_compile app.py' }
        }
        stage('Test') {
            steps { sh 'python3 -m unittest -v' }
        }
    }
    post {
        success { echo 'JENKINS LAB PASSED' }
    }
}
