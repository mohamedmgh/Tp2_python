pipeline {
    agent any
    
    triggers {
        pollSCM('* * * * *') // toutes les minutes
    }

    
    environment {
        IMAGE_NAME = "tp2"
        CONTAINER_NAME = "tp2-app"
        PORT = "8501"
        DOCKER_BUILDKIT = "0"
    }
    
    stages {
        stage('📥 Checkout') {
            steps {
                echo '📥 Récupération du code...'
                checkout scm
            }
        }
        
       
        stage('🐳 Build Docker Image') {
            steps {
                bat 'docker build -t tp2:latest .'
            }
        }

        stage('🚀 Run Docker Container') {
            steps {
                bat '''
                docker stop tp2 || exit 0
                docker rm tp2 || exit 0
                docker run -d -p 8501:8501 --name tp2 tp2:latest
                '''
            }
        }
    }

    post {
        success {
            echo '🎉 Build and deploy finished!'
            echo 'Open http://<YOUR_JENKINS_HOST>:8501 to view the app'
        }
        failure {
            echo '❌ The pipeline failed. Check logs for errors.'
        }
    }
}