pipeline {
    agent any


    stages {
        stage('Build') {
            steps {
                script {
                    // Clone the repo and setup venv environment
                    // sh "printenv | sort"
                    sh 'bash $WORKSPACE/Build/build.sh'

                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'bash $WORKSPACE/Tests/test.sh'
                }
            }
        }
        // stage('Approve') {
        //     steps {
        //         script {
        //             input "Deploy?"
        //         }
        //     }
        // }
        stage('Deploy') {
            when {
                branch 'production'
            }
            steps {
                script {
                    sh 'ansible-playbook $WORKSPACE/Deploy/deploy.sh'
                }
                
            }
        }
    }
    // post{
    //     success {
    //         sh 'ansible-playbook notify.yml -vvv'
    //     }
    // }
}