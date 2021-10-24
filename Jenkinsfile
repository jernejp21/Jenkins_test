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
          bat 'compile.bat'
        }

      }
    }

    stage('winIDEA test') {
      steps {
        dir(path: 'winIDEA') {
          bat 'run_test.bat'
        }

      }
    }

  }
}