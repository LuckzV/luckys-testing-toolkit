#!/usr/bin/env python3
# server testing tool - still working on this
# TODO: add more tests

import os
import sys
import json
import time
import subprocess
import threading
import argparse
from datetime import datetime
from pathlib import Path

class Colors:
    # colors for terminal output
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    BRIGHT_RED = '\033[1;91m'
    BRIGHT_GREEN = '\033[1;92m'
    BRIGHT_YELLOW = '\033[1;93m'
    BRIGHT_BLUE = '\033[1;94m'
    BRIGHT_MAGENTA = '\033[1;95m'
    BRIGHT_CYAN = '\033[1;96m'
    BRIGHT_WHITE = '\033[1;97m'
    
    BG_RED = '\033[101m'
    BG_GREEN = '\033[102m'
    BG_YELLOW = '\033[103m'
    BG_BLUE = '\033[104m'
    BG_MAGENTA = '\033[105m'
    BG_CYAN = '\033[106m'
    
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # Reset
    RESET = '\033[0m'
    
    @staticmethod
    def colorize(text, color):
        """Apply color to text"""
        return f"{color}{text}{Colors.RESET}"
    
    @staticmethod
    def success(text):
        """Green text for success messages"""
        return Colors.colorize(text, Colors.BRIGHT_GREEN)
    
    @staticmethod
    def error(text):
        """Red text for error messages"""
        return Colors.colorize(text, Colors.BRIGHT_RED)
    
    @staticmethod
    def warning(text):
        """Yellow text for warning messages"""
        return Colors.colorize(text, Colors.BRIGHT_YELLOW)
    
    @staticmethod
    def info(text):
        """Blue text for info messages"""
        return Colors.colorize(text, Colors.BRIGHT_BLUE)
    
    @staticmethod
    def header(text):
        """Cyan text for headers"""
        return Colors.colorize(text, Colors.BRIGHT_CYAN)
    
    @staticmethod
    def highlight(text):
        """Magenta text for highlights"""
        return Colors.colorize(text, Colors.BRIGHT_MAGENTA)

