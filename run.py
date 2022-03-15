from sys import argv
import urllib
from urllib import request
import datetime
import os

import os
from datetime import datetime
from jinja2 import Environment, PackageLoader
from markdown2 import markdown




def help():
    print("ini pesan help help")
    exit()

def newsite(root_path):
    os.mkdir(root_path)
    
  
    list = ['output', 'content', 'templates'] 

    for items in list: 
        path = os.path.join(root_path, items) 
        os.mkdir(path)
        

    tulissan = """Congratulations! Your new Hugo site is created in /data/data/com.termux/files/home/site/p/tes.

Just a few more steps and you're ready to go:

1. Download a theme into the same-named folder.
   Choose a theme from https://themes.gohugo.io/ or
   create your own with the "hugo new theme <THEMENAME>" command.
2. Perhaps you want to add some content. You can add single files
   with "hugo new <SECTIONNAME>/<FILENAME>.<FORMAT>".
3. Start the built-in live server via "hugo server".

Visit https://gohugo.io/ for quickstart guide and full documentation. """

        

    print(tulissan)

def main():
    # mengubah markdown menjadi html

    #os.mkdir("output")
    POSTS = {}

    for markdown_post in os.listdir('content'):
        file_path = os.path.join('content', markdown_post)

        with open(file_path, 'r') as file:
            POSTS[markdown_post] = markdown(file.read(), extras=['metadata'])

    
    POSTS = {
        post: POSTS[post] for post in sorted(POSTS, key=lambda post: datetime.strptime(POSTS[post].metadata['date'], '%Y-%m-%d'), reverse=True)
    }

    env = Environment(loader=PackageLoader('main', 'templates'))
    home_template = env.get_template('home.html')
    post_template = env.get_template('post.html')

    posts_metadata = [POSTS[post].metadata for post in POSTS]
    tags = [post['tags'] for post in posts_metadata]
    home_html = home_template.render(posts=posts_metadata, tags=tags)

    with open('output/index.html', 'w') as file:
        file.write(home_html)

    for post in POSTS:
        post_metadata = POSTS[post].metadata

    post_data = {
        'content': POSTS[post],
        'title': post_metadata['title'],
        'date': post_metadata['date']
    }

    post_html = post_template.render(post=post_data)
    post_file_path = 'output/posts/{slug}.html'.format(slug=post_metadata['slug'])

    os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
    with open(post_file_path, 'w') as file:
        file.write(post_html)
    exit()
        



if __name__ == '__main__':
	if len(argv) == 1:
		main()

	if argv[1] in ('-h', '--help'):
		help()
	
	elif argv[1] == '-new':
		NameSite = argv[2]
		newsite(NameSite)