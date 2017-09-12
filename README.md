# Reporting Tool for News Site

This is the Logs Analysis project for the Udacity Fullstack Nanodegree. The program connects to a database and answers some analytics questions.

## Requirements
* Python 2.7
* Vagrant
* VirtualBox

## Getting Started
1. Install Vagrant and VirtualBox
2. Clone [the respository](https://github.com/colbeezy/reporting-tool)
3. Launch the Vagrant VM with `vagrant up` and log in with `vagrant ssh`
4. Load and connect to the database with `psql -d news -f newsdata.sql`
5. Create the following Views

## Running the Program

1. Create the Views below

### View 1: Articles sorted by page views
```
CREATE VIEW article_views as
    select articles.title, count (*) as views
    from articles, log
    where log.path like CONCAT('%', articles.slug, '%')
    and log.path like '%article%'
    and status = '200 OK'
    group by articles.title
    order by views desc;
```

### View 2: Articles with authors
```
CREATE VIEW articles_by_author as
    select authors.name, articles.title
    from authors, articles
    where authors.id = articles.author;
```

### View 3: Articles with authors and page views
```
CREATE VIEW views_by_author_article as
    select articles_by_author.name, article_views.title, article_views.views
    from article_views, articles_by_author
    where article_views.title = articles_by_author.title;
```

### View 4: Authors by page views
```
CREATE VIEW views_by_author as
    select name, sum(views) as views
    from views_by_author_article
    group by name
    order by views desc;
```


### View 5: Dates with page views and errors
```
CREATE VIEW status_by_date as
    select time::timestamp::date AS date, 
        count (*) as requests,
        count(case when status = '200 OK' then 1 end) as views,
        count(case when status != '200 OK' then 1 end) as errors
    from log
    group by date;
```

2. Execute the program with `python reporting_tool.py`
