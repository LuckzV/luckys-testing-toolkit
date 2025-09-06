#!/bin/bash
# Lucky's Testing Toolkit - Server Setup Script
# Generated on: 2025-09-05 20:15:11

set -e

echo "Starting server setup..."

# Update system
echo "Updating system packages..."
apt update && apt upgrade -y

# Install essential packages
echo "Installing essential packages..."
apt install -y curl wget git vim htop net-tools

# Install development tools
echo "Installing development tools..."
apt install -y build-essential python3 python3-pip nodejs npm

# Install monitoring tools
echo "Installing monitoring tools..."
apt install -y sysbench iperf3 htop iotop nethogs

# Install security tools
echo "Installing security tools..."
apt install -y ufw fail2ban

# Configure firewall
echo "Configuring firewall..."
ufw --force enable
ufw allow ssh
ufw allow 80
ufw allow 443

echo "Server setup complete!"
