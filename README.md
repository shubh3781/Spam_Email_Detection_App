

# Spam_Email_Detection_App

This repository contains a simple Flask-based web application to classify emails as spam or ham using a machine learning model. The app is designed to be deployed on AWS EC2 instances with Amazon Linux AMI but can also be run locally.

## Features
- Classifies an email as spam or ham using a trained model (`model.spam.pkl`).
- User-friendly web interface created using HTML (`home.html`).
- Built using Python's Flask framework.
  
## Prerequisites

Make sure you have the following installed:
- Python 3.x
- Flask 3.0.3
- NLTK 3.6.6
- Scikit-learn 1.5.1

You can install these dependencies by running:
```bash
pip install -r requirements.txt
```

### Important:
The following are **updated** dependencies:
- `Flask==3.0.3`
- `nltk==3.6.6`
- `scikit-learn==1.5.1`

## How to Run Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Spam_Email_Detection_App.git
    cd Spam_Email_Detection_App
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Start the Flask application:
    ```bash
    python app.py
    ```

4. By default, the app runs on port 5000. Open your browser and navigate to:
    ```
    http://localhost:5000
    ```

### Important:
If you're running this app on a local machine, ensure you modify the following line in `app.py`:

```python
app.run(use_reloader=True, debug=True)
```
to:
```python
app.run(debug=True)
```

This change is necessary to avoid issues with reloading the app when making changes locally.

### Common Issue: NLTK `punkt` Resource Error

If you encounter the following error when running the app:

```
LookupError: 
**********************************************************************
  Resource punkt not found.
  Please use the NLTK Downloader to obtain the resource:
  >>> import nltk
  >>> nltk.download('punkt')
**********************************************************************
```

Follow these steps to resolve it:

1. Open a Python terminal and run the following commands:
    ```python
    import nltk
    nltk.download('punkt')
    ```

2. This will download the required resource and resolve the error.

## How to Deploy on AWS EC2

Follow these steps to deploy the app on an Amazon EC2 instance:

1. **Sign up for AWS and create an EC2 instance**:
   - Go to [AWS](https://aws.amazon.com) and sign up for an account.
   - Navigate to the EC2 service.
   
2. **Create a Key Pair**: This is used for SSH access to your instance.

3. **Create a Security Group**: Set the following inbound rules:
   - **SSH**: To allow access to the EC2 instance.
   - **ICMP**: To check ping.
   - **HTTP**: To allow HTTP connections.
   - **Custom (Port 5000)**: To allow Flask app (default port 5000).

4. **Launch the Instance**:
   - Name your instance.
   - Select the Amazon Linux AMI (Free Tier).
   - Choose instance type **t3.micro** (Free Tier eligible).
   - Assign the previously created key pair and security group.

5. **Connect to the Instance**:
   - Download your private key file (.pem) when creating the key pair.
   - Use an SSH client like Putty or your terminal to connect to the instance:
     ```bash
     ssh -i "your-key.pem" ec2-user@<public-ip-address>
     ```

6. **Deploy the App**:
   - Clone your repository on the EC2 instance:
     ```bash
     git clone https://github.com/yourusername/Spam_Email_Detection_App.git
     cd Spam_Email_Detection_App
     ```
   
   - Install Python and required libraries:
     ```bash
     sudo yum install python3
     pip3 install -r requirements.txt
     ```
   
   - Start the Flask app on the EC2 instance:
     ```bash
     python3 app.py
     ```

7. **Access the App**:
   - Once the app is running, navigate to `http://<your-ec2-public-ip>:5000` in your browser.

## File Structure

- `app.py`: The main Flask application file.
- `Main.py`: Supporting Python logic.
- `model.spam.pkl` and `tv_spam.pkl`: Pre-trained machine learning models.
- `requirements.txt`: Lists all the Python dependencies.
- `home.html`: The HTML file for the front-end interface.

## License
This project is licensed under the MIT License.

---