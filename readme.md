## Getting Started
Follow these steps to set up and run the project locally:

### Clone the Repository
git clone https://github.com/2024tm93298/fitness.git
cd fitness

### Install Python 3
brew install python@3.10  # For macOS
sudo apt install python3.10 -y # For Ubuntu

### Create and Activate the Virtual Environment
python3 -m venv venv
source venv/bin/activate

### Install Dependencies
pip install flask
pip install pytest
pip install pytest-mock
apt-get install python3-tk

### Running Tests
pytest

### Run the Applications
python3 -m flask --app web_app.py run
python3 ACEest_Fitness.py

### Containerization using Docker
sudo snap install docker
sudo docker build -t fitness-app .
sudo docker run -p 5000:5000 fitness-app