from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)
IMAGE_FILE = 'images.txt'

# Load existing image URLs from the text file
def load_images():
    if os.path.exists(IMAGE_FILE):
        with open(IMAGE_FILE, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

# Save new image URLs to the text file
def save_image(image_url):
    # Read the existing contents of the file
    with open(IMAGE_FILE, 'r') as file:
        existing_contents = file.readlines()

    # Prepend the new image URL to the existing contents
    existing_contents.insert(0, image_url + '\n')

    # Write the updated contents back to the file
    with open(IMAGE_FILE, 'w') as file:
        file.writelines(existing_contents)

def delete_image():
    with open('images.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('images.txt', 'w') as fout:
        fout.writelines(data[1:])



@app.route('/')
def index():
    image_urls = load_images()
    return render_template('index.html', image_urls=image_urls)

@app.route('/upload', methods=['POST'])
def upload():
    image_url = request.form['image_link']
    save_image(image_url)  # Save the new image URL
    image_urls = load_images()  # Load updated list of image URLs
    return redirect("/")

@app.route('/delete/')
def delete():
    with open('images.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('images.txt', 'w') as fout:
        fout.writelines(data[1:])
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)