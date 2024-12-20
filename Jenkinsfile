pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/ripplepad/JenkinsBeispiel.git'
        DEV_BRANCH = 'development'
        MAIN_BRANCH = 'main'
    }

    stages {
        stage('Checkout Development Branch') {
            steps {
                script {
                    // Checkout the development branch
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: "*/${DEV_BRANCH}"]],
                        userRemoteConfigs: [[url: GIT_REPO, credentialsId: 'your-credentials-id']]
                    ])
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Install dependencies and run tests
                    sh '''
                        pip install -r requirements.txt || true
                        pytest
                    '''
                }
            }
        }

        stage('Merge and Push to Main') {
            when {
                expression {
                    // Proceed only if the tests passed
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                script {
                    sh '''
                        git config user.name "ripplepad"
                        git config user.email "kerne-prosaisch.4l@icloud.com"

                        # Checkout the main branch
                        git checkout ${MAIN_BRANCH}

                        # Merge development into main
                        git merge ${DEV_BRANCH} --no-ff

                        # Push the changes to the main branch
                        git push origin ${MAIN_BRANCH}
                    '''
                }
            }
        }
    }

    post {
        failure {
            echo 'Tests failed. Not merging to main branch.'
        }
    }
}
