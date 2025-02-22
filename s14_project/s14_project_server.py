import os
from flask import Flask, send_from_directory
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return 'Final project'

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('/home/pi/Desktop/final/img', filename)

@app.route('/check-photos')
def check_photos():
    """Displays number of photos since last visit to /check-photos"""
    last_time_checked = get_last_time_checked()
    photos_since_last_time = get_photos_since_time(last_time_checked)
    print(photos_since_last_time)
    last_photo = photos_since_last_time[-1] if photos_since_last_time else 'https://placebear.com/cache/395-205.jpg'
    save_time_checked()

    html = """
    <html>
        <head>
            <title>Check Photos</title>
        </head>
        <body>
            <h1>Check Photos</h1>
            <p>Number of photos taken since last visit: {number_of_photos}</p>
            <p>Latest photo taken: <img src="{latest_photo}" /></p>
        </body>
    </html>
    """
    return html.format(
        number_of_photos=len(photos_since_last_time),
        latest_photo=last_photo
    )


def save_time_checked():
    """Records the current time when we go to /check-photos"""
    filename = "/home/pi/Desktop/final/logs/check-photos-log.txt"
    with open(filename, "w") as f:
        f.write(f"{str(datetime.now().timestamp())}\n")

def get_last_time_checked():
    filename = "/home/pi/Desktop/final/logs/check-photos-log.txt"
    if not os.path.exists(filename):
        print("No log file found")
        default_time = datetime(2025, 1, 1).timestamp()
        return default_time
    else:
        with open(filename, "r") as f:
            lines = f.readlines()
            return lines[-1].rstrip()

def get_photos_since_time(timestamp):
    """Returns a list of photos taken since the given time"""
    log_filename = "/home/pi/Desktop/final/logs/log.txt"
    photos = []

    if not os.path.exists(log_filename):
        return photos

    with open(log_filename, "r") as f:
        for line in f:
            photo_path = line.strip()
            photo_timestamp = float(photo_path.split('_')[1].split('.')[0])
            if photo_timestamp > float(timestamp):
                # Convert filesystem path to web path
                filename = os.path.basename(photo_path)
                web_path = f"/images/{filename}"
                photos.append(web_path)

    return photos


if __name__ == '__main__':
    app.run(host='0.0.0.0')
