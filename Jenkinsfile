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
                    dockerImage = docker.build("${registry}:${BUILD_NUMBER}")
                }
            }
        }

        stage('Push Docker Image to GitLab Registry') {
            steps {
                script {
                    docker.withRegistry('https://registry.gitlab.com', registryCredential) {
                        dockerImage.push()
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
                    if [ -f ${k8sConfigPath}/app.yaml ]; then
                        echo "File exists."
                        if kubectl get pods -l app=gitlab-app --field-selector=status.phase=Running | grep -q Running; then
                            kubectl delete pods -l app=gitlab-app --force --grace-period=0
                        fi
                        kubectl apply -f ${k8sConfigPath}/app.yaml
                        kubectl set image deployment/gitlab-app gitlab-container=${registry}:${BUILD_NUMBER}
                        kubectl rollout restart deployment gitlab-app
                    else
                        echo "File does not exist at ${k8sConfigPath}/app.yaml"
                        exit 1
                    fi
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
