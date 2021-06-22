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
          echo "this is build"
            }
         }
    
    stage(test) {
      steps{
         echo "this is test"
            }
         }
    
    
      }

  
  
  
  
}
