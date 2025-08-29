// Declarative Pipeline
pipeline {
    agent any 

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Cloning repository...'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // This step is crucial. You need to install any libraries your tests depend on.
                // It's a good practice to use a requirements.txt file.
                echo 'Installing Python dependencies...'
                // The 'sh' command is for Linux/macOS. For Windows, use 'bat' or 'powershell'
                // Assuming you have 'requirements.txt' in your repo root
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Automated Tests') {
            steps {
                echo 'Starting the automated test suite...'
                // This command runs all your test files with pytest
                // For Windows, it might be 'bat "pytest"'
                bat 'pytest'
                // Or if you want to run a specific file
                // sh 'pytest "Check field validations UI feedback.py"'
                echo 'Tests finished!'
            }
        }
    }
}
