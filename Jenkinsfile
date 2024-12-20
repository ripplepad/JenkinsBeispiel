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
                    // Create and activate a virtual environment, then install dependencies and run tests
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        export PYTHONPATH=$PWD
                        pytest
                    '''
                }
            }
        }

        stage('Merge and Push to Main') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                script {
                    sh '''
                        git config user.name "ripplepad"
                        git config user.email "kerne-prosaisch.4l@icloud.com"

                        git checkout ${MAIN_BRANCH}
                        git merge ${DEV_BRANCH} --no-ff
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
