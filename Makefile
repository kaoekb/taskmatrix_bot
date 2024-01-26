.PHONY: install start enable status

install:
	sudo cp taskmatrix_bot.service /etc/systemd/system/
	sudo systemctl daemon-reload

nano:
	nano .env
start:
	sudo systemctl start taskmatrix_bot

enable:
	sudo systemctl enable taskmatrix_bot

status:
	sudo systemctl status taskmatrix_bot
