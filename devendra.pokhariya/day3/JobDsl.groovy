pipelineJob('awsInstanceConfiguration') {
    definition {
             cpsScm {
                 scriptPath 'Jenkinsfile'
                 scm {
                   git {
                       remote { url 'https://github.com/Devpokhariya/Jobdsl.git' }
                       branch '*/master'
                       extensions {}
                   }             }
         }
     }
  }
