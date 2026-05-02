pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                deleteDir()
                git branch: 'main', url: 'https://github.com/Chigozie-473/django-polls-tutorial.git'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m pip install --break-system-packages --upgrade pip'
                sh 'pip install --break-system-packages -r requirements.txt'
            }
        }

        stage('Django Check') {
            steps {
                sh 'python3 manage.py check'
            }
        }
    }
}
