from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'

@app.route('/')
def index():
    """Main portfolio page"""
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        # Here you can add email sending logic or save to database
        # For now, we'll just return a success message
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your message! I will get back to you soon.'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Sorry, there was an error sending your message. Please try again.'
        }), 500

@app.route('/download-cv')
def download_cv():
    """Download CV endpoint"""
    # You can add logic to serve your CV file
    return jsonify({'message': 'CV download endpoint'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
