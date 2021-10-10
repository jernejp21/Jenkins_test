pipeline {
  agent any
  stages {
    stage('Git') {
      steps {
        git(url: 'https://github.com/jernejp21/Jenkins_test', branch: 'master', credentialsId: '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')
      }
    }

    stage('Build with makefile') {
      steps {
        sh '''cd STM32L476/Debug
make clean
make'''
      }
    }

  }
}