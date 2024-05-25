# Navigate to your repository
cd aiq-bios

# Create and switch to the new branch
git checkout -b feature/github-commands-template

# Create a templates directory if it doesn't exist
mkdir -p templates

# Create a new template file with GitHub commands
cat <<EOL > templates/github_commands_template.sh
#!/bin/bash

# Set up the repository
REPO_URL="https://github.com/q8ai/aiq-bios"

# Clone the repository
git clone \$REPO_URL

# Navigate into the cloned repository
cd aiq-bios

# Add a remote repository (if needed)
git remote add origin \$REPO_URL

# Pull the latest changes from the main branch
git pull origin main

# Create a new branch (replace 'new-branch' with your branch name)
git checkout -b new-branch

# Add all changes to staging
git add .

# Commit the changes with a message (replace 'your commit message' with an appropriate message)
git commit -m "your commit message"

# Push the changes to the new branch
git push origin new-branch

# Create a pull request (requires GitHub CLI or hub)
# Ensure you have GitHub CLI (gh) or hub installed
# This example uses the GitHub CLI (gh); replace 'main' with your target branch
gh pr create --base main --head new-branch --title "Title of your PR" --body "Description of your PR"

EOL

# Stage and commit the template file
git add templates/github_commands_template.sh
git commit -m "Add GitHub commands template"

# Push the changes to the repository
git push origin feature/github-commands-template
