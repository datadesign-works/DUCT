mkdir -p ../media/tmpfiles
mkdir ../media/datasets
mkdir ../logs/
touch ../logs/db.log
python ../manage.py migrate
sh run_script.sh country_load.py