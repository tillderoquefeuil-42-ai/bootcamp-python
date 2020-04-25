echo 'Check for old directories and remove them'

if [ -d "ai42" ]; then
    rm -rf ai42
fi
if [ -d "ai42.egg-info" ]; then
    rm -rf ai42.egg-info
fi
if [ -d "build" ]; then
    rm -rf build
fi
if [ -d "dist" ]; then
    rm -rf dist
fi

mkdir ai42
echo 'Directory ai42 created...'

echo 'Copying necessary files in ai42 directory...'

mkdir ai42/logging

cp __init__.py ai42
cp progressbar.py ai42
cp __init__.py ai42/logging
cp log.py ai42/logging

echo 'Upgrading setuptools and wheel if necessary...'
pip install --upgrade setuptools wheel

echo 'Creating package...'
python setup.py sdist bdist_wheel