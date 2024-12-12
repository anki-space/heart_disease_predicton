# Heart Disease Predictor

This project aims to develop Health Management system by using a machine learning model for predicting the likelihood of heart disease in patients. This can predict 5 different types of disease :- 'Arrhythmia','Coronary Artery Disease','Heart Disease','Hypertension', 'Stroke'.


## Model

We have implemented a classification model using a combination of feature engineering and bases on S.V.C machine learning algorithm. The model is trained on the dataset to learn patterns and make predictions on new, unseen data.

### Setup 🔧

1. Clone the repository:

    ```bash
    git clone https://github.com/anki-space/heart_disease_predicton
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    cd heart_diesease_predict
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

    Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).



## Results

The performance of the heart disease predictor model is evaluated using various metrics such as accuracy, precision, recall, and F1 score. 

Classification Report on Test Data:
              precision    recall  f1-score   support

           0       1.00      0.88      0.94        50
           1       1.00      0.96      0.98        50
           2       0.84      0.96      0.90        54
           3       0.90      1.00      0.95        52
           4       1.00      0.83      0.91        36

    accuracy                           0.93       242


The results indicate the effectiveness of the model in predicting heart disease.



