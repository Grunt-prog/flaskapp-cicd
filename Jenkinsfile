pipeline {
    agent any

    environment {
        registry = "registry.gitlab.com/devops9033903/devops"
        registryCredential = 'gitlab-credentials-id'
        dockerImage = ''
        k8sConfigPath = '/home/ubuntu/cicd'
        vmHost = '13.208.182.172' // Replace with your VM's IP address
        sshKey = credentials('ssh-key') // Jenkins credential ID for your PEM file
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

        stage('Deploy to Minikube') {
            steps {
                script {
                    // SSH into the VM and deploy the application
                    sshagent(['your-ssh-key-id']) { // Use SSH agent with your key
                        sh """
                            ssh -o StrictHostKeyChecking=no -i ${sshKey} user@${vmHost} '
                                # Set up Minikube environment if necessary
                                eval \$(minikube docker-env)

                                # Optionally, you can also set image if needed
                                kubectl set image deployment/your-deployment-name your-container-name=${registry}:${BUILD_NUMBER}
                                # Apply Kubernetes configuration
                                kubectl apply -f ${k8sConfigPath}
                                

                            '
                        """
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
