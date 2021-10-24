pipeline {
  agent {
    node {
      label 'STM32node'
    }

  }
  stages {
    stage('Build with makefile') {
      steps {
        dir(path: 'STM32L476/Debug') {
          bat 'wsl make -j6'
        }

      }
    }

  }
}