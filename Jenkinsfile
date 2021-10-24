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
          powershell 'wsl make -j6'
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