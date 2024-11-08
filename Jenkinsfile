pipeline {
    agent any

    environment {
        registry = "registry.gitlab.com/devops9033903/devops"
        registryCredential = 'gitlab-credentials-id' // Jenkins credential ID for GitLab registry
        dockerImage = ''
        k8sConfigPath = '/home/ubuntu/cicd'
        vmHost = '13.208.182.172' // Replace with your VM's IP address
        sshKey = 'ssh-key' // Jenkins credential ID for SSH key
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
                        dockerImage.push("latest") // Push both unique and latest tags
                    }
                }
            }
        }

        stage('Deploy to Minikube') {
    steps {
        sshagent([sshKey]) {
            sh """
            ssh -o StrictHostKeyChecking=no ubuntu@${vmHost} << 'EOF'
            kubectl set image deployment/gitlab-app gitlab-container=registry.gitlab.com/devops9033903/devops:${BUILD_NUMBER}
            kubectl apply -f ${k8sConfigPath}/deployment.yaml
            kubectl rollout restart deployment gitlab-app
EOF
            """
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
