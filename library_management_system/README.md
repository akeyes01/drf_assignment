Test DRF api view:

View authors:

1. Open Postman
2. Select GET method
3. Enter URL -> http://127.0.0.1:8000/api/authors/
4. Press Send button

Add an author:

1. Open Postman
2. Select POST method
3. Enter URL -> http://127.0.0.1:8000/api/authors/
4. Add new record info in Body tab
5. Press Send button

How to filter:

1. Go to Author List DRF url: http://127.0.0.1:8000/api/authors/
2. Click "Filters" button
3. Add ID or partial author name in appropriate fields
4. Click "Submit" button

How to use pagination:

1. Go to Author List DRF url: http://127.0.0.1:8000/api/authors/
2. Click page number in upper right hand corner or
3. Click "next" or "previous" link near the top of the body

How to test permissions:

1. Open Postman
2. Use the directions above to create a new author
3. Change the user by providing a new Username and Password in the "Authorization" tab
4. Change the method to "DELETE"
5. Click the "Send" button. You should receive a "403 Forbidden: You do not have permission to perform this action." error because this user is not the owner of the new record.
