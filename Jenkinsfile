pipeline {
    agent any

    environment {
        registry = "https://registry.gitlab.com/devops9033903/devops"  // Replace with your GitLab registry path
        registryCredential = 'gitlab-credentials-id'  // Jenkins credential ID for GitLab
        dockerImage = ''
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile in the repository
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }

        stage('Push Docker Image to GitLab Registry') {
            steps {
                script {
                    // Log in and push the image to the GitLab container registry
                    docker.withRegistry('https://registry.gitlab.com', registryCredential) {
                        dockerImage.push()
                        dockerImage.push("latest")  // Optionally tag and push as 'latest'
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Remove any existing container with the same name (optional)
                    sh "docker rm -f flask-app || true"

                    // Run the Docker container
                    sh "docker run -d --name flask-app -p 5000:5000 ${registry}:$BUILD_NUMBER"
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
