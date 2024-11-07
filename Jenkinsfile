pipeline {
    agent any

    environment {
        registry = "registry.gitlab.com/devops9033903/devops"
        registryCredential = 'gitlab-credentials-id'
        dockerImage = ''
        k8sConfigPath = 'cicd/app.yaml'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }

        stage('Push Docker Image to GitLab Registry') {
            steps {
                script {
                    docker.withRegistry('https://registry.gitlab.com', registryCredential) {
                        dockerImage.push()
                        dockerImage.push("latest")
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
