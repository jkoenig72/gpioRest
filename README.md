# gpioRest
simple gpioRest service for using gpio command line commands to control orange pi / raspberry pi gpio pins via REST



sudo cp gpio_rest.service /etc/systemd/system/

sudo chmod 644 /etc/systemd/system/gpio_rest.service

sudo systemctl daemon-reload

sudo systemctl enable gpio_rest.service

sudo systemctl start gpio_rest.service
