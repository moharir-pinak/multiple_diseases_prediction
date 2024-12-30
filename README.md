# Multiple_disease_prediction

This project utilizes machine learning algorithms to predict the likelihood of a patient having multiple diseases based on their medical history and symptoms.

## Features

- **Disease Prediction**: Predicts the probability of various diseases using patient data.
- **Machine Learning Models**: Employs algorithms such as Decision Trees, Support Vector Machines, and Random Forests for accurate predictions.
- **User Interface**: Provides an interactive web application for users to input data and receive predictions.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/moharir-pinak/multiple_diseases_prediction.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd multiple_diseases_prediction
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Train the models**:

   The `colab_files_to_train_models` directory contains Jupyter notebooks for training the machine learning models. Execute these notebooks to train and save the models.

2. **Run the application**:

   ```bash
   streamlit run app.py
   ```

3. **Access the web application**:

   Open your web browser and navigate to `http://localhost:8501` to use the application.

## Dataset

The `dataset` directory includes the data used for training and testing the models. Ensure that the data is preprocessed appropriately before training.

## Models

Trained models are stored in the `saved_models` directory. If you have pre-trained models, place them in this directory to use them directly without retraining.

## Requirements

- Python 3.7 or higher
- Streamlit
- scikit-learn
- pandas
- numpy

For a complete list of dependencies, refer to the `requirements.txt` file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

This project is inspired by various studies on disease prediction using machine learning, including:

- [Feasible Prediction of Multiple Diseases using Machine Learning](https://www.e3s-conferences.org/articles/e3sconf/pdf/2023/67/e3sconf_icmpc2023_01051.pdf)
- [Multi Disease Prediction System Using Machine Learning](https://www.researchgate.net/publication/381309960_MULTI_DISEASE_PREDICTION_SYSTEM_USING_MACHINE_LEARNING)

These resources provided valuable insights into the development of this project.

## Contact

For any inquiries or issues, please open an issue on the GitHub repository. 
