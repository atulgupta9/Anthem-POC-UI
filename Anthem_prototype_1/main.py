from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from Anthem_POC import html_parsing
from Anthem_POC import stop_word_and_punctuation_removal
from Anthem_POC import find_keyword_from_query
from Anthem_POC import matched_sentence_to_query
 
# App config.
DEBUG = True
app = Flask(__name__,static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('Query:', validators=[validators.required()])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print(form.errors)
    if request.method == 'POST':
        query = request.form['name']		
        text_strip, text = html_parsing()
        list_word = stop_word_and_punctuation_removal(text)
        keyword_list = find_keyword_from_query(query, list_word)
        final_output = matched_sentence_to_query(keyword_list, text_strip)
		
        #print(name)
		
        if form.validate():
            # Save the comment here.
            output = ''
            for i in range(0, len(final_output)):
                output = output + final_output[i] + '\n'		
            flash(query)
            flash(output)			
        else:
            flash('All the form fields are required. ')
	
    return render_template('anthem_poc_template.html', form=form)
 
if __name__ == "__main__":
    app.run()