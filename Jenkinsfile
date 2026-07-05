pipeline {

    agent any

    stages {

        stage('Checkout Code') {

            steps {

                git branch: 'main',
                url: 'https://github.com/sapellysaivivek/T6A_Automation_capstone_project.git'

            }
        }

        stage('Create Virtual Environment') {

            steps {

                bat '''
                python -m venv venv
                '''

            }
        }

        stage('Install Dependencies') {

            steps {

                bat '''
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''

            }
        }

        stage('Start Selenium Grid') {

            steps {

                bat '''
                docker-compose up -d
                '''

            }
        }

        stage('Run API Tests') {

            steps {

                bat '''
                call venv\\Scripts\\activate
                pytest -m api -n 4 -v --reruns 2 --alluredir=allure-results
                '''

            }
        }

        stage('Run UI Tests') {

            steps {

                bat '''
                call venv\\Scripts\\activate
                pytest -m ui -v --reruns 2 --alluredir=allure-results
                '''

            }
        }
        stage('Run Api and ui integrating tests') {

            steps {

                bat '''
                call venv\\Scripts\\activate
                pytest -m uiandapi -v --reruns 2 --alluredir=allure-results
                '''

            }
        }

        stage('Generate Allure Report') {

            steps {

                allure(
                    commandline: 'Allure',
                    results: [[path: 'reports/allure-results']]
                )

            }
        }
    }

    post {

        always {

            archiveArtifacts artifacts: 'automation.log', allowEmptyArchive: true

            bat '''
            docker-compose down
            '''

        }

        success {

            echo 'Pipeline executed successfully'

        }

        failure {

            echo 'Pipeline failed'

        }
    }
}