class ServerTestToolkit:
    def __init__(self):
        self.version = "1.0.0"
        self.name = "Lucky's Testing Toolkit"
        self.config_file = "toolkit_config.json"
        self.results_dir = "test_results"
        self.log_file = "toolkit.log"
        
        # Initialize directories
        self.setup_directories()
        self.load_config()
        
    def setup_directories(self):
        """Create necessary directories"""
        Path(self.results_dir).mkdir(exist_ok=True)
        Path("logs").mkdir(exist_ok=True)
        Path("configs").mkdir(exist_ok=True)
        Path("scripts").mkdir(exist_ok=True)
        
    def load_config(self):
        """Load configuration from file"""
        default_config = {
            "server": {
                "host": "localhost",
                "port": 22,
                "username": "root",
                "timeout": 30
            },
            "testing": {
                "performance_duration": 300,
                "load_test_users": 100,
                "stress_test_duration": 600
            },
            "monitoring": {
                "check_interval": 60,
                "alert_thresholds": {
                    "cpu": 80,
                    "memory": 85,
                    "disk": 90
                }
            }
        }
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            except:
                self.config = default_config
        else:
            self.config = default_config
            self.save_config()
    
    def save_config(self):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def log(self, message, level="INFO"):
        """Log message to file and console"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] [{level}] {message}"
        
        print(log_message)
        with open(self.log_file, 'a') as f:
            f.write(log_message + "\n")
    
    def run_command(self, command, timeout=30):
        """Run system command with timeout"""
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=timeout
            )
            return {
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "stdout": "",
                "stderr": f"Command timed out after {timeout} seconds",
                "returncode": -1
            }
        except Exception as e:
            return {
                "success": False,
                "stdout": "",
                "stderr": str(e),
                "returncode": -1
            }
    
    def server_build_tools(self):
        """Server building and configuration tools"""
        while True:
            print("\n" + Colors.GREEN + "="*50 + Colors.RESET)
            print(Colors.header(Colors.BOLD + "SERVER BUILD TOOLS"))
            print(Colors.GREEN + "="*50 + Colors.RESET)
            print(Colors.info("1. Validate Server Configuration"))
            print(Colors.info("2. Generate Build Scripts"))
            print(Colors.info("3. Install Required Packages"))
            print(Colors.info("4. Configure System Services"))
            print(Colors.info("5. Setup Network Configuration"))
            print(Colors.info("6. Run OS Installation Script"))
            print(Colors.error("7. Back to Main Menu"))
            
            choice = input(Colors.highlight("\nSelect option (1-7): ")).strip()
            
            if choice == "1":
                self.validate_server_config()
            elif choice == "2":
                self.generate_build_scripts()
            elif choice == "3":
                self.install_packages()
            elif choice == "4":
                self.configure_services()
            elif choice == "5":
                self.setup_network()
            elif choice == "6":
                self.run_os_installation()
            elif choice == "7":
                break
            else:
                print("Invalid option. Please try again.")
    
    def testing_suite(self):
        """Comprehensive testing suite"""
        while True:
            print("\n" + Colors.YELLOW + "="*50 + Colors.RESET)
            print(Colors.header(Colors.BOLD + "TESTING SUITE"))
            print(Colors.YELLOW + "="*50 + Colors.RESET)
            print(Colors.info("1. Server Health Check"))
            print(Colors.info("2. Performance Benchmark"))
            print(Colors.info("3. Load Testing"))
            print(Colors.info("4. Stress Testing"))
            print(Colors.info("5. Network Connectivity Test"))
            print(Colors.info("6. Security Scan"))
            print(Colors.info("7. Compatibility Test"))
            print(Colors.warning("8. Run Full Test Suite"))
            print(Colors.error("9. Back to Main Menu"))
            
            choice = input(Colors.highlight("\nSelect option (1-9): ")).strip()
            
            if choice == "1":
                self.server_health_check()
            elif choice == "2":
                self.performance_benchmark()
            elif choice == "3":
                self.load_testing()
            elif choice == "4":
                self.stress_testing()
            elif choice == "5":
                self.network_connectivity_test()
            elif choice == "6":
                self.security_scan()
            elif choice == "7":
                self.compatibility_test()
            elif choice == "8":
                self.run_full_test_suite()
            elif choice == "9":
                break
            else:
                print("Invalid option. Please try again.")
    
    def monitoring_tools(self):
        """Real-time monitoring and alerting"""
        while True:
            print("\n" + Colors.MAGENTA + "="*50 + Colors.RESET)
            print(Colors.header(Colors.BOLD + "MONITORING TOOLS"))
            print(Colors.MAGENTA + "="*50 + Colors.RESET)
            print(Colors.info("1. Real-time System Monitor"))
            print(Colors.info("2. Service Availability Check"))
            print(Colors.info("3. Performance Monitoring"))
            print(Colors.info("4. Log Analysis"))
            print(Colors.info("5. Alert Configuration"))
            print(Colors.info("6. Generate Monitoring Report"))
            print(Colors.error("7. Back to Main Menu"))
            
            choice = input(Colors.highlight("\nSelect option (1-7): ")).strip()
            
            if choice == "1":
                self.real_time_monitor()
            elif choice == "2":
                self.service_availability_check()
            elif choice == "3":
                self.performance_monitoring()
            elif choice == "4":
                self.log_analysis()
            elif choice == "5":
                self.alert_configuration()
            elif choice == "6":
                self.generate_monitoring_report()
            elif choice == "7":
                break
            else:
                print("Invalid option. Please try again.")
    
    def reporting_tools(self):
        """Reporting and analytics"""
        while True:
            print("\n" + Colors.BLUE + "="*50 + Colors.RESET)
            print(Colors.header(Colors.BOLD + "REPORTING TOOLS"))
            print(Colors.BLUE + "="*50 + Colors.RESET)
            print(Colors.info("1. Generate Test Report"))
            print(Colors.info("2. Performance Analysis"))
            print(Colors.info("3. Trend Analysis"))
            print(Colors.info("4. Compliance Report"))
            print(Colors.info("5. Executive Summary"))
            print(Colors.info("6. Export Results"))
            print(Colors.error("7. Back to Main Menu"))
            
            choice = input(Colors.highlight("\nSelect option (1-7): ")).strip()
            
            if choice == "1":
                self.generate_test_report()
            elif choice == "2":
                self.performance_analysis()
            elif choice == "3":
                self.trend_analysis()
            elif choice == "4":
                self.compliance_report()
            elif choice == "5":
                self.executive_summary()
            elif choice == "6":
                self.export_results()
            elif choice == "7":
                break
            else:
                print("Invalid option. Please try again.")
    
    def validate_server_config(self):
        """Validate server configuration"""
        print("\nValidating server configuration...")
        
        checks = [
            ("System Information", "uname -a"),
            ("CPU Information", "lscpu"),
            ("Memory Information", "free -h"),
            ("Disk Information", "df -h"),
            ("Network Interfaces", "ip addr show"),
            ("Running Services", "systemctl list-units --type=service --state=running"),
            ("Open Ports", "ss -tuln"),
            ("System Load", "uptime")
        ]
        
        results = {}
        for check_name, command in checks:
            print(f"  Running: {check_name}")
            result = self.run_command(command)
            results[check_name] = result
            
            if result["success"]:
                print(f"    {Colors.success('✓')} {check_name}: {Colors.success('OK')}")
            else:
                print(f"    {Colors.error('✗')} {check_name}: {Colors.error('FAILED')} - {result['stderr']}")
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        result_file = f"{self.results_dir}/config_validation_{timestamp}.json"
        with open(result_file, 'w') as f:
            json.dump(results, f, indent=4)
        
        print(f"\nConfiguration validation complete. Results saved to: {result_file}")
    
    def server_health_check(self):
        """Comprehensive server health check"""
        print("\nRunning server health check...")
        
        health_checks = {
            "CPU Usage": "top -bn1 | grep 'Cpu(s)' | awk '{print $2}' | cut -d'%' -f1",
            "Memory Usage": "free | grep Mem | awk '{printf \"%.1f\", $3/$2 * 100.0}'",
            "Disk Usage": "df -h | awk '$NF==\"/\"{printf \"%s\", $5}'",
            "Load Average": "uptime | awk -F'load average:' '{print $2}'",
            "Uptime": "uptime -p",
            "Active Connections": "ss -tuln | wc -l",
            "Zombie Processes": "ps aux | awk '$8 ~ /^Z/ { print $2 }' | wc -l"
        }
        
        results = {}
        for check_name, command in health_checks:
            result = self.run_command(command)
            results[check_name] = {
                "command": command,
                "output": result["stdout"].strip(),
                "success": result["success"]
            }
            
            if result["success"]:
                print(f"  {Colors.success('✓')} {check_name}: {Colors.success(result['stdout'].strip())}")
            else:
                print(f"  {Colors.error('✗')} {check_name}: {Colors.error(result['stdout'].strip())}")
        
        # Save health check results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        result_file = f"{self.results_dir}/health_check_{timestamp}.json"
        with open(result_file, 'w') as f:
            json.dump(results, f, indent=4)
        
        print(f"\nHealth check complete. Results saved to: {result_file}")
    
    def performance_benchmark(self):
        """Run performance benchmarks"""
        print("\nRunning performance benchmarks...")
        
        benchmarks = {
            "CPU Benchmark": "sysbench cpu --cpu-max-prime=20000 run",
            "Memory Benchmark": "sysbench memory --memory-total-size=1G run",
            "Disk I/O Benchmark": "sysbench fileio --file-total-size=1G --file-test-mode=rndrw run",
            "Network Speed Test": "iperf3 -c localhost -t 10"
        }
        
        results = {}
        for bench_name, command in benchmarks:
            print(f"  Running: {bench_name}")
            result = self.run_command(command, timeout=300)
            results[bench_name] = {
                "command": command,
                "success": result["success"],
                "output": result["stdout"],
                "error": result["stderr"]
            }
            
            if result["success"]:
                print(f"    ✓ {bench_name}: Completed")
            else:
                print(f"    ✗ {bench_name}: Failed - {result['stderr']}")
        
        # Save benchmark results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        result_file = f"{self.results_dir}/performance_benchmark_{timestamp}.json"
        with open(result_file, 'w') as f:
            json.dump(results, f, indent=4)
        
        print(f"\nPerformance benchmark complete. Results saved to: {result_file}")
    
    def run_full_test_suite(self):
        """Run all tests in sequence"""
        print("\nRunning full test suite...")
        print("This may take several minutes...")
        
        start_time = time.time()
        
        # Run all tests
        self.server_health_check()
        self.performance_benchmark()
        self.network_connectivity_test()
        self.security_scan()
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"\nFull test suite completed in {duration:.2f} seconds")
        print("All results saved to the test_results directory")
    
    def generate_build_scripts(self):
        """Generate automated build scripts"""
        print("\nGenerating build scripts...")
        
        scripts = {
            "server_setup.sh": """#!/bin/bash
