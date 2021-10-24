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

    stage('winIDEA test') {
      steps {
        dir(path: 'winIDEA') {
          bat 'PATH=C:\\iSYSTEM\\winIDEA9\\Python'
          bat 'python test.py'
        }

      }
    }

  }
}