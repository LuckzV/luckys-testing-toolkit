#!/bin/bash
# Lucky's Testing Toolkit - Network Configuration Script

echo "Configuring network settings..."

# Backup original network config
cp /etc/netplan/01-netcfg.yaml /etc/netplan/01-netcfg.yaml.backup

# Create new network configuration
cat > /etc/netplan/01-netcfg.yaml << 'EOF'
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: true
      dhcp6: false
      optional: true
EOF

# Apply network configuration
netplan apply

echo "Network configuration complete!"
