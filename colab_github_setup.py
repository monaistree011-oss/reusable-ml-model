# Step 3: Configure Git & Push to GitHub
# To push to GitHub from Colab, you need a GitHub Personal Access Token (PAT)

# ============================================================================
# SETUP INSTRUCTIONS:
# ============================================================================
# 1. Go to: https://github.com/settings/tokens/new
# 2. Generate a new token (classic)
# 3. Give it a name (e.g., "Colab GitHub Access")
# 4. Check the 'repo' permission scope (this allows full control of private repositories)
# 5. Copy the generated token

# ============================================================================
# RUN THIS CELL IN COLAB (replace YOUR_GITHUB_TOKEN with your actual token):
# ============================================================================

import os
import subprocess
from google.colab import userdata

# Option 1: Get token from Colab Secrets (Recommended)
try:
    GITHUB_TOKEN = userdata.get('GITHUB_TOKEN')
    print("✓ GitHub token loaded from Colab Secrets")
except:
    # Option 2: Manually paste your token (Less secure - only for testing)
    GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"  # Replace with your actual token
    print("⚠ Using manually provided token")

# Configure Git with your GitHub token
username = "YOUR_GITHUB_USERNAME"  # Replace with your GitHub username
email = "YOUR_EMAIL@example.com"    # Replace with your email

# Set Git configuration
subprocess.run(['git', 'config', '--global', 'user.name', username], check=True)
subprocess.run(['git', 'config', '--global', 'user.email', email], check=True)

# Configure Git to use your token for authentication
git_config = f'https://{username}:{GITHUB_TOKEN}@github.com'
subprocess.run(['git', 'config', '--global', 'url.https://github.com/.insteadOf', git_config], check=True)

print("✓ Git configured successfully!")
print(f"✓ Ready to push to GitHub as: {username}")

# ============================================================================
# NOW YOU CAN RUN GIT COMMANDS:
# ============================================================================
# Example: Clone a repository
# !git clone https://github.com/monaistree011-oss/reusable-ml-model.git

# Example: Add files and commit
# !cd reusable-ml-model
# !git add .
# !git commit -m "Your commit message"
# !git push origin main

# ============================================================================
# SECURE WAY: Using Colab Secrets (Recommended)
# ============================================================================
# 1. In Colab, click the 🔑 "Secrets" icon in the left sidebar
# 2. Click "+ Add new secret"
# 3. Name it: GITHUB_TOKEN
# 4. Paste your GitHub Personal Access Token
# 5. Run the code above - it will automatically use userdata.get('GITHUB_TOKEN')
