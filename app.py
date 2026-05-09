from flask import Flask, render_template, request, jsonify, send_file
from pathlib import Path
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

@app.route('/favicon.ico')
def favicon():
    """Avoid noisy 404s for the default browser favicon request."""
    return ('', 204)

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
    cv_path = Path(__file__).resolve().parent / 'Resume.pdf'
    if not cv_path.exists():
        return jsonify({'success': False, 'message': 'Resume file not found.'}), 404

    return send_file(
        cv_path,
        as_attachment=True,
        download_name='Muhammad_Daiym_Mughal_Resume.pdf',
        mimetype='application/pdf',
    )


@app.route('/download-medpres-apk')
def download_medpres_apk():
    """Download MedPres APK (place the file first)."""
    base_dir = Path(__file__).resolve().parent

    candidates = [
        base_dir / 'MedPres.apk',
        base_dir / 'app-release.apk',
        base_dir / 'static' / 'downloads' / 'MedPres.apk',
        base_dir / 'static' / 'downloads' / 'app-release.apk',
    ]

    apk_path = next((p for p in candidates if p.exists()), None)
    if apk_path is None:
        # Fallback: pick any APK placed in common locations.
        for search_dir in [base_dir, base_dir / 'static' / 'downloads']:
            if search_dir.exists():
                found = list(search_dir.glob('*.apk'))
                if found:
                    apk_path = sorted(found)[0]
                    break

    if apk_path is None:
        return jsonify({
            'success': False,
            'message': 'MedPres APK not found. Add an APK to the project root (e.g., MedPres.apk or app-release.apk) or static/downloads/.'
        }), 404

    return send_file(
        apk_path,
        as_attachment=True,
        download_name='MedPres.apk',
        mimetype='application/vnd.android.package-archive',
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
