from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)
DATABASE_FILE = 'data.csv'


@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()

    return render_template('list.html', user_stories=user_stories)


@app.route('/story', methods=['GET', 'POST'])
def new_story():
    stories = data_handler.get_all_user_story()
    if stories == []:
        new_key = 0
    else:
        new_key = int(stories[-1]['id']) + 1
    if request.method == "POST":
        new_id = str(new_key)
        new_title = request.form.get('title')
        new_user_story = request.form.get('user_story')
        new_acceptance_criteria = request.form.get('acceptance_criteria')
        new_business_value = str(request.form.get('business_value'))
        new_estimation = str(request.form.get('estimation'))

        # left new_status like this by choice because it seems like a legit input
        # I can always hard code 'Planning' into it for the "Add User Story" step
        # and remove the HTML select tag or added a jinja section on the site

        new_status = request.form.get('status')
        new_dictionary = {'id': new_id,
                          'title': new_title,
                          'user_story': new_user_story,
                          'acceptance_criteria': new_acceptance_criteria,
                          'business_value': new_business_value,
                          'estimation': new_estimation,
                          'status': new_status
                          }
        stories.append(new_dictionary)
        data_handler.write_to_file(stories)
        return redirect(url_for('route_list'))
    return render_template('story.html', stories=stories)


@app.route('/story/<story_id>', methods=['GET', 'POST'])
def edit_story(story_id):
    stories = data_handler.read_from_file(DATABASE_FILE)
    if request.method == 'GET':
        for story in stories:
            if story['id'] == story_id:
                story_id = story['id']
                story_title = story['title']
                user_story = story['user_story']
                acceptance_criteria = story['acceptance_criteria']
                business_value = story['business_value']
                estimation = story['estimation']
                status = story['status']
                return render_template('edit_story.html',
                                       id=story_id,
                                       story_title=story_title,
                                       user_story=user_story,
                                       acceptance_criteria=acceptance_criteria,
                                       business_value=business_value,
                                       estimation=estimation,
                                       status=status)
    elif request.method == 'POST':
        for story in stories:
            if story['id'] == story_id:
                story['title'] = request.form.get('title')
                story['user_story'] = request.form.get('user_story')
                story['acceptance_criteria'] = request.form.get('acceptance_criteria')
                story['business_value'] = request.form.get('business_value')
                story['estimation'] = request.form.get('estimation')
                story['status'] = request.form.get('status')
        data_handler.write_to_file(stories)
        return redirect(url_for('route_list'))


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
