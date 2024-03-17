# Sample demo app: backend + frontend

How to run application:

1. Open Cloud9 service. Connect to Cloud9 environment.
2. In Cloud9 IDE, in the Bash terminal verify that you are in the folder `~/environment`, then clone this demo: `git clone https://github.com/pwr-cloudprogramming/cloud9-demo.git`
4. Open AWS management console and switch to EC2 service.
5. Find the EC2 instance running Cloud9 environment, and select it.
6. Write down the public IPv4 address of the EC2 instance.
7. Open **Security** tab, and click link to security group.
8. Click **Edit inbound rules** button.
9. Click **Add rule** button, then:
   - select Type: Custom TCP
   - select Port range: 8080-8081
   - select Source: Anywhere-IPv4
10. Click **Save rules** button.
11. Return to Cloud9 service.
12. In the terminal perform the following command: `python3 -m pip install flask flask-cors`
13. Change directory to backend/src folder: `cd ~/environment/cloud9-demo/backend/src`
14. Run Flask application: `python3 app.py` 
15. Open new browser tab. Open the address: `http://<CLOUD9-PUBLIC-IP>:8080/`. Replace `<CLOUD9-PUBLIC-IP>` with the public IP address of EC2 instance.
16. In the other tab open address: `http://<CLOUD9-PUBLIC-IP>:8080/current_time` . Compare the displayed results.
17. In Cloud9 open **New Terminal** tab. Do not close the previous tab, and do not stop Python app.
18. In new terminal, change directory to backend/src folder: `cd ~/environment/cloud9-demo/frontend/src`
19. Run command `python3 -m http.server --bind 0.0.0.0 8081` to run web server serving frontend page.
20. Open new tab in the browser and open the address `http://<CLOUD9-PUBLIC-IP>:8081/`
21. Press F12 key to open Web Developer Tools in your browser.
22. Refresh the page few times. Observe, how data is sent from backend to frontend.


## Appendix

Commands to install `docker compose` plugin in Cloud9 environment:

```
sudo mkdir -p /usr/local/lib/docker/cli-plugins

sudo curl -sL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-$(uname -m) \
  -o /usr/local/lib/docker/cli-plugins/docker-compose

sudo chown root:root /usr/local/lib/docker/cli-plugins/docker-compose
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
```
