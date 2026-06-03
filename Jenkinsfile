pipeline {
agent any

```
tools {
    python 'Python3'
}

environment {
    VENV = "venv"
}

stages {

    stage('Checkout') {
        steps {
            git 'https://github.com/anubhavbharti73/SMS-Email_Classifier.git'
        }
    }

    stage('Setup Environment') {
        steps {
            sh '''
            python3 -m venv $VENV
            . $VENV/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt
            pip install pytest
            '''
        }
    }

    stage('Run Tests') {
        steps {
            sh '''
            . $VENV/bin/activate
            echo "Running pytest..."
            pytest --maxfail=1 --disable-warnings -v
            '''
        }
    }

    stage('Build Model (Optional)') {
        steps {
            sh '''
            . $VENV/bin/activate
            echo "Training or loading model..."
            # python train.py
            '''
        }
    }

    stage('Run App (Smoke Test)') {
        steps {
            sh '''
            . $VENV/bin/activate
            echo "Starting Streamlit app..."
            nohup streamlit run app.py --server.port 8501 &
            sleep 10
            '''
        }
    }

    stage('Deploy') {
        when {
            expression { currentBuild.currentResult == 'SUCCESS' }
        }
        steps {
            echo 'Deploy to Docker / AWS / Render'
        }
    }
}

post {
    success {
        echo '✅ Pipeline executed successfully!'
    }
    failure {
        echo '❌ Pipeline failed. Check test cases or build logs.'
    }
}
```

}
