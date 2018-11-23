#!groovy

pipeline
{
  agent none

  stages
  {
    stage("test")
    {
      agent
      {
        docker
        {
          image 'tjhei/dealii-doc-gen:v3'
        }
      }

      post { cleanup { cleanWs() } }

      stages
      {
        stage("permission")
        {
          when { not {branch 'master'}}
          steps
          {
            githubNotify context: 'CI', description: 'need ready to test label and /rebuild',  status: 'PENDING'
            // For /rebuild to work you need to:
            // 1) select "issue comment" to be delivered in the github webhook setting
            // 2) install "GitHub PR Comment Build Plugin" on Jenkins
            // 3) in project settings select "add property" "Trigger build on pr comment" with
            //    the phrase ".*/rebuild.*" (without quotes)
            sh '''
               wget -q -O - https://api.github.com/repos/dealii/publication-list/issues/${CHANGE_ID}/labels | grep 'ready to test' || \
               { echo "This commit will only be tested when it has the label 'ready to test'. Trigger a rebuild by adding a comment that contains '/rebuild'..."; exit 1; }
            '''
            githubNotify context: 'CI', description: 'running tests...',  status: 'PENDING'
          }
        }

        stage("latex")
        {
          steps
          {
            sh '''
	       cd offline
	       pdflatex -interaction=nonstopmode publication_list.tex
	       biber publication_list
	       pdflatex -interaction=nonstopmode publication_list.tex
	       '''
            archiveArtifacts artifacts: 'offline/publication_list.pdf', fingerprint: true
            githubNotify context: 'latex', description: '',  status: 'SUCCESS'
          }
        }
      }
    }

    stage('html')
    {
          agent
          {
            docker
            {
              image 'tjhei/dealii-java-jabref'
            }
          }
          post { cleanup { cleanWs() } }

          steps
          {
          timeout(time: 6, unit: 'HOURS')
          {
            sh '''
	       mkdir ~/source
	       cat publications-*.bib >~/source/aspect.bib
	       cp jabref-template/* ~/source/
	       cd ~; ./script.sh
	       cp ~/source/output.html $WORKSPACE
            '''
            archiveArtifacts artifacts: 'output.html', fingerprint: true
            githubNotify context: 'html', description: '',  status: 'SUCCESS'
          }
          }
    }

    stage("finalize")
    {
      agent none

      steps
      {
        githubNotify context: 'CI', description: 'OK',  status: 'SUCCESS'
      }
    }
  }
}
