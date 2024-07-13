**Get started.**

This is a Static HTML space running on CPUs. Upload at least the `index.html` file that complies with the HTML specifications. Then the space automatically triggers image building and runs the NGINX Static HTML service. See the demo below:

**Clone this repository:**

```bash
git clone [git_https_url]
cd [repo_name]
```

**Create index.html:**

```bash
cat > index.html << EOF
<!DOCTYPE html>
<html>
    <head>
        <title>Example Demo</title>
    </head>
    <body>
        <p>This is an example of a simple HTML page with one paragraph.</p>
    </body>
</html>
EOF
```

**Upload file.**

Run the **git push** command and use the username and [Token](/my/tokens) to complete the push.

```bash
git add .
git commit -m "space init"
git branch -M main
git push -u origin main
```
