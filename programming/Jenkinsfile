pipeline {
  agent any
  stages {
    stage('Preparation') {
      steps {
        git(url: 'git@github.com:vamsitallapudi/PythonProgramming.git', branch: 'master', changelog: true, credentialsId: '6c581a4c-63e2-4a7a-9df1-fe0fd7deb612')
      }
    }
  }
}