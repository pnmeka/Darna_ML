##needs to be added to Darna_local instance flask file

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if 'logged_in' not in session:
        return redirect('/login')

    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        ignore_words = request.form['ignore-words']
        print(f"Age: {age}")
        print(f"Sex: {sex}")
        print(f"Ignore Words: {ignore_words}")
        formatted_ignore_words = ignore_words.replace(' ', '|')

        content = f"age = '{age}'\nsex = '{sex}'\nignore_words = '{formatted_ignore_words}'\n"
        file_path = f"{HS_path}/variables2.py"

        try:
            with open(file_path, 'w') as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing to variables2.py: {str(e)}")
            return str(e)

        # Run the analyze script asynchronously using nohup
        command = f'nohup python3 analyze2.py > /dev/null 2>&1 &'
        try:
            subprocess.Popen(command, shell=True)
        except Exception as e:
            print(f"Error running analyze.py: {str(e)}")
            return str(e)

        return render_template('success.html')

    return render_template('analyze.html', submitted=True)
