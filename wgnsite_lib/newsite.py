
# membiat sebuah direktori web baru    
def newweb(root_path):
    os.mkdir(root_path)
    
  
    list = ['output', 'content', 'templates'] 

    for items in list: 
        path = os.path.join(root_path, items) 
        os.mkdir(path)
        
    
    
    # ini file html untuk tema

    layout = """<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/picnic@6.5.0/picnic.min.css">
    <!-- <link rel="stylesheet" href="main.css"> -->
    <title>My Recipes</title>
    <style>
        .container {
            width: 80%;
            margin: auto;
            margin-top: 3em;
        }

        .mybutton {
            background: #f7786b;
            font-size: 0.75em;
        }
    </style>
</head>
<body class="container">
    
    {% block content %} {% endblock %}

    <br>

</body>
</html>


    """
    
    home = """
{% extends "layout.html" %}

{% block content %}

<h1>My Recipes</h1>

<div class="flex three demo">

{% for post in posts %}

    <div>

        <article class="card">
            <header>
                <img src="{{ post.thumbnail }}">
            </header>
            <footer>
                <h2>{{ post.title }}</h2>
                <small>{{ post.date }}</small>
                <p>
                    {{ post.summary}}
                </p>
                <a class="button" href="posts/{{ post.slug }}.html">Recipe</a>
                <br>
                {% set list_of_tags = post.tags.split(",") %}
                {% for tag in list_of_tags %}
                    <button class="shyButton mybutton">{{ tag }}</button>
                {% endfor %}
            </footer>
            
        </article>

    </div>

<!-- 
    <p>
            <h2>{{loop.index}}: <a href="posts/{{ post.slug }}.html">{{post.title}}</a> <small>{{post.date}}</small></h2>
            {{post.summary}}
        </p> -->

{% endfor %}

</div>

{% endblock %}

    """

    postingan = """{% extends "layout.html" %}

{% block content %}

<h1>{{post.title}}</h1>
<p>
    <small>{{post.date}}</small>
    {{post.content}}
</p>

{% endblock %}


    """











    tulissan = """Congratulations! Your new site is created !!
"""        

    print(tulissan)
    exit()

