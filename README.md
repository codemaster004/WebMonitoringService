# Small Project for Monitoring PC components Prices

## Set Up for dev environment
### Step 1: Download Geckodriver for Firefox Automation

1. **Go to the Geckodriver Releases Page**: Visit [Geckodriver Releases](https://github.com/mozilla/geckodriver/releases) on GitHub.
2. **Download the Appropriate Version**:
   - **For Windows**: Download the `.zip` file for Windows (e.g., `geckodriver-vX.XX.XX-win64.zip` for 64-bit Windows).
   - **For macOS**: Download the `.tar.gz` file for macOS (e.g., `geckodriver-vX.XX.XX-macos.tar.gz`).

### Step 2: Install the Driver

**For Windows:**

1. **Unzip the Downloaded File:**
   - Extract the contents of the `.zip` file you downloaded. You should get a file called `geckodriver.exe`.
2. **Move the `geckodriver.exe` to a Safe Location:**
   - Move the `geckodriver.exe` to a folder where it can be easily accessed (e.g., `C:\Program Files\Geckodriver\`).
3. **Add Geckodriver to System PATH:**
   - Right-click on "This PC" or "My Computer" and select "Properties."
   - Click on "Advanced system settings" (on the left).
   - Click on "Environment Variables."
   - Under "System variables," find the `Path` variable, select it, and click "Edit."
   - Click "New" and add the path to the folder where you placed `geckodriver.exe` (e.g., `C:\Program Files\Geckodriver\`).
   - Click "OK" on all windows to save changes.
4. **Verify Installation:**
   - Open a command prompt (cmd) and type:
   ```bash
   geckodriver --version
   ```
   - If installed correctly, you should see the Geckodriver version information.

**For macOS:**

1. **Extract the `tar.gz` File:**
   - Open the Terminal, navigate to the folder where you downloaded the `.tar.gz` file, and run:
   ```bash
   tar -xvzf geckodriver-vX.XX.XX-macos.tar.gz
   ```
   - This will extract the `geckodriver` executable.
2. **Move `geckodriver` to a Safe Location:**
   - Move the `geckodriver` file to a directory such as `/usr/local/bin/`:
   ```bash
   sudo mv geckodriver /usr/local/bin/
   ```
3. Verify Installation:
   - In the Terminal, type:
   ```bash
   geckodriver --version
   ```
   - If installed correctly, you should see the Geckodriver version information.
### Step 3: Test Geckodriver with Selenium

Once the driver is installed and added to your system’s PATH, you can test it with a simple Selenium script (as shown earlier). If everything is set up correctly, Firefox should launch successfully.
