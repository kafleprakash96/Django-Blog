# Django-Blog

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/default.min.css">



Welcome to the Django Blog app! This app allows users to create and view blog posts.

Prerequisites

Before you begin, make sure you have the following:

Python 3.6 or newer
Django 3.1 or newer
Installation

To install the app, follow these steps:

Clone the repository
Navigate to the root directory of the repository
Run the following command to install the required packages:

<pre><code class="python hljs">pip install -r requirements.txt</code></pre>


Run the following command to migrate the database:


<pre><code class="python hljs">python manage.py migrate</code></pre>
<h3> For mac user <h3>
Mac comes with Python 2.7 So python3 is written to explicitly use Python3 version installed in your machine.
  
<pre><code class="python hljs">python3 manage.py migrate</code></pre>

Usage

To start the development server, run the following command:

<pre><code class="python hljs">python manage.py runserver</code></pre>

Then, visit http://localhost:8000 in your web browser to view the app.

To create a new blog post, click the "New Post" button on the homepage.

To view an existing blog post, click on the title of the post on the homepage.

Contributing

If you would like to contribute to the app, please fork the repository and submit a pull request.


