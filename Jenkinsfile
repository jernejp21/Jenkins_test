pipeline {
  agent {
    node {
      label 'Rpi'
    }

  }
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