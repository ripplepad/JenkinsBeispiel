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
                // Pull the latest code from the development branch
                git branch: "${DEV_BRANCH}", url: "${GIT_REPO}"
            }
        }

        stage('Run Tests') {
            steps {
                // Install dependencies (if any) and run tests
                sh 'pip install -r requirements.txt || true'
                sh 'pytest'
            }
        }

        stage('Merge and Push to Main') {
            when {
                expression {
                    // Proceed only if the tests passed (exit code 0)
                    return currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                // Merge development into main and push
                script {
                    sh '''
                        git config user.name "ripplepad"
                        git config user.email "kerne-prosaisch.4l@icloud.com
"

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