# Lucky's Testing Toolkit - Server Setup Script
# Generated on: {timestamp}

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
""",
            
            "service_config.sh": """#!/bin/bash
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
""",
            
            "network_config.sh": """#!/bin/bash
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
"""
        }
        
        # Generate scripts with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        for script_name, script_content in scripts.items():
            script_path = f"scripts/{script_name}"
            with open(script_path, 'w') as f:
                # Only format the first script that has timestamp placeholder
                if script_name == "server_setup.sh":
                    f.write(script_content.format(timestamp=timestamp))
                else:
                    f.write(script_content)
            
            # Make executable
            os.chmod(script_path, 0o755)
            print(f"  {Colors.success('✓')} Generated: {Colors.highlight(script_path)}")
        
        print(f"\n{Colors.success('Build scripts generated successfully!')}")
        print(Colors.info("Scripts are ready to run on your target server."))
    
    def install_packages(self):
        """Install required packages"""
        print("\nInstalling packages...")
        
        # Define package categories
        packages = {
            "Essential Tools": ["curl", "wget", "git", "vim", "htop", "tree", "unzip"],
            "Development": ["build-essential", "python3", "python3-pip", "nodejs", "npm"],
            "Monitoring": ["sysbench", "iperf3", "iotop", "nethogs", "ncdu"],
            "Security": ["ufw", "fail2ban", "nmap", "nmap-common"],
            "Network": ["net-tools", "dnsutils", "traceroute", "mtr-tiny"],
            "System": ["htop", "iotop", "lsof", "strace", "tcpdump"]
        }
        
        print("Available package categories:")
        for i, category in enumerate(packages.keys(), 1):
            print(f"  {i}. {category}")
        
        try:
            choice = input("\nSelect category to install (1-6) or 'all' for everything: ").strip()
            
            if choice.lower() == 'all':
                # Install all packages
                all_packages = []
                for category_packages in packages.values():
                    all_packages.extend(category_packages)
                
                print(f"\nInstalling {len(all_packages)} packages...")
                self._install_package_list(all_packages)
                
            elif choice.isdigit() and 1 <= int(choice) <= len(packages):
                # Install specific category
                category_name = list(packages.keys())[int(choice) - 1]
                category_packages = packages[category_name]
                
                print(f"\nInstalling {category_name} packages...")
                self._install_package_list(category_packages)
                
            else:
                print("Invalid choice. Returning to menu.")
                return
                
        except KeyboardInterrupt:
            print("\nInstallation cancelled.")
        except Exception as e:
            print(f"Error during installation: {e}")
    
    def _install_package_list(self, packages):
        """Install a list of packages"""
        for package in packages:
            print(f"  Installing {package}...")
            result = self.run_command(f"apt install -y {package}", timeout=120)
            
            if result["success"]:
                print(f"    {Colors.success('✓')} {package} {Colors.success('installed successfully')}")
            else:
                print(f"    {Colors.error('✗')} {package} {Colors.error('failed to install')}: {result['stderr']}")
        
        print(f"\n{Colors.success('Package installation complete!')}")
    
    def configure_services(self):
        """Configure system services"""
        print("\nConfiguring services...")
        print("This feature will configure system services.")
        print("Implementation coming soon!")
    
    def setup_network(self):
        """Setup network configuration"""
        print("\nSetting up network...")
        print("This feature will configure network settings.")
        print("Implementation coming soon!")
    
    def run_os_installation(self):
        """Run OS installation script"""
        print("\nRunning OS installation...")
        print("This feature will run automated OS installation.")
        print("Implementation coming soon!")
    
    def load_testing(self):
        """Run load testing"""
        print("\nRunning load testing...")
        print("This feature will perform load testing on the server.")
        print("Implementation coming soon!")
    
    def stress_testing(self):
        """Run stress testing"""
        print("\nRunning stress testing...")
        print("This feature will perform stress testing on the server.")
        print("Implementation coming soon!")
    
    def network_connectivity_test(self):
        """Test network connectivity"""
        print("\nTesting network connectivity...")
        
        # Test targets
        test_targets = [
            ("Google DNS", "8.8.8.8"),
            ("Cloudflare DNS", "1.1.1.1"),
            ("Google", "google.com"),
            ("GitHub", "github.com"),
            ("Local Gateway", "192.168.1.1")
        ]
        
        results = {}
        
        for name, target in test_targets:
            print(f"  Testing {name} ({target})...")
            
            # Ping test
            ping_result = self.run_command(f"ping -c 3 -W 2 {target}", timeout=10)
            
            # DNS resolution test
            dns_result = self.run_command(f"nslookup {target}", timeout=5)
            
            # Port connectivity test (if it's an IP)
            port_result = None
            if target.replace('.', '').isdigit():
                port_result = self.run_command(f"nc -z -v {target} 80 443 22", timeout=5)
            
            results[name] = {
                "target": target,
                "ping": ping_result["success"],
                "dns": dns_result["success"],
                "ports": port_result["success"] if port_result else "N/A",
                "ping_output": ping_result["stdout"],
                "dns_output": dns_result["stdout"]
            }
            
            # Display results
            status = "✓" if ping_result["success"] else "✗"
            print(f"    {status} Ping: {'OK' if ping_result['success'] else 'FAILED'}")
            
            if dns_result["success"]:
                print(f"    ✓ DNS Resolution: OK")
            else:
                print(f"    ✗ DNS Resolution: FAILED")
        
        # Test local network
        print("\n  Testing local network...")
        local_scan = self.run_command("nmap -sn 192.168.1.0/24", timeout=30)
        if local_scan["success"]:
            print("    ✓ Local network scan completed")
        else:
            print("    ✗ Local network scan failed")
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        result_file = f"{self.results_dir}/network_test_{timestamp}.json"
        with open(result_file, 'w') as f:
            json.dump(results, f, indent=4)
        
        print(f"\nNetwork connectivity test complete. Results saved to: {result_file}")
    
    def security_scan(self):
        """Run security scan"""
        print("\nRunning security scan...")
        
        security_checks = {
            "Open Ports": "nmap -sS -O localhost",
            "SSH Configuration": "sshd -T",
            "Firewall Status": "ufw status verbose",
            "Failed Login Attempts": "grep 'Failed password' /var/log/auth.log | tail -10",
            "Sudo Usage": "grep 'sudo:' /var/log/auth.log | tail -5",
            "System Updates": "apt list --upgradable",
            "Running Services": "systemctl list-units --type=service --state=running",
            "File Permissions": "find /etc -type f -perm /o+w 2>/dev/null | head -10",
            "SUID Files": "find / -perm -4000 2>/dev/null | head -10",
            "World Writable Files": "find / -type f -perm -002 2>/dev/null | head -10"
        }
        
        results = {}
        
        for check_name, command in security_checks.items():
            print(f"  Running: {check_name}")
            result = self.run_command(command, timeout=30)
            
            results[check_name] = {
                "command": command,
                "success": result["success"],
                "output": result["stdout"],
                "error": result["stderr"]
            }
            
            if result["success"]:
                print(f"    ✓ {check_name}: Completed")
                # Show first few lines of output
                lines = result["stdout"].split('\n')[:3]
                for line in lines:
                    if line.strip():
                        print(f"      {line.strip()}")
            else:
                print(f"    ✗ {check_name}: Failed")
        
        # Additional security checks
        print("\n  Running additional security checks...")
        
        # Check for common vulnerabilities
        vuln_checks = {
            "Weak Passwords": "grep -E 'password.*[0-9]{1,3}$' /etc/passwd",
            "Empty Passwords": "awk -F: '($2 == \"\") {print $1}' /etc/shadow",
            "Root Login": "grep '^PermitRootLogin' /etc/ssh/sshd_config",
            "Password Auth": "grep '^PasswordAuthentication' /etc/ssh/sshd_config"
        }
        
        for vuln_name, vuln_command in vuln_checks.items():
            vuln_result = self.run_command(vuln_command, timeout=10)
            results[f"Vulnerability_{vuln_name}"] = {
                "command": vuln_command,
                "success": vuln_result["success"],
                "output": vuln_result["stdout"],
                "error": vuln_result["stderr"]
            }
            
            if vuln_result["success"] and vuln_result["stdout"].strip():
                print(f"    ⚠ {vuln_name}: Potential issue found")
            else:
                print(f"    ✓ {vuln_name}: No issues found")
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        result_file = f"{self.results_dir}/security_scan_{timestamp}.json"
        with open(result_file, 'w') as f:
            json.dump(results, f, indent=4)
        
        print(f"\nSecurity scan complete. Results saved to: {result_file}")
        print("Review the results for potential security issues.")
    
    def compatibility_test(self):
        """Run compatibility test"""
        print("\nRunning compatibility test...")
        print("This feature will test hardware/software compatibility.")
        print("Implementation coming soon!")
    
    def real_time_monitor(self):
        """Real-time system monitor"""
        print("\nStarting real-time monitor...")
        print("Press Ctrl+C to stop monitoring")
        
        try:
            import psutil
        except ImportError:
            print("psutil not available. Installing...")
            result = self.run_command("pip3 install psutil")
            if not result["success"]:
                print("Failed to install psutil. Using basic monitoring.")
                self._basic_monitor()
                return
        
        try:
            while True:
                # Clear screen (works on most terminals)
                os.system('clear' if os.name == 'posix' else 'cls')
                
                print(Colors.CYAN + "=" * 60 + Colors.RESET)
                print(Colors.header(Colors.BOLD + "LUCKY'S TESTING TOOLKIT - REAL-TIME MONITOR"))
                print(Colors.CYAN + "=" * 60 + Colors.RESET)
                print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print()
                
                # CPU Usage
                cpu_percent = psutil.cpu_percent(interval=1)
                print(f"CPU Usage: {cpu_percent}%")
                
                # Memory Usage
                memory = psutil.virtual_memory()
                print(f"Memory Usage: {memory.percent}% ({memory.used // (1024**3)}GB / {memory.total // (1024**3)}GB)")
                
                # Disk Usage
                disk = psutil.disk_usage('/')
                print(f"Disk Usage: {disk.percent}% ({disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB)")
                
                # Load Average
                load_avg = psutil.getloadavg()
                print(f"Load Average: {load_avg[0]:.2f}, {load_avg[1]:.2f}, {load_avg[2]:.2f}")
                
                # Network I/O
                net_io = psutil.net_io_counters()
                print(f"Network: RX {net_io.bytes_recv // (1024**2)}MB, TX {net_io.bytes_sent // (1024**2)}MB")
                
                # Running Processes
                processes = psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])
                print(f"\nTop 5 Processes by CPU:")
                sorted_procs = sorted(processes, key=lambda x: x.info['cpu_percent'] or 0, reverse=True)[:5]
                for proc in sorted_procs:
                    print(f"  {proc.info['name']}: {proc.info['cpu_percent']:.1f}% CPU, {proc.info['memory_percent']:.1f}% RAM")
                
                print("\nPress Ctrl+C to stop...")
                time.sleep(2)
                
        except KeyboardInterrupt:
            print("\n\nMonitoring stopped.")
        except Exception as e:
            print(f"\nError during monitoring: {e}")
    
    def _basic_monitor(self):
        """Basic monitoring without psutil"""
        try:
            while True:
                os.system('clear' if os.name == 'posix' else 'cls')
                
                print(Colors.CYAN + "=" * 60 + Colors.RESET)
                print(Colors.header(Colors.BOLD + "LUCKY'S TESTING TOOLKIT - BASIC MONITOR"))
                print(Colors.CYAN + "=" * 60 + Colors.RESET)
                print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print()
                
                # Basic system info
                uptime_result = self.run_command("uptime")
                if uptime_result["success"]:
                    print(f"Uptime: {uptime_result['stdout'].strip()}")
                
                # Memory info
                mem_result = self.run_command("free -h")
                if mem_result["success"]:
                    print(f"\nMemory:\n{mem_result['stdout']}")
                
                # Disk info
                disk_result = self.run_command("df -h")
                if disk_result["success"]:
                    print(f"\nDisk Usage:\n{disk_result['stdout']}")
                
                print("\nPress Ctrl+C to stop...")
                time.sleep(5)
                
        except KeyboardInterrupt:
            print("\n\nMonitoring stopped.")
    
    def service_availability_check(self):
        """Check service availability"""
        print("\nChecking service availability...")
        print("This feature will check service uptime.")
        print("Implementation coming soon!")
    
    def performance_monitoring(self):
        """Performance monitoring"""
        print("\nStarting performance monitoring...")
        print("This feature will monitor system performance.")
        print("Implementation coming soon!")
    
    def log_analysis(self):
        """Log analysis"""
        print("\nAnalyzing logs...")
        print("This feature will analyze system logs.")
        print("Implementation coming soon!")
    
    def alert_configuration(self):
        """Alert configuration"""
        print("\nConfiguring alerts...")
        print("This feature will set up alerting.")
        print("Implementation coming soon!")
    
    def generate_monitoring_report(self):
        """Generate monitoring report"""
        print("\nGenerating monitoring report...")
        print("This feature will generate monitoring reports.")
        print("Implementation coming soon!")
    
    def generate_test_report(self):
        """Generate test report"""
        print("\nGenerating test report...")
        
        # Find all result files
        result_files = []
        if os.path.exists(self.results_dir):
            for file in os.listdir(self.results_dir):
                if file.endswith('.json'):
                    result_files.append(os.path.join(self.results_dir, file))
        
        if not result_files:
            print("No test results found. Run some tests first!")
            return
        
        # Generate comprehensive report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"{self.results_dir}/comprehensive_report_{timestamp}.html"
        
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Lucky's Testing Toolkit - Test Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .header {{ background: #2c3e50; color: white; padding: 20px; border-radius: 5px; }}
        .section {{ margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }}
        .success {{ color: #27ae60; }}
        .error {{ color: #e74c3c; }}
        .warning {{ color: #f39c12; }}
        pre {{ background: #f8f9fa; padding: 10px; border-radius: 3px; overflow-x: auto; }}
        .summary {{ background: #ecf0f1; padding: 15px; border-radius: 5px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Lucky's Testing Toolkit - Test Report</h1>
        <p>Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>Toolkit Version: {self.version}</p>
    </div>
    
    <div class="summary">
        <h2>Report Summary</h2>
        <p>Total result files analyzed: {len(result_files)}</p>
        <p>Report generated from: {self.results_dir}</p>
    </div>
"""
        
        # Process each result file
        for result_file in result_files:
            try:
                with open(result_file, 'r') as f:
                    data = json.load(f)
                
                filename = os.path.basename(result_file)
                html_content += f"""
    <div class="section">
        <h3>{filename}</h3>
        <pre>{json.dumps(data, indent=2)}</pre>
    </div>
"""
            except Exception as e:
                html_content += f"""
    <div class="section">
        <h3>{filename} - Error</h3>
        <p class="error">Failed to process: {str(e)}</p>
    </div>
"""
        
        html_content += """
    <div class="section">
        <h2>End of Report</h2>
        <p>This report was generated by Lucky's Testing Toolkit.</p>
    </div>
</body>
</html>
"""
        
        # Write HTML report
        with open(report_file, 'w') as f:
            f.write(html_content)
        
        print(f"✓ Comprehensive test report generated: {report_file}")
        
        # Also generate a simple text report
        text_report_file = f"{self.results_dir}/test_summary_{timestamp}.txt"
        with open(text_report_file, 'w') as f:
            f.write(f"Lucky's Testing Toolkit - Test Summary\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Version: {self.version}\n")
            f.write("=" * 50 + "\n\n")
            
            for result_file in result_files:
                f.write(f"File: {os.path.basename(result_file)}\n")
                f.write("-" * 30 + "\n")
                try:
                    with open(result_file, 'r') as rf:
                        data = json.load(rf)
                    f.write(json.dumps(data, indent=2))
                except Exception as e:
                    f.write(f"Error reading file: {e}")
                f.write("\n\n")
        
        print(f"✓ Text summary generated: {text_report_file}")
        print(f"\nReports saved to: {self.results_dir}")
    
    def performance_analysis(self):
        """Performance analysis"""
        print("\nAnalyzing performance...")
        print("This feature will analyze performance data.")
        print("Implementation coming soon!")
    
    def trend_analysis(self):
        """Trend analysis"""
        print("\nAnalyzing trends...")
        print("This feature will analyze performance trends.")
        print("Implementation coming soon!")
    
    def compliance_report(self):
        """Compliance report"""
        print("\nGenerating compliance report...")
        print("This feature will generate compliance reports.")
        print("Implementation coming soon!")
    
    def executive_summary(self):
        """Executive summary"""
        print("\nGenerating executive summary...")
        print("This feature will generate executive summaries.")
        print("Implementation coming soon!")
    
    def export_results(self):
        """Export results"""
        print("\nExporting results...")
        print("This feature will export test results.")
        print("Implementation coming soon!")
    
    def view_configuration(self):
        """View current configuration"""
        print("\nCurrent Configuration:")
        print(json.dumps(self.config, indent=4))
    
    def edit_server_settings(self):
        """Edit server settings"""
        print("\nEdit server settings...")
        print("This feature will allow editing server settings.")
        print("Implementation coming soon!")
    
    def edit_testing_settings(self):
        """Edit testing settings"""
        print("\nEdit testing settings...")
        print("This feature will allow editing testing settings.")
        print("Implementation coming soon!")
    
    def edit_monitoring_settings(self):
        """Edit monitoring settings"""
        print("\nEdit monitoring settings...")
        print("This feature will allow editing monitoring settings.")
        print("Implementation coming soon!")
    
    def reset_to_defaults(self):
        """Reset to defaults"""
        print("\nResetting to defaults...")
        self.config = {
            "server": {"host": "localhost", "port": 22, "username": "root", "timeout": 30},
            "testing": {"performance_duration": 300, "load_test_users": 100, "stress_test_duration": 600},
            "monitoring": {"check_interval": 60, "alert_thresholds": {"cpu": 80, "memory": 85, "disk": 90}}
        }
        self.save_config()
        print("Configuration reset to defaults!")
    
    def main_menu(self):
        """Main menu interface"""
        while True:
            print("\n" + Colors.CYAN + "="*60 + Colors.RESET)
            print(Colors.header(Colors.BOLD + self.name.upper() + " v" + self.version))
            print(Colors.CYAN + "="*60 + Colors.RESET)
            print(Colors.info("1. Server Build Tools"))
            print(Colors.info("2. Testing Suite"))
            print(Colors.info("3. Monitoring Tools"))
            print(Colors.info("4. Reporting Tools"))
            print(Colors.info("5. Configuration"))
            print(Colors.info("6. About"))
            print(Colors.error("7. Exit"))
            
            choice = input(Colors.highlight("\nSelect option (1-7): ")).strip()
            
            if choice == "1":
                self.server_build_tools()
            elif choice == "2":
                self.testing_suite()
            elif choice == "3":
                self.monitoring_tools()
            elif choice == "4":
                self.reporting_tools()
            elif choice == "5":
                self.configuration_menu()
            elif choice == "6":
                self.show_about()
            elif choice == "7":
                print("\nGoodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    
    def configuration_menu(self):
        """Configuration management"""
        while True:
            print("\n" + "="*50)
            print("CONFIGURATION")
            print("="*50)
            print("1. View Current Configuration")
            print("2. Edit Server Settings")
            print("3. Edit Testing Settings")
            print("4. Edit Monitoring Settings")
            print("5. Reset to Defaults")
            print("6. Back to Main Menu")
            
            choice = input("\nSelect option (1-6): ").strip()
            
            if choice == "1":
                self.view_configuration()
            elif choice == "2":
                self.edit_server_settings()
            elif choice == "3":
                self.edit_testing_settings()
            elif choice == "4":
                self.edit_monitoring_settings()
            elif choice == "5":
                self.reset_to_defaults()
            elif choice == "6":
                break
            else:
                print("Invalid option. Please try again.")
    
    def show_about(self):
        """Show about information"""
        print("\n" + "="*60)
        print(self.name.upper())
        print("="*60)
        print(f"Version: {self.version}")
        print("Author: Lucky")
        print("Description: Comprehensive tool for server building, testing, and monitoring")
        print("\nFeatures:")
        print("- Server configuration and build tools")
        print("- Comprehensive testing suite")
        print("- Real-time monitoring and alerting")
        print("- Detailed reporting and analytics")
        print("- Portable and easy to use")
        print("\nThis tool is designed to run from a USB drive on any Linux system.")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Server Test Engineer Toolkit")
    parser.add_argument("--config", help="Configuration file path")
    parser.add_argument("--log-level", choices=["DEBUG", "INFO", "WARNING", "ERROR"], 
                       default="INFO", help="Log level")
    
    args = parser.parse_args()
    
    # Create toolkit instance
    toolkit = ServerTestToolkit()
    
    # Set log level
    if args.log_level:
        toolkit.log_level = args.log_level
    
    # Load custom config if provided
    if args.config:
        toolkit.config_file = args.config
        toolkit.load_config()
    
    # Start main menu
    toolkit.main_menu()

if __name__ == "__main__":
    main()
