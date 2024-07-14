This application was developed with React for the frontend server and Flask for the backend server. 
In production, a proxy NGINX server is used to serve the frontend build, and GUNICORN to serve the flask app. Nginx is also used as a reverse proxy server, redirecting requests to the GUNICORN backend server. 
The machine (Linux) the servers are running on, configured to reload those servers when they stopped, or on a system reboot, ensuring Liveness of the app.


Down below there are some useful commands to modify and configure the servers:

**********
Connect to the machine (need to establish VPN connection to BGU):
ssh stud@132.73.84.52
pass:  xeGSKAqP

Basic commands:
sudo systemctl reload/stop/start/stats nginx/gunicorn

Edit NGINX � server configuration file:
sudo nano /etc/nginx/nginx.conf

Test NGINX config file after modifying:
sudo nginx -t


Edit NGINX � machine configuration file (manage how nginx reactivate after a stop):
sudo systemctl edit nginx

Edit GUNICORN � machine configuration file (manage how gunicorn reactivate after a stop):
sudo nano /etc/systemd/system/gunicorn.service

After editing machine configuration � apply them:
sudo systemctl daemon-reload


Watch NGINX error log and access log:
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/access.log

Watch gunicorn log:
sudo journalctl -u gunicorn -f (-f for real time watch)

**********


Certbot:
HTTPS certificate is installed and auto renew for this domain https://nlp-cetrification.cs.bgu.ac.il/. ,
NGINX use the certificates in the config file, 
visit certbot website for further help https://certbot.eff.org/.
