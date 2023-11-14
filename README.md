# Django CRUD App with Django Rest Framework

This is a simple Django project demonstrating CRUD (Create, Read, Update, Delete) operations using Django Rest Framework. The project provides a RESTful API for managing items and includes CORS (Cross-Origin Resource Sharing) support for easy integration with frontend applications.

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/warrenshiv/-Django-REST-CRUD.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd Django-REST-CRUD
    ```

3. **Install dependencies:**
    - [Django](https://www.djangoproject.com/)
    - [Django Rest Framework](https://www.django-rest-framework.org/)
    - [CORS Headers](https://github.com/adamchainz/django-cors-headers)

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Start the development server:**
    ```bash
    python manage.py runserver
    ```
    The app will be accessible at [http://localhost:8000/](http://localhost:8000/).

## API Endpoints

- **List and create items:**
    - Endpoint: [http://localhost:8000/api/items/](http://localhost:8000/api/items/)
    - Methods: GET, POST

- **Retrieve, update, and delete items:**
    - Endpoint: [http://localhost:8000/api/items/<item_id>/](http://localhost:8000/api/items/<item_id>/)
    - Methods: GET, PUT, DELETE

## Technologies Used

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [CORS Headers](https://github.com/adamchainz/django-cors-headers)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
