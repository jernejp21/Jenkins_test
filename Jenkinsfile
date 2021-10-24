pipeline {
  agent {
    node {
      label 'STM32node'
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

    stage('Run winIDEA tests') {
      steps {
        sh '''source ~bin/embeddedPy/bin/activate
echo $PWD'''
      }
    }

  }
}