# Certbot 

Certbot is used to generate valid certificates for free.
Before using it, certbot needs to be installed on your system. For instructions depending on the distribution check the official website

## Requirements

In order for Certbot to generate certificate, port 80 must be ether available or it must host a valid website

## Regular certificates

Run 
```
sudo certbot certonly --standalone
```
or
```
sudo certbot certonly --webroot
```
Depending if you have or haven't got a website already running on port 80 and follow the on screen instructionsa.   


## Wildcard certificates

Before generating this kind of certificate you must be sure that you have access to DNS hosting of this domain
Generate cert with the following command:
```
sudo /usr/local/bin/certbot-auto certonly --manual --preferred-challenges=dns --email <email> -d *.<domain> --agree-tos --manual-public-ip-logging-ok
```
eg.
```
sudo /usr/local/bin/certbot-auto certonly --manual --preferred-challenges=dns --email branislav.knezevic@devtechgroup.com -d *.acronistap.devtech-labs.com --agree-tos --manual-public-ip-logging-ok
```

This will initiate certificate creation but it will require a `txt` record to be added to the DNS hosting.
Make sure to remove the domian part and just add the required record.

Once the certificate is crated it will be shown where the certificate is stored, it will most probably be `/etc/letsencrypt/live/<domain>`
Copy the certificate over to the desired machine via `rsync` or some other platrom and install/implement it as needed.
Permisions on the private key might need to be changed before making a copy and once the copying is done (from 600 to something else and then back to 600)

## Resources

https://certbot.eff.org/
