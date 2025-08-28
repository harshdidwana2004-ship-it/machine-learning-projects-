from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='A small chrome plugin to detect youtube comment sentiments',
    author='CampusX',
    license='',
)
echo "# hp" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:HRx1-spec/hp.git
git push -u origin main