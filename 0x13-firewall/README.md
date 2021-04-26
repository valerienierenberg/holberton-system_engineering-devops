# 0x13-firewall

## Learning Objectives
- Install firewall on our provided server and configure it as required

## File Descriptions
- 0-block_all_incoming_traffic_but - 
    - install ufw and configure it on web-01 server
    - Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
        * 22 (SSH)
        * 443 (HTTPS SSL)
        * 80 (HTTP)
    - Share the ufw commands that you used in your answer file
- 100-port_forwarding - Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP. Your answer file should be a copy of the ufw configuration file that you modified to make this happen
