### Run Project

```powershell
backend> python manage.py runserver

// Initializing DB
$ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
$ find . -path "*/migrations/*.pyc" -delete
$ rm db.sqlite3

backend> python manage.py makemigrations
backend> python manage.py migrate
backend> python manage.py createsuperuser
backend> python manage.py runserver
```

```powershell
forntend> yarn start
```



### DRF (Django REST Framework)

![image](https://user-images.githubusercontent.com/41619898/81501449-65373500-9313-11ea-8be1-482b50f68958.png)



```javascript
...

async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/api/');
            const posts = await res.json();
            this.setState({
                posts
            });
        } catch (e) {
            console.log(e);
        }
    }

...
```

