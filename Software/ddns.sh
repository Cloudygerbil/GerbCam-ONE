#!/bin/bash

IP=$(curl -s https://api.ipify.org)

curl "https://dynamicdns.park-your-domain.com/update?host=@&domain=[DOMAIN_NAME_HERE&password=[PASSWORD_HERE]&ip=$IP"
