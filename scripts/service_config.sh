#!/bin/bash
# Lucky's Testing Toolkit - Service Configuration Script

echo "Configuring system services..."

# Enable and start essential services
systemctl enable ssh
systemctl start ssh

systemctl enable fail2ban
systemctl start fail2ban

# Configure log rotation
cat > /etc/logrotate.d/toolkit << 'EOF'
/var/log/toolkit/*.log {
    daily
    missingok
    rotate 7
    compress
    notifempty
    create 644 root root
}
EOF

echo "Service configuration complete!"
