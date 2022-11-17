from django.shortcuts import render

posts = [
    {
        "author": "Prakash Kafle",
        "title": "Blog 1",
        "content": "First Post Content",
        "date_posted": "11/16/2022",
    },
    {
        "author": "Dipika Bhandari",
        "title": "Blog 2",
        "content": "Second Post Content",
        "date_posted": "11/15/2022",
    },
]


# Create your views here.
def home(request):
    context = {"posts": posts, "title": "home"}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "about"})
