pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Chigozie-473/Chigozie-django-polls.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Django Check') {
            steps {
                bat 'python manage.py check'
            }
        }
    }
}
