# cloud-tools
Python utilities to manage cloud services, such as AWS.

## Local run

clone the [repository](https://github.com/RedHatQE/cloud-tools.git)

```
git clone https://github.com/RedHatQE/cloud-tools.git
```

Install [poetry](https://github.com/python-poetry/poetry)

```
poetry install
```

## Docs
- [AWS Readme](clouds/aws/README.md)

## Release new version
### requirements:
* Export GitHub token
```bash
export GITHUB_TOKEN=<your_github_token>
```
* [release-it](https://github.com/release-it/release-it)
Run the following once (execute outside repository dir for example `~/`):
```bash
sudo npm install --global release-it
npm install --save-dev @j-ulrich/release-it-regex-bumper
rm -f package.json package-lock.json
```
### usage:
* Create a release, run from the relevant branch.
To create a new release, run:
```bash
git checkout main
git pull
release-it # Follow the instructions
```
