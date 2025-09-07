# Lucky's Testing Toolkit

A comprehensive, portable tool for server building, testing, and monitoring designed for test engineers.

## Features

### 🏗️ Server Build Tools
- **Server Configuration Validation** - Validate system configuration
- **Build Script Generation** - Create automated build scripts
- **Package Installation** - Install required packages automatically
- **Service Configuration** - Configure system services
- **Network Setup** - Configure network interfaces
- **OS Installation** - Automated OS installation scripts

### 🧪 Testing Suite
- **Server Health Check** - Comprehensive health monitoring
- **Performance Benchmark** - CPU, memory, disk, network tests
- **Load Testing** - Simulate high load conditions
- **Stress Testing** - Push server to limits
- **Network Connectivity** - Test all network connections
- **Security Scan** - Scan for vulnerabilities
- **Compatibility Test** - Test hardware/software compatibility
- **Full Test Suite** - Run all tests in sequence

### Monitoring Tools
- **Real-time Monitor** - Live system monitoring
- **Service Availability** - Monitor service uptime
- **Performance Monitoring** - Track system performance
- **Log Analysis** - Analyze system logs
- **Alert Configuration** - Set up custom alerts
- **Monitoring Reports** - Generate monitoring reports

### 📈 Reporting Tools
- **Test Reports** - Generate detailed test reports
- **Performance Analysis** - Analyze performance data
- **Trend Analysis** - Track performance trends
- **Compliance Reports** - Generate compliance reports
- **Executive Summary** - High-level summaries
- **Export Results** - Export data in various formats

## Installation

### Quick Start (Linux)
```bash
# Make installation script executable
chmod +x install.sh

# Run installation
./install.sh

# Start the toolkit
./server_test_toolkit.py
```

### Manual Installation
```bash
# Create virtual environment
python3 -m venv toolkit_env
source toolkit_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x server_test_toolkit.py

# Run toolkit
./server_test_toolkit.py
```

## Usage

### Basic Usage
```bash
# Run with default settings
./server_test_toolkit.py

# Run with custom config
./server_test_toolkit.py --config my_config.json

# Run with debug logging
./server_test_toolkit.py --log-level DEBUG
```

### Menu Navigation
The toolkit provides an intuitive menu-driven interface:

1. **Server Build Tools** - Configure and build servers
2. **Testing Suite** - Run comprehensive tests
3. **Monitoring Tools** - Monitor system health
4. **Reporting Tools** - Generate reports and analytics
5. **Configuration** - Manage toolkit settings

## Configuration

The toolkit uses a JSON configuration file (`toolkit_config.json`) with the following structure:

```json
{
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
```

## Portable Usage

This toolkit is designed to run from a USB drive on any Linux system:

1. **Copy the entire folder** to your USB drive
2. **Insert USB drive** into any Linux system
3. **Navigate to the folder** and run `./install.sh`
4. **Start using** the toolkit immediately

## Requirements

- **Python 3.6+**
- **Linux operating system**
- **Root/sudo access** (for some operations)
- **Internet connection** (for package installation)

## Dependencies

- `psutil` - System and process utilities
- `requests` - HTTP library
- `paramiko` - SSH client library
- `netifaces` - Network interface information
- `python-nmap` - Network scanner

## File Structure

```
server-test-toolkit/
├── server_test_toolkit.py    # Main application
├── requirements.txt          # Python dependencies
├── install.sh               # Installation script
├── README.md                # This file
├── toolkit_config.json      # Configuration file
├── test_results/            # Test results directory
├── logs/                    # Log files
├── configs/                 # Configuration files
└── scripts/                 # Generated scripts
```

## Examples

### Run Server Health Check
```bash
./server_test_toolkit.py
# Select: 2. Testing Suite
# Select: 1. Server Health Check
```

### Generate Performance Report
```bash
./server_test_toolkit.py
# Select: 2. Testing Suite
# Select: 2. Performance Benchmark
# Select: 4. Reporting Tools
# Select: 1. Generate Test Report
```

### Monitor System in Real-time
```bash
./server_test_toolkit.py
# Select: 3. Monitoring Tools
# Select: 1. Real-time System Monitor
```

## Troubleshooting

### Permission Issues
```bash
# Make sure the script is executable
chmod +x server_test_toolkit.py

# Run with appropriate permissions
sudo ./server_test_toolkit.py
```

### Missing Dependencies
```bash
# Install missing packages
pip install -r requirements.txt

# Or install individually
pip install psutil requests paramiko
```

### Configuration Issues
```bash
# Reset to default configuration
rm toolkit_config.json
./server_test_toolkit.py
```

## Contributing

This toolkit is designed to be easily extensible. To add new features:

1. **Add new methods** to the `ServerTestToolkit` class
2. **Update menu options** in the respective menu methods
3. **Add configuration options** to the config structure
4. **Test thoroughly** on different Linux distributions

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or contributions, please refer to the project documentation or create an issue in the project repository.
