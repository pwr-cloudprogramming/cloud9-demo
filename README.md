# Sample demo app: backend + frontend

How to run application:

1. Open AWS management console and switch to EC2 service.
2. Find the EC2 instance running Cloud9 environment, and select it.
3. Open **Security** tab, and click link to security group.
4. Click **Edit inbound rules** button.
5. Click **Add rule button** button, then:
   - select Type: Custom TCP
   - select Port range: 8080-8081
   - select Source: Anywhere-IPv4
6. Click **Save rules** button.
7. Open Cloud9 service.
8. In the terminal perform the following command: `python3 -m pip install flask flask-cors`
9. Change directory to backend/src folder: `cd ~/environment/cloud9-demo/backend/src`
10. Run Flask application: `python3 app.py` 
11. Open new browser tab. Type the address in the address bar: `http://<CLOUD9-PUBLIC-IP>:8080/`. Replace `<CLOUD9-PUBLIC-IP>` with the public IP address of EC2 instance.
12. In the other tab open address: `http://<CLOUD9-PUBLIC-IP>:8080/current_time` . Compare the displayed results.
13. In Cloud9 open **New Terminal** tab.
14. Change directory to backend/src folder: `cd ~/environment/cloud9-demo/frontend/src`
15. Run command `python3 -m http.server --bind 0.0.0.0 8081` to run web server serving frontend page.
16. Open new tab in the browser and open the address `http://<CLOUD9-PUBLIC-IP>:8081/`
17. Press F12 key to open Web Developer Tools in your browser.
18. Refresh few times the page. Observe how data is sent from backend to frontend.
