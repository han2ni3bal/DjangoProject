nohup gunicorn demoApp.wsgi:application -w 4 -k gevent -b 0.0.0.0:$1 --limit-request-field_size 32768 --timeout 300 --access-logfile /dev/stdout 2>&1 | tee /var/log/demoProject/demo.log &

nohup ./manage.py demo_heartbeat 2>&1 | tee /var/log/demoProject/demo_heartbeat.log  &
