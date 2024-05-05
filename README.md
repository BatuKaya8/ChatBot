# Turkcell Assistant Development Project

## Overview
This project consists of RASA files aimed at developing the Turkcell Assistant using AI and machine learning techniques. It provides the necessary files to train and interact with the Turkcell Assistant. Please note that this project does not have a graphical interface and is intended to be integrated into a Python project.

## Installation
1. Create a new Python project.
2. Install RASA by running the following command in the terminal:
```
pip install rasa
```
4. Clone or download this repository and copy the provided folder into your Python project directory.

## Usage
To train and interact with the Turkcell Assistant, follow these steps:
1. Open a terminal and navigate to your Python project directory.
2. Train the NLU (Natural Language Understanding) model:
```
rasa train nlu
```
4. Train the core model:
```
rasa train
```
6. Start the shell to chat with the Turkcell Assistant:
```
rasa shell
```
## Note:
Because of some decisions made in the code, training the model can take a while and the model file size can be huge. Please be patient in this process.


## Contributing
Contributions to this project are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## License
This project is licensed under the [MIT License](LICENSE).
