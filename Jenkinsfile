pipeline {
  agent any
  stages {
    stage('Build with makefile') {
      steps {
        sh '''cd STM32L476/Debug
make clean
make'''
      }
    }

  }
}