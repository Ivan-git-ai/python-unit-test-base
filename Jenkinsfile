pipeline {
    agent {
        docker {
            image 'python:latest'
            args '-u root'
        }
    }

    stages {
        stage("install deps") {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests with Coverage') {
            steps {
                sh 'coverage run -m nose2'
            }
        }
        stage('Reports') {
            steps {
                script {
                    sh 'coverage report -m'
                    sh 'coverage xml -o coverage.xml'
                    sh 'coverage html -d htmlcov'
                    archiveArtifacts artifacts: 'coverage.xml, htmlcov/**/*', allowEmptyArchive: true
                }
            }
        }
    }
     post {
        always {
            cobertura coberturaReportFile: 'coverage.xml'
        }
    }
}
