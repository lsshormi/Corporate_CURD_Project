
echo "Create migrations"
python manage.py makemigrations 
echo "=================================="

echo "Migrate"
python manage.py migrate
echo "=================================="

echo "Start server"
python manage.py runserver 