pipeline {
    agent any {
        stages {
            stage ('Checkout code') {
                steps {
                    git credentialsId:'MY_PAT', url:'https://github.com/gayathri7022/Test_repo.git', branch:'main'
                }
            }

            stage ('Install Dependencies') {
                steps {
                    bat '''
                        python3 -m venv venv
                        call venv\\Scripts\\activate
                        pip install --upgrade pip
                        pip install pytest
                        '''
                }
            }

            stage ('Run') {
                steps {
                    bat '''
                    call venv\\Scripts\\activate
                    pytest test.py
                    '''
                }
                
            }

            stage ('Deploy') {
                steps {
                    echo "Deplying Feature"
                    bat '''
                       call venv\\Scripts\\activate
                       pyhton login.py
                       '''
                }
            }
        }
    }
}