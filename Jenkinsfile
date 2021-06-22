pipeline {

agent any
  
  stages {
    stage(git_checkout) {
      steps{
          git branch: 'main', credentialsId: 'brijesh2311', url: 'https://github.com/brijesh2311/boards.git'
            }
         }
    stage(Build) {
      steps{
          script {
          echo 'this is build'
            }
         }
    }
    stage(test) {
      steps{
         script {
          echo 'this is test'
            }
         }
    
    
      }

  
  
  }
  
}
