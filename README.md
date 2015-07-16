# MelbDjango School Lesson One

Congratulations, you've made it to the git repository for our first lesson. Hopefully you also made it to the class
and some of this makes sense to you.

Check our RESOURCES.md for some links we think you'll find handy.


## Displaying the class slides

Install reveal-md with npm and use that to display the class slides.

```
    npm install -g reveal-md

    cd slides
    reveal-md CLASS.md --theme melbdjango
```

## Homework Checklist

- [ ] [Fork this repository][gh-fork]
- [ ] Clone the repo to your own machine
- [ ] Create a virtualenv for our MelbDjango School project
- [ ] Install our requirements and use `python manage.py runserver` to test the application
- [ ] Update the view we created in class to accept a `name` GET parameter and say hello to that person.
      You'll need to access the [request.GET][dj-request-response] object.
- [ ] A step further - Add a `<form>` and `<input>` to let the user submit the name to be displayed

You'll need to be familiar with HTML and forms to do the last step above – check out the [MDN Introduction to HTML][mdn-html]
to understand the basics.

When you've completed some or all of the homework please make a [Pull Request][gh-pr] against this repository. If you submit
your work before Wednesday evening we'll give you feedback before the next class.

If you'd like help, make a Pull Request with your incomplete work and ask a question to @darrenfrenkel, @sesh or
@funkybob.

[gh-fork]: https://help.github.com/articles/fork-a-repo/
[gh-pr]: https://help.github.com/articles/using-pull-requests/
[dj-request-response]: https://docs.djangoproject.com/en/1.8/ref/request-response/
[mdn-html]: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Introduction
